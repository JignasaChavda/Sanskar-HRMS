// Copyright (c) 2024, jignasha and contributors
// For license information, please see license.txt

frappe.query_reports["Recruitment Summary"] = {
	"filters": [
		{
			"label": "No.of Days",
			"fieldname": "no_of_days",
			"fieldtype": "Select",
			"options": [ "", 10, 20, 30, 45, 60, 90, "Above 90 days"]
		},
		{
			"label": "Staffing Plan",
			"fieldname": "staffing_plan",
			"fieldtype": "Link",
			"options": "Staffing Plan"
		},
		{
			"label": "Designation",
			"fieldname": "designation",
			"fieldtype": "Link",
			"options": "Designation"
		}
	]
};
