from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/v1/accounts/', include('account.urls')),
    path('admin/', admin.site.urls),
]
