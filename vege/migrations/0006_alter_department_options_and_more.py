# Generated by Django 4.2 on 2023-07-02 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0005_rename_student_id_student_id_student_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='department',
            options={'ordering': ['Department']},
        ),
        migrations.RenameField(
            model_name='department',
            old_name='department',
            new_name='Department',
        ),
    ]
