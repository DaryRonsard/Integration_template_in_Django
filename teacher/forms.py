from django import forms


class TeacherForm(forms.Form):
    name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=100)
    old = forms.IntegerField()
    vacant = forms.BooleanField()
    matiereEnseigne = forms.CharField()
    prochainCours = forms.CharField(max_length=100)
    sujetProchaineReunion = forms.CharField(max_length=100)



class TeacherModifieForm(forms.Form):
    name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=100)
    old = forms.IntegerField()
    vacant = forms.BooleanField()
    matiereEnseigne = forms.CharField(max_length=100)
    prochainCours = forms.CharField(max_length=100)
    sujetProchaineReunion = forms.CharField(max_length=100)


"""
    class Meta:
        model = Customer
        fields = (
        'name', 'email', 'password', 'instrument_purchase', 'house_no', 'address_line1', 'address_line2', 'telephone',
        'zip_code', 'state', 'country')
"""