<div align="center" width="100%">
    <h1>Django-Ultimate</h1>
    <img width="150px" src="myapp/static/assets/img/logo.png">
    <p>The ultimative Django 5 Boostrap Template</p><p>
    <a target="_blank" href="https://github.com/l4rm4nd"><img src="https://img.shields.io/badge/maintainer-LRVT-orange" /></a>
    <a target="_blank" href="https://GitHub.com/l4rm4nd/Django-Ultimate/graphs/contributors/"><img src="https://img.shields.io/github/contributors/l4rm4nd/Django-Ultimate.svg" /></a>
    <a target="_blank" href="https://github.com/PyCQA/bandit"><img src="https://img.shields.io/badge/security-bandit-yellow.svg"/></a><br>
    <a target="_blank" href="https://GitHub.com/l4rm4nd/Django-Ultimate/commits/"><img src="https://img.shields.io/github/last-commit/l4rm4nd/Django-Ultimate.svg" /></a>
    <a target="_blank" href="https://GitHub.com/l4rm4nd/Django-Ultimate/issues/"><img src="https://img.shields.io/github/issues/l4rm4nd/Django-Ultimate.svg" /></a>
    <a target="_blank" href="https://github.com/l4rm4nd/Django-Ultimate/issues?q=is%3Aissue+is%3Aclosed"><img src="https://img.shields.io/github/issues-closed/l4rm4nd/Django-Ultimate.svg" /></a><br>
        <a target="_blank" href="https://github.com/l4rm4nd/Django-Ultimate/stargazers"><img src="https://img.shields.io/github/stars/l4rm4nd/Django-Ultimate.svg?style=social&label=Star" /></a>
    <a target="_blank" href="https://github.com/l4rm4nd/Django-Ultimate/network/members"><img src="https://img.shields.io/github/forks/l4rm4nd/Django-Ultimate.svg?style=social&label=Fork" /></a>
    <a target="_blank" href="https://github.com/l4rm4nd/Django-Ultimate/watchers"><img src="https://img.shields.io/github/watchers/l4rm4nd/Django-Ultimate.svg?style=social&label=Watch" /></a><br>
    <a href="https://www.buymeacoffee.com/LRVT" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>
</div>

## ⭐ Features

- Django Framework (v5) + SQLite3 Database
- Nice Admin Bootstrap Template with light/dark theme
- Django-Celery-Beat for Periodic Task Execution
- OIDC Single-Sign-On via `mozilla-django-oidc`
- Custom Login Panel with support for local auth and OIDC SSO
- GitHub Action for automatic changelogs, releases, code SAST scanning and docker image builds based on Conventional Commits specification

## 💡 Usage

````
# clone this repository
git clone https://github.com/l4rm4nd/Django-Ultimate && cd Django-Ultimate

# create virtual environment and activate
virtualenv venv
source venv/bin/activate

# install requirements
pip install -r requirements.txt

# collect migrations
python manage.py makemigrations
python manage.py makemigrations myapp

# migrate
python manage.py migrate
python manage.py migrate myapp

# create superuser
python manage.py createsuperuser

# spawn the development server
python manage.py runserver 127.0.0.1:8000 --insecure
````

## 🌏 Environment Variables

Django Ultimate template takes various environment variables to configure `settings.py`:

| Variable                         | Description                                                                                                     | Default                    | Optional/Mandatory  |
|----------------------------------|-----------------------------------------------------------------------------------------------------------------|----------------------------|---------------------|
| `DOMAIN`                         | Your Fully Qualified Domain Name (FQDN) or IP address. Used to define `ALLOWED_HOSTS` and `CSRF_TRUSTED_ORIGINS` for the Django framework. | `localhost` | Mandatory           |
| `SECURE_COOKIES`                 | Set to `True` if you use a reverse proxy with TLS. Enables the `secure` cookie flag and `HSTS` HTTP response header, which will only work for SSL/TLS encrypted communication channels (HTTPS). | `False`                    | Optional            |
| `SECRET_KEY`                     | Defines a fixed secret key for the Django framework. If missing, a secure secret is auto-generated on the server-side each time the container starts. | `<auto-generated>`         | Optional            |
| `PORT`                           | Defines a custom port. Used to set `CSRF_TRUSTED_ORIGINS` in conjunction with the `DOMAIN` environment variable for the Django framework. Only necessary, if VoucherVault is operated on a different port than `8000`, `80` or `443`. | `8000`                     | Optional            |
| `REDIS_HOST`                     | Defines the Redis instance to use for Django-Celery-Beat task processing.                                       | `redis`                    | Optional            |
| `OIDC_ENABLED`                   | Set to `True` to enable OIDC authentication.                                                                    | `False`                    | Optional            |
| `OIDC_CREATE_USER`               | Set to `True` to allow the creation of new users through OIDC.                                                  | `True`                     | Optional            |
| `OIDC_RP_SIGN_ALGO`              | The signing algorithm used by the OIDC provider (e.g., RS256, HS256).                                           | `HS256`                    | Optional            |
| `OIDC_RP_IDP_SIGN_KEY`           | The signing key used by the OIDC provider. If RS256 signing algo is used, either this or `OIDC_OP_JWKS_ENDPOINT` must be defined.                                                   | `None`                     | Optional            |
| `OIDC_OP_JWKS_ENDPOINT`          | URL of the JWKS endpoint for the OIDC provider. If RS256 signing algo is used, either this or `OIDC_RP_IDP_SIGN_KEY` must be defined.                                                                | `None`                     | Optional            |
| `OIDC_RP_CLIENT_ID`              | Client ID for your OIDC RP.                                                                                     | `None`                     | Optional            |
| `OIDC_RP_CLIENT_SECRET`          | Client secret for your OIDC RP.                                                                                 | `None`                     | Optional            |
| `OIDC_OP_AUTHORIZATION_ENDPOINT` | Authorization endpoint URL of the OIDC provider.                                                                | `None`                     | Optional            |
| `OIDC_OP_TOKEN_ENDPOINT`         | Token endpoint URL of the OIDC provider.                                                                        | `None`                     | Optional            |
| `OIDC_OP_USER_ENDPOINT`          | User info endpoint URL of the OIDC provider.                                                                    | `None`                     | Optional            |
| `OIDC_RENEW_ID_TOKEN_EXPIRY_SECONDS`          | The length of time it takes for an id token to expire in seconds.                                                                    | 900                     | Optional            |

## 📷 Screenshots

![PoC](https://github.com/user-attachments/assets/19a06770-fa54-4ce9-8934-da838a721650)

![image](https://github.com/user-attachments/assets/b86093ec-4677-41a9-9e62-3dfde1309738)
