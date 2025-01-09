from django.shortcuts import render, redirect
from .models import Ticket
# Create your views here.

def show_all_tickets(request):
    tickets = Ticket.objects.all()
    return render(request, 'ticket/all_tickets.html', context={'tickets': tickets})


def show_detail_ticket(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    if ticket.status == 'open':
        ticket.status = 'pending'
        ticket.save()
    return render(request, 'ticket/detail_ticket.html', context={'ticket': ticket})


def add_new_ticket(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        Ticket.objects.create(title=title, description=description)
        return redirect('/tickets/')
    return render(request, 'ticket/add_ticket.html')