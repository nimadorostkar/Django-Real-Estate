from django.urls import path
from .views import (anonymous_contact, user_contact, chat_message,
                    MessageHistoryListView)


urlpatterns = [
    path('anonymous-contact', anonymous_contact, name='anonymous-contact'),
    path('user-contact', user_contact, name='user-contact'),
    path('chat', chat_message, name='chat'),
    path('history/<int:pk>', MessageHistoryListView.as_view(), name='chat-history'),
]
