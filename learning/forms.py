from django import forms
from .models import FileTransfer, ContactUs

class FileTransferForm(forms.ModelForm):
    sender_email = forms.EmailField(
        label='From:',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Sender\'s Email'})
    )
    receiver_email = forms.EmailField(
        label='To:',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Receiver\'s Email'})
    )
    title = forms.CharField(
        label='Title',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'})
    )
    message = forms.CharField(
        label='Message',
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message', 'rows': 3})
    )
    files = forms.FileField(
    label='Upload File',
    widget=forms.ClearableFileInput(attrs={'class': 'form-control'}),
    required=True
    )
    class Meta:
        model = FileTransfer
        fields = ['sender_email', 'receiver_email', 'title', 'message', 'files']

class OTPForm(forms.Form):
    otp = forms.CharField(
        max_length=6,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter OTP'})
    )

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'message']
