# Generated by Django 4.2 on 2023-07-04 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0008_alter_department_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Subject_Marks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.IntegerField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studentmarks', to='vege.student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vege.subject')),
            ],
            options={
                'unique_together': {('student', 'subject')},
            },
        ),
    ]
