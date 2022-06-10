from django.urls import path
from . import views

urlpatterns = [
    path('network/', views.BlockchainNetworkView.as_view(), name='retrieve_blockchain_network'),
    path('network/<int:pk>/', views.TokenView.as_view(), name='retrieve_token'),
]