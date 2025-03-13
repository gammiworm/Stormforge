# Generated by Django 5.1.7 on 2025-03-13 06:09

from django.db import migrations, connection

def create_datapoint_table(apps, schema_editor):
    with connection.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS datapoint (
                id SERIAL PRIMARY KEY,
                x_value FLOAT NOT NULL,
                y_value FLOAT NOT NULL,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)

def create_dataset_table(apps, schema_editor):
    with connection.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS dataset (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                description TEXT
            );
        """)

class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.RunPython(create_datapoint_table),
        migrations.RunPython(create_dataset_table),
    ]
