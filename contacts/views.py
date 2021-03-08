from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact, ChatMessage
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext_lazy as _
from django.core.paginator import Paginator
from django.views.generic import (DetailView, TemplateView)
from listings.models import Listing


def user_contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        #  Check if user has made inquiry already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(
                listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(
                    request, _("You have already made an inquiry "
                               "for this listing"))
                return redirect('listing', listing_id)

        contact = Contact(listing_id=listing_id, phone=phone, message=message,
                          user_id=user_id)

        contact.save()

        # Send email
        send_mail(f'Property Listing Inquiry',
                  f'There has been an inquiry for '
                  f'{Listing.objects.get(id=listing_id)}'
                  f'. Sign into the admin panel for more info',
                  'schonefeld.dev@gmail.com',
                  [realtor_email, 'schonefeld.dev@gmail.com'],
                  fail_silently=False)

        messages.success(
            request, (_("Your request has been submitted, a realtor will "
                        "get back to you soon")))
        return redirect('/listings/' + listing_id)


def anonymous_contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = request.POST['phone']
        message = request.POST['message']
        realtor_email = request.POST['realtor_email']

        #  Check if user has made inquiry already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(
                listing_id=listing_id, first_name=first_name,
                last_name=last_name)
            if has_contacted:
                messages.error(
                    request, _("You have already made an inquiry for this "
                               "listing"))
                return redirect('listing', pk=listing_id)

        contact = Contact(listing_id=listing_id, phone=phone, message=message,
                          user_id=user_id)

        contact.save()

        # Send email
        send_mail('Property Listing Inquiry',
                  'There has been an inquiry for '
                  + Listing.object.get(id=listing_id)
                  + '. Sign into the admin panel for more info',
                  'schonefeld.dev@gmail.com',
                  [realtor_email, 'schonefeld.dev@gmail.com'],
                  fail_silently=False)

        messages.success(
            request, (_("Your request has been submitted, a realtor will "
                        "get back to you soon")))
        return redirect('/listings/' + listing_id)


@login_required
def chat_message(request):
    if request.method == 'POST':
        contact_id = request.POST['contact_id']
        user_id = request.POST['user_id']
        message = request.POST['message']

        obj = ChatMessage(contact_id=contact_id, message=message,
                          user_id=user_id)

        obj.save()

        messages.success(
            request, (_("Your request has been submitted, a realtor will ' \
                        'get back to you soon")))
        return redirect('chat-history', pk=contact_id)


class MessageHistoryListView(DetailView):
    model = Contact
    template_name = 'contacts/messages_history.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Showcase Section Infos
        context['title'] = _("Message History")
        context['subtitle'] = self.object.listing.title
        # SEO
        context['page_title'] = _("Message History")
        context['page_description'] = _("Real estate manager."
                                        "Here you can follow your message "
                                        "history, related to a specific "
                                        "listing you are interested in..")
        return context


class AdminContactView(TemplateView):
    # TODO finish this crap
    template_name = 'admin/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact'] = Contact.objects.get(id=5)
        return context
