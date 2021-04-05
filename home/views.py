from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from .models import Gallery, Staff, General_Enquiry, ATL_Lab_Picture, Product, Notice_Board, Order, eSamachar
import json
from django.core.mail import send_mail
from django.urls import reverse_lazy


def index(request):
    achivements = Gallery.objects.all()
    staff       = Staff.objects.all()
    atl         = ATL_Lab_Picture.objects.all()
    showcase    = Product.objects.all()

    context = {
        'achievements' : achivements,
        'staff'        : staff,
        'atl'          : atl,
        'showcase'     : showcase,
    }

    return render(request, 'index.html', context)


def gallery(request):
    gallery = Gallery.objects.all()

    context = {
        'gallery' : gallery,
    }

    return render(request, 'gallery.html', context)


def staff(request):
    staff       = Staff.objects.all()

    context = {
        'staff'        : staff,
    }

    return render(request, 'staff.html', context)


def atl(request):
    atl       = ATL_Lab_Picture.objects.all()

    context = {
        'atl'        : atl,
    }

    return render(request, 'atl.html', context)


def showcase(request):
    showcase   = Product.objects.all()

    context = {
        'showcase'    : showcase,
    }

    return render(request, 'showcase.html', context)


def contact(request):
    if request.method == 'POST':
        name    = request.POST['name']
        email   = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']


        contact = General_Enquiry( name=name, email=email, subject=subject, message=message )
        contact.save()
        # send_mail(subject,message,email,[email, 'imacac94@gmail.com'])
        return HttpResponse('OK')

    return HttpResponse('We are facing some error.')


def notice(request):
    notice = Notice_Board.objects.all().order_by('-date')

    context = {
        'notice'    : notice,
    }

    return render(request, 'notice.html', context)


def samachar(request):
    news = eSamachar.objects.all()

    context = {
        'eSamachar' : news,
    }

    return render(request, 'eSamachar.html', context)


def checkout(request, pk):
    product = Product.objects.get(id=pk)

    context = {
        'product'    : product,
    }

    return render(request, 'checkout.html', context)


def purchase_form(request):
    if request.method == 'POST':
        product  = request.POST.get('product')
        email    = request.POST.get('email')
        quantity = request.POST.get('quantity')
        mobile   = request.POST.get('mobile')
        name     = request.POST.get('name')
        orderId  = request.POST.get('productId')
        address  = request.POST.get('address')
        pincode  = request.POST.get('pincode')



        subject = f'Enquiry of Order No. {orderId} of {product}'
        message = f'You have received a new Order/enquiry \n\n {product} - Quantity = {quantity} \n\n Customer : {name}\n Mobile No. : {mobile} \n Email : {email} \n Address : {address} \n Pin Code : {pincode} \n\n Kindly contact for further process  '

        order = Order( product=product, email=email, quantity=quantity, mobile=mobile, name=name, orderId=orderId, pincode=pincode, address=address )
        order.save()
        send_mail(subject,message,email,[ 'ssvschoolshop@gmail.com'])
        send_mail(f'Order for {product}',f'Dear {name}, \n\n Your Order Id is {orderId},\n Thank you for contacting SSV School Shop. We are glad to have your interest in our products. \n\n Our SSV shop incharge will connect to you shortly regarding your order. \n\n Thank you for your contribution in Women Empowerment ',email,[ email])
        
        return HttpResponse('OK')

    return HttpResponse('We are facing some error.')
