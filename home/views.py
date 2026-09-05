from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import ContactForm
from .models import Contact

# Create your views here.
def index(request):
    context = {}
    return render(request,'home/index.html',context)

def skills(request):
    context = {}
    return render(request,'home/skills.html',context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "پیام شما با موفقیت ارسال شد!")
            return redirect('home:contact') 
        else:
            messages.error(request, "خطایی در ارسال پیام رخ داد. لطفاً اطلاعات را بررسی کنید.")
    else:
        form = ContactForm()
    
    return render(request, 'home/contact.html', {'form': form})

def experience(request):
    context = {}
    return render(request,'home/experience.html',context)
def portfolio(request):
    context = {}
    return render(request,'home/portfolio.html',context)