import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-)5qd1zz2tuxsgmv33gk9l*fy7dk0l@&55^r3r*xr*v0#k_r+=p'

DEBUG = True

ALLOWED_HOSTS = []
import os

# Get the current directory where the settings.py file is located
current_directory = os.path.dirname(os.path.abspath(__file__))

# Move back to the parent directory
parent_directory = os.path.dirname(current_directory)
media_folder_path = os.path.join(parent_directory, 'media')

INSTALLED_APPS = [
    'django_crontab',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'loan_app.apps.LoanAppConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'loan_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'loan_project.wsgi.application'


# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'loan_management_system',
#         'PORT': 3306,
#         'USER': 'root',
#         'PASSWORD': 'rootpassword',
#         'HOST': 'localhost',
#     }
# }



AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR,'static')

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SESSION_COOKIE_AGE = 43200  # (Auto Logout) In Seconds

EMAIL_HOST= "smtp.gmail.com"
EMAIL_PORT= 587
EMAIL_HOST_USER= 'info.eshikshapie@gmail.com'
EMAIL_HOST_PASSWORD= 'PulkitArora@2001'
EMAIL_USE_TLS= True


razorpay_test_key = 'rzp_test_puB8XsnY3rMKeW'
razorpay_test_secret_key = 'Uqnd7TgykjF7bGvCt1hhYRNa'


CRONJOBS = [
    ('59 23 * * *', 'loan_app.cron.emi_due_reminder'),
    ('59 23 * * *', 'loan_app.cron.defaulters_list'),
    ('59 23 * * *', 'loan_app.cron.loan_completed'),
]