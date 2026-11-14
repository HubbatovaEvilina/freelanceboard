from django import forms
from .models import Order, Response

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('title', 'description', 'category', 'budget')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'budget': forms.NumberInput(attrs={'class': 'form-control'}),
        }
from .models import Response # Добавьте этот импорт в начало файла

# Новая форма для отклика
class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ('message', 'proposed_budget')
        widgets = {
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Расскажите, почему вы подходите для этой задачи...'}),
            'proposed_budget': forms.NumberInput(attrs={'class': 'form-control'}),
        }