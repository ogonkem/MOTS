from django.contrib import admin
from .models import Organization, organizationOverview, Branch, HomeCell

# Register your models here.
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('user', 'organization_name', 'email', 'is_church', 'modified_date')
    list_editable = ('is_church',)
    list_filter = ('organization_name', 'modified_date')

class OrganizationOverviewAdmin(admin.ModelAdmin):
    list_display = ('organization',)

class BranchAdmin(admin.ModelAdmin):
    list_display = ('organization', 'branch_name')

class HomeCellAdmin(admin.ModelAdmin):
    list_display = ('organization', 'home_cell_name')

admin.site.register(Organization, OrganizationAdmin)
admin.site.register(organizationOverview, OrganizationOverviewAdmin)
admin.site.register(Branch, BranchAdmin)
admin.site.register(HomeCell, HomeCellAdmin)
