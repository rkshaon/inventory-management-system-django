# Generated by Django 4.1.1 on 2022-11-25 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ims_user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.TextField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('cell', models.CharField(blank=True, max_length=500, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('added_date_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]