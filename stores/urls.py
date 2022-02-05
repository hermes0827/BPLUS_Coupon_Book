from django.urls import path
from . import views as store_views

app_name = "stores"


""" urlpatterns of FBV"""
# urlpatterns = [path("<int:pk>", store_views.store_detail, name="detail")]

""" urlpatterns of CBV """
urlpatterns = [
    path("<int:pk>", store_views.StoreDetail.as_view(), name="detail"),
    path("search/", store_views.search, name="search"),
]
