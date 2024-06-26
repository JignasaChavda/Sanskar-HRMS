from hrms.controllers.employee_boarding_controller import EmployeeBoardingController as BaseEmployeeBoardingController
import frappe
from frappe import _
from frappe.utils import unique

class extendclass(BaseEmployeeBoardingController):
    def create_task_and_notify_user(self):
        # Your overridden method implementation here
        holiday_list = self.get_holiday_list()

        for activity in self.activities:
            if activity.task:
                continue

            dates = self.get_task_dates(activity, holiday_list)
            employee_id = frappe.db.get_value('Employee', {'user_id': activity.user}, 'name')
            print(employee_id)

            task = frappe.get_doc(
                {
                    "doctype": "Task",
                    "project": self.project,
                    "subject": activity.activity_name + " : " + self.employee_name,
                    "description": activity.description,
                    "department": self.department,
                    "company": self.company,
                    "task_weight": activity.task_weight,
                    "exp_start_date": dates[0],
                    "exp_end_date": dates[1],
                    "priority": self.custom_priority,
                    "expected_time": self.custom_expected_time_in_hours,
                    "custom_assigned_user":activity.user,
                    "custom_employee": employee_id


                }
            ).insert(ignore_permissions=True)
            activity.db_set("task", task.name)

            users = [activity.user] if activity.user else []
            if activity.role:
                user_list = frappe.db.sql_list(
                    """
                    SELECT
                        DISTINCT(has_role.parent)
                    FROM
                        `tabHas Role` has_role
                            LEFT JOIN `tabUser` user
                                ON has_role.parent = user.name
                    WHERE
                        has_role.parenttype = 'User'
                            AND user.enabled = 1
                            AND has_role.role = %s
                """,
                    activity.role,
                )
                users = unique(users + user_list)

                if "Administrator" in users:
                    users.remove("Administrator")

            # assign the task the users
            if users:
                self.assign_task_to_users(task, users)
    