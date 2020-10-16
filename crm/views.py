from django.shortcuts import render
# Create your views here.
from django.shortcuts import render
from .models import *
from django.shortcuts import render, redirect
from multiuser.models import FranchiseProfile,InstituteProfile,TrainerProfile
from student.models import Student
from .models import location1, customer , Order
from django.template.loader import get_template
from  io  import BytesIO
from xhtml2pdf import pisa
from django.http import HttpResponse
from inventory.models import CourseDetails
from django.shortcuts import render, get_object_or_404
import  json
def BulckEmail(request):
    if request.method=='POST':
        from django.core import mail
        connection=mail.get_connection()
        connection.open()
        recivers_list=[]
        name=request.POST['name']
        subject=request.POST['subject']
        message=request.POST['message']
        if name=='Student':
            print(name)
            for user in Student.objects.all():
                recivers_list.append(user.stdent_Email)
        elif name=='Trainer':
            print(name)
            for user in TrainerProfile.objects.all():
                recivers_list.append(user.trainerEmail)
        elif name=='Institution':
            print(name)
            for user in InstituteProfile.objects.all():
                recivers_list.append(user.instituteEmail)
        elif name=='Franchise':
            print(name)
            for user in FranchiseProfile.objects.all():
                recivers_list.append(user.franchiseEmail)
        email1=mail.EmailMessage( subject, message , 'rajasaini12345641@gmail.com', recivers_list, connection=connection)
        email1.send()
        connection.close()
    return render(request, "bulk-mail.html")

def singlemail(request):
    institution=InstituteProfile.objects.all()
    train=TrainerProfile.objects.all()
    student=Student.objects.all()
    print(student, train, institution)
    params={'context': institution, 'context1': train, 'context2': student}
    return render(request, "individual-mail.html", params)




def studentsingeemail(request):
    if request.method=='POST':
        from django.core import mail
        connection=mail.get_connection()
        connection.open()
        recivers_list=[]
        name=request.POST['name']
        subject=request.POST['subject']
        message=request.POST['message']
        print(name)
        recivers_list.append(name)
        print(name)
        email1=mail.EmailMessage(subject, message , 'rajasaini12345641@gmail.com', recivers_list, connection=connection)
        email1.send()
        connection.close()
    return render(request , "individual-mail.html")
def trainersingeemail(request):
    if request.method=='POST':
        from django.core import mail
        connection=mail.get_connection()
        connection.open()
        recivers_list=[]
        name=request.POST['name']
        subject=request.POST['subject']
        message=request.POST['message']
        recivers_list.append(name)
        email1=mail.EmailMessage(subject, message , 'rajasaini12345641@gmail.com', recivers_list, connection=connection)
        email1.send()
        connection.close()
    return  render(request, "individual-mail.html")


def Institutionsingeemail(request):
    if request.method=='POST':
        from django.core import mail
        connection=mail.get_connection()
        connection.open()
        recivers_list=[]
        name=request.POST['name']
        subject=request.POST['subject']
        message=request.POST['message']
        recivers_list.append(name)
        email1=mail.EmailMessage(subject, message , 'rajasaini12345641@gmail.com', recivers_list, connection=connection)
        email1.send()
        connection.close()
    return  render(request, "individual-mail.html")


def location(request):
    if request.method=='POST':
        country1=request.POST['country']
        state=request.POST['state']
        city=request.POST['city']
        locat=location1(country=country1, state=state, city=city)
        locat.save()
        return render(request, 'locat.html')

    return render(request, 'locat.html')


def customerdetails(request):
    customer1=customer.objects.all()
    return render(request,'customer.html',  {'context': customer1})



def orederdetails(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        iteam_jso=request.POST['itemsJson']
        amount=request.POST['amount']
        phone=request.POST['phone']
        data=json.loads(iteam_jso)
        prices=request.POST['prices1']
        qty=request.POST['items1']

        val1=""
        for val in data['pr'][1]:
            val1=val1 + val
            order=Order(    items_json= iteam_jso,  name=name, email=email,  amount=amount, phone=phone,  coursename=val1, prices=prices, qty=qty)
            order.save()
            thank = True
            id = order.order_id
            return render(request, 'checkout.html', {'thank':thank, 'id': id})
    return render(request, 'checkout.html')






def InvoicePDFView(request, id):
    obj = get_object_or_404(Order, order_id=id)
    obj={"obj1":obj}
    template_name =get_template('invoice-template.html')
    respone=BytesIO()
    data=template_name.render(obj)
    pdfpage=pisa.pisaDocument(BytesIO(data.encode("ISO-8859-1")), respone)
    if not pdfpage.err:
        return HttpResponse(respone.getvalue(), content_type='application/pdf')
    else:
        return HttpResponse('error genertation pdf')
