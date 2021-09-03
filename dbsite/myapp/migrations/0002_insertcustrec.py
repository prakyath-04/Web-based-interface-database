# Generated by Django 3.2.6 on 2021-08-24 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InsertCustRec',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30)),
                ('middlename', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('street', models.CharField(max_length=20)),
                ('house_no', models.IntegerField()),
                ('apt_no', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('zip', models.IntegerField()),
                ('gender', models.CharField(max_length=1)),
                ('mart_status', models.CharField(max_length=1)),
            ],
        ),
    ]