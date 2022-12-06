from django import forms

level = [
    ('ЭКОНОМ', 'Эконом'),
    ('КОМФОРТ', 'Комфорт'),
    ('УНИВЕРСАЛ', 'Универсал'),
    ]

class CHOICES(forms.Form):
    level = forms.CharField(widget=forms.RadioSelect(choices=level))