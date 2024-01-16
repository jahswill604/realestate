# listings/views.py

from django.shortcuts import render,get_object_or_404
from django.conf import settings
from .models import Listing
from paystackapi.transaction import Transaction
from django.http import JsonResponse

def index(request):
    return render(request, 'listings/index.html')

def about(request):
    return render(request, 'listings/about.html')

def contact(request):
    return render(request, 'listings/contact.html')
def property (request):
    listings = Listing.objects.all()
    context = {'listings': listings,}
    return render (request, 'listings/property.html', context)

def paystack(request):
    return render (request, 'listings/paystack.html')

def single_view(request, item_id):
    # Dummy data for demonstration, replace this with your logic to fetch item details
    listing = get_object_or_404(Listing, id=item_id)
    return render(request, 'listings/single.html', {'listing': listing})


    # item_details = {
    #     'id': item_id,
    #     'title': f'Item {item_id}',
    #     'description': f'Description of Item {item_id}',
    #     'price': 100 * item_id,
    #     'bathrooms': 2,
    #     'bedrooms': 3,
    #     # Add other details as needed
    # }

    # return render(request, 'listings/single.html', {'item': item_details})

# listings/views.py





def initiate_payment(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    amount_in_kobo = int(listing.price * 100)  # Paystack amount is in kobo

    response = Transaction.initialize(amount=amount_in_kobo,
                                      email='buyer@example.com',
                                      reference=f'listing-{listing.id}')

    return JsonResponse(response)






