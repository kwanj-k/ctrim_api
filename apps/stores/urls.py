from django.urls import path

from .views import StoreListCreateView

app_name = 'stores'
urlpatterns = [
    path('stores/', StoreListCreateView.as_view(), name='stores_list'),
]
