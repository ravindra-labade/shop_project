from django.shortcuts import render, redirect
from .forms import ShopForm
from .models import Shop



def add_shop(request):
    template_name = 'shop/add.html'
    form = ShopForm()
    if request.method == 'POST':
        form = ShopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {'form': form}
    return render(request, template_name, context)


def show_shop(request):
    template_name = 'shop/show.html'
    shops = Shop.objects.all()
    context = {'shops': shops}
    return render(request, template_name, context)


def update_shop(request, pk):
    template_name = 'shop/add.html'
    obj = Shop.objects.get(id=pk)
    form = ShopForm(instance=obj)
    if request.method == 'POST':
        form = ShopForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {'form': form}
    return render(request, template_name, context)



def delete_shop(request, pk):
    obj = Shop.objects.get(id=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('show_url')
    return render(request, 'shop/confirm.html')