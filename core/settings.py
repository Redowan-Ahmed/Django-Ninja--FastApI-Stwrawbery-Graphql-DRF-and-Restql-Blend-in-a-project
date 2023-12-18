from datetime import timedelta
from pathlib import Path
from corsheaders.defaults import default_headers
import os
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-mhss6+o@%%iwlor4hf)!orshfc_epwivx9!sfbf%nx_y9srp&8'
DEBUG = True
CORS_ALLOWED_ORIGINS = [
    "https://mercegrower.com",
    "https://redowan.mercegrower.com",
    "http://localhost:8000",
    "http://localhost:5173",
]

CORS_ALLOW_METHODS = (
    "GET",
    "OPTIONS",
    "POST",
)
ALLOWED_HOSTS = ['localhost', '127.0.0.1',
                 'mercegrower.com', 'redowan.mercegrower.com', '*']


ALLOWED_HEADER_FOR_FRONTEND = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3NTQ2NTQ2ODQ2NTQxNTE5ODE1NjE4ODkwIiwibmFtZSI6IlJlZG93YW4gQWhtZWQiLCJpYXQiOjEuNTE2MjM5MDIyNzQ1NDQ2NWUrMzksIndlYnNpdGUiOiJodHRwczovL3JlZG93YW4ubWVyY2Vncm93ZXIuY29tLyJ9.LqkkmeKglcJNzP6KRFtGV6brqCJ7VQ5RFauVioQqlvU'


NINJA_PAGINATION_PAGE_SIZE = 1

INSTALLED_APPS = [
    # Third Party Prio App
    'jazzmin',

    # Inner Battery Apps
   'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',

    # Third party Apps
    'graphene_django',
    'graphql_jwt.refresh_token.apps.RefreshTokenConfig',
    'rest_framework',
    'colorfield',
    'ckeditor',
    'ckeditor_uploader',
    'corsheaders',
    'easy_thumbnails',
    #'filer',


    # inner Apps
    'portfolio',
    'account',

]

CORS_ALLOW_HEADERS = [
    *default_headers,
    "decoader552",
    "decoader221",
    "decoader772"
]

AUTH_USER_MODEL = 'account.CustomUser'

GRAPHENE = {
    "SCHEMA": "core.schema.schema",
    "MIDDLEWARE": [
        "graphql_jwt.middleware.JSONWebTokenMiddleware",
    ],
}

GRAPHQL_JWT = {
    "JWT_VERIFY_EXPIRATION": True,
    "JWT_LONG_RUNNING_REFRESH_TOKEN": True,
    "JWT_EXPIRATION_DELTA": timedelta(minutes=5),
    "JWT_REFRESH_EXPIRATION_DELTA": timedelta(days=7),
    "JWT_REFRESH_EXPIRED_HANDLER": lambda orig_iat, context: False,
}

AUTHENTICATION_BACKENDS = [
    "graphql_jwt.backends.JSONWebTokenBackend",
    "django.contrib.auth.backends.ModelBackend",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
   # 'portfolio.middelwares.CustomSecurityMiddleware'
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
""" 'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
} """

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': BASE_DIR / 'cache',
    }
}
# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = '/uploads/'
MEDIA_ROOT = BASE_DIR / "uploads"

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

#STATICFILES_STORAGE = "'django.contrib.staticfiles.storage.StaticFilesStorage'"
#STATICFILES_STORAGE = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"
#STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

WHITENOISE_AUTOREFRESH = True  # Serve fresh static files in development
WHITENOISE_USE_FINDERS = True  # Look for static files using Django's finders

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
CKEDITOR_UPLOAD_PATH = "uploads/"

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
    }
}

