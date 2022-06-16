# Generated by Django 4.0.4 on 2022-06-16 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_coursefeedback'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CourseTeacher',
            new_name='CoursesTeacher',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='preamble',
            new_name='intro',
        ),
        migrations.AlterField(
            model_name='coursefeedback',
            name='feedback',
            field=models.TextField(default='Без отзыва', verbose_name='Отзыв'),
        ),
    ]
