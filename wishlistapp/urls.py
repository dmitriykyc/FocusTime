from django.urls import path
import wishlistapp.views as wishlistapp
app_name = 'wishlistapp'

urlpatterns = [
    path('', wishlistapp.index, name='index'),
    path('wish_done/', wishlistapp.wish_done, name='wish_done')
]
