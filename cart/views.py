from django.shortcuts import render, redirect, get_object_or_404

from .cart import Cart
from .forms import AddToCart
from cases.models import Case
def cart_detail_view(request):
    cart = Cart(request)
    context = {
        'cart': cart,
    }
    return render(request, 'cart/cart_detail.html', context)

def add_to_cart_view(request, case_id):
    cart = Cart(request)
    case = get_object_or_404(Case, id=case_id)
    form = AddToCart(request.POST)
    if form.is_valid():
        cleaned_data = form.cleaned_data
        meter = cleaned_data['meter']
        cart.add(case, meter, replace_current_meter=cleaned_data['inplace'])
    return redirect('cart_detail')


