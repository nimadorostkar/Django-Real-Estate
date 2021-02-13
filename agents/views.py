from django.shortcuts import render,get_object_or_404
from .models import Agent

# Create your views here.

def agentList(request):
    agents = Agent.objects.all()
    return render(request,'agents/agents_list.html',{'agents':agents})


def agentDetail(request,agent_id):
    agent = get_object_or_404(Agent,id=agent_id)
    return render(request,'agents/agent_detail.html',{'agent':agent})
