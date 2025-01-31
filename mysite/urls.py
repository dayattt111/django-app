from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("testing.urls")),
    # path("absen_masuk/", include("testing.urls")),
    # path("absen_keluar/", include("testing.urls")),
    # path("data_rekapan/", include("testing.urls")),
    path('admin/', admin.site.urls),
]
