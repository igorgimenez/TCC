from django import forms
from django.forms import formset_factory, modelformset_factory
from .models import Roteiro


class RoteiroEditForm(forms.ModelForm):  
    class Meta:  
        model = Roteiro  
        fields = "__all__" 

class RoteiroForm(forms.Form):

    dia = forms.CharField(
        label='Dia',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Dia da viagem Ex: 1',
            'style': 'width: 100px;'
            
        })
        
    )

    horario_inicial = forms.CharField(
        label='Horario Inicial',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Horario inicial',
            'style': 'width: 100px;'
        })
        
    )

    horario_final = forms.CharField(
        label='Horario Final',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Horario final',
            'style': 'width: 100px;'
        })
        
    )

    lugar = forms.CharField(
        label='Lugar',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Lugar',
            'style': 'width: 100px;'
        })
    )
    acao = forms.CharField(
        label='Atividade',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Atividade',
            'style': 'width: 100px;'
        })
    )
    v_id = forms.CharField(
        label='v_id',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'v_id'
        }),
        
    required=False)



RoteiroFormset = formset_factory(RoteiroForm)
RoteiroModelFormset = modelformset_factory(
    Roteiro,
    fields=('dia','horario_inicial','horario_final', 'lugar','acao','v_id'),
    extra=5,
    widgets={
        'dia': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite dia'
            }
        ),
        'horario_inicial': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite o horario inicial'
            }
        ),
        'horario_final': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite o horario final'
            }
        ),
        'lugar': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Lugar'
            }
        ),
        'acao': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'acao'
            }
        ),
        'v_id': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'v_id'
            }
        )
    }
)