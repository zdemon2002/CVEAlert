# Generated by Django 5.0.3 on 2024-03-19 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0006_alter_cve_assigner_org_id_alter_cve_date_publish_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cve',
            name='year',
            field=models.CharField(default='', max_length=255),
        ),
    ]