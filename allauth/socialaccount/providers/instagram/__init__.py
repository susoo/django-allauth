from django.apps import AppConfig


class InstagramConfig(AppConfig):
    name = 'allauth.socialaccount.providers.instagram'
    label = 'allauth_instagram'


default_app_config = 'allauth.socialaccount.providers.instagram.InstagramConfig'git status

