from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Order, Response
from .forms import OrderForm, ResponseForm

def index(request):
    orders = Order.objects.all().order_by('-created_at')
    return render(request, 'marketplace/index.html', {'orders': orders})

@login_required
def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.customer = request.user
            order.save()
            return redirect('index')
    else:
        form = OrderForm()
    return render(request, 'marketplace/create_order.html', {'form': form})

def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    user_response = None
    if request.user.is_authenticated:
        user_response = Response.objects.filter(order=order, executor=request.user).first()
    
    return render(request, 'marketplace/order_detail.html', {
        'order': order,
        'user_response': user_response
    })

@login_required
def create_response(request, pk):
    order = get_object_or_404(Order, pk=pk)
    
    if order.customer == request.user:
        return redirect('order_detail', pk=order.pk)

    if request.method == 'POST':
        form = ResponseForm(request.POST)
        if form.is_valid():
            response = form.save(commit=False)
            response.order = order
            response.executor = request.user
            response.save()
            return redirect('order_detail', pk=order.pk)
    else:
        form = ResponseForm()
    
    return render(request, 'marketplace/create_response.html', {'form': form, 'order': order})