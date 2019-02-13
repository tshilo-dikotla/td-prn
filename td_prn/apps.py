from django.apps import AppConfig as DjangoAppConfig
from django.core.management.color import color_style

style = color_style()


class AppConfig(DjangoAppConfig):
    name = 'td_prn'
    verbose_name = 'Tshilo dikotla prn'
