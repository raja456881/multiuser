# Generated by Django 3.0.7 on 2020-09-27 11:34

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventory', '0001_initial'),
        ('multiuser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursedetails',
            name='franchise',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='multiuser.FranchiseProfile'),
        ),
        migrations.AddField(
            model_name='coursedetails',
            name='institute',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='multiuser.InstituteProfile'),
        ),
        migrations.AddField(
            model_name='coursedetails',
            name='trainer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='multiuser.TrainerProfile'),
        ),
        migrations.AddField(
            model_name='categories',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='inventory.Categories'),
        ),
    ]