from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import (TemplateView)
from django.utils.translation import ugettext_lazy as _

from core.models import State
from listings.models import Listing, ListingType
from accounts.models import Realtor


def bad_request(request, exception):
    return render(request, 'core/errors/400.html', status=400)


def permission_denied(request, exception):
    return render(request, 'core/errors/403.html', status=403)


def page_not_found(request, exception):
    return render(request, 'core/errors/404.html', status=404)


def server_error(request):
    return render(request, 'core/errors/500.html', status=500)


class IndexView(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['listings'] = Listing.objects.order_by('-created').filter(
                               is_published=True)[:3]
        context['states'] = State.objects.all()
        context['list_types'] = ListingType.objects.all()
        context['index'] = True
        # SEO
        context['page_title'] = _("Real estate manager."
                                  " Renting, buying and selling.")
        context['page_description'] = _("Real estate manager. We offer"
                                        " real estate objects and takes care"
                                        " of every aspect for you. Services"
                                        " offered: renting, selling, buying,"
                                        " consultation and way more.")
        return context


class AboutView(TemplateView):
    template_name = 'core/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['realtors'] = Realtor.objects.order_by('-hire_date')
        # Showcase Section Infos
        context['title'] = _("About us")
        context['subtitle'] = _("Real Estate and Consulting")
        # SEO
        context['page_title'] = _("About Us")
        context['page_description'] = _("Real estate manager."
                                        "Our services include "
                                        "renting, selling, buying, consulting "
                                        "and much more.")
        return context


class PrivacyView(TemplateView):
    template_name = 'core/privacy.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Showcase Section Infos
        context['title'] = _("Privacy")
        context['subtitle'] = _("Real-Estate")
        # SEO
        context['page_title'] = _("Privacy")
        context['page_description'] = _("Real estate manager."
                                        "This is our privacy page.")
        return context


class ImpressumView(TemplateView):
    template_name = 'core/impressum.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Showcase Section Infos
        context['title'] = _("Impressum")
        context['subtitle'] = _("Real-Estate")
        # SEO
        context['page_title'] = _("Impressum")
        context['page_description'] = _("Real estate manager."
                                        "This is our impressum page.")
        return context



class RobotsTXTView(TemplateView):
    template_name = 'core/robots.txt'
