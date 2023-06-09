# Generated by Django 4.2.1 on 2023-05-14 15:34

from django.db import migrations

def populate_roles(apps,schemaeditor):
    entries = {
        "Veterinarian":"Responsible for the healthcare program for the animal collection and the maintenance of health records.",
        "Veterinary Technician":"Responsible for the healthcare program for the animal collection and the maintenance of health records.",
        "Keeper/Aquarist":"Provides daily care to the institution's animals, including diet preparation, cleaning, general exhibit maintenance, and record keeping.",
        "Senior Keeper/Aquarist":"Provides primary animal care for a department.",
        "Head Keeper/Aquarist":"Supervises a section or department of the institution; provides training and scheduling for keepers.",
        "Animal Curator":"Manages a certain portion of an institution's animal collection; i.e., mammals, birds, fish,reptiles, etc.",
        "General Curator":"Oversees an institution's entire animal collection and animal management staff. Responsible for strategic collection planning."
    }
    Role = apps.get_model("accounts","Role")
    for key, value in entries.items():
        role = Role(name=key, description=value)
        role.save()

def populate_departments(apps,schemaeditor):
    entries = {
        "Veterinary":"The department tasked with taking care of animal health",
        "Ecotherm":"First and lizards department",
        "Husbandy":"Hoofed animals department",
        "Avian":"Birds and bird-like animals department",
        "Mammal":"Mammalian species department",
    }
    Department = apps.get_model("accounts","Department")
    for key, value in entries.items():
        dept = Department(name=key,description=value)
        dept.save()


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_departments),
        migrations.RunPython(populate_roles)
    ]
