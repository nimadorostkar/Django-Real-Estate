from django.urls import path
from .views import (ListingListView, ListingDetailView, search)


urlpatterns = [
    path('', ListingListView.as_view(), name='listings'),
    path('<int:pk>', ListingDetailView.as_view(), name='listing'),
    path('search', search, name='search'),
]
