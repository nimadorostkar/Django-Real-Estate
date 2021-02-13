from django.urls import path
from . import views
urlpatterns = [
    path('',views.agentList,name='agents_list'),
    path('agent-detail/<int:agent_id>/',views.agentDetail,name='agent_detail'),
]