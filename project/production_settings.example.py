# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'replace with secret key'

DEBUG = False

ALLOWED_HOSTS = ['your-domain.com']

# Email Config example gmail
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'your-email'
EMAIL_HOST_PASSWORD = 'your-password'
EMAIL_USE_TLS = True

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 3600
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True