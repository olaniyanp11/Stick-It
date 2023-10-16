# Generated by Django 4.2.6 on 2023-10-11 22:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_workspacetask_acheived'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workspace',
            name='Admin',
        ),
        migrations.RemoveField(
            model_name='workspace',
            name='members',
        ),
        migrations.RemoveField(
            model_name='workspacetask',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='workspacetask',
            name='workspace',
        ),
        migrations.DeleteModel(
            name='Task',
        ),
        migrations.DeleteModel(
            name='Workspace',
        ),
        migrations.DeleteModel(
            name='WorkspaceTask',
        ),
    ]
