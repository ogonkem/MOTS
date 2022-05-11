from django.db import models
from accounts.models import Account
from django.urls import reverse

# Create your models here.
class Organization(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True, null=True)
    organization_name = models.CharField(max_length=50)
    website_address = models.URLField(max_length=200, blank=True)
    email = models.EmailField(max_length=50)
    address_line_1 = models.CharField(max_length=50)
    address_line_2 = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=12, blank=True)
    country = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    logo = models.ImageField(upload_to='photos/logos')
    is_church = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    facebook = models.CharField(max_length=50, blank=True, null=True)
    youtube = models.CharField(max_length=50, blank=True, null=True)
    instagram = models.CharField(max_length=50, blank=True, null=True)
    open_hours = models.CharField(max_length=50, blank=True, null=True)

    def address(self):
        return f'{self.address_line_1} {self.address_line_2}'

    def province(self):
        return f'{self.city} {self.state} {self.country}'

    # def update_url(self):
    #     return reverse('update_organization', args=[self.id])
    #
    # def delete_url(self):
    #     return reverse('delete_organization', args=[self.id])

    # within the admin django pluralizes models by adding 's' to name
    # e.g. company = companys to correct this
    class Meta:
        verbose_name = 'organization'
        verbose_name_plural = 'organizations'

    def __str__(self):
        return self.organization_name

class organizationOverview(models.Model):
    organization = models.OneToOneField(
        Organization,
        on_delete=models.CASCADE,
        unique=True,
    )
    organization_overview = models.TextField(max_length=500, blank=True)
    organization_mandate = models.TextField(max_length=500, blank=True)
    mission_statement = models.TextField(max_length=500, blank=True)
    vision = models.TextField(max_length=500, blank=True)
    philosophy = models.TextField(max_length=500, blank=True)
    id = models.AutoField(primary_key=True, default=None)

    def update_url(self):
        return reverse('update_business_overview', args=[self.company_id])

    def delete_url(self):
        return reverse('delete_business_overview', args=[self.company_id])

    def __str__(self):
        return self.organization.organization_name

class Branch(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    branch_name = models.CharField(max_length=50)
    address_line_1 = models.CharField(max_length=50)
    address_line_2 = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=12, blank=True)
    country = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Branch'
        verbose_name_plural = 'Branches'

    def __str__(self):
        return self.branch_name

class HomeCell(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    home_cell_name = models.CharField(max_length=50)
    address_line_1 = models.CharField(max_length=50)
    address_line_2 = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=12, blank=True)
    country = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.home_cell_name

    class Meta:
        verbose_name = 'Home Cell'
        verbose_name_plural = 'Home Cells'
