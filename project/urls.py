from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from contacts.views import AdminContactView
from django.contrib.auth import views as auth_views
# from django.conf.urls import (handler400, handler403, handler404, handler500)

handler400 = 'core.views.bad_request'
handler403 = 'core.views.permission_denied'
handler404 = 'core.views.page_not_found'
handler500 = 'core.views.server_error'


urlpatterns = i18n_patterns(
    path('i18n/', include('django_translation_flags.urls')),
    path('admin/', admin.site.urls),
    path('admin/contact/', AdminContactView.as_view(), name='admin-contact'),

    path('', include('core.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/auth/password_reset_done.html'),
         name='password-reset-done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(  # noqa
        template_name="accounts/auth/password_reset_confirm.html"),
         name='password-reset-confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/auth/password_reset_complete.html'),
         name='password_reset_complete'),

    path('listings/', include('listings.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('allauth.urls')),
    path('contacts/', include('contacts.urls')),
    path('listings/', include('documents.urls')),

)


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
