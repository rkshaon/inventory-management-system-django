# Generated by Django 4.1.1 on 2022-11-24 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='category')),
                ('is_deleted', models.BooleanField(default=False)),
                ('added_date_time', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
