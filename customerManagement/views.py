from django.shortcuts import render ,  redirect
from .forms import *
from multiuser.models import *
from django.shortcuts import HttpResponse
from django.contrib.auth  import  get_user_model
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
#from itertools import chain
# Create your views here.


def Customer(request):

    #get details from all multiuser model
    adminDetails = AdminProfile.objects.all()
    trainerDetails = TrainerProfile.objects.all()
    instituteDetails = InstituteProfile.objects.all()
    franchiseDetails = FranchiseProfile.objects.all()

    context = {'franchiseDetails':franchiseDetails,'adminDetails':adminDetails,
               'instituteDetails':instituteDetails,'trainerDetails':trainerDetails}

    return render(request,'crm/view_customer.html',context)

def addCustomer(request):
    adminForm = AdminForm()
    userForm = UserForm()
    trainerForm = TrainerForm()
    studentForm=StudentForm
    context = {'adminForm':adminForm,'userForm':userForm,'trainerForm':trainerForm}
    return render(request,'crm/addUser.html',context)

def addAdmin(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        if ' ' in username:
            messages.info(request , "Error there is space in Username")
            return redirect('view_Customer')
        password = request.POST['password']
        email= request.POST['email']
        try:
            about= request.POST['about']
        except:
            about = ''
        try:
            middle_name = request.POST['middle_name']
        except:
            middle_name = ''
        if middle_name == '':
            full_name = first_name +" "+ last_name
        else:
            full_name = first_name+" "+ middle_name+" "+ last_name
        #image= request.FILES['image']
        gender=request.POST['gender']
        image=''
        phone1 = request.POST['phone1']
        phone2 = request.POST['phone2']
        address = request.POST['address']
        city = request.POST['city']
        postal_code = request.POST['postal_code']
        country = request.POST['country']
        state = request.POST['state']
        status = request.POST['status']

        if User.objects.filter(username = username).exists():
            messages.info(request,'Username already exists')
            return redirect("view_Customer")
        elif User.objects.filter(email = email).exists():
            messages.info(request,'Email already exists')
            return redirect("view_Customer")
        else:
            user=get_user_model()
            new_user = user.objects.create_user(username = username, first_name = first_name , last_name =last_name, password = password ,is_admin=True)
            new_user.save()

            new_admin = AdminProfile.objects.create(user = new_user,adminFullName= full_name, adminGender =gender, adminAbout = about ,adminImage =image , adminPhoneNo1 = phone1 ,
                                                    adminPhoneNo2 = phone2 , adminAddress = address , adminCountry = country, adminCity = city,
                                                    adminPostalCode = postal_code ,adminState = state , adminEmail = email, adminStatus = status
                                                    )
            new_admin.save()
         

            messages.info(request,'Admin is added succesfully')
            return redirect("view_Customer")

def addTrainer(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        if ' ' in username:
            messages.info(request , "Error there is space in Username")
            return redirect('view_Customer')
        password = request.POST['password']
        email= request.POST['email']
        try:
            about= request.POST['about']
        except:
            about = ''
        try:
            middle_name = request.POST['middle_name']
        except:
            middle_name = ''
        if middle_name == '':
            full_name = first_name +" "+ last_name
        else:
            full_name = first_name+" "+ middle_name+" "+ last_name
        gender=request.POST['gender']
        #image= request.FILES['image']
        image=''
        phone1 = request.POST['phone1']
        phone2 = request.POST['phone2']
        address = request.POST['address']
        city = request.POST['city']
        postal_code = request.POST['postal_code']
        country = request.POST['country']
        state = request.POST['state']
        status = request.POST['status']
        if User.objects.filter(username = username).exists():
            messages.info(request,'Username already exists')
            return redirect("view_Customer")
        elif User.objects.filter(email = email).exists():
            messages.info(request,'Email already exists')
            return redirect("view_Customer")
        else:
            user=get_user_model()
            new_user = user.objects.create_user(username = username, first_name = first_name , last_name =last_name, password = password ,is_trainer=True)
            new_user.save()

            new_trainer = TrainerProfile.objects.create(user = new_user,trainerFullName= full_name, trainerGender =gender,trainerAbout = about , trainerImage =image , trainerPhoneNo1 = phone1 ,
                                                    trainerPhoneNo2 = phone2 , trainerAddress = address , trainerCountry = country, trainerCity = city,
                                                    trainerPostalCode = postal_code,trainerState = state , trainerEmail = email, trainerStatus = status
                                                    )
            new_trainer.save()

            messages.info(request,'Tranier is added succesfully')
            return redirect("view_Customer")

def addInstitute(request):
    if request.method == 'POST':
        username = request.POST['username']
        if ' ' in username:
            messages.info(request , "Error there is space in Username")
            return redirect('view_Customer')
        password = request.POST['password']
        email= request.POST['email']
        full_name = request.POST['full_name']
        try:
            about= request.POST['about']
        except:
            about = ''
        #image= request.FILES['image']
        image=''
        phone1 = request.POST['phone1']
        phone2 = request.POST['phone2']
        address = request.POST['address']
        city = request.POST['city']
        postal_code = request.POST['postal_code']
        country = request.POST['country']
        state = request.POST['state']
        status = request.POST['status']
        if User.objects.filter(username = username).exists():
            messages.info(request,'Username already exists')
            return redirect("view_Customer")
        elif User.objects.filter(email = email).exists():
            messages.info(request,'Email already exists')
            return redirect("view_Customer")
        else:
            user=get_user_model()
            new_user = user.objects.create_user(username = username, password = password ,is_institute=True)
            new_user.save()

            new_institute = InstituteProfile.objects.create(user = new_user,instituteName= full_name ,instituteAbout = about  ,instituteImage =image , institutePhoneNo1 = phone1 ,
                                                    institutePhoneNo2 = phone2 , instituteAddress = address , instituteCountry = country,instituteCity = city,
                                                    institutePostalCode = postal_code,instituteState = state , instituteEmail = email, instituteStatus = status
                                                    )
            new_institute.save()



            messages.info(request,'Institute is added succesfully')
            return redirect("view_Customer")


def addFranchise(request):
    if request.method == 'POST':
        username = request.POST['username']
        if ' ' in username:
            messages.info(request , "Error there is space in Username")
            return redirect('view_Customer')
        password = request.POST['password']
        email= request.POST['email']
        full_name = request.POST['full_name']
        try:
            about= request.POST['about']
        except:
            about = ''
        #image= request.FILES['image']
        image=''
        phone1 = request.POST['phone1']
        phone2 = request.POST['phone2']
        address = request.POST['address']
        country = request.POST['country']
        city = request.POST['city']
        postal_code = request.POST['postal_code']
        state = request.POST['state']
        status = request.POST['status']
        user=get_user_model()
        if User.objects.filter(username = username).exists():
            messages.info(request,'Username already exists')
            return redirect("view_Customer")
        elif User.objects.filter(email = email).exists():
            messages.info(request,'Email already exists')
            return redirect("view_Customer")
        else:
            new_user = user.objects.create_user(username = username, password = password ,is_franchise=True)
            new_user.save()

            new_franchise = FranchiseProfile.objects.create(user = new_user,franchiseName= full_name ,franchiseAbout = about , franchiseImage =image , franchisePhoneNo1 = phone1 ,
                                                    franchisePhoneNo2 = phone2 , franchiseAddress = address , franchiseCountry = country,franchiseCity = city,
                                                    franchisePostalCode = postal_code,franchiseState = state , franchiseEmail = email, franchiseStatus = status
                                                    )
            new_franchise.save()



            messages.info(request,'Franchise is added succesfully')
            return redirect("view_Customer")



def updateAdmin(request , username):
    user = User.objects.get(username =username)
    admin = AdminProfile.objects.get(user = user)
    adminForm = AdminForm(instance = admin)
    if request.method == 'POST':
        adminForm = AdminForm(request.POST , request.FILES,instance = admin)
        username1 = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        if adminForm.is_valid():
            try:
                User.objects.filter(username=username).update(username=username1 , first_name = first_name , last_name=last_name )
            except:
                messages.info(request,'Username already exists')
                return redirect("view_Customer")
            adminForm.save()
            messages.info(request,"Changes are made successfully")
            return redirect('view_Customer')
        else:
            messages.info(request,adminForm.errors)
            return redirect('view_Customer')
    context = {'adminForm':adminForm, 'admin':admin , 'user':user}
    return render(request,'crm/updateAdmin.html',context)


def updateTrainer(request , username):
    user = User.objects.get(username =username)
    trainer = TrainerProfile.objects.get(user = user)
    trainerForm = TrainerForm(instance = trainer)
    if request.method == 'POST':
        trainerForm = TrainerForm(request.POST , request.FILES,instance = trainer)
        username1 = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        if trainerForm.is_valid():
            try:
                User.objects.filter(username=username).update(username=username1 , first_name = first_name , last_name=last_name )
            except:
                messages.info(request,'Username already exists')
                return redirect("view_Customer")
            trainerForm.save()
            messages.info(request,"Changes are made successfully")
            return redirect('view_Customer')
        else:
            messages.info(request,trainerForm.errors)
            return redirect('view_Customer')
    context = {'trainerForm':trainerForm, 'trainer':trainer , 'user':user}
    return render(request,'crm/updateTrainer.html',context)

def updateInstitute(request , username):
    user = User.objects.get(username =username)
    institute = InstituteProfile.objects.get(user = user)
    instituteForm = InstituteForm(instance = institute)
    if request.method == 'POST':
        instituteForm = InstituteForm(request.POST , request.FILES,instance = institute)
        username1 = request.POST['username']
        if instituteForm.is_valid():
            try:
                User.objects.filter(username=username).update(username=username1)
            except:
                messages.info(request,'Username already exists')
                return redirect("view_Customer")
            instituteForm.save()
            messages.info(request,"Changes are made successfully")
            return redirect('view_Customer')
        else:
            messages.info(request,instituteForm.errors)
            return redirect('view_Customer')
    context = {'instituteForm':instituteForm, 'institute':institute , 'user':user}
    return render(request,'crm/updateInstitute.html',context)


def updateFranchise(request , username):
    user = User.objects.get(username =username)
    franchise = FranchiseProfile.objects.get(user = user)
    franchiseForm = FranchiseForm(instance = franchise)
    if request.method == 'POST':
        franchiseForm = FranchiseForm(request.POST , request.FILES,instance = franchise)
        username1 = request.POST['username']
        if franchiseForm.is_valid():
            try:
                User.objects.filter(username=username).update(username=username1)
            except:
                messages.info(request,'Username already exists')
                return redirect("view_Customer")
            franchiseForm.save()
            messages.info(request,"Changes are made successfully")
            return redirect('view_Customer')
        else:
            messages.info(request,franchiseForm.errors)
            return redirect('view_Customer')
    context = {'franchiseForm':franchiseForm, 'franchise':franchise , 'user':user}
    return render(request,'crm/updateFranchise.html',context)





def deleteAdmin(request , uniqueId):
    if request.method == 'POST' or 'GET':
        user = User.objects.get(id=uniqueId)
        admin = AdminProfile.objects.get(user=user)
        name = user.username
        user.delete()
        admin.delete()
        messages.info(request ,"{} username of admin is deleted succesfully".format(name))
        return redirect('view_Customer')

def deleteTrainer(request , uniqueId):
    if request.method == 'POST' or 'GET':
        user = User.objects.get(id=uniqueId)
        trainer = TrainerProfile.objects.get(user=user)
        name = user.username
        user.delete()
        trainer.delete()
        messages.info(request ,"{} username of trainer is deleted succesfully".format(name))
        return redirect('view_Customer')

def deleteInstitute(request , uniqueId):
    if request.method == 'POST' or 'GET':
        user = User.objects.get(id=uniqueId)
        institute = InstituteProfile.objects.get(user=user)
        name = user.username
        user.delete()
        institute.delete()
        messages.info(request ,"{} username of institute is deleted succesfully".format(name))
        return redirect('view_Customer')

def deleteFranchise(request , uniqueId):
    if request.method == 'POST' or 'GET':
        user = User.objects.get(id=uniqueId)
        franchise = FranchiseProfile.objects.get(user=user)
        name = user.username
        user.delete()
        franchise.delete()
        messages.info(request ,"{} username of franchise is deleted succesfully".format(name))
        return redirect('view_Customer')


def pendingUser(request):

    #to display pending user which are yet to verify

    adminDetails = AdminProfile.objects.all().filter(adminStatus = 'Pending')
    trainerDetails = TrainerProfile.objects.all().filter(trainerStatus = 'Pending')
    instituteDetails = InstituteProfile.objects.all().filter(instituteStatus = 'Pending')
    franchiseDetails = FranchiseProfile.objects.all().filter(franchiseStatus = 'Pending')
    context = {'franchiseDetails':franchiseDetails,'adminDetails':adminDetails,
               'instituteDetails':instituteDetails,'trainerDetails':trainerDetails}

    return render(request,'crm/pendingUser.html',context)


#to verfiy admin trainer franchise and institute


def verifyAdmin(request , uniqueId):
    if request.method == 'POST' or 'GET':
        user = User.objects.get(id=uniqueId)
        AdminProfile.objects.filter(user=user).update(adminStatus = 'Verified')
        obj = AdminProfile.objects.get(user=user)
        name = obj.adminFullName
        messages.info(request,"{} is approved".format(name))
        return redirect('view_Customer')

def verifyTrainer(request , uniqueId):
    if request.method == 'POST' or 'GET':
        user = User.objects.get(id=uniqueId)
        TrainerProfile.objects.filter(user=user).update(trainerStatus = 'Verified')
        obj = TrainerProfile.objects.get(user=user)
        name = obj.trainerFullName
        messages.info(request,"{} is approved".format(name))
        return redirect('view_Customer')

def verifyFranchise(request , uniqueId):
    if request.method == 'POST' or 'GET':
        user = User.objects.get(id=uniqueId)
        FranchiseProfile.objects.filter(user=user).update(franchiseStatus = 'Verified')
        obj = FranchiseProfile.objects.get(user=user)
        name = obj.franchiseName
        messages.info(request,"{} is approved".format(name))
        return redirect('view_Customer')


def verifyInstitute(request , uniqueId):
    if request.method == 'POST' or 'GET':
        user = User.objects.get(id=uniqueId)
        InstituteProfile.objects.filter(user=user).update( instituteStatus = 'Verified')
        obj = InstituteProfile.objects.get(user=user)
        name = obj.instituteName
        messages.info(request,"{} is approved".format(name))
        return redirect('view_Customer')

    #to discard admin trainer franchise and institute

def discardAdmin(request , username):
    if request.method == 'POST' or 'GET':
        user = User.objects.get(username=username)
        AdminProfile.objects.filter(user=user).update(adminStatus = 'Discarded')
        obj = AdminProfile.objects.get(user=user)
        name = obj.adminFullName
        messages.info(request,"{} is discarded".format(name))
        return redirect('view_Customer')


def discardTrainer(request , username):
    if request.method == 'POST' or 'GET':
        user = User.objects.get(username=username)
        TrainerProfile.objects.filter(user=user).update(trainerStatus = 'Discarded')
        obj = TrainerProfile.objects.get(user=user)
        name = obj.trainerFullName
        messages.info(request,"{} is discarded".format(name))
        return redirect('view_Customer')


def discardFranchise(request , username):
    if request.method == 'POST' or 'GET':
        user = User.objects.get(username=username)
        FranchiseProfile.objects.filter(user=user).update(franchiseStatus = 'Discarded')
        obj = FranchiseProfile.objects.get(user=user)
        name = obj.franchiseName
        messages.info(request,"{} is discarded".format(name))
        return redirect('view_Customer')

def discardInstitute(request , username):
    if request.method == 'POST' or 'GET':
        user = User.objects.get(username=username)
        InstituteProfile.objects.filter(user=user).update( instituteStatus = 'Discarded')
        obj = InstituteProfile.objects.get(user=user)
        name = obj.instituteName
        messages.info(request,"{} is discarded".format(name))
        return redirect('view_Customer')
    

    #to display profile of various users 

def adminProfile(request , username):
    user = User.objects.get(username = username)
    admin = AdminProfile.objects.get(user = user)
    profile = 'admin'
    context = {'admin':admin,'profile':profile}
    return render(request,'crm/profile-view.html',context)


def trainerProfile(request , username):
    user = User.objects.get(username = username)
    trainer = TrainerProfile.objects.get(user = user)
    profile = 'trainer'
    context = {'trainer':trainer,'profile':profile}
    return render(request,'crm/profile-view.html',context)

def instituteProfile(request , username):
    user = User.objects.get(username = username)
    institute = InstituteProfile.objects.get(user = user)
    profile = 'institute'
    context = {'institute':institute,'profile':profile}
    return render(request,'crm/profile-view.html',context)

def franchiseProfile(request , username):
    user = User.objects.get(username = username)
    franchise = FranchiseProfile.objects.get(user = user)
    profile = 'franchise'
    context = {'franchise':franchise,'profile':profile}
    return render(request,'crm/profile-view.html',context)
          
        
        
            
            
