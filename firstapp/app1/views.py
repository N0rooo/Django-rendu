from django.shortcuts import (get_object_or_404, render, HttpResponseRedirect)
from .models import Product
from .forms import ProductForm


def index(request):
    return render(request, "index.html")


def create_view(request):

    context = {}
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/list")


    context['form'] = form
    return render(request, "create_view.html", context)


def list_view(request):
    context = {}
    context["dataset"] = Product.objects.all()
    return render(request, "list_view.html", context)


def detail_view(request, id):

    context = {}

    context["data"] = Product.objects.get(id=id)

    return render(request, "detail_view.html", context)


def update_view(request, id):

    context = {}

    obj = get_object_or_404(Product, id=id)

    # pass the object as instance in form
    form = ProductForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)

    # add form dictionary to context
    context["form"] = form

    return render(request, "update_view.html", context)


def delete_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Product, id=id)

    if request.method == "POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/list")

    return render(request, "delete_view.html", context)
