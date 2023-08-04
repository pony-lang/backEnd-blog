# Generated by Django 3.2 on 2023-07-06 02:32

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='devtemplate',
            name='username',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='devtemplate',
            name='id',
            field=models.UUIDField(default=uuid.UUID('369bf9dc-68c5-48bf-a626-84f04ea3d26c'), editable=False, primary_key=True, serialize=False),
        ),
    ]
