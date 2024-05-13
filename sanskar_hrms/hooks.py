app_name = "sanskar_hrms"
app_title = "Sanskar HRMS"
app_publisher = "jignasha"
app_description = "Sanskar HRMS"
app_email = "jignasha@sanskartechnolab.com"
app_license = "mit"
# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/sanskar_hrms/css/sanskar_hrms.css"
# app_include_js = "/assets/sanskar_hrms/js/sanskar_hrms.js"

# include js, css files in header of web template
# web_include_css = "/assets/sanskar_hrms/css/sanskar_hrms.css"
# web_include_js = "/assets/sanskar_hrms/js/sanskar_hrms.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "sanskar_hrms/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "sanskar_hrms/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "sanskar_hrms.utils.jinja_methods",
# 	"filters": "sanskar_hrms.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "sanskar_hrms.install.before_install"
# after_install = "sanskar_hrms.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "sanskar_hrms.uninstall.before_uninstall"
# after_uninstall = "sanskar_hrms.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "sanskar_hrms.utils.before_app_install"
# after_app_install = "sanskar_hrms.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "sanskar_hrms.utils.before_app_uninstall"
# after_app_uninstall = "sanskar_hrms.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "sanskar_hrms.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }
override_doctype_class = {
	"Interview": "sanskar_hrms.interview.Interview",
    "Job Offer":"sanskar_hrms.job_offer.JobOffer",
    "Interview Feedback":"sanskar_hrms.interview_feedback.InterviewFeedback"
}

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"sanskar_hrms.tasks.all"
# 	],
# 	"daily": [
# 		"sanskar_hrms.tasks.daily"
# 	],
# 	"hourly": [
# 		"sanskar_hrms.tasks.hourly"
# 	],
# 	"weekly": [
# 		"sanskar_hrms.tasks.weekly"
# 	],
# 	"monthly": [
# 		"sanskar_hrms.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "sanskar_hrms.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "sanskar_hrms.event.get_events"
# }
override_whitelisted_methods = {
	"hrms.hr.doctype.job_applicant.job_applicant.create_interview": "sanskar_hrms.job_applicant.create_interview"
}
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "sanskar_hrms.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["sanskar_hrms.utils.before_request"]
# after_request = ["sanskar_hrms.utils.after_request"]

# Job Events
# ----------
# before_job = ["sanskar_hrms.utils.before_job"]
# after_job = ["sanskar_hrms.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"sanskar_hrms.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

fixtures = [
    "Workflow",
    "Workflow State",
    {"dt":"Server Script","filters":[
        [
            "module","in",[
               "Sanskar HRMS"
            ],
        ]
    ]},
    {"dt":"Client Script","filters":[
        [
            "module","in",[
               "Sanskar HRMS"
            ],
        ]
    ]},
    {"dt":"Custom Field","filters":[
        [
            "module","in",[
               "Sanskar HRMS"
            ]
        ]
    ]},
    {"dt":"Property Setter","filters":[
        [
            "module","in",[
               "Sanskar HRMS"
            ],
        ]
    ]},
    {"dt":"Print Format","filters":[
        [
            "module","in",[
               "Sanskar HRMS"
            ],
        ]
    ]},
    {"dt":"Report","filters":[
        [
            "module","in",[
               "Sanskar HRMS"
            ],
        ]
    ]},
    {"dt":"Letter Head","filters":[
        [
            "name","in",[
                "Sanskar Tecnolab",
                "Sanskar Technolab - Letter Head 2"
            ],
        ]
    ]},
    {"dt":"Notification","filters":[
        [
            "name","in",[
               "Send mail to Interviewers"
            ],
        ]
    ]}
]