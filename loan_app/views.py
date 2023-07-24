from datetime import datetime,timedelta,date
from multiprocessing import parent_process
import re
from xml.dom.pulldom import parseString
from django.utils import timezone
import math
from dateutil.relativedelta import relativedelta
from django.core.mail import send_mail,EmailMessage
from django.shortcuts import redirect, render
from django.contrib.auth import login,logout,authenticate
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
import csv
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.decorators import login_required
from loan_app.models import Contact, LoanApplication, LoanDefaultersReminder, LoanSchedule, UserProfile,LoanType
import loan_app
from django.db.models import Sum
from django.views.decorators.csrf import csrf_exempt
import razorpay
from loan_project.settings import razorpay_test_secret_key,razorpay_test_key


def index(request):
    data = LoanType.objects.all()
    context = {
        'loan_type':data,
    }
    return render(request, 'index.html',context)


def about(request):
    return render(request, 'about_us.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        new_enquiry = Contact(name=name,email=email,subject=subject,message=message)
        new_enquiry.save()

        subject = "Loanpay"
        message = "Thanks For Contacting Us "+name+". We will get in touch with you within 24 hours."
        from_email = settings.EMAIL_HOST_USER
        to_mail = [email]
        send_mail(subject,message,from_email,to_mail,fail_silently=True)
        messages.add_message(request,messages.success,"Thanks for Contacting Us.We will get in touch with you within 24 hours.") 
    return render(request, 'contact.html')


def user_login(request):
    if request.user.is_authenticated:
        messages.add_message(request,messages.WARNING,"You already logged in.")
        return redirect('loan_app:index')
    else:
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(username=email,password=password)
            if user:
                login(request,user)
                messages.add_message(request,messages.WARNING,f"Welcome, {request.user.first_name} {request.user.last_name} you logged in successfully.")
                return redirect('loan_app:index')
            else:
                messages.add_message(request,messages.WARNING,"Sorry, check again your username or password.")

    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        contact = request.POST['contact']
        password = request.POST['password']

        user_exists = User.objects.filter(username=email)
        
        if not user_exists:
            new_user = User.objects.create_user(first_name=fname, last_name= lname,username=email, email=email, password=password,is_active=True)
            new_user.save()

            full_name = fname+" "+lname
            print(full_name)
            user_profile = UserProfile(contact=contact,user=new_user,full_name=full_name)
            user_profile.save()

            subject = "Loanpay Registration"
            message = "Thanks For Registering on our Website Mr. "+fname+" "+lname+"."
            from_email = settings.EMAIL_HOST_USER
            to_mail = [email]
            send_mail(subject,message,from_email,to_mail,fail_silently=True)
            messages.add_message(request,messages.SUCCESS,"Thanks for Registering with us.Please Login") 
            return redirect('loan_app:login')
        else:
            messages.add_message(request,messages.WARNING,"You Already have an Account. Please Login")
    
    return render(request, 'register.html')


def user_logout(request):
    logout(request)
    messages.add_message(request,messages.SUCCESS,"Success, You Logged Out Successfully.")
    return redirect('loan_app:index')

@login_required(login_url='loan_app:login')
def dashboard(request):
    user = request.user
    print(user)

    approved_loans = LoanApplication.objects.filter(user=user).filter(is_approved=True).filter(is_disbursed=False).count()

    disbursed_loans = LoanApplication.objects.filter(user=user).filter(loan_application_status="Disbursed").filter(is_disbursed=True).count()

    rejected_loans = LoanApplication.objects.filter(user=user).filter(is_approved=False).filter(is_disbursed=False).filter(loan_application_status="Rejected").count()
    
    pending_loans = LoanApplication.objects.filter(user=user).filter(loan_application_status="Pending").count()

    total_disbursed_loans_amount = LoanApplication.objects.filter(loan_application_status="Disbursed").filter(is_disbursed=True).aggregate(Sum('expected_loan_amount'))


    context = {'approved_loans': approved_loans,'disbursed_loans':disbursed_loans,'rejected_loans':rejected_loans,'pending_loans':pending_loans,'total_disbursed_loans_amount':total_disbursed_loans_amount.get('expected_loan_amount__sum')}

    return render(request, 'dashboard.html',context)

@login_required(login_url='loan_app:login')
def emi_calculator(request):
    if request.method == 'POST':
        amount = request.POST['amount']
        interest = request.POST['interest']
        tenure = request.POST['tenure']

        if not amount or not interest or not tenure:
            messages.add_message(request,messages.WARNING,"Fill All the Details Properly")
            return render(request, 'emi_calculate.html')
        else:
            rate_of_interest_per_month = float(interest)/(12*100)

            monthly_emi = float(amount) * float(rate_of_interest_per_month) * ((1+float(rate_of_interest_per_month))**float(tenure))/((1+float(rate_of_interest_per_month)) ** float(tenure) - 1)

            total_interest_amount = (float(monthly_emi)*float(tenure)) - float(amount)

            context = {
                'amount':amount,
                'rate_of_interest_per_month':rate_of_interest_per_month,
                'tenure':tenure,
                'monthly_emi':monthly_emi,
                'total_interest_amount':total_interest_amount,
                'interest':interest,
                'total_amount': round((float(amount)+float(total_interest_amount)),2),
            }

            return render(request, 'emi_calculate.html',context)
    else:
        return render(request, 'emi_calculate.html')

#========================= New Loan =====================================
@login_required(login_url='loan_app:login')
def new_loan(request):
    user = request.user
    if not user.is_superuser:
        return redirect('loan_app:index')
    else:
        if request.method == 'POST':
            name = request.POST.get('name')
            description = request.POST.get('description')
            amount = request.POST.get('amount')
            roi = request.POST.get('roi')
            duration = request.POST.get('duration')
            category = request.POST.get('category')
            need_security = request.POST.get('need_collateral')

            if need_security == 'on':
                need_security = True
            else:
                need_security = False

            try:
                loan_image = request.FILES['loan_img']
                fs = FileSystemStorage()
                filename = fs.save(loan_image.name,loan_image)
                loan_image_url = fs.url(filename)
            except:
                loan_image_url = ""

            if not name or not description or not amount or not roi or not duration or not category:
                messages.add_message(request,messages.WARNING,"Fill All the Details Properly")
                return render(request, 'add_new_loan.html')

            else:
                is_exists = LoanType.objects.filter(loan_name=name,loan_category=category).exists()
                if is_exists:
                    messages.add_message(request,messages.WARNING,"Loan Already Exists with same name.")

                else:
                    loan = LoanType(loan_name=name,loan_desc=description,max_loan_amount=amount,loan_roi=roi,max_loan_duration=duration,
                    loan_category=category,need_security=need_security,loan_image=loan_image_url)

                    loan.save()

                    messages.add_message(request,messages.WARNING,"New Type of Loan Created Successfully.")


        return render(request, 'add_new_loan.html')

@login_required(login_url='loan_app:login')
def loan_list(request):
    user = request.user
    if not user.is_superuser:
        return redirect('loan_app:index')
    else:
        all_loans = LoanType.objects.all()
        context = {
            'loans':all_loans,
        }
        return render(request, 'availlable_loan_list.html',context)

@login_required(login_url='loan_app:login')
def delete_loan(request,id):
    user = request.user
    if not user.is_superuser:
        return redirect('loan_app:index')
    else:
        loan = LoanType.objects.filter(id=id)
        loan.delete()
        messages.add_message(request,messages.WARNING,"Loan Deleted Successfully")

    return redirect('loan_app:loan_list')


@login_required(login_url='loan_app:login')
def update_loan(request,id):
    user = request.user
    if not user.is_superuser:
        return redirect('loan_app:index')
    else:
        fetch_loan = LoanType.objects.filter(id=id)
        if request.method == 'POST':
            fetch_loan = LoanType.objects.filter(id=id)
            name = request.POST.get('name')
            description = request.POST.get('description')
            amount = request.POST.get('amount')
            roi = request.POST.get('roi')
            duration = request.POST.get('duration')
            category = request.POST.get('category')
            need_security = request.POST.get('need_collateral')
            if need_security == "on":
                need_security = True
            else:
                need_security = False

            try:
                loan_image = request.FILES['loan_img']
                fs = FileSystemStorage()
                filename = fs.save(loan_image.name,loan_image)
                loan_image_url = fs.url(filename)
            except:
                loan_image_url = ""

            loan_update = LoanType.objects.filter(id=id).first()
            loan_update.loan_name = name
            loan_update.loan_desc = description
            loan_update.max_loan_amount = amount
            loan_update.loan_roi = roi
            loan_update.max_loan_duration = duration
            loan_update.loan_category = category
            loan_update.need_security = need_security
            if loan_image_url:
                loan_update.loan_image = loan_image_url

            loan_update.save()

            messages.add_message(request,messages.WARNING,"Loan Edit Successfully")
            return redirect('loan_app:loan_list')

        context = {
            'data':fetch_loan,
        }
        return render(request, 'update_loan.html',context)


@login_required(login_url='loan_app:login')
def apply_loan(request,id):
    aadhar_validation = 0
    pan_validation = 0

    loan_types = LoanType.objects.filter(id=id)

    last_application_id = LoanApplication.objects.all().order_by('id').last()
    if not last_application_id:
        app_id =  'LOANPAY' + '000001'
    else:
        application_no = last_application_id.application_id
        application_id_int = int(application_no[7:13])
        new_application_no_int = application_id_int + 1
        app_id = 'LOANPAY'  + str(new_application_no_int).zfill(6)

    if request.method == 'POST':
        full_name = request.POST['full_name']
        contact_no = request.POST['contact_no']
        pan_no = request.POST['pan_no']
        aadhar_no = request.POST['aadhar_no']
        residential_address = request.POST['residential_address']
        service_type = request.POST['service_type']
        official_address = request.POST['official_address']
        income = request.POST['income']
        existing_loan = request.POST['existing_loan']
        loan_applied_for = request.POST['loan_applied_for']
        expected_loan_amount = request.POST['expected_loan_amount']
        expected_loan_tenure = request.POST['expected_loan_tenure']
        account_number = request.POST['ac_no']
        bank_name = request.POST['ac_name']
        bank_ifsc_code = request.POST['ac_ifsc']
        remarks = request.POST['remarks']
        collateral_name = request.POST.get('security',"")
        collateral_value = request.POST.get('coll_value',0)

        loan_type = LoanType.objects.filter(loan_name=loan_applied_for).first()

        #======================== Regex Pattern For AADHAR, PAN =========
        aadhar_regex = ("^[2-9]{1}[0-9]{3}[0-9]{4}[0-9]{4}$")

        aadhar_regex_compile = re.compile(aadhar_regex)

        if(re.search(aadhar_regex_compile, aadhar_no)):
            aadhar_validation += 1

        pan_regex = "[A-Z]{5}[0-9]{4}[A-Z]{1}" 
        pan_regex_compile = re.compile(pan_regex)
        if(re.search(pan_regex_compile, pan_no)):
            pan_validation += 1


        if pan_validation and aadhar_validation:   
            try:
                profile_photo = request.FILES['profile_photo']
                fs = FileSystemStorage()
                filename = fs.save(profile_photo.name,profile_photo)
                profile_url = fs.url(filename)
            except:
                profile_url = ""

            try:
                pan_image = request.FILES['pan_image']
                fs = FileSystemStorage()
                filename = fs.save(pan_image.name,pan_image)
                pan_url = fs.url(filename)
            except:
                pan_url = ""

            try:
                aadhar_image = request.FILES['aadhar_image']
                fs = FileSystemStorage()
                filename = fs.save(aadhar_image.name,aadhar_image)
                aadhaar_url = fs.url(filename)
            except:
                aadhaar_url = ""     
            new_application = LoanApplication(full_name=full_name,contact_no=contact_no,pan_no=pan_no,aadhar_no=aadhar_no,residential_address=residential_address,service_type=service_type,official_address=official_address,income=income,existing_loan=existing_loan,loan_applied_for=loan_type,expected_loan_amount=expected_loan_amount,expected_loan_tenure=expected_loan_tenure,remarks=remarks,profile_photo=profile_url,pan_image=pan_url,aadhar_image=aadhaar_url,application_id=app_id,collateral_name=collateral_name,collateral_value=collateral_value,user=request.user,account_number=account_number,bank_name=bank_name,bank_ifsc_code=bank_ifsc_code)

            new_application.save()

            subject = "Loan Application Created:LOANPAY"
            message = "Your Application Successfully Created. Application ID: {0}. We will get back to you shortly.".format(app_id)
            from_email = settings.EMAIL_HOST_USER
            to_mail = [request.user.email]
            send_mail(subject,message,from_email,to_mail,fail_silently=True)

            messages.add_message(request,messages.WARNING,"Application Submitted Successfully.")

            return redirect('loan_app:dashboard')
        
        else:
            messages.add_message(request,messages.WARNING,"Please Enter Valid PAN/AADHAR Card Number") 

    context = {
        'loans': loan_types,
    }
    return render(request, 'apply_loan.html',context)


@login_required(login_url='loan_app:login')
def approve_loans(request):
    user = request.user
    approved_loans = LoanApplication.objects.filter(user=user).filter(is_approved=True).filter(is_disbursed=False).order_by('-created_on')
    context = {'approved_loans': approved_loans}
    return render(request, 'approve_loans.html',context)


@login_required(login_url='loan_app:login')
def pending_loans(request):
    user = request.user
    pending_loans = LoanApplication.objects.filter(user=user).filter(loan_application_status="Pending").order_by('-created_on')
    context = {'pending_loans': pending_loans}
    return render(request, 'pending_loans.html',context)


@login_required(login_url='loan_app:login')
def rejected_loans(request):
    user = request.user
    rejected_loans = LoanApplication.objects.filter(user=user).filter(is_approved=False).filter(is_disbursed=False).filter(loan_application_status="Rejected").order_by('-created_on')
    context = {'rejected_loans': rejected_loans}
    return render(request, 'rejected_loans.html',context)


@login_required(login_url='loan_app:login')
def disbursed_loans(request):
    user = request.user
    disbursed_loans = LoanApplication.objects.filter(user=user).filter(is_approved=True).filter(loan_application_status="Disbursed").filter(is_disbursed=True).order_by('-created_on')
    context = {'disbursed_loans': disbursed_loans}
    return render(request, 'disbursed_loans.html',context)


@login_required(login_url='loan_app:login')
def disbursed_loans_history(request):
    user = request.user
    if not user.is_superuser:
        return redirect('loan_app:index')
    else:
        total_disbursed_amount = 0.0

        if request.method == 'POST':
            from_date = request.POST.get('from_date')
            to_date = request.POST.get('to_date')

            if from_date and to_date:
                disbursed_loans = LoanApplication.objects.filter(is_approved=True).filter(loan_application_status="Disbursed").filter(is_disbursed=True).filter(disbursed_date__range=[from_date,to_date]).order_by('-created_on')

                for loans in disbursed_loans:
                    total_disbursed_amount += float(loans.expected_loan_amount)

                context = {'disbursed_loans': disbursed_loans,
                'total_disbursed_amount':total_disbursed_amount}

                return render(request, 'disbursed_loans_history.html',context)
            
            else:
                messages.add_message(request,messages.WARNING,"Please Enter Correct Date Range.")

        disbursed_loans = LoanApplication.objects.filter(is_approved=True).filter(loan_application_status="Disbursed").filter(is_disbursed=True).order_by('-created_on')

        for loans in disbursed_loans:
            total_disbursed_amount += float(loans.expected_loan_amount)

        context = {'disbursed_loans': disbursed_loans,
        'total_disbursed_amount':total_disbursed_amount}

        return render(request, 'disbursed_loans_history.html',context)


@login_required(login_url='loan_app:login')
def pending_loan_applications(request):
    user = request.user
    if not user.is_superuser:
        return redirect('loan_app:index')
    else:
        pending_applications = LoanApplication.objects.filter(loan_application_status="Pending").order_by('-created_on')
        context = {'pending_applications': pending_applications}
        return render(request, 'pending_loan_applications.html',context)


@login_required(login_url='loan_app:login')
def approve_loan_application(request,id):
    user = request.user
    if not user.is_superuser:
        return redirect('loan_app:index')
    else:
        loan_application = LoanApplication.objects.get(id=id)
        loan_application.approved_date = datetime.now()
        loan_application.is_approved = True
        loan_application.loan_application_status = "Approved"
        loan_application.save()

        subject = "Application Update {0}:LOANPAY".format(loan_application.application_id)
        message = "Dear {0}, Congratulations Welcome to Loanpay. Your Loan Application is Approved. We will contact you shortly for further discussions.".format(loan_application.full_name)
        from_email = settings.EMAIL_HOST_USER
        to_mail = [loan_application.user.email]
        send_mail(subject,message,from_email,to_mail,fail_silently=True)
        
        return redirect('loan_app:loan_applications')


@login_required(login_url='loan_app:login')
def reject_loan_application(request,id):
    user = request.user
    if not user.is_superuser:
        return redirect('loan_app:index')
    else:
        loan_application = LoanApplication.objects.get(id=id)
        loan_application.rejected_date = datetime.now()
        loan_application.is_approved = False
        loan_application.loan_application_status = "Rejected"
        loan_application.save()

        subject = "Application Update {0}:LOANPAY".format(loan_application.application_id)
        message = "Dear {0}, Thanks for applying, However we regret to inform you of our inability to process the same, as it doesn't meet the Terms and Conditions. We would like to thanks again for your interest.".format(loan_application.full_name)
        from_email = settings.EMAIL_HOST_USER
        to_mail = [loan_application.user.email]
        send_mail(subject,message,from_email,to_mail,fail_silently=True)

        return redirect('loan_app:loan_applications')


@login_required(login_url='loan_app:login')
def rejected_loan_application(request):
    user = request.user
    if not user.is_superuser:
        return redirect('loan_app:index')
    else:
        rejected_applications = LoanApplication.objects.filter(loan_application_status="Rejected").order_by('-rejected_date')

        context = {'rejected_applications': rejected_applications}
        return render(request, 'rejected_loan_applications.html',context)


@login_required(login_url='loan_app:login')
def rejected_loan_application_reason(request,id):
    user = request.user
    if not user.is_superuser:
        return redirect('loan_app:index')
    else:
        application = LoanApplication.objects.get(id=id)

        if request.method == 'POST':
            rejected_reason = request.POST.get('rejected_reason')

        application.reject_reason = rejected_reason
        application.save()
        
        return redirect('loan_app:rejected_loan_application')


@login_required(login_url='loan_app:login')
def approved_loan_application(request):
    user = request.user
    if not user.is_superuser:
        return redirect('loan_app:index')
    else:
        approved_applications = LoanApplication.objects.filter(loan_application_status="Approved").filter(is_approved=True).order_by('-approved_date')

        context = {'approved_applications': approved_applications}
        return render(request, 'approved_loan_application.html',context)



@login_required(login_url='loan_app:login')
def disbursed_loan_application(request):
    user = request.user
    if not user.is_superuser:
        return redirect('loan_app:index')
    else:
        disbursed_loan_applications = LoanApplication.objects.filter(loan_application_status="Disbursed").filter(is_disbursed=True).order_by('-disbursed_date')

        context = {'disbursed_loan_applications':disbursed_loan_applications}
        return render(request, 'disbursed_loan_application.html',context)


@login_required(login_url='loan_app:login')
def loan_schedule(request,id):
    loan_application = LoanApplication.objects.filter(id=id).first()

    payment_schedule_loan_application = LoanSchedule.objects.filter(loan_id=id)

    if payment_schedule_loan_application:
        payment_schedule_exist = True
    else:
        payment_schedule_exist = False

    file_name = loan_application.application_id
    
    initial_loan_balance = float(loan_application.expected_loan_amount)

    ending_balance = float(loan_application.expected_loan_amount)

    total_months = int(loan_application.expected_loan_tenure)

    loan_disbursed_date = loan_application.disbursed_date
    loan_disbursed_day = loan_disbursed_date.day

    emi_date = None
    if loan_disbursed_day >= 1 and loan_disbursed_day <= 15:
        emi_date = 10
    elif loan_disbursed_day > 15 and loan_disbursed_day <= 31:
        emi_date = 20

    rate_of_interest = float(loan_application.loan_applied_for.loan_roi)/(100)

    monthly_emi = (float(loan_application.expected_loan_amount)*(rate_of_interest/12)*(math.pow(1+rate_of_interest/12,total_months)))/(math.pow(1+rate_of_interest/12,total_months)-1)

    fields = ['S.No', 'Initial Balance', 'Interest Charge', 'Principal Amount', 'Monthly EMI', 'Ending Balance','Payment Date (yyyy/mm/dd)'] 

    loan_schedule = []

    for month in range(1,total_months+1):

        loan_disbursed_date = (loan_disbursed_date + timedelta(30))
        split_date = str(loan_disbursed_date).split("-")

        new_payment_date = "{}-{}-{}".format(split_date[0], split_date[1],emi_date)


        interest_charge = (float(loan_application.loan_applied_for.loan_roi)/(12*100)) * initial_loan_balance 

        ending_balance = initial_loan_balance + interest_charge - monthly_emi

        loan_schedule.append({'S.No':str(month),'Initial Balance': "Rs "+str(round(initial_loan_balance,2)),'Interest Charge': "Rs "+str(round(interest_charge,2)),'Principal Amount': "Rs "+str(round((monthly_emi-interest_charge),2)),'Monthly EMI': "Rs "+str(round(monthly_emi,2)),'Ending Balance': "Rs "+str(round(ending_balance,2)),'Payment Date (yyyy/mm/dd)': new_payment_date})

        if not payment_schedule_exist:
            payment_schedule = LoanSchedule.objects.create(loan_id=loan_application,payment_date=datetime.strptime(new_payment_date, '%Y-%m-%d').date(),monthly_amount=round(monthly_emi,2),
            user=loan_application.user)
            
            payment_schedule.save()

        initial_loan_balance = ending_balance


    with open("media/loan_schedules/"+file_name+".csv", 'w', newline='') as csvfile: 
        writer = csv.DictWriter(csvfile, fieldnames = fields) 
        writer.writeheader() 
        writer.writerows(loan_schedule) 

    with open("media/loan_schedules/"+file_name+'.csv') as myfile:
        response = HttpResponse(myfile, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={0}.csv'.format(file_name)
        
    return response


@login_required(login_url='loan_app:login')
def disbursed_application(request,id):
    user = request.user
    if not user.is_superuser:
        return redirect('loan_app:index')
    else:
        loan_id = id

        loan_application = LoanApplication.objects.get(id=id)
        loan_application.is_disbursed = True
        loan_application.loan_application_status = "Disbursed"
        loan_application.disbursed_date = datetime.now()

        loan_disbursed_date = (loan_application.disbursed_date + timedelta(30))
        split_date = str(loan_disbursed_date).split("-")

        loan_disbursed_day = loan_disbursed_date.day

        emi_date = None
        if loan_disbursed_day >= 1 and loan_disbursed_day <= 15:
            emi_date = 10
        elif loan_disbursed_day > 15 and loan_disbursed_day <= 31:
            emi_date = 20

        first_payment_date = ("{}-{}-{}").format(split_date[0], split_date[1], emi_date)

        first_payment_date = datetime.strptime(first_payment_date, '%Y-%m-%d').date()

        loan_application.first_payment_date = first_payment_date
        loan_application.save()

        loan_schedule(request,loan_id)
        
        return redirect('loan_app:disbursed_loan_application')


@login_required(login_url='loan_app:login')
def loan_schedule_history(request):
    requested_user = request.user
    if request.method == 'GET':
        query = LoanApplication.objects.filter(user=requested_user).filter(is_disbursed=True).filter(loan_application_status='Disbursed').all()
        context = {'schedule': query}
        return render(request, 'loan_schedule_history.html',context)
    
    elif request.method == 'POST':
        today_date = datetime.now().date()

        selected_loan_id = request.POST.get('selected_loan_id')
        if selected_loan_id:
            loan_id = LoanApplication.objects.get(application_id=selected_loan_id)

            query_for_monthly_emi = LoanSchedule.objects.filter(loan_id=loan_id).first()

            query = LoanSchedule.objects.filter(loan_id=loan_id).all().order_by('payment_date')
            # Multiply with 100 as razorpay takes amount in paisa
            monthly_emi = (query_for_monthly_emi.monthly_amount) * 100 

            client = razorpay.Client(auth=(razorpay_test_key,razorpay_test_secret_key))

            payment_data = {"amount": monthly_emi, "currency": "INR", 'payment_capture':'1'}
            client.order.create(data=payment_data)
            
            context = {
                'complete_schedule':query,
                'selected_loan_id':selected_loan_id,
                'today_date': today_date,
                'monthly_emi':monthly_emi,
                'razorpay_test_key':razorpay_test_key
                }
            return render(request, 'complete_loan_schedule.html',context)



@csrf_exempt
def success_payment(request,id):
    query = LoanSchedule.objects.filter(id=id).first()

    if request.method == 'POST':
        payment_id = request.POST.get('razorpay_payment_id','')
    
    query.razorpay_payment_id = payment_id
    query.emi_paid = True
    query.emi_paid_date = timezone.now()
    query.save()

    subject = "Payment Reciept: LOANPAY"
    message = "Thanks for Paying Monthly EMI. Your Payment ID is {0} for your refrence.".format(payment_id)
    from_email = settings.EMAIL_HOST_USER
    to_mail = [query.user]
    send_mail(subject,message,from_email,to_mail,fail_silently=True)

    return render(request, 'success_payment.html')


def defaulters_list(request):
    user = request.user
    if not user.is_superuser:
        return redirect('loan_app:index')
    else:
        query = LoanDefaultersReminder.objects.filter(status="Recovery").all()

        context = {'defaulters':query}
        return render(request, 'defaulters_list.html',context)


def defaulters_list_remarks(request,id):
    user = request.user
    if not user.is_superuser:
        return redirect('loan_app:index')
    else:
        application = LoanDefaultersReminder.objects.get(id=id)

        if request.method == 'POST':
            recovered_amount = request.POST.get('recovered_amount')
            recovery_date = request.POST.get('recovery_date')
            remarks = request.POST.get('remarks')

        application.recovered_amount = recovered_amount
        application.recovery_date = recovery_date
        application.remarks = remarks
        application.save()
        
        return redirect('loan_app:defaulters_list')


def emi_due_reminders(request):
    user = request.user
    if not user.is_superuser:
        return redirect('loan_app:index')
    else:
        query = LoanDefaultersReminder.objects.filter(status="Reminder").all().order_by('-created_on')
        
        context = {'reminders':query}
        return render(request, 'emi_due_reminders.html',context)