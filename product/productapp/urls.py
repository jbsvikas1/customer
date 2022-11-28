from django.urls import path
from .views import *


urlpatterns = [
    path('product', create_view),
    path('list', list_view),
    path('update',update_view),

]