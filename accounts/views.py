from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserForm
from vendor.forms import VendorForm
from .models import User, UserProfile
from django.contrib import messages

# Create your views here.
def registerUser(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            user = form.save(commit=False)
            user.set_password(password)
            user.role = User.CUSTOMER
            user.save()
            messages.success(request, 'User has been registered successfully')
            return redirect('registerUser')
        else:
            print(form.errors)
    else:
        form = UserForm()
    context = {
        'form': form
    }
   
    return render(request, 'accounts/registerUser.html',context)
'''
def registerVendor(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        v_form = VendorForm(request.POST, request.FILES)
        if form.is_valid() and v_form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            user.role = User.RESTAURANT
            user.save()
            vendor = v_form.save(commit=False)
            vendor.user = user
            user_profile = UserProfile.objects.get(user=user)
            vendor.user_profile = user_profile
            vendor.save()
            messages.success(request, 'Restaurant has been registered successfully')
            return redirect('registerVendor')
        else:
            print(form.errors)
    else:
        form = UserForm()
        v_form= VendorForm()
        


    context = {
        'form': form, 
        'v_form': v_form
    }

    return render(request, 'accounts/registerVendor.html',context)
'''
def registerVendor(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        v_form = VendorForm(request.POST, request.FILES)

        if form.is_valid() and v_form.is_valid():
            # Create user but don't save it yet
            user = form.save(commit=False)
            
            # Securely set the password
            user.set_password(form.cleaned_data['password'])
            user.role = User.RESTAURANT
            user.save()

            # Ensure the UserProfile exists or create it
            user_profile, created = UserProfile.objects.get_or_create(user=user)

            # Create vendor but don't save yet
            vendor = v_form.save(commit=False)
            vendor.user = user
            vendor.user_profile = user_profile
            vendor.save()

            # Success message and redirect
            messages.success(request, 'Restaurant has been registered successfully')
            return redirect('registerVendor')
        else:
            # Show validation errors to the user
            messages.error(request, "Please correct the errors below.")

    else:
        form = UserForm()
        v_form = VendorForm()

    context = {
        'form': form,
        'v_form': v_form
    }

    return render(request, 'accounts/registerVendor.html', context)
