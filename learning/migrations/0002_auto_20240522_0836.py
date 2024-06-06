# Generated by Django 3.2.25 on 2024-05-22 05:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filetransfer',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='filetransfer',
            name='file',
        ),
        migrations.AlterField(
            model_name='filetransfer',
            name='otp',
            field=models.CharField(default=None, max_length=6),
        ),
        migrations.CreateModel(
            name='FileTransferFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploads/')),
                ('transfer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learning.filetransfer')),
            ],
        ),
    ]
