# Generated by Django 5.0.4 on 2024-08-08 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0004_uploadedimage_delete_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('complete', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='UploadedImage',
        ),
    ]