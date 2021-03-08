from django.utils.translation import gettext_lazy as _
from django.views.generic import (DetailView, TemplateView)
from django.utils.html import format_html

from listings.models import Listing
from contacts.models import Contact


class UserDocumentView(DetailView):
    model = Listing
    template_name = 'documents/documents.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact'] = Contact.objects.get(listing_id=self.object.id,
                                                 user_id=self.request.user.id)
        # Showcase Section Infos
        context['title'] = _("Documents")
        context['subtitle'] = _("Manage your own documents")
        # SEO
        context['page_title'] = _("User documents")
        context['page_description'] = _("Real estate manager."
                                        "Here you can upload and manage your "
                                        "own documents")
        return context


class ListingDocumentView(TemplateView):
    template_name = 'documents/user-documents.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['docs'] = True
        # Showcase Section Infos
        context['title'] = self.object.listing.title
        context['subtitle'] = format_html(f'<i class="fas fa-map-marker"></i>'
                                          f' {self.object.listing.address}')
        # SEO
        context['page_title'] = _("Documents")
        context['page_description'] = _("Real estate manager."
                                        "Here you can manage your documents, "
                                        "related to a specific object you are "
                                        "interested in.")
        return context
