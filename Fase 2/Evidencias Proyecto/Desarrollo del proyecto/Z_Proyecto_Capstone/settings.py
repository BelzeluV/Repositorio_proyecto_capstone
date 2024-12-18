from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-&^fl4&ah_l@7p0elf3@n+naw4&!n6=*jd5^c^hv8s(+g(w2&0!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_REDIRECT_URL = '/validations/'

LOGOUT_REDIRECT_URL = '/'
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# settings.py

QUILL_CONFIGS = {
    'default': {  # Configuración completa, permite todo
        'theme': 'snow',
        'modules': {
            'toolbar': [
                [{'header': [1, 2, 3, False]}],  # Títulos
                ['bold', 'italic', 'underline', 'strike'],  # Estilos de texto
                [{'list': 'ordered'}, {'list': 'bullet'}],  # Listas
                ['link', 'image', 'code-block'],  # Permite imágenes y bloques de código
            ]
        }
    },
    'restricted': {  # Configuración sin imágenes ni código
        'theme': 'snow',
        'modules': {
            'toolbar': [
                [{'header': [1, 2, 3, False]}],  # Títulos
                ['bold', 'italic', 'underline', 'strike'],  # Estilos de texto
                [{'list': 'ordered'}, {'list': 'bullet'}],  # Listas
                ['link'],  # Solo enlaces, sin imagen ni código
            ]
        }
    }
}

# Application definition

INSTALLED_APPS = [
    'Store.apps.StoreConfig',
    'Classes.apps.ClassesConfig',
    'Library.apps.LibraryConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django_quill',
    'crispy_forms',
    'crispy_bootstrap4',
    'livereload',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'livereload.middleware.LiveReloadScript',
]

MIDDLEWARE_CLASSES = (
    'livereload.middleware.LiveReloadScript',
)

ROOT_URLCONF = 'Z_Proyecto_Capstone.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["Store/Templates","Forum/Templates","Classes/Templates", "Library/Templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'Store.Cart.context_processor.importe_total_carro',

            ],
        },
    },
]

WSGI_APPLICATION = 'Z_Proyecto_Capstone.wsgi.application'




# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'oracle': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': 'xe',
        'USER': 'usuariodjango',
        'PASSWORD': 'asdfqwer1234',
        'HOST': '192.168.1.111',
        'PORT': '1521',
    },
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
AUTH_USER_MODEL = 'Store.Usuario'

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

LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'UTC'

TIME_INPUT_FORMATS = [
    '%H:%M',    # Ejemplo: 14:30
    '%H:%M:%S', # Ejemplo: 14:30:00
]


USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_URL = '/static/'     

STATICFILES_DIRS = [BASE_DIR / "static"]


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field
FILE_UPLOAD_HANDLERS = [
    'django.core.files.uploadhandler.MemoryFileUploadHandler',
    'django.core.files.uploadhandler.TemporaryFileUploadHandler',
]


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


"""
Django settings for Proyecto_Integracion project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
