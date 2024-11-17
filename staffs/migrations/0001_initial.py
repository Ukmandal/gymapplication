# Generated by Django 5.1.3 on 2024-11-17 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staffs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staffs_id', models.CharField(max_length=10)),
                ('staffs_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.IntegerField(max_length=20)),
                ('email', models.EmailField(max_length=50)),
                ('dob', models.DateField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('stauts', models.CharField(max_length=2)),
            ],
        ),
    ]