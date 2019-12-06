# Generated by Django 2.2.6 on 2019-12-05 14:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, default='no-img.jpg', upload_to='assets/images')),
                ('first_name', models.CharField(default='', max_length=255)),
                ('events', multiselectfield.db.fields.MultiSelectField(choices=[('event a', 'event a'), ('Offshore Riggers', 'Offshore Riggers'), ('Naval warfare', 'Naval warfare'), ('Data tussle', 'Data tussle'), ('Case Study', 'Case Study'), ('Beyond 2', 'Beyond 2'), ('OCEANIA QUIZ', 'OCEANIA QUIZ'), ('PAPER PRESENTATION', 'PAPER PRESENTATION'), ('Blockchain Workshop', 'Blockchain Workshop')], max_length=300)),
                ('email', models.EmailField(default='none@email.com', max_length=254)),
                ('birth_date', models.DateField(default='1999-12-31')),
                ('city', models.CharField(default='', max_length=255)),
                ('state', models.CharField(default='', max_length=255)),
                ('College', models.CharField(default='', max_length=255)),
                ('Contact', models.CharField(default='', max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
