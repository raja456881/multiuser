from django.urls import path
from . import views
urlpatterns = [
    #for view customer
     path('',views.Customer, name = 'view_Customer'),

    #To add customer

     path('add',views.addCustomer, name = 'add_Customer'),
     path('add_admin',views.addAdmin, name = 'add_Admin'),
     path('add_trainer',views.addTrainer, name = 'add_Trainer'),
     path('add_institute',views.addInstitute, name = 'add_Institute'),
     path('add_franchise',views.addFranchise, name = 'add_Franchise'),

     #To edit customer
     path('update_admin/<str:username>',views.updateAdmin, name = 'update_Admin'),
     path('update_trainer/<str:username>',views.updateTrainer, name = 'update_Trainer'),
     path('update_institute/<str:username>',views.updateInstitute, name = 'update_Institute'),
     path('update_franchise/<str:username>',views.updateFranchise, name = 'update_Franchise'),

     #To delete Customer
     path('delete_admin/<int:uniqueId>',views.deleteAdmin, name = 'delete_Admin'),
     path('delete_trainer/<int:uniqueId>',views.deleteTrainer, name = 'delete_Trainer'),
     path('delete_institute/<int:uniqueId>',views.deleteInstitute, name = 'delete_Institute'),
     path('delete_franchise/<int:uniqueId>',views.deleteFranchise, name = 'delete_Franchise'),


     #for pending users view
     path('pending',views.pendingUser, name = 'pending_User'),

     #to verify user

     path('verify_admin/<int:uniqueId>',views.verifyAdmin, name = 'verify_Admin'),
     path('verify_trainer/<int:uniqueId>',views.verifyTrainer, name = 'verify_Trainer'),
     path('verify_institute/<int:uniqueId>',views.verifyInstitute, name = 'verify_Institute'),
     path('verify_franchise/<int:uniqueId>',views.verifyFranchise, name = 'verify_Franchise'),

     
     #to discard user

     path('discard_admin/<str:username>',views.discardAdmin, name = 'discard_Admin'),
     path('discard_trainer/<str:username>',views.discardTrainer, name = 'discard_Trainer'),
     path('discard_institute/<str:username>',views.discardInstitute, name = 'discard_Institute'),
     path('discard_franchise/<str:username>',views.discardFranchise, name = 'discard_Franchise'),



     #to display profile
     path('profile_admin/<str:username>',views.adminProfile, name = 'admin_Profile'),
     path('profile_trainer/<str:username>',views.trainerProfile, name = 'trainer_Profile'),
     path('profile_institute/<str:username>',views.instituteProfile, name = 'institute_Profile'),
     path('profile_franchise/<str:username>',views.franchiseProfile, name = 'franchise_Profile'),

    
]