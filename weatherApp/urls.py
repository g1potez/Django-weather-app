from django.contrib import admin
from django.urls import path
import web.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', web.views.index, name='index')
]
