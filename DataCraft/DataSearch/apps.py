from django.apps import AppConfig
# from .signals import index_data
from django.utils.translation import ugettext_lazy as _

class DatasearchConfig(AppConfig):
    name = 'DataSearch'
    verbose_name = _('DataSearch')
    def ready(self):
        import DataSearch.signals