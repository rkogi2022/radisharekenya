from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.contrib import messages
from .forms import FileTransferForm, OTPForm, ContactForm
from .models import FileTransfer, FileTransferFile
import random

def generate_otp():
    return ''.join([str(random.randint(0, 9)) for _ in range(6)])

def Index(request):
    if request.method == 'POST':
        form = FileTransferForm(request.POST, request.FILES)
        files = request.FILES.getlist('files')
        if form.is_valid() and files:
            transfer = form.save(commit=False)
            transfer.otp = generate_otp()
            transfer.save()
            for f in files:
                FileTransferFile.objects.create(transfer=transfer, file=f)
            send_mail(
                'Your verification code',
                f'Your verification code is {transfer.otp}',
                'from@example.com',
                [transfer.sender_email],
                fail_silently=False,
            )
            messages.info(request, 'Verification code sent to your email.')
            return redirect('verify', transfer_id=transfer.id)
    else:
        form = FileTransferForm()
    return render(request, 'learning/index.html', {'form': form})

def verify(request, transfer_id):
    transfer = get_object_or_404(FileTransfer, id=transfer_id)
    if request.method == 'POST':
        form = OTPForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['otp'] == transfer.otp:
                transfer.is_verified = True
                transfer.save()
                messages.success(request, 'Verification successful. File transferred.')
                return redirect('success', transfer_id=transfer.id)
            else:
                messages.error(request, 'Invalid verification code.')
    else:
        form = OTPForm()
    return render(request, 'learning/verify.html', {'form': form, 'transfer': transfer})

def success(request, transfer_id):
    transfer = get_object_or_404(FileTransfer, id=transfer_id)
    files = FileTransferFile.objects.filter(transfer=transfer)
    return render(request, 'learning/success.html', {'transfer': transfer, 'files': files})


def about(request):
    template='learning/aboutus.html'
    context={}
    return render(request,template, context)

def services(request):
    template='learning/whatwedo.html'
    context={}
    return render(request,template, context)

def pricing(request):
    template='learning/pricing.html'
    context={}
    return render(request,template, context)

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your request was sent successfully. We will get back to you as soon as possible.')
            return redirect('learning:index')  # Redirect to the homepage after saving
        else:
            # If form is not valid, display error messages
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
    else:
        form = ContactForm()
    return render(request, 'learning/contactus.html', {'form': form})