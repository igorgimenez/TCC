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


