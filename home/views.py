from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from .forms import ContactForm
from .models import Contact, Portfolio


def index(request):
    return render(request, 'home/index.html')


def skills(request):
    return render(request, 'home/skills.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "پیام شما با موفقیت ارسال شد!")
            return redirect('home:contact')
        messages.error(request, "خطایی در ارسال پیام رخ داد. لطفاً اطلاعات را بررسی کنید.")
    else:
        form = ContactForm()
    return render(request, 'home/contact.html', {'form': form})


def experience(request):
    return render(request, 'home/experience.html')


def portfolio(request):
    portfolios = Portfolio.objects.all()
    return render(request, 'home/portfolio.html', {'portfolios': portfolios})


def portfolio_detail(request, id):
    portfolio = get_object_or_404(Portfolio, pk=id)
    return render(request, 'home/portfolio_detail.html', {'portfolio': portfolio})
