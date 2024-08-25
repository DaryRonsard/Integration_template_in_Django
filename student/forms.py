from django import forms


class StudentForm(forms.Form):
    name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-check form-check-inline'}))
    last_name = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=100)
    old = forms.DateField(widget= forms.DateInput(attrs={"type": "date"}))
    classeroom = forms.ChoiceField(choices=[('Tle', 'Tle'), ('1er', '1er'), ('2nd', '2nd'),('3', "3"),('4', '4'), ('5', "5"), ('6', "6")])
    #classeroom = forms.CharField(max_length=100)
    identify = forms.CharField(max_length=100)
    classe = forms.CharField(max_length=100)
    identify = forms.CharField(max_length=100)


class StudentModifieForm(forms.Form):
    name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=100)
    old = forms.IntegerField()
    classe = forms.CharField(max_length=100)
    identify = forms.CharField(max_length=100)
    classeroom = forms.CharField(max_length=100)
    identify = forms.CharField(max_length=100)