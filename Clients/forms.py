from django import forms

class TryDemoForm(forms.Form):
    name = forms.CharField(max_length=30,
                            widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'enter your full names'}))
    email = forms.EmailField(max_length=254,
                            widget = forms.EmailInput(attrs={'class':'form-control', 'placeholder':'your email'}))

    def clean(self):
        cleaned_data = super(TryDemoForm, self).clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        if not name and not email:
            raise forms.ValidationError('You have to write something!')

class getAnvilForm(forms.Form):
        name = forms.CharField(max_length=30,
                                widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'enter your full names'}))
        email = forms.EmailField(max_length=254,
                                widget = forms.EmailInput(attrs={'class':'form-control', 'placeholder':'your email'}))

        nameOfChurch = forms.CharField(max_length=254,
                                widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'name of your church'}))

        location = forms.CharField(max_length=254,
                                        widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'describe the location of your church'}))
        def clean(self):
            cleaned_data = super(getAnvilForm, self).clean()
            name = cleaned_data.get('name')
            email = cleaned_data.get('email')
            if not name and not email:
                raise forms.ValidationError('You have to write something!')
