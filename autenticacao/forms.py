from django import forms  
from autenticacao.models import Autenticacao  

class AutenticacaoForm(forms.Form):  
    class Meta:  
        model = Autenticacao  
        fields = "__all__"
       
    senha = forms.CharField(
        label='Senha',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Dia da viagem Ex: 1',
            'style': 'width: 100px;'
            
        })
        
    )
    confirma = forms.CharField(
        label='Senha',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Dia da viagem Ex: 1',
            'style': 'width: 100px;'
            
        })
        
    )

def clean(self):
    cleaned_data = super.clean()

    p1=cleaned_data.get('senha')
    p2=cleaned_data.get('confirma')

    if p1 != p2:
        raise forms.ValidationError("Senhas divergentes")