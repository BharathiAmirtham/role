from django.contrib import admin
from .models import Person
from .models import Role,Admin

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'department')


# admin.site.site_header = 'Scientific Journal Admin'
# admin.site.site_title = 'Scientific Journal '
# admin.site.site_url = 'http://Scientific+Jounal.com/'
# admin.site.index_title = 'Scientific Journal administration'
# admin.empty_value_display = '**Empty**'

admin.site.register(Role)
admin.site.register(Admin)
