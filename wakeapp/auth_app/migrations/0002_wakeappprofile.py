# Generated by Django 4.1.3 on 2022-12-08 14:10

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import wakeapp.auth_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WakeAppProfile',
            fields=[
                ('username', models.CharField(max_length=20, unique=True)),
                ('first_name', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2), wakeapp.auth_app.models.validate_only_letters])),
                ('last_name', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2), wakeapp.auth_app.models.validate_only_letters])),
                ('profile_image', models.ImageField(blank=True, max_length=255, upload_to=None)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Do not show', 'Do not show')], default='Do not show', max_length=11, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
