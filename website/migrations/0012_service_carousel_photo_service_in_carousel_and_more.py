# Generated by Django 5.0.6 on 2024-06-23 05:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_alter_contacts_working_hours_alter_discount_validity'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='carousel_photo',
            field=models.ImageField(blank=True, null=True, upload_to='media/import/service', verbose_name='фото для карусели'),
        ),
        migrations.AddField(
            model_name='service',
            name='in_carousel',
            field=models.BooleanField(default=True, verbose_name='отображать в карусели'),
        ),
        migrations.AddField(
            model_name='service',
            name='specialist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='services', to='website.specialist', verbose_name='специалист'),
        ),
    ]
