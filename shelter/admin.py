from django.contrib import admin
from .models import Listening,Quickcontact,AgentContact

# Register your models here.
class ListeningAdmin(admin.ModelAdmin):
    list_display = ('title','agent','location','price','area','bedrooms','bathrooms','available','status')
    search_fields = ['title','location','price']
    list_filter = ('agent',)

class UserAgentContactAdmin(admin.ModelAdmin):
    list_display = ('agentname','user_name','user_email','user_subject')
    search_fields = ['agentname']

admin.site.register(Listening,ListeningAdmin)
admin.site.register(Quickcontact)
admin.site.register(AgentContact,UserAgentContactAdmin)


