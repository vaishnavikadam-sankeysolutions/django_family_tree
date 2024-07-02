# Generated by Django 5.0.6 on 2024-07-02 06:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='birth_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='from_person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relationships_from', to='tree.person'),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='relationship_type',
            field=models.CharField(choices=[('PARENT', 'Parent'), ('SPOUSE', 'Spouse'), ('CHILD', 'Child')], max_length=10),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='to_person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relationships_to', to='tree.person'),
        ),
    ]
