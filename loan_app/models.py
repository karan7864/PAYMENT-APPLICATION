from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    name = models.CharField(max_length=60,null=False,blank=False)
    email = models.CharField(max_length=80,null=False,blank=False)
    subject = models.CharField(max_length=200,null=False,blank=False)
    message = models.CharField(max_length=1000,null=False,blank=False)

    def __str__(self):
        return self.name
    
class UserProfile(models.Model):
    contact = models.CharField(max_length=10,null=False,blank=False)
    full_name = models.CharField(max_length=200,null=False,blank=False)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (self.user.email)

loan_types = (
    ("Secured","Secured"),
    ("Unsecured","Unsecured"),
)

class LoanType(models.Model):
    loan_name = models.CharField(max_length=200,null=False,blank=False)
    loan_desc = models.TextField(max_length=1000,null=False,blank=False)
    max_loan_amount = models.FloatField(null=False, blank=False)
    loan_roi = models.FloatField(null=False, blank=False)
    max_loan_duration = models.CharField(max_length=4,null=False, blank=False)
    loan_category = models.CharField(max_length=100,null=False,blank=False,choices=loan_types)
    need_security = models.BooleanField(default=False,null=True,blank=True)
    loan_image = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.loan_name

loan_status = (
    ("Pending","Pending"),
    ("Approved","Approved"),
    ("Disbursed","Disbursed"),
    ("Rejected","Rejected")
)

class LoanApplication(models.Model):
    application_id = models.CharField(max_length=100,null=True,blank=True)
    full_name = models.CharField(max_length=60,null=False,blank=False)
    contact_no = models.CharField(max_length=10,null=False,blank=False)
    pan_no = models.CharField(max_length=10,null=False,blank=False)
    aadhar_no = models.CharField(max_length=12,null=False,blank=False)
    residential_address = models.CharField(max_length=200,null=False,blank=False)
    service_type = models.CharField(max_length=60,null=False,blank=False)
    official_address = models.CharField(max_length=200,null=False,blank=False)
    income = models.CharField(max_length=30,null=False,blank=False)
    existing_loan = models.CharField(max_length=10,null=False,blank=False)
    loan_applied_for = models.ForeignKey(LoanType,on_delete=models.CASCADE,related_name="loan_type")
    expected_loan_amount = models.FloatField(null=False,blank=False)
    expected_loan_tenure = models.CharField(max_length=30,null=False,blank=False)
    collateral_name = models.CharField(max_length=200,null=True,blank=True)
    collateral_value = models.FloatField()
    profile_photo = models.FileField()
    pan_image = models.FileField()
    aadhar_image = models.FileField()
    account_number = models.CharField(max_length=100,null=False,blank=False)
    bank_name = models.CharField(max_length=100,null=False,blank=False)
    bank_ifsc_code = models.CharField(max_length=30,null=False,blank=False)

    remarks = models.CharField(max_length=300,null=True,blank=True)
    reject_reason = models.CharField(max_length=1000,null=True,blank=True)
    loan_application_status = models.CharField(max_length=50,null=True,blank=True,default="Pending",choices =loan_status)
    is_approved = models.BooleanField(default=False)
    approved_date = models.DateTimeField(null=True, blank=True)
    rejected_date = models.DateTimeField(null=True, blank=True)
    is_disbursed = models.BooleanField(default=False)
    disbursed_date = models.DateTimeField(null=True, blank=True)
    first_payment_date = models.DateField(null=True, blank=True)
    tenure_left = models.IntegerField(null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_schedule = models.FileField(null=True, blank=True)
    loan_completed = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

class LoanSchedule(models.Model):
    loan_id = models.ForeignKey(LoanApplication, on_delete=models.CASCADE,related_name='loan_schedule')
    payment_date = models.DateField(null=True, blank=True)
    monthly_amount = models.FloatField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    emi_paid = models.BooleanField(default=False)
    emi_paid_date = models.DateField(null=True, blank=True)
    razorpay_payment_id = models.CharField(max_length=200,null=True, blank=True)


recovery_state = (
    ('Reminder','Reminder'),
    ('Recovery', 'Recovery')
)

class LoanDefaultersReminder(models.Model):
    loan_id = models.ForeignKey(LoanApplication, on_delete=models.CASCADE, related_name='loan_defaulters')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=100,null=True, blank=True, choices=recovery_state)
    recovered_amount = models.FloatField(null=True, blank=True, default=0.0)
    recovery_date = models.DateTimeField(null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)