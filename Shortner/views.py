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
        
        
        return "https://urlsh0rtner.herokuapp.com/" + str(shorten_url)

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
            check_link = "https://urlsh0rtner.herokuapp.com/" + str(result_str)
            try_get_link = Input_URL.objects.filter(shorten_url = check_link).first()
            if try_get_link is not None:
                self.encode(6)
            else:
                return result_str
        except:
            return result_str
        

def get_ip_address(request):
    """ use requestobject to fetch client machine's IP Address """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
        ip = ip[len(ip) - 1]
    else:
        ip = request.META.get('REMOTE_ADDR')    ### Real IP address of client Machine
    return ip

# def get_ip_address(request):
#     x_forwarded_for = request.headers('HTTP_X_FORWARDED_FOR')
#     if x_forwarded_for:
#         ipps = x_forwarded_for.split(',')
#         ips = ipps[len(ipps) - 1]
#     else:
#         ips = request.META.get('REMOTE_ADDR')
#     return ips



def home(request):
    ip_address = get_ip_address(request)
    if request.method == 'POST':
        input = URL_Form(request.POST)
        if input.is_valid():
            name = input.cleaned_data['name']           
            email = input.cleaned_data['email']
            url = input.cleaned_data['input_url']
            shorten_urls = URL_Shortner().shorten_url(url)
            set_UserData = User(Name = name, Email = email)
            set_UserData.save()
            
            set_data = Input_URL(UserID= set_UserData, ip_addresss= ip_address ,input_url = url , shorten_url = shorten_urls, CreationDate = timezone.now(), ExpirationDate = timezone.now() + timezone.timedelta(days= 730) )
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

    ready_link = "https://urlsh0rtner.herokuapp.com/" + str(link)
    
    try:
        get_link = Input_URL.objects.filter(shorten_url = ready_link).first()
        final_link = get_link.input_url

        
    except Input_URL.DoesNotExist:
        raise Http404('Page not Found')

    return redirect(final_link)

