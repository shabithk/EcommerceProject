from django.urls import path, include
from .import views
app_name='ecommerceapp'
urlpatterns = [

    path('',views.allProdCart,name='allProdCart'),
    path('<slug:c_slug>/',views.allProdCart,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.proDetail,name='ProdCatdetail')
]
