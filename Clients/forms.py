from django import forms

class TryDemoForm(forms.Form):
    first_name = forms.CharField(max_length=30,
                            widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'enter your first name'}))

    last_name = forms.CharField(max_length=30,
                                widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'enter your last name'}))

    email = forms.EmailField(max_length=254,
                            widget = forms.EmailInput(attrs={'class':'form-control', 'placeholder':'your email'}))

    def clean(self):
        cleaned_data = super(TryDemoForm, self).clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        email = cleaned_data.get('email')
        if not first_name and not last_name and not email:
            raise forms.ValidationError('all Fields are required')

class getAnvilForm(forms.Form):
        first_name = forms.CharField(max_length=30,
                                widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'enter your first name'}))

        last_name = forms.CharField(max_length=30,
                                    widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'enter your last name'}))

        email = forms.EmailField(max_length=254,
                                widget = forms.EmailInput(attrs={'class':'form-control', 'placeholder':'your email'}))

        nameOfChurch = forms.CharField(max_length=254,
                                widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'name of your church'}))

        location = forms.CharField(max_length=254,
                                        widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'describe the location of your church'}))

        def clean(self):
            cleaned_data = super(getAnvilForm, self).clean()
            first_name = cleaned_data.get('first_name')
            last_name = cleaned_data.get('last_name')
            nameOfChurch = cleaned_data.get('nameOfChurch')
            email = cleaned_data.get('email')
            if not first_name and not last_name and not email and not nameOfChurch:
                raise forms.ValidationError('All fields are required')
