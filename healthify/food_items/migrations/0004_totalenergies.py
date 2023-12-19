# Generated by Django 4.1 on 2022-11-09 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food_items', '0003_adddetail_date_d'),
    ]

    operations = [
        migrations.CreateModel(
            name='TotalEnergies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_pro', models.IntegerField()),
                ('total_carbo', models.IntegerField()),
                ('total_fat', models.IntegerField()),
                ('total_cal', models.IntegerField()),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_items.adddate')),
            ],
        ),
    ]