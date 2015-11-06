from django.contrib import admin
from west.models import Character,Contact,Tag

# Register your models here.
#class ContactAdmin(admin.ModelAdmin):
#    list_display = ('name', 'age', 'email')#list

class TagInline(admin.TabularInline):
    model = Tag


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'email')#list
    search_fields = ('name',)
    inlines = [TagInline] #Inline
    fieldsets = (
        ['Main',{
            'fields':('name','email'),
        }],
        ['Advance',{
            'classes': ('collapse',), #css
            'fields': ('age',),
        }]
    )


admin.site.register(Contact, ContactAdmin)
admin.site.register([Character])
