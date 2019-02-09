from django.contrib import admin
from .models import Player,Position,Stadium,Team
from django_admin_listfilter_dropdown .filters import (DropdownFilter,ChoiceDropdownFilter,RelatedDropdownFilter)
admin.site.register(Player)
admin.site.register(Position)
admin.site.register(Stadium)
admin.site.register(Team)


class EntityAdmin(admin.ModelAdmin):
    list_display = (
        'name'
    )
    list_filter = (
        ('a_charfield',DropdownFilter),
        ('a_choicefield', ChoiceDropdownFilter),
        ('a_foreign key_field',RelatedDropdownFilter)
    )
    search_fields = ['name']