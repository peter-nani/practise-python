# Generated by Django 2.1.14 on 2020-06-14 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='it_emp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('emp_id', models.IntegerField),
                ('desk_no', models.CharField(max_length=100)),
                ('sytem_op_sy', models.CharField(max_length=100)),
                ('age', models.IntegerField),
                ('wing', models.CharField(max_length=100)),
                ('floor', models.CharField(max_length=100)),
            ],
        ),
    ]
