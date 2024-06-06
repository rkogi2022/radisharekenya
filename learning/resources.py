from import_export import resources
from .models import ContactUs

class ContactUsResource(resources.ModelResource):
    class Meta:
        model = ContactUs


