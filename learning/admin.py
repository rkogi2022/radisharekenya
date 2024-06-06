from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import ContactUs
from .models import FileTransfer
from .models import FileTransferFile
from .resources import ContactUsResource


admin.site.site_header="Radishare Dashboard"

# Register your models here.
class ContactUsAdmin(ImportExportModelAdmin):
    resource_class = ContactUsResource

admin.site.register(ContactUs, ContactUsAdmin)

admin.site.register(FileTransfer),

admin.site.register(FileTransferFile)

