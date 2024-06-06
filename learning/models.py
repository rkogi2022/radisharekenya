from django.db import models

class FileTransfer(models.Model):
    sender_email = models.EmailField()
    receiver_email = models.EmailField()
    title = models.CharField(max_length=255)
    message = models.TextField()
    otp = models.CharField(max_length=6, default=None)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class FileTransferFile(models.Model):
    transfer = models.ForeignKey(FileTransfer, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/')
    
    def __str__(self):
        return self.file

class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.message}"