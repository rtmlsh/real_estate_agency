from django.contrib import admin

from .models import Flat, Complaint, Owner

class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address', 'owner']
    readonly_fields = ['created_at']
    list_display = ['address', 'owners_phonenumber', 'owner_pure_phone', 'price', 'new_building', 'construction_year', 'town']
    list_editable = ['new_building']
    list_filter = ['new_building', 'rooms_number', 'has_balcony']
    raw_id_fields = ['liked_by']


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ['user', 'complaint_flat']


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ['own_flats']
    list_display = ['owner', 'owners_phonenumber', 'owner_pure_phone']


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)