from django.http import HttpResponse
from django.utils import timezone
import datetime

from django.shortcuts import render, get_object_or_404

from shop.models import Product, Setting, ProductImage, ProductOption, Discount


def home(request):
    # # products = Product.objects.all()
    # products = Product.objects.filter(is_active=True)
    # return render(request, template_name="home.html", context={'products': products})
    products = Product.objects.filter(is_active=True).order_by('category')
    context = {"products": products}
    return render(request, template_name="home_page.html", context=context)





def product(request, product_id):
    p = get_object_or_404(Product, id=product_id, is_active=True)
    p.view = p.view + 1
    p.save()
    # p = Product.objects.get(id=product_id, is_active=True)
    images = ProductImage.objects.filter(product=product_id)
    options = ProductOption.objects.filter(product=product_id)
    price = p.price
    additional = ""
    try:
        discount = Discount.objects.get(product=product_id, is_active=True).percent
        price = (p.price // 100) * (100 - discount)
        additional = p.price
    except:
        pass
    context = {"product": p, "images": images, "options": options, "price": price, "additional": additional}
    return render(request, template_name="product.html", context=context)






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

