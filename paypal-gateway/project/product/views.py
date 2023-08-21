from django.shortcuts import render
from .models import *
from django.urls import reverse
from django.shortcuts import render
from paypal.standard.forms import PayPalPaymentsForm

# def view_that_asks_for_money(request):

#     # What you want the button to do.
#     host = request.get_host()
#     paypal_dict = {
        
#         "business": "receiver_email@example.com",
#         "amount": "10000000.00",
#         "item_name": "name of the item",
#         "invoice": "unique-invoice-id",
#         "notify_url": 'https://{}{}'.format(host, reverse("core: paypal-ipn")),
#         # "return": request.build_absolute_uri(reverse('your-return-view')),
#         # "cancel_return": request.build_absolute_uri(reverse('your-cancel-view')),
#         # "custom": "premium_plan",  # Custom command to correlate to some function later (optional)
#     }

#     # Create the instance.
#     form = PayPalPaymentsForm(initial=paypal_dict)
    
def products(request,id):
    product = Product.objects.get(id= id)
    return render(request, 'product.html', {'product':product})