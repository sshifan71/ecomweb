from django.shortcuts import render, redirect
from django.views import View
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.db.models import Q
from django.http import JsonResponse
# Create your views here.
def Home(request):
    return render(request, 'app/home.html')

class CategoryView(View):
    def get(self, request, val):
        product = Product.objects.filter(category = val)
        title = Product.objects.filter(category=val).values('title')
        return render(request, 'app/category.html', locals())
    
class ProductDetail(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, "app/productdetail.html", locals())
    


"""This part takes the input from the forms.py form and creates a new user"""
class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'app/registration.html', {'form':form})
    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend="django.contrib.auth.backends.ModelBackend")
            messages.success(request, "Congratulation! User Register Successful!")
        else:
            messages.warning(request, "Invalid Input Data")
        return render(request, 'app/registration.html', {'form':form})
    
class CustomLoginView(LoginView):
    authentication_form = EmailOrUsernameAuthenticationForm
    template_name = 'app/login.html'
    redirect_authenticated_user = True  # Redirect authenticated users to another page
    
    def get_success_url(self):
        """
        Returns the URL to redirect to after successful login.
        """
        return 'home'
    
class CustomLogoutView(LogoutView):
    http_method_names = ["post", "options"]
    template_name = "app/logged_out.html"

"""
The Login method doesn't have any view function or class.
Because Django has a built-in method called LoginView, that
can be called directly in the urls.py file and executed in the
path creating section.
"""

"""
After LoggingIn the user should update his profile giving the name, mobile number, address so that the delivery of the ordered
product can be secured
"""

class CustomerProfileView(View):
    def get(self, request):
        return render(request, 'app/profile.html', locals())
    
# class EditProfile(View):
#     def get(self,request):
#         form = CustomerProfileForm()
#         return render(request, 'app/editprofile.html', locals())

def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id = product_id)
    # Check if the cart item already exists
    c, created = Cart.objects.get_or_create(user=user, product=product)
    
    if not created:
        # If the cart item already exists, increment the quantity
        c.quantity += 1
        c.save()
    
    return redirect("/cart")

def show_cart(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    amount = 0
    for p in cart:
        value = p.quantity * p.product.discounted_price
        amount = amount + value
    totalamount = amount + 40
    return render(request, 'app/addtocart.html', locals())

def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product = prod_id) & Q(user = request.user))
        c.quantity+=1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount = amount + value
        totalamount = amount + 40
        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': totalamount,
        }

        return JsonResponse(data)
    

def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product = prod_id) & Q(user = request.user))
        c.quantity-=1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount = amount + value
        totalamount = amount + 40
        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': totalamount,
        }

        return JsonResponse(data)
    


def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product = prod_id) & Q(user = request.user))
        c.delete()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount = amount + value
        totalamount = amount + 40
        data = {
            'amount': amount,
            'totalamount': totalamount,
        }

        return JsonResponse(data)
    
class checkout(View):
    def get(self, request):
        user = request.user
        add = CustomUser.objects.filter(email=user)
        cart_item = Cart.objects.filter(user=user)
        famount=0
        for i in cart_item:
            value = i.quantity * i.product.discounted_price
            famount = famount + value
        totalamount = famount + 70
        return render(request, 'app/checkout.html',locals())
