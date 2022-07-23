# Generated by Django 4.0.5 on 2022-07-23 10:05

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0002_alter_company_company_size_alter_employee_dob_and_more'),
        ('skills', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=50)),
                ('level', models.CharField(choices=[('JUNIOR', 'Junior'), ('SENIOR', 'Senior'), ('ENTRY-LEVEL', 'Entry-level')], max_length=50)),
                ('Description', models.TextField()),
                ('job_type', models.CharField(choices=[('FULLTIME', 'Full-Time'), ('PARTTIME', 'Part-Time'), ('INTERN', 'Internship')], max_length=50)),
                ('work_type', models.CharField(choices=[('REMOTE', 'Remote'), ('ONSITE', 'Onsite'), ('HYBRID', 'Hybrid')], max_length=50)),
                ('salary', models.IntegerField()),
                ('state', models.CharField(choices=[('OPEN', 'Open'), ('CLOSED', 'Closed')], default='OPEN', max_length=50)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.company', verbose_name='Company')),
                ('skills', models.ManyToManyField(blank=True, null=True, to='skills.skill')),
            ],
        ),
        migrations.CreateModel(
            name='AppliedEmployees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cv', models.FileField(blank=True, null=True, upload_to='user_cvs/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])])),
                ('notice_period', models.IntegerField()),
                ('years_of_exp', models.IntegerField()),
                ('cover_letter', models.TextField()),
                ('accepted', models.BooleanField(default=False)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.employee', verbose_name='Employee')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.job', verbose_name='Job')),
            ],
        ),
    ]
