django-sfibase
==============

Common base for all SFI projects based on Django.

## What it handles
* Authentication with SFI SSO and auto user creation
* Consistent base template with top navbar
* Perfectionist's touches (e.g. l10n fixes)

## Usage
1. `pip install -e git+https://git.sfi.pl/scm/djbase/django-sfibase.git#egg=django-sfibase`
2. In your `settings.py`:
   * At the top, add:
     ```python
     from sfi_base.base_settings import *
     ```
   * Add to your `INSTALLED_APPS` list:
     ```python
     INSTALLED_APPS = [
         # Django apps
         'sfi_base',
         # Your apps
     ]
     ```
   * Add to your `MIDDLEWARE` list:
     ```python
     MIDDLEWARE = [
         ...
         'sfi_base.middleware.TryAuthenticateMiddleware',
         'sfi_base.middleware.ForceAdminInEnglish',
     ]
     ```
   * Modify your `AUTHENTICATION_BACKENDS`:
     ```python
     AUTHENTICATION_BACKENDS = (
         'django.contrib.auth.backends.ModelBackend',
         'sfi_base.auth.OIDCAuthenticationBackend',
     )
     ```
3. In your `urls.py`, add:
   ```python
   path('oidc/', include('sfi_base.urls')),
   ```
4. In your base template file, use:
   ```djangotemplate
   {% extends "sfi_base/base.html" %}
   ```
