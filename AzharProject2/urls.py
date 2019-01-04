from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('App1.urls')),
    # arguments in include must be in "'"
    path('admin/', admin.site.urls),
    # arguments in path need not be in "'"
]
