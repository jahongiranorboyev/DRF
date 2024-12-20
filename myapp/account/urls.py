from django.urls import path

from myapp.account.api_views import AccountListAPIView, AccountDetailAPIView
from django.urls import path
from .api_generics import (
    AccountGenericListAPIView,
    AccountListCreateAPIView,
    AccountDestroyAPIView,
    AccountRetrieveAPIView,
    AccountUpdateAPIView,
    AccountRetrieveUpdateDestroyAPIView
)
from myapp.account.api_login import CustomAuthToken

urlpatterns =[
    path('list/', AccountListAPIView.as_view(), name='account_list'),
    path('detail/<uuid:guid>/', AccountDetailAPIView.as_view(), name='account_list'),
]

urlpatterns += [
    path('generic-list/', AccountGenericListAPIView.as_view(), name='account_generics_list'),
    path('generic-create/', AccountListCreateAPIView.as_view(), name='account_generics_create'),
    path('generic-retrieve/<uuid:guid>/', AccountRetrieveAPIView.as_view(), name='account_retrieve'),
    path('generic-update/<uuid:guid>/', AccountUpdateAPIView.as_view(), name='account_update'),
    path('generic-destroy/<uuid:guid>/', AccountDestroyAPIView.as_view(), name='account_destroy'),
    path('generic-retrieve-update-destroy/<uuid:guid>/', AccountRetrieveUpdateDestroyAPIView.as_view(), name='account_rud'),
]

urlpatterns += [
    path('token-auth/',CustomAuthToken.as_view())
]
