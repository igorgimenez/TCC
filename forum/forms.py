from django import forms  
from forum.models import Comentario, Forum , ReportarTopico, ReportarComentario

class ForumForm(forms.ModelForm):  
    class Meta:  
        model = Forum  
        fields = "__all__"



class ComentarioForm(forms.ModelForm):  
    class Meta:  
        model = Comentario  
        fields = "__all__"

class ReportarTopicoForm(forms.ModelForm):  
    class Meta:  
        model = ReportarTopico  
        fields = "__all__"

class ReportarComentarioForm(forms.ModelForm):  
    class Meta:  
        model = ReportarComentario  
        fields = "__all__"