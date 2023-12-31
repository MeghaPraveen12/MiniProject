# Generated by Django 4.2.7 on 2023-11-29 03:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_screen_remove_movie_theatrescreen_movie_screen'),
    ]

    operations = [
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat', models.CharField(max_length=100)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.movie')),
                ('screen', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='booking.screen')),
            ],
        ),
    ]
