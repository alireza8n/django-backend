from django.conf import settings

from .admin_configuration import *
from .local_urls import local_urlpatterns

urlpatterns = admin_urlpatterns + local_urlpatterns

if settings.DEBUG:
    from .development_urls import development_urlpatterns

    urlpatterns += development_urlpatterns
