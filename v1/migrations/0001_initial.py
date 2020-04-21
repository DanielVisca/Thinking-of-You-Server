# Generated by Django 3.0.5 on 2020-04-13 23:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=1024, null=True)),
                ('auth_token', models.CharField(default='ammIO-mq8mKfPfNX-oi8t4Ob6Tf9uoLRte7_RVD_ajHt9uN0zqaC4mUbPQtRwqewXztJkiWof7kXYG4T6su1oQ', max_length=1024)),
                ('phone_number', models.CharField(max_length=30, null=True)),
                ('password', models.CharField(max_length=1024, null=True)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TOY',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_sent', models.DateTimeField()),
                ('seen', models.BooleanField(default=False)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='v1.User')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='v1.User')),
            ],
        ),
    ]