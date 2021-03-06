import os  
from os.path import abspath, basename, dirname, join, normpath
import urls

# Replace BASE_DIR with this
DJANGO_ROOT = dirname(dirname(abspath(__file__)))  
SITE_ROOT = dirname(DJANGO_ROOT)  
SITE_NAME = basename(DJANGO_ROOT)

SECRET_KEY = 'de%n%m+8@ohw+2o9l0pyyl%d7ndtbxd4#r4j+e*7f@03=es6zi'
ROOT_URLCONF = urls

DEBUG = 1

INSTALLED_APPS = (  
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.auth',

    # Pipeline
    'pipeline',

    # DRF
    'rest_framework',
)

# Configure templates
TEMPLATES = [  
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'  
STATIC_ROOT = normpath(join(SITE_ROOT, 'static'))  
STATICFILES_DIRS = ()  

# Django Pipeline (and browserify)
STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

STATICFILES_FINDERS = (  
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)

# browserify-specific
PIPELINE_COMPILERS = (  
    'pipeline_browserify.compiler.BrowserifyCompiler',
)

PIPELINE_CSS_COMPRESSOR = 'pipeline.compressors.NoopCompressor'  
PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.uglifyjs.UglifyJSCompressor'

if DEBUG:  
    PIPELINE_BROWSERIFY_ARGUMENTS = '-t babelify'

PIPELINE = {  
    'mysite_css': {
        'source_filenames': (
            'css/style.css',
        ),
        'output_filename': 'css/mysite_css.css',
    },
}

PIPELINE = {  
    'mysite_js': {
        'source_filenames': (
            'js/bower_components/jquery/dist/jquery.min.js',
            'js/bower_components/react/JSXTransformer.js',
            'js/bower_components/react/react-with-addons.js',
            'js/app.browserify.js',
        ),
        'output_filename': 'js/mysite_js.js',
    }
}
