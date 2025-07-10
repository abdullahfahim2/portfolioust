from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Tailwind classes to all fields
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-[#3CCBFE]',
                'placeholder': self.get_placeholder(field_name)
            })
        # Special handling for textarea
        self.fields['message'].widget.attrs.update({'rows': '4'})
    
    def get_placeholder(self, field_name):
        placeholders = {
            'name': 'Enter Your name..',
            'email': 'Enter Email Here..',
            'subject': 'Add Subject ...',
            'message': 'Enter Your Message........'
        }
        return placeholders.get(field_name, '')