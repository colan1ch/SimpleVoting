from django import forms


class EditVotingForm(forms.Form):
    TYPES = ['first', 'second', 'third']
    title = forms.CharField(required=True)
    text = forms.CharField()
    type = forms.Select(choices=TYPES)
    option_1 = forms.CharField(required=True)
    option_2 = forms.CharField(required=True)
    option_3 = forms.CharField(required=False)
    option_4 = forms.CharField(required=False)
