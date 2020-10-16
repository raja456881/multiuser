# Generated by Django 3.0.7 on 2020-09-27 11:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventory', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_FullName', models.CharField(blank=True, max_length=150)),
                ('student_About', models.CharField(blank=True, max_length=2500)),
                ('student_gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('others', 'Transgender')], max_length=50)),
                ('student_Image', models.FileField(blank=True, null=True, upload_to='Student_image/')),
                ('stdent_Email', models.EmailField(max_length=111)),
                ('student_created_at', models.DateTimeField(auto_now_add=True)),
                ('student_PhoneNo1', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('student_PhoneNo2', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('student_Address', models.CharField(default='', max_length=250)),
                ('student_City', models.CharField(default='', max_length=100)),
                ('student_Zipcode', models.IntegerField(default=273003)),
                ('student_State', models.CharField(default='', max_length=100)),
                ('student_Country', models.CharField(default='', max_length=100)),
                ('course_id', models.ManyToManyField(default=1, to='inventory.CourseDetails')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
