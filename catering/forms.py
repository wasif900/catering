from django import forms
from .models import gigs

class ImageForm(forms.ModelForm):
    class Meta:
        model=gigs
        fields=("gig1_image","gig2_image","gig3_image",)

