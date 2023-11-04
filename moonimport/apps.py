from django.apps import AppConfig

from . import __version__


class MoonImportConfig(AppConfig):
    name = 'moonimport'
    label = 'moonimport'

    verbose_name = f"Moon Import v{__version__}"
