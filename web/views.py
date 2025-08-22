from django.shortcuts import render
from .forms import OrderForm

from django.http import HttpResponse



def home(request):
    return render(request, 'main/home.html')



def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')

def login(request):
    return render(request, 'main/login.html')

def signup(request):
    return render(request, 'main/signup.html')

#signup

from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto login after signup
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'main/signup.html', {'form': form})


#login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'main/login.html', {'form': form})

def logout_view(request):
    auth_logout(request)
    return redirect('home')


#comment
from .forms import CommentForm
from .models import Comment

def contact(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            if request.user.is_authenticated:
                comment.user = request.user
            comment.save()
            return render(request, 'main/contact.html', {
                "form": CommentForm(),
                "success": True,
                "comments": Comment.objects.all()
            })
    else:
        form = CommentForm()
    return render(request, 'main/contact.html', {"form": form, "comments": Comment.objects.all()})


from django.db.models import Q
from .models import Product

def product_list(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    else:
        products = Product.objects.all()
    return render(request, 'main/products.html', {"products": products})


#payment
def payment(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            return render(request, 'main/payment.html', {'form': OrderForm(), 'success': True})
    else:
        form = OrderForm()
    return render(request, 'main/payment.html', {'form': form})




from django.shortcuts import render
from .models import Product

def home(request):
    products = Product.objects.all()
    return render(request, 'main/home.html', {'products': products})



# Create your views here.
