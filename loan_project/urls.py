from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('loan_app.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "LOANPAY"
admin.site.site_title = "LOANPAY:Loan Management System"
admin.site.index_title = "Welcome to LOANPAY Admin Portal"