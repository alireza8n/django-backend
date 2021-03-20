from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.admin import site
from django.urls import path
from django.utils.translation import gettext_lazy

site.site_title = gettext_lazy("Boilerplate")
site.site_header = gettext_lazy("Boilerplate")
site.index_title = gettext_lazy("Boilerplate")

admin_urlpatterns = i18n_patterns(
    path("admin/", admin.site.urls, name="admin"),
    prefix_default_language=False,
)
