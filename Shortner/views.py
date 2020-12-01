from django.http.request import HttpRequest
from django.http.response import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import URL_Form
from .models import Input_URL
from .models import User
from django.utils import timezone
from django.views.generic import CreateView
from django import forms
import random
import string
# Create your views here.
# id = 1
# length = 5

# class UserFormCreateView(CreateView):
#     model = User
#     fields = ('name', 'email')
    


class URL_Shortner:
    
    def __init__(self):
        global length
        length = random.randint(5,8)
    
    def shorten_url(self, input_url):
        shorten_url = self.encode(length)
        
        
        return "localhost:8000/" + str(shorten_url)

    def encode(self, length):
        # characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+/"
        # base = len(characters)
        # ret = []
        # while id > 0:
        #     val = id % base
        #     ret.append(characters[val])
        #     id = id // base

        # return "".join(ret[::-1])
        letters_and_digits = string.ascii_letters + string.digits
        result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))

        try:
            check_link = "localhost:8000/" + str(result_str)
            try_get_link = Input_URL.objects.filter(shorten_url = check_link).first()
            if try_get_link is not None:
                self.encode(6)
            else:
                return result_str
        except:
            return result_str
        




def home(request):
    if request.method == 'POST':
        input = URL_Form(request.POST)
        if input.is_valid():
            name = input.cleaned_data['name']
            if len(name) < 4:
                raise forms.ValidationError("Name is too Short")
            email = input.cleaned_data['email']
            url = input.cleaned_data['input_url']
            shorten_urls = URL_Shortner().shorten_url(url)
            set_UserData = User(Name = name, Email = email)
            set_UserData.save()
            set_data = Input_URL(UserID= set_UserData ,input_url = url , shorten_url = shorten_urls, CreationDate = timezone.now(), ExpirationDate = timezone.now() + timezone.timedelta(days= 730) )
            set_data.save()
            

            new_input = URL_Form()
            return render(request, 'home.html', {
                'form' : new_input, 'short_url' : shorten_urls, 'input_url' : url,
            })
    else:
        form = URL_Form()
        return render(request, 'home.html',{
        'form' : form , 
        })

def redirect_fun(request, link):

    ready_link = "localhost:8000/" + str(link)
    
    try:
        get_link = Input_URL.objects.filter(shorten_url = ready_link).first()
        final_link = get_link.input_url

        
    except Input_URL.DoesNotExist:
        raise Http404('Page not Found')

    return redirect(final_link)

