from django.shortcuts import render,redirect
from django.http import  HttpResponse

from .models import *
from .form import OpportunityForm,AccountForm,UserRegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate ,login,logout
from  django.contrib import  messages


# Create your views here.

def homepage(request):
    opportunity=Opportunity.objects.all()
    account = Account.objects.all()
    context={"opportunity":opportunity,"account":account}
    return render(request ,"account/index.html", context)


def opportunity_create(request):
    form=OpportunityForm()
    if request.method=="POST":
        form = OpportunityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')


    context = {"form": form}

    return render(request, "account/oppotunity_form.html",context)




def opportunity_update(request ,pk):
    opportunity=Opportunity.objects.get(id=pk)
    form=OpportunityForm(instance=opportunity)
    if request.method=="POST":
        form = OpportunityForm(request.POST, instance=opportunity)
        if form.is_valid():
            form.save()
            return redirect('index')


    context = {"form": form}


    return render(request, "account/opportunity_update.html",context)


def opportunity_delete(request, pk):
    opportunity=Opportunity.objects.get(id=pk)
    context = {"opportunity": opportunity}
    if request.method == "POST":
        opportunity.delete()
        return redirect('index')

    return render(request, "account/opportunity_delete.html",context)



def account_form(request):
    form = AccountForm()

    if request.method == "POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account-view')

    context = {"form": form}

    return render(request, "account/account_form.html", context)


def account_list(request):
    account = Account.objects.all()
    context = {"account":account}
    return render(request, "account/index.html", context)


def account(request):
    account = Account.objects.all()
    context = {"account":account}
    return render(request, "account/account.html", context)



def accountUpdate(request ,pk):
    account=Account.objects.get(id=pk)
    form=AccountForm(instance=account)
    if request.method == "POST":
        form = AccountForm(request.POST, instance=account)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {"form": form}

    return render(request, "account/account_update.html", context)


def account_delete(request, pk):
    account=Account.objects.get(id=pk)
    context = {"account": account}
    if request.method == "POST":
        account.delete()
        return redirect('account-view')

    return render(request, "account/account_delete.html",context)




#authentifecation



def register(request):
    form=UserRegisterForm()
    if request.method=='POST':
        form =UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'Account was created for '+user)
            return redirect('login')




    context = {"form": form}

    return render(request, "account/register.html", context)


def logoutPage(request):
  logout(request)
  return render(request, 'account/logout.html')



def LoginPage(request):
    form =UserRegisterForm()
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get('password1')
        user=authenticate(request, username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')

    context = {'form': form}

    return render(request, 'account/login.html', context)


