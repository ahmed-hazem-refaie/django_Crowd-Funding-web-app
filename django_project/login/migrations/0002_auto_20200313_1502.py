# Generated by Django 3.0.3 on 2020-03-13 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='code',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('F', 'female'), ('M', 'male')], default=None, max_length=2),
        ),
        migrations.AddField(
            model_name='user',
            name='state',
            field=models.CharField(choices=[('A', 'active'), ('D', 'disable')], default='A', max_length=2),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='login/static'),
        ),
    ]