JAZZMIN_SETTINGS = {
    "site_title": "Redowan Ahmed",
    "site_header": "Redowan Ahmed",
    "site_brand": "Redowan Ahmed",
    "site_icon": None,
    "custom_css": "css/index.css",
    # Add your own branding here
    "site_logo": 'static/media/logo.png',
    # Logo to use for login form in dark themes (defaults to login_logo)
    "login_logo_dark": 'static/media/logo.png',
    "site_logo_classes": "img-circle",


    "welcome_sign": "Welcome to the Redowan Ahmed Portfolio Backend",
    # Copyright on the footer
    "copyright": "Redowan Ahmed",
    "user_avatar": 'profile_picture',
    ############
    # Top Menu #
    ############
    # List of model admins to search from the search bar, search bar omitted if excluded
    # If you want to use a single search field you dont need to use a list, you can use a simple string 
    "search_model": ["account.CustomUser", "auth.Group"],
    # Links to put along the top menu
    "topmenu_links": [
        # Url that gets reversed (Permissions can be added)
        {"name": "Visit Portfolio", "url": "/home",
        "permissions": ["account.CustomUser.view_user"]},
        # model admin to link to (Permissions checked against model)
        {"model": "account.CustomUser"},
        {"app": "portfolio"},
    ],
    #############
    # Side Menu #
    #############
    # Whether to display the side menu
    "show_sidebar": True,

    # Whether to aut expand the menu
    "navigation_expanded": True,
    "icons": {
        "account": "fas fa-users-cog",
        "account.CustomUser": "fas fa-user",
        "account.CustomUser": "fas fa-user",
        "auth.Group": "fas fa-users",
        "admin.LogEntry": "fas fa-file",
        'portfolio.Contact': 'fas fa-users',
        'portfolio.Skill': 'fas fa-code',
        'portfolio.Project': 'fas fa-code-branch',
        'portfolio.SocialMedia': 'fas fa-globe-asia',
        'portfolio.WorkExperience': 'fas fa-laptop-code',
    },
    # # Icons that are used when one is not manually specified
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-arrow-circle-right",
    #################
    # Related Modal #
    #################
    # Use modals instead of popups
    "related_modal_active": False,
    #############
    # UI Tweaks #
    #############
    # Relative paths to custom CSS/JS scripts (must be present in static files)
    # Uncomment this line once you create the bootstrap-dark.css file
    # "custom_css": "css/bootstrap-dark.css",
    "custom_js": None,
    # Whether to show the UI customizer on the sidebar
    "show_ui_builder": False,
    ###############
    # Change view #
    ###############
    "changeform_format": "horizontal_tabs",
    # override change forms on a per modeladmin basis
    "changeform_format_overrides": {
        "account.CustomUser": "collapsible",
        "auth.group": "vertical_tabs",
    },
}

JAZZMIN_UI_TWEAKS = {
    "actions_sticky_top": True,
    "sidebar_nav_child_indent": True,
    "sidebar_nav_compact_style": True,
    "sidebar_fixed": True,
    "theme": "default",
    "navbar": "navbar-navy navbar-dark",
    "brand_colour": "navbar-primary",
    "accent": "accent-primary",
}

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    #'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)
FILER_CANONICAL_URL = 'sharing/'

FILER_STORAGES = {
    'public': {
        'main': {
            'ENGINE': 'filer.storage.PublicFileSystemStorage',
            'OPTIONS': {
                'location': '/path/to/media/filer',
                'base_url': '/media/filer/',
            },
            'UPLOAD_TO': 'filer.utils.generate_filename.randomized',
            'UPLOAD_TO_PREFIX': 'filer_public',
        },
        'thumbnails': {
            'ENGINE': 'filer.storage.PublicFileSystemStorage',
            'OPTIONS': {
                'location': '/path/to/media/filer_thumbnails',
                'base_url': '/media/filer_thumbnails/',
            },
        },
    },
    'private': {
        'main': {
            'ENGINE': 'filer.storage.PrivateFileSystemStorage',
            'OPTIONS': {
                'location': '/path/to/smedia/filer',
                'base_url': '/smedia/filer/',
            },
            'UPLOAD_TO': 'filer.utils.generate_filename.randomized',
            'UPLOAD_TO_PREFIX': 'filer_public',
        },
        'thumbnails': {
            'ENGINE': 'filer.storage.PrivateFileSystemStorage',
            'OPTIONS': {
                'location': '/path/to/smedia/filer_thumbnails',
                'base_url': '/smedia/filer_thumbnails/',
            },
        },
    },
}