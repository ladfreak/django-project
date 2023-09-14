from django.urls import path
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('',views.home,name="home"),
    path('accounts/profile/',views.home1,name="home1"),
    path('myregister/',views.myregister,name="myregister"),
    path("login/",auth_views.LoginView.as_view(template_name='login.html'),name="login"),
    path('categories/',views.categories,name="categories"),
    path("logout/",auth_views.LogoutView.as_view(template_name='logout.html'),name="logout"),
    path('info',views.info,name="info"),
    path('addtocart',views.add_to_cart,name="addtocart"),
    path('collection/<str:name>',views.collection,name="collection"),
    path('product_details<str:cname>/<str:pname>',views.product_details,name="product_details"),
    path('cart',views.cart_page,name="cart"),
    path('cart_remove/<str:cid>',views.cart_remove,name="cart_remove"),
    path('fav',views.fav_page,name="fav"),
    path('favourite',views.favourite,name="favourite"),
        path('fav_remove/<str:cid>',views.fav_remove,name="fav_remove"),
    
]