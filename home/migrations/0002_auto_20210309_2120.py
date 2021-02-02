# Generated by Django 2.2.13 on 2021-03-09 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='is_parent_section',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='section',
            name='parent_section',
            field=models.ForeignKey(blank=True, limit_choices_to={'is_parent_section': True}, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.Section'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='day',
            field=models.IntegerField(choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday')]),
        ),
    ]
