from django.urls import path
from .views import *
from .forms import *
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
urlpatterns= [
    path("", Home, name='home'),
    path("category/<slug:val>", CategoryView.as_view(), name="category"),
    path("product-detail/<int:pk>", ProductDetail.as_view(), name="product-detail"),

    #login & registrations

    path("register", CustomerRegistrationView.as_view(), name="register"),

#This LoginView will automatically log the user in and the LOGIN_REDIRECT_URL set in the
#settings.py will redirect it to the userprofile.

    path('login', CustomLoginView.as_view(), name="login"),
    path('confirmlogout', TemplateView.as_view(template_name='app/logged_out.html'), name="confirmlogout"),
    path('logout/', CustomLogoutView.as_view(), name="logout"),
    path("profile", CustomerProfileView.as_view(), name="profile"),


    path('add-to-cart/', add_to_cart, name='add-to-cart'),
    path('cart/', show_cart, name='showcart'),
    path('pluscart/', plus_cart),
    path('minuscart/', minus_cart),
    path('removecart/', remove_cart),
    path('checkout/', checkout.as_view(), name="checkout"),

    #path("editprofile", EditProfile.as_view(), name="edit"),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)