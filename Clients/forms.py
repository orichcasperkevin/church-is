from django import forms

class TryDemoForm(forms.Form):
    demo_first_name = forms.CharField(max_length=30,
                            widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'enter your first name'}))

    demo_last_name = forms.CharField(max_length=30,
                                widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'enter your last name'}))
    demo_email = forms.EmailField(max_length=30,
                            widget = forms.EmailInput(attrs={'class':'form-control', 'placeholder':'your email'}))

    def clean(self):
        cleaned_data = super(TryDemoForm, self).clean()
        first_name = cleaned_data.get('demo_first_name')
        last_name = cleaned_data.get('demo_last_name')
        email = cleaned_data.get('demo_email')
        if not first_name and not last_name and not email:
            raise forms.ValidationError('all Fields are required')

class GetAnvilForm(forms.Form):
        first_name = forms.CharField(max_length=30,
                                widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'enter your first name'}))

        last_name = forms.CharField(max_length=30,
                                    widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'enter your last name'}))

        ID_number = forms.CharField(max_length=8,
                                widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'your ID number'}))

        phone_number = forms.CharField(max_length=12,
                                widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'+2547######'}))

        email = forms.EmailField(max_length=50,
                                widget = forms.EmailInput(attrs={'class':'form-control', 'placeholder':'your email'}))


        name_of_church = forms.CharField(max_length=30,
                                widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'name of your church'}))

        city_or_town = forms.CharField(max_length=30,
                                widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'where is your church located?'}))

        road_or_street = forms.CharField(max_length=30,
                                widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'eg Gakere Road, first Street'}))

        location_description = forms.CharField(max_length=254,
                                        widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'eg. opposite Mountain mall'}))

        website = forms.CharField(max_length=30,
                                widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'your church website'}))

        def clean(self):
            cleaned_data = super(GetAnvilForm, self).clean()

            first_name = cleaned_data.get('first_name')
            last_name = cleaned_data.get('last_name')
            ID_number = cleaned_data.get('ID_number')
            email = cleaned_data.get('email')

            name_of_church = cleaned_data.get('name_of_church')
            city_or_town = cleaned_data.get('city_or_town')
            road_or_street = cleaned_data.get('road_or_street')
            location_description = cleaned_data.get('location_description')

            website = cleaned_data.get('website')

            if not first_name and not last_name and not email and not ID_number and not name_of_church and not city_or_town and not road_or_street and not location_description:
                raise forms.ValidationError('All fields are required')

class ChangePasswordForm(forms.Form):
    new_password = forms.CharField(max_length=30,
                            widget = forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'enter your new password'}))

    confirm_password = forms.CharField(max_length=30,
                                widget = forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'confirm password'}))


    def clean(self):
        cleaned_data = super(ChangePasswordForm, self).clean()
        new_password = cleaned_data.get('new_password')
        confirm_password = cleaned_data.get('confirm_password')

        if not new_password and not confirm_password:
            raise forms.ValidationError('all Fields are required')

        if new_password != confirm_password:
            raise forms.ValidationError('passwords do not match')
