from django import forms
from .models import Voter


class AddVoterForm(forms.ModelForm):
    class Meta:
        model = Voter
        fields = "__all__"
