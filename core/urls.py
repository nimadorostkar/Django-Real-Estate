from django.urls import path

from .views import (IndexView, AboutView, ImpressumView, PrivacyView,
                    RobotsTXTView)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('robots.txt', RobotsTXTView.as_view(content_type="text/plain")),
    path('about-us', AboutView.as_view(), name='about'),
    path('impressum', ImpressumView.as_view(), name="impressum"),
    path('privacy', PrivacyView.as_view(), name="privacy"),

]
