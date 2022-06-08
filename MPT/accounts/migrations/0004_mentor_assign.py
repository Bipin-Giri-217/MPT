# Generated by Django 4.0.4 on 2022-06-08 09:25

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_rename_mentors_mentorprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mentor_assign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('Mentee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.mentorprofile')),
                ('Mentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.studentprofile')),
            ],
        ),
    ]