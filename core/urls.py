from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from bot1.views import *

urlpatterns = [
    path("", test),
    path("admin/", admin.site.urls),
    path("bot1/", webhook),
    path("bot2/", webhook2),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
