from django.http import HttpResponse
import datetime

from django.shortcuts import render

from shop.models import Product, Setting


def home(request):
    # products = Product.objects.all()
    products = Product.objects.filter(is_active=True)
    return render(request, template_name="home.html", context={'products': products})


def time(request, hour=0):
    last_time = datetime.datetime.now() + datetime.timedelta(hours=hour)
    if hour > 0:
        added_hour = f"we have added: {str(hour)} hours"
    else:
        added_hour = f""
    html = f""
    names = ['ALI', 'MINA', 'HASAN', 'MOHSEN', 'SAIED']
    multiline_text = "welcome to my shop"
    return render(request, "time.html", context={"add_hour": added_hour, "l_time": last_time, "names": names, "multiline_text": multiline_text})

