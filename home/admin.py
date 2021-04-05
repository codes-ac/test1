from django.contrib import admin
from .models import Gallery, General_Enquiry, Staff, ATL_Lab_Picture, Product, Notice_Board, Order

admin.site.register(Gallery)
admin.site.register(ATL_Lab_Picture)
admin.site.register(Product)
admin.site.register(Staff)
admin.site.register(General_Enquiry)
admin.site.register(Notice_Board)
admin.site.register(Order)
