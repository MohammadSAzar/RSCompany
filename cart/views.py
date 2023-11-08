from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib import messages

from .cart import Cart
from .forms import AddToCart
from cases.models import Case

def cart_detail_view(request):
    cart = Cart(request)
    for item in cart:
        item['case_update_meter_form'] = AddToCart(initial={
            'meter': item['meter'],
            'inplace': True,
        })
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


def remove_from_cart_view(request, case_id):
    cart = Cart(request)
    case = get_object_or_404(Case, id=case_id)
    cart.remove(case)
    return redirect('cart_detail')

@require_POST
def cart_clear(request):
    cart = Cart(request)
    if len(cart):
        cart.clear()
        messages.success(request, 'سبد با موفقیت خالی شد')
    else:
        messages.warning(request, 'سبد شما خالی است')
    return redirect('case_list')


