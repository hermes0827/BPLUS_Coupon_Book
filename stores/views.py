from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.http import Http404
from . import models, forms


class Homeview(ListView):
    model = models.Store
    paginate_by = 10


""" FBV of the detail view """

# def store_detail(request, pk):
#     try:
#         store = models.Store.objects.get(pk=pk)
#         return render(request, "stores/store_detail.html", context={"store": store})
#     except models.Store.DoesNotExist:
#         raise Http404()


""" CBV of the detail view """


class StoreDetail(DetailView):
    model = models.Store


def search(request):
    form = forms.SearchForm(request.GET)
    return render(request, "stores/search.html", {"form": form})
