import frappe
from hrms.hr.doctype.interview.interview import get_interviewers
from hrms.hr.doctype.job_applicant.job_applicant import JobApplicant as BaseJobApplicant

class extendclass(BaseJobApplicant):
	def before_save(self):
		if self.custom_interview_round == "Telephonic Round" and not self.custom_recruiter:
			self.custom_recruiter = frappe.session.user
		# frappe.msgprint("Hello")

@frappe.whitelist(allow_guest=True)
def create_interview(doc, interview_round):
	import json

	if isinstance(doc, str):
		doc = json.loads(doc)
		doc = frappe.get_doc(doc)

	round_designation = frappe.db.get_value("Interview Round", interview_round, "designation")
	round_type = frappe.db.get_value("Interview Round", interview_round, "custom_round")

	if round_designation and doc.designation and round_designation != doc.designation:
		frappe.throw(
			_("Interview Round {0} is only applicable for the Designation {1}").format(
				interview_round, round_designation
			)
		)

	interview = frappe.new_doc("Interview")
	interview.interview_round = interview_round
	interview.custom_round = round_type
	interview.job_applicant = doc.name
	interview.custom_applicant_name = doc.applicant_name
	interview.designation = doc.designation
	interview.resume_link = doc.resume_link
	interview.job_opening = doc.job_title

	interviewers = get_interviewers(interview_round)
	for d in interviewers:
		interview.append("interview_details", {"interviewer": d.interviewer})

	return interview