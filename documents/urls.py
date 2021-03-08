from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import (ListingDocumentView, UserDocumentView)


urlpatterns = [
    path('<int:pk>/docs/', ListingDocumentView.as_view(), name='documents'),
    path('profile/', login_required(UserDocumentView.as_view()),
         name='user-docs'),
]
