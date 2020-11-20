# Generated by Django 3.1.3 on 2020-11-19 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stud', '0002_auto_20201119_0731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='grant',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='stud.grant', verbose_name='Грант'),
        ),
        migrations.AlterField(
            model_name='event',
            name='rate',
            field=models.CharField(choices=[('a', 'Наивысший'), ('б', 'Высокий'), ('в', 'Средний'), ('г', 'Низкий'), ('д', 'Наинизший')], default='в', max_length=1, verbose_name='Рейтинг мероприятия'),
        ),
    ]
