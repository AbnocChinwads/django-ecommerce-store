from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
               'order_form': order_form,
               'stripe_public_key': 'pk_test_51HjmKKI9votNfXXUWws6PPKjPAqY50VLYMv7kjrRoYZYBo1BH1Ao4Qaj83syvZn72lVFENhwdJq0qzr9aSnvMhto00myWBuYzi',
               'client_secret': 'test secret key',
              }

    return render(request, template, context)
