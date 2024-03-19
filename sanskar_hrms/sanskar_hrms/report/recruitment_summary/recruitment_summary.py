# Copyright (c) 2024, jignasha and contributors
# For license information, please see license.txt



import datetime
import frappe


def execute(filters=None):
	columns, data = [], []
 
	columns = get_columns()
 

	recruiment_data = get_recruitment_data(filters)
	prev_data = None
	for r_data in recruiment_data:
		if r_data['name'] == prev_data:
			r_data['name'] = ''
		data.append(r_data)
		prev_data = r_data['name']	
	return columns, data



def get_columns():
    return[
		{
			'label': 'Staffing Plan',
			'fieldname': 'name',
			'fieldtype': 'Data',
			'width': '200'
		},
		{
			'label': 'Job Opening',
			'fieldname' : 'job_opening',
			'fieldtype' : 'Data',
			'width' : '200'
		},
		{
			'label': 'Designation',
			'fieldname' : 'designation',
			'fieldtype' : 'Data',
			'width' : '200'
		},
		{
			'label': 'Vacancy Opening Date',
			'fieldname' : 'opening_date',
			'fieldtype' : 'Date',
			'width' : '200'
		},
		{
			'label': 'No of Vacancies',
			'fieldname' : 'no_of_vacancies',
			'fieldtype' : 'Data',
			'width' : '200'
		},
		{
			'label': 'Given Offer',
			'fieldname' : 'given_offer',
			'fieldtype' : 'Data',
			'width' : '200'
		},
		{
			'label': 'Accepted Offer',
			'fieldname' : 'accepted_offer',
			'fieldtype' : 'Data',
			'width' : '200'
		},
		{
			'label': 'Hired Vacancies',
			'fieldname' : 'accepted_offer',
			'fieldtype' : 'Data',
			'width' : '200'
		},
		{
			'label': 'Remaining Vacancies',
			'fieldname' : 'remaining_vacancies',
			'fieldtype' : 'Data',
			'width' : '200'
		},
	]



