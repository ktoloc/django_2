from django import forms

from movie.models import MovieReview


class MovieReviewForm(forms.ModelForm):
    class Meta:
        model = MovieReview
        fields = ('content',)
        widgets = {'movie': forms.HiddenInput(), 'reviewer': forms.HiddenInput()}
