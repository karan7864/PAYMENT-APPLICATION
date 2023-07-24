from django.urls import path, reverse_lazy
from loan_app import views
from django.contrib.auth import views as auth_views
from loan_app.views import *

app_name = 'loan_app'

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),

    # Login Page
    path('login/', views.user_login, name="login"),

    # Register Page
    path('register/', views.register, name="register"),

    # Logout Page
    path('logout/', views.user_logout, name="logout"),

    # User and admin dashboard
    path('dashboard/', views.dashboard, name="dashboard"),

    # To Calculate Loan Monthly EMI
    path('emi-calculator/', views.emi_calculator, name="emi_calculator"),

    # Different Loan Types (CRUD)
    path('add-new-loan/', views.new_loan, name="new_loan"),
    path('available-loans/', views.loan_list, name="loan_list"),
    path('delete-loan/<int:id>/', views.delete_loan, name="delete_loan"),
    path('update-loan/<int:id>/', views.update_loan, name="update_loan"),

    # Apply For Loan
    path('apply-loan/<int:id>/', views.apply_loan, name="apply_loan"),

    # Approved Loans
    path('approve-loans/', views.approve_loans, name="approved_loan"),

    # Pending Loans
    path('pending-loans/', views.pending_loans, name="pending_loan"),

    # Rejected Loans
    path('rejected-loans/', views.rejected_loans, name="rejected_loan"),

    # Disbursed Loans
    path('disbursed-loans/', views.disbursed_loans, name="disbursed_loan"),
    path('disbursed-loans/history/', views.disbursed_loans_history, name="disbursed_loans_history"),

    # Loan Applications (Admin)
    path('pending-loan-applications/', views.pending_loan_applications,name="loan_applications"),

    # To Approve Loan Application
    path('approve-loan-applications/<int:id>/', views.approve_loan_application,name="approve_loan_application"),

    # To Reject Loan Application
    path('reject-loan-applications/<int:id>/', views.reject_loan_application,name="reject_loan_application"),

    # Rejected Loan Applications Summary
    path('rejected-loan-applications/', views.rejected_loan_application,name="rejected_loan_application"),

    # Rejected Loan Applications Reason
    path('rejected-loan-applications/reason/<int:id>/', views.rejected_loan_application_reason,name="rejected_loan_application_reason"),

    # Approved Loan Applications Summary
    path('approved-loan-applications/', views.approved_loan_application,name="approved_loan_application"),

    # Disbursed Loan Applications Summary
    path('disbursed-loan-applications/', views.disbursed_loan_application,name="disbursed_loan_application"),

    path('disbursed-loan-application/<int:id>/', views.disbursed_application,name="disbursed_application"),

    # Loan Repayment Schedule
    path('loan-schedule/<int:id>/',views.loan_schedule,name='loan_schedule_csv'),

    # Forgot/Reset Password
    path('forgot-password/', auth_views.PasswordResetView.as_view(template_name='reset/password_reset.html',
    email_template_name = 'reset/password_reset_email.html',
    success_url = reverse_lazy('loan_app:password_reset_done')),
    name='password_reset'),

    path('forgot-password/sent/', auth_views.PasswordResetDoneView.as_view(template_name='reset/password_reset_done.html'),  name='password_reset_done'),
    
    path('forgot-password/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='reset/password_reset_form.html',success_url = reverse_lazy('loan_app:password_reset_complete')), name='password_reset_confirm'),

    path('forgot-password/complete/', auth_views.PasswordResetCompleteView.as_view(template_name='reset/password_reset_complete.html'), name='password_reset_complete'),

    # Payment Schedule/History
    path('payment_schedule/',views.loan_schedule_history,name='loan_schedule_history'),

    # Payment Success Using Gateway
    path('payment_success/<int:id>/',views.success_payment,name='success_payment'),

    # Defaulters List (Not pay EMI for last 3 consecutive months)
    path('defaulters_list/',views.defaulters_list,name='defaulters_list'),
    path('defaulters_remarks/<int:id>/',views.defaulters_list_remarks,name='defaulters_list_remarks'),

    # EMI Due Reminders
    path('emi_due_reminders/list/',views.emi_due_reminders,name='reminders_list'),
]
