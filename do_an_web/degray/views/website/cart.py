from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render

def index(request):
    template = loader.get_template('website/cart/cart.html')
    return HttpResponse(template.render({'title': 'Giỏ Hàng'}, request))