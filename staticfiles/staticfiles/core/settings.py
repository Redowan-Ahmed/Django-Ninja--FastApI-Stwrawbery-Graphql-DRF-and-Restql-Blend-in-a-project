from pathlib import Path
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
                 'mercegrower.com', 'redowan.mercegrower.com']

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',

    # Third party Apps
    'rest_framework',
    'colorfield',
    'ckeditor',
    'ckeditor_uploader',
    'corsheaders',

    # inner Apps
    'portfolio',

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
    BASE_DIR, "static",
]
# STATICFILES_STORAGE = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

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
    "user_avatar": None,
    ############
    # Top Menu #
    ############
    # List of model admins to search from the search bar, search bar omitted if excluded
    # If you want to use a single search field you dont need to use a list, you can use a simple string 
    "search_model": ["auth.User", "auth.Group"],
    # Links to put along the top menu
    "topmenu_links": [
        # Url that gets reversed (Permissions can be added)
        {"name": "Visit Portfolio", "url": "home",
            "permissions": ["auth.view_user"]},
        # model admin to link to (Permissions checked against model)
        {"model": "auth.User"},
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
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "users.User": "fas fa-user",
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
        "auth.user": "collapsible",
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
