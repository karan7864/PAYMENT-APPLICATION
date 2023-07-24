from loan_app.models import LoanApplication,LoanSchedule,LoanDefaultersReminder

from datetime import datetime,date,timedelta
from django.conf import settings
from django.core.mail import send_mail,EmailMessage
from dateutil.relativedelta import relativedelta


def emi_due_reminder():
  today_date = date.today()
  yesterday_date = today_date - timedelta(days = 1)

  query = LoanApplication.objects.filter(is_disbursed=True).filter(loan_completed=False).all()

  for loan in query:
    emi_due = LoanSchedule.objects.filter(loan_id=loan).filter(payment_date=yesterday_date)

    if emi_due:
      for i in emi_due:
        subject = "EMI DUE REMINDER: LOANPAY"
        message = "Dear {0}, Your EMI Is Due. Please Make Payment Against Loan ID: ({1}).".format(i.user.first_name,i.loan_id.application_id)

        from_email = settings.EMAIL_HOST_USER
        to_mail = [i.user.email]
        send_mail(subject,message,from_email,to_mail,fail_silently=True)

        new_entry = LoanDefaultersReminder(loan_id=i.loan_id,user=i.user,status='Reminder')
        
        new_entry.save()
  

def defaulters_list():
  today_date = date.today()
  yesterday_date = today_date - timedelta(days = 1)

  query = LoanApplication.objects.filter(is_disbursed=True).filter(loan_completed=False).all()

  for loan in query:
    emi_dues_count = 0

    # EMI DUE For Yesterday
    emi_due = LoanSchedule.objects.filter(loan_id=loan).filter(payment_date=yesterday_date).filter(emi_paid=False)
        
    if emi_due:
      emi_dues_count += 1

      # EMI DUE For Last One Month From Yesterday   
      one_month_back = yesterday_date - relativedelta(months=1)
      emi_due = LoanSchedule.objects.filter(loan_id=loan).filter(payment_date=one_month_back).filter(emi_paid=False)

      if emi_due:
        emi_dues_count += 1
        
        # EMI DUE For Last Two Month From Yesterday         
        two_month_back = yesterday_date - relativedelta(months=2)
        emi_due = LoanSchedule.objects.filter(loan_id=loan).filter(payment_date=two_month_back).filter(emi_paid=False)
                
        if emi_due:
          emi_dues_count += 1

    if emi_dues_count == 3:
      for i in emi_due:
        subject = "Loan Recovery: LOANPAY"
        message = "Dear {0}, As You Are Not Paying EMI For Last 3 Consecutive Months. You Are Now A Defaulter And The Recovery Process Of Loan Is Started. Loan ID: ({1})".format(i.user.first_name,i.loan_id.application_id)

        from_email = settings.EMAIL_HOST_USER
        to_mail = [i.user.email]
        send_mail(subject,message,from_email,to_mail,fail_silently=True)

        new_entry = LoanDefaultersReminder(loan_id=i.loan_id,user=i.user,status='Recovery')
        new_entry.save()
    else:
      pass       


    print("Defaulters List")


def loan_completed():
  query = LoanApplication.objects.filter(is_disbursed=True).filter(loan_completed=False).all()

  for loan in query:
    payment_filter_query = LoanSchedule.objects.filter(loan_id=loan).all()

    emi_paid_months = 0
        
    for i in payment_filter_query:
      if i.emi_paid == True:
        emi_paid_months += 1

    if int(loan.expected_loan_tenure) == int(emi_paid_months):
      loan.loan_completed = True
      loan.save()
