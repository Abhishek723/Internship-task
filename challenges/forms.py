from django import forms
from challenges.models import Challenge,Tags
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Submit




class ChallengeForm(forms.ModelForm):
    class Meta:
        model = Challenge
        fields = ('title','text','end_date','published_date','active_solvers','price','tags','model_pic')
        
    