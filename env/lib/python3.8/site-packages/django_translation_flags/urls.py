from django.urls import path, include

urlpatterns = [
    path('', include('django.conf.urls.i18n')),
]