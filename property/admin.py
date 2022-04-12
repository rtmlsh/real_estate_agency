from django.contrib import admin

from .models import Complaint, Flat, Owner


class PropertyOwnerOwnFlatsInline(admin.TabularInline):
    model = Flat.owned_by.through
    raw_id_fields = ['owner']
    list_display = ['owner']


class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address', 'owner']
    readonly_fields = ['created_at']
    list_display = ['address', 'price', 'new_building', 'construction_year', 'town']
    list_editable = ['new_building']
    list_filter = ['new_building', 'rooms_number', 'has_balcony']
    raw_id_fields = ['liked_by']
    inlines = [
        PropertyOwnerOwnFlatsInline
    ]


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ['user', 'complaint_flat']


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ['own_flats']
    list_display = ['owner', 'owners_phonenumber', 'owner_pure_phone']


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)
