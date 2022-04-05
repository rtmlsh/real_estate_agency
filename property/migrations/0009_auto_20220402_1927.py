# Generated by Django 2.2.24 on 2022-04-02 16:27

from django.db import migrations
import phonenumbers

def create_pure_phonenumbers(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        phone_num = phonenumbers.parse(flat.owners_phonenumber, 'RU')
        flat.owner_pure_phone = phonenumbers.format_number(
                phone_num,
                phonenumbers.PhoneNumberFormat.E164
            ) if phonenumbers.is_valid_number(phone_num) else None
        flat.save()

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_flat_owner_pure_phone'),
    ]

    operations = [
        migrations.RunPython(create_pure_phonenumbers)
    ]
