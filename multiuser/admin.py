from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(User)
admin.site.register(TrainerProfile)
admin.site.register(AdminProfile)
admin.site.register(InstituteProfile)
admin.site.register(FranchiseProfile)

