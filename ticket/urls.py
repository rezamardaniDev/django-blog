from django.urls import path
from . import views

app_name = 'ticket'

urlpatterns = [
    path('', views.show_all_tickets, name='tickets'),
    path('viewTicket/<ticket_id>', views.show_detail_ticket, name='ticket-detail'),
    path('add_new_ticket', views.add_new_ticket, name='add-new-ticket')
]
