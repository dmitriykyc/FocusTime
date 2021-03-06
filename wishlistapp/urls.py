from django.urls import path
import wishlistapp.views as wishlistapp
app_name = 'wishlistapp'

urlpatterns = [
    path('', wishlistapp.index, name='index_wishlist'),
    path('wish_done/', wishlistapp.wish_done, name='wish_done'),
    path('wish_delete/', wishlistapp.wish_delete, name='wish_delete'),
    path('wish_edit/', wishlistapp.wish_edit, name='wish_edit')
]
