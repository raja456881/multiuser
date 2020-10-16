from django.urls import path
from.import views
urlpatterns = [
    path("" ,views.BulckEmail, name='bulkemail'),
    path('singlemail', views.singlemail, name='singlemail'),
    path('singlemailt', views.studentsingeemail, name='studentmail'),
    path('singlemail1', views.Institutionsingeemail,name='institutemail'),
    path('single2', views.trainersingeemail,name='trainersinglemail'),
    path('location', views.location, name='location'),
    path('customer', views.customerdetails,name='customer_detail'),
    path('crm/invoice/<int:id>/', views.InvoicePDFView,name='invoice'),
    path('checkout', views.orederdetails, name='buynow1'),
]
