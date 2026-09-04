from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name', 'email', 'subject', 'message']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'w-full p-3 bg-gray-800 border border-gray-700 rounded-lg focus:border-blue-500 outline-none'}),
            'email': forms.EmailInput(attrs={'class': 'w-full p-3 bg-gray-800 border border-gray-700 rounded-lg focus:border-blue-500 outline-none'}),
            'subject': forms.TextInput(attrs={'class': 'w-full p-3 bg-gray-800 border border-gray-700 rounded-lg focus:border-blue-500 outline-none'}),
            'message': forms.Textarea(attrs={'class': 'w-full p-3 bg-gray-800 border border-gray-700 rounded-lg focus:border-blue-500 outline-none', 'rows': 5}),
        }