def get_recruitment_data(filters):
    conditions = get_filters(filters)
    no_of_days = conditions.get("no_of_days")
    staffing_plan = conditions.get("staffing_plan")
    designation = conditions.get("designation")
    
    # Handling case when no_of_days is None (null)
    if no_of_days is None:
        # Set a large value for no_of_days to include all dates
        no_of_days = 999
        query_upto_joins = """ 
			SELECT 
				sp.name AS 'name',
				jo.name AS 'job_opening',
				jo.designation AS 'designation',
				jo.posted_on AS 'opening_date',
				DATE_ADD(jo.posted_on, INTERVAL %s DAY) AS 'date_after_no_of_days',
				jo.planned_vacancies AS 'no_of_vacancies',
				SUM(CASE WHEN jof.offer_date BETWEEN jo.posted_on AND DATE_ADD(jo.posted_on, INTERVAL %s DAY) THEN 1 ELSE 0 END) AS 'given_offer',
				SUM(CASE WHEN jof.status = "Accepted" AND jof.offer_date BETWEEN jo.posted_on AND DATE_ADD(jo.posted_on, INTERVAL %s DAY) THEN 1 ELSE 0 END) AS 'accepted_offer',
				(jo.planned_vacancies - SUM(CASE WHEN jof.status = "Accepted" AND jof.offer_date BETWEEN jo.posted_on AND DATE_ADD(jo.posted_on, INTERVAL %s DAY) THEN 1 ELSE 0 END)) AS 'remaining_vacancies'
			FROM 
				`tabStaffing Plan` sp
			LEFT JOIN
				`tabJob Opening` jo ON sp.name = jo.staffing_plan
			LEFT JOIN
				`tabJob Offer` jof ON jo.name = jof.custom_job_opening 
		"""
        values = [no_of_days, no_of_days, no_of_days, no_of_days]
        
        conditions_added = False
        if staffing_plan:
              query_upto_joins += " WHERE sp.name = %s"
              conditions_added = True
              values.append(staffing_plan)
        if designation:
               if conditions_added:
                      query_upto_joins += " AND jo.designation = %s"
               else:
                      query_upto_joins += " WHERE jo.designation = %s"
               conditions_added = True
               values.append(designation)
        query_upto_joins += " GROUP BY jo.name"
        data = frappe.db.sql(query_upto_joins, tuple(values), as_dict=True)
        # print("\n\n\n",data,"\n\n\n")
        return data
    else:
         if no_of_days=='Above 90 days':
               no_of_days = 90
               query_upto_joins = """ 
					SELECT 
						sp.name AS 'name',
						jo.name AS 'job_opening',
						jo.designation AS 'designation',
						jo.posted_on AS 'opening_date',
						DATE_ADD(jo.posted_on, INTERVAL %s DAY) AS 'date_after_no_of_days',
						jo.planned_vacancies AS 'no_of_vacancies',
						SUM(CASE WHEN jof.offer_date > DATE_ADD(jo.posted_on, INTERVAL %s DAY) THEN 1 ELSE 0 END) AS 'given_offer',
						SUM(CASE WHEN jof.status = "Accepted" AND jof.offer_date > DATE_ADD(jo.posted_on, INTERVAL %s DAY) THEN 1 ELSE 0 END) AS 'accepted_offer',
						(jo.planned_vacancies - SUM(CASE WHEN jof.status = "Accepted" AND jof.offer_date BETWEEN jo.posted_on AND DATE_ADD(jo.posted_on, INTERVAL %s DAY) THEN 1 ELSE 0 END)) AS 'remaining_vacancies'
					FROM 
						`tabStaffing Plan` sp
					LEFT JOIN
						`tabJob Opening` jo ON sp.name = jo.staffing_plan
					LEFT JOIN
						`tabJob Offer` jof ON jo.name = jof.custom_job_opening 
				"""
               values = [no_of_days, no_of_days, no_of_days, no_of_days]
               conditions_added = False
               if staffing_plan:
                      query_upto_joins += " WHERE sp.name = %s"
                      conditions_added = True
                      values.append(staffing_plan)
               if designation:
                      if conditions_added:
                             query_upto_joins += " AND jo.designation = %s"
                      else:
                             query_upto_joins += " WHERE jo.designation = %s"
                      conditions_added = True
                      values.append(designation)
               query_upto_joins += " GROUP BY jo.name"
               data = frappe.db.sql(query_upto_joins, tuple(values), as_dict=True)
               return data
         else:
               query_upto_joins = """ 
					SELECT 
						sp.name AS 'name',
						jo.name AS 'job_opening',
						jo.designation AS 'designation',
						jo.posted_on AS 'opening_date',
						DATE_ADD(jo.posted_on, INTERVAL %s DAY) AS 'date_after_no_of_days',
						jo.planned_vacancies AS 'no_of_vacancies',
						SUM(CASE WHEN jof.offer_date BETWEEN jo.posted_on AND DATE_ADD(jo.posted_on, INTERVAL %s DAY) THEN 1 ELSE 0 END) AS 'given_offer',
						SUM(CASE WHEN jof.status = "Accepted" AND jof.offer_date BETWEEN jo.posted_on AND DATE_ADD(jo.posted_on, INTERVAL %s DAY) THEN 1 ELSE 0 END) AS 'accepted_offer',
						(jo.planned_vacancies - SUM(CASE WHEN jof.status = "Accepted" AND jof.offer_date BETWEEN jo.posted_on AND DATE_ADD(jo.posted_on, INTERVAL %s DAY) THEN 1 ELSE 0 END)) AS 'remaining_vacancies'
					FROM 
						`tabStaffing Plan` sp
					LEFT JOIN
						`tabJob Opening` jo ON sp.name = jo.staffing_plan
					LEFT JOIN
						`tabJob Offer` jof ON jo.name = jof.custom_job_opening 
				"""
               values = [no_of_days, no_of_days, no_of_days, no_of_days]
               conditions_added = False
               if staffing_plan:
                      query_upto_joins += " WHERE sp.name = %s"
                      conditions_added = True
                      values.append(staffing_plan)
               if designation:
                      if conditions_added:
                             query_upto_joins += " AND jo.designation = %s"
                      else:
                             query_upto_joins += " WHERE jo.designation = %s"
                             conditions_added = True
                             values.append(designation)
               query_upto_joins += " GROUP BY jo.name"
               data = frappe.db.sql(query_upto_joins, tuple(values), as_dict=True)
               
               return data
               
                
		

def get_filters(filters):
    conditions = {}
    for key, value in filters.items():
        conditions[key] = value
    
    return conditions
