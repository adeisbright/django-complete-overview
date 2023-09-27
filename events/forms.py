from django import forms


choices = (("Lagos", "Ikeja"), ("Ondo", "Akure"))


class EventsForm(forms.Form):
    title = forms.CharField(required=True, label="Title", max_length=50)
    description = forms.CharField(widget=forms.Textarea)
    price = forms.FloatField(min_value=10, max_value=10000)
    venue = forms.ChoiceField(choices=choices)

    # creator = forms.IntegerField(label="creator")
    # start_date = forms.DateField(label="start date")
