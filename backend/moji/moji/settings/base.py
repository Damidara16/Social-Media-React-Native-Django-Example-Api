import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'p32o79th6p2=f88w-ev4var@*u__7f!cp$r#7*@1oh=m@8+e02'
#SECRET_KEY = os.environ.get('SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [] 

#EMAIL
#if DEBUG == True:
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
#else:
#EMAIL_HOST = 'smtp.gmail.com'
#EMAIL_HOST_USER = 'yourgmail@gmail.com'
#EMAIL_HOST_PASSWORD = 'yourpassword'
#EMAIL_PORT = '587'
#EMAIL_USE_TLS = True
# Application definition
AUTH_USER_MODEL = "account.User"
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'account',
    'pages',
    'content',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders'
]

    #'home',
    #'banking',
    #'product',
    #'notif'
def verify_following(f_user_following,c_user):
    return f_user.profile.following.filter(user=c_user).exists()
#FILE_UPLOAD_HANDLERS = []
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'moji.middleware.CorsMiddleware'
    #'moji.middleware.AuthRequiredMiddleware',
    #'moji.middleware.BlockedMiddleware',
]

ROOT_URLCONF = 'moji.urls'

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

WSGI_APPLICATION = 'moji.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

#MEDIA_URL = '/media/'
#MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

AUTHENTICATION_BACKENDS = ['django.contrib.auth.backends.ModelBackend']
LOGIN_REDIRECT_URL = '/home'

AUTH_URL = '/accounts/login/'

AUTH_REQUIRED_URLS = (
    r'^account/update/profile/$'
    r'^account/create/user/$'
    r'^account/manage/block_unblock/$'
    r'^account/delete/user/$'
    r'^account/update/authed_password/$'
    r'^account/get/following/$'
    r'^account/get/followers/$'
    r'^account/post/remove_follower/$'
)
SUB_POPUP_URLS = (
    r'^content/detail/(?P<uuid>[\w]{8}(-[\w]{4}){3}-[\w]{12})/$',
    r'^product/sub/(?P<uuid>[\w]{8}(-[\w]{4}){3}-[\w]{12})/$',
    r'^product/subscription/(?P<uuid>[\w]{8}(-[\w]{4}){3}-[\w]{12})/$',
    r'^product/tipcreation/(?P<name>\w+)/$',
)

BLOCKED_URLS = (
    r'^profile/(?P<name>\w+)/$',
    r'^detail/(?P<uuid>[\w]{8}(-[\w]{4}){3}-[\w]{12})/$',
    r'^following/requests/(?P<name>\w+)/$',
    r'^following/requests/(?P<name>\w+)/accept/$',
    r'^following/requests/(?P<name>\w+)/decline/$',
    r'^following/requests/(?P<name>\w+)/sent/$',
)

STRIPE_KEY = "sk_test_jTTjKLvfrEeL6cXjKqoF1KdB"

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
     'DEFAULT_PERMISSION_CLASSES':[
        'rest_framework.permissions.IsAuthenticated',
    ]
}

CORS_REPLACE_HTTPS_REFERER      = False
HOST_SCHEME                     = "http://"
SECURE_PROXY_SSL_HEADER         = None
SECURE_SSL_REDIRECT             = False
SESSION_COOKIE_SECURE           = False
CSRF_COOKIE_SECURE              = False
SECURE_HSTS_SECONDS             = None
SECURE_HSTS_INCLUDE_SUBDOMAINS  = False
SECURE_FRAME_DENY               = False
