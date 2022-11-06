from django import forms
from django.forms import formset_factory, modelformset_factory
from .models import Custo


class CustoEditForm(forms.ModelForm):  
    class Meta:  
        model = Custo  
        fields = "__all__"


Escolha = (
    ("Alimentação", ("Alimentação")),
    ("Passagem Viagem", ("Passagem Viagem")),
    ("Transporte", ("Transporte")),
    ("Compras", ("Compras")),
    ("Atividade", ("Atividade")),
    ("Outro", ("Outro")),
)



class CustoForm(forms.Form):

    tipo = forms.ChoiceField(choices = Escolha, label="", initial='', widget=forms.Select(), required=True)
        
    

    valor = forms.CharField(
        label='valor',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'valor'
        })
        
    )
    obs = forms.CharField(
        label='obs',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'obs'
        })
    )
    v_id = forms.CharField(
        label='v_id',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'v_id'
        }),
        
    required=False)



CustoFormset = formset_factory(CustoForm)
CustoModelFormset = modelformset_factory(
    Custo,
    fields=('tipo','valor', 'obs','v_id'),
    extra=4,
    widgets={
        'tipo': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite tipo'
            }
        ),
        'valor': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite a valor'
            }
        ),
        'obs': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'obs'
            }
        ),
        'v_id': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'v_id'
            }
        )
    }
)