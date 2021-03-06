# Generated by Django 2.2 on 2019-04-27 06:13

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('author', models.CharField(max_length=500)),
                ('published_date', models.DateField(default=datetime.date.today)),
                ('genre', models.CharField(max_length=100)),
                ('keyword', models.CharField(max_length=1000, null=True)),
                ('ebook_logo', models.FileField(upload_to='')),
                ('bookpdf', models.FileField(blank=True, null=True, upload_to='')),
                ('bookurl', models.CharField(default='D:\\IIIT-B\\2nd_SEM\\DataModeling\\DM_Custom_Ebook\\Django_Project\\EBook3\\media', max_length=500)),
                ('ebook_price', models.DecimalField(decimal_places=2, max_digits=100)),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=2000)),
                ('start_page', models.IntegerField()),
                ('end_page', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=100)),
                ('ebook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.EBook')),
            ],
        ),
    ]
