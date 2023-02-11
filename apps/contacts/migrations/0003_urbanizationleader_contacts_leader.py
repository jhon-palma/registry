# Generated by Django 4.1.5 on 2023-02-07 02:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_remove_contacts_leader_delete_urbanizationleader'),
    ]

    operations = [
        migrations.CreateModel(
            name='UrbanizationLeader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leaders', to='contacts.contacts')),
                ('urbanization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='urbanizations', to='contacts.urbanization')),
            ],
        ),
        migrations.AddField(
            model_name='contacts',
            name='leader',
            field=models.ManyToManyField(blank=True, related_name='urbanization_leader', through='contacts.UrbanizationLeader', to='contacts.urbanization'),
        ),
    ]