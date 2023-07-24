from django.contrib import admin
from loan_app.models import Contact, UserProfile,LoanType,LoanApplication,LoanSchedule,LoanDefaultersReminder

admin.site.register(Contact)
admin.site.register(UserProfile)
admin.site.register(LoanType)
admin.site.register(LoanApplication)
admin.site.register(LoanSchedule)
admin.site.register(LoanDefaultersReminder)