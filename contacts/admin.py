from django.contrib import admin
from crum import get_current_user

from .models import Contact, ChatMessage


class InlineChatMessageAdmin(admin.StackedInline):
    model = ChatMessage

    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return self.readonly_fields + ('contact', 'user', 'message',
                                           'timestamp')
        return self.readonly_fields


@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('contact', 'user', 'message', 'timestamp', 'get_read')

    def get_read(self, obj):
        user = get_current_user()
        if obj.user.id == user.id:
            return f"Yes {user.first_name} - {obj.user.first_name}"
        else:
            return f"No {user.first_name}  - {obj.user.first_name}"

    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return self.readonly_fields + ('contact', 'user', 'message',
                                           'timestamp')
        return self.readonly_fields


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    inlines = [InlineChatMessageAdmin]
    autocomplete_fields = ('user', 'listing')
    list_display = ('id', 'get_full_name', 'get_email', 'listing', 'phone',
                    'message', 'contact_date', 'can_access_documents')
    list_display_links = ('id', 'get_full_name')
    list_editable = ('can_access_documents',)
    list_filter = ['listing', 'can_access_documents']
    search_fields = ('user__first_name', 'user__email', 'listing__title')
    readonly_fields = ('contact_date',)
    list_per_page = 25

    def get_contact_msg_link(self):
        return 2

class CustomAdminSite(admin.AdminSite):
    pass
