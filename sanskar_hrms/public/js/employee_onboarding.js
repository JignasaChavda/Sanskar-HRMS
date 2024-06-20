frappe.ui.form.on('Employee Onboarding', {
    refresh(frm) {
        
        // Apply filter on job_applicant field
        frm.set_query('job_applicant', function () {
            return {
                filters: [
                    ['status', '=', 'Job Offer - Accepted']
                ]
            };
        });
    }
});