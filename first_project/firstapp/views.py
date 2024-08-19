from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomerForm
from .models import Customer

# Create your views here.
def home(request):
    return render(request, "customer_register/index.html")

def base(request):
    return render(request, "customer_register/base.html")

def customer_list(request):
    context = {'customer_list': Customer.objects.all()}
    return render(request, "customer_register/customer_list.html", context)

def customer_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = CustomerForm()
        else:
            customer = get_object_or_404(Customer, pk=id)
            form = CustomerForm(instance=customer)
        return render(request, "customer_register/customer_form.html", {'form': form})
    else:
        if id == 0:
            form = CustomerForm(request.POST)
        else:
            customer = get_object_or_404(Customer, pk=id)
            form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('/home/list')
        return render(request, "customer_register/customer_form.html", {'form': form})

def customer_delete(request, id):
    customer = get_object_or_404(Customer, pk=id)
    customer.delete()
    return redirect('/home/list')

