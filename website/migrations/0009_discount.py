# Generated by Django 5.0.6 on 2024-06-22 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_pricesection_alter_pricecategory_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='заголовок')),
                ('validity', models.CharField(blank=True, help_text='Продолжите фразу: Опыт работы ...', max_length=300, verbose_name='срок действия')),
                ('photo', models.ImageField(upload_to='media/import/discount', verbose_name='фото')),
                ('about', models.TextField(blank=True, verbose_name='описание')),
                ('note', models.TextField(blank=True, verbose_name='примечание')),
            ],
            options={
                'verbose_name': 'акция',
                'verbose_name_plural': 'акции',
            },
        ),
    ]
