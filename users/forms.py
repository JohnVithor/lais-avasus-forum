from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField
import datetime

User = get_user_model()

class StudentRegisterForm(forms.ModelForm):
    """
    The Student Register Form 

    """
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password_2 = forms.CharField(label='Confirmação de senha', widget=forms.PasswordInput)
    
    use_terms = forms.BooleanField(label='Confirmo que li e concordo com os termos de uso', required=True)

    class Meta:
        model = User
        exclude = ['is_professor']
        fields = ['cpf', 'name', 'social_name', 'birth_date', 'state', 'city']

    def digit_generator(self, cpf, m):
        d = 0
        for n in range(m - 1):
            d = d + int(cpf[n]) * m
            m = m - 1
        digit = 11 - d % 11
        return 0 if digit > 9 else digit

    def clean_cpf(self):
        '''
        Verify cpf is valid.
        '''
        cpf = self.cleaned_data.get('cpf')
        qs = User.objects.filter(cpf=cpf)
        if qs.exists():
            raise forms.ValidationError("CPF já está em uso")
        if len(cpf) != 11:
            raise forms.ValidationError('CPF deve conter 11 números')
        d1 = self.digit_generator(cpf, 10)
        d2 = self.digit_generator(cpf, 11)
        if cpf[-2:] != f'{d1}{d2}':
            raise forms.ValidationError('Número de CPF inválido')
        return cpf

    def clean_birth_date(self):
        '''
        Verify birth date is valid.
        '''
        birth_date = self.cleaned_data.get('birth_date')
        age = (datetime.date.today() - birth_date).days / 365
        if age < 18:
            raise forms.ValidationError('Apenas maiores de 18 anos podem se cadastrar')
        return birth_date

    def clean(self):
        '''
        Verify both passwords match.
        '''
        cleaned_data = super().clean()
        if (not cleaned_data.get("use_terms")):
            self.add_error("use_terms", "Você deve aceitar os termos de uso")
        password = cleaned_data.get("password")
        password_2 = cleaned_data.get("password_2")
        if password is not None and password != password_2:
            self.add_error("password_2", "Your passwords must match")
        return cleaned_data

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class RegisterForm(forms.ModelForm):
    """
    The default 

    """
    # password = forms.CharField(widget=forms.PasswordInput)
    # password_2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['cpf', 'name', 'social_name', 'birth_date', 'is_professor', 'state', 'city']

    def digit_generator(self, cpf, m):
        d = 0
        for n in range(m - 1):
            d = d + int(cpf[n]) * m
            m = m - 1
        digit = 11 - d % 11
        return 0 if digit > 9 else digit

    def clean_cpf(self):
        '''
        Verify cpf is valid.
        '''
        cpf = self.cleaned_data.get('cpf')
        qs = User.objects.filter(cpf=cpf)
        if qs.exists():
            raise forms.ValidationError("CPF já está em uso")
        if len(cpf) != 11:
            raise forms.ValidationError('CPF deve conter 11 números')
        d1 = self.digit_generator(cpf, 10)
        d2 = self.digit_generator(cpf, 11)
        if cpf[-2:] != f'{d1}{d2}':
            raise forms.ValidationError('Número de CPF inválido')
        return cpf

    def clean_birth_date(self):
        '''
        Verify birth date is valid.
        '''
        birth_date = self.cleaned_data.get('birth_date')
        age = (datetime.date.today() - birth_date).days / 365
        if age < 18:
            raise forms.ValidationError('Apenas maiores de 18 anos podem se cadastrar')
        return birth_date

    # def clean(self):
    #     '''
    #     Verify both passwords match.
    #     '''
    #     cleaned_data = super().clean()
    #     # password = cleaned_data.get("password")
    #     # password_2 = cleaned_data.get("password_2")
    #     # if password is not None and password != password_2:
    #         # self.add_error("password_2", "Your passwords must match")
    #     return cleaned_data

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class UserAdminCreationForm(forms.ModelForm):
    """
    A form for creating new users. Includes all the required
    fields, plus a repeated password.
    """
    password = forms.CharField(widget=forms.PasswordInput)
    password_2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['cpf', 'name', 'social_name', 'birth_date', 'is_professor', 'state', 'city']

    def digit_generator(self, cpf, m):
        d = 0
        for n in range(m - 1):
            d = d + int(cpf[n]) * m
            m = m - 1
        digit = 11 - d % 11
        return 0 if digit > 9 else digit

    def clean_cpf(self):
        '''
        Verify cpf is valid.
        '''
        cpf = self.cleaned_data.get('cpf')
        qs = User.objects.filter(cpf=cpf)
        if qs.exists():
            raise forms.ValidationError("CPF já está em uso")
        if len(cpf) != 11:
            raise forms.ValidationError('CPF deve conter 11 números')
        d1 = self.digit_generator(cpf, 10)
        d2 = self.digit_generator(cpf, 11)
        if cpf[-2:] != f'{d1}{d2}':
            raise forms.ValidationError('Número de CPF inválido')
        return cpf

    def clean_birth_date(self):
        '''
        Verify birth date is valid.
        '''
        birth_date = self.cleaned_data.get('birth_date')
        age = (datetime.date.today() - birth_date).days / 365
        if age < 18:
            raise forms.ValidationError('Apenas maiores de 18 anos podem se cadastrar')
        return birth_date

    def clean(self):
        '''
        Verify both passwords match.
        '''
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_2 = cleaned_data.get("password_2")
        if password is not None and password != password_2:
            self.add_error("password_2", "Your passwords must match")
        return cleaned_data

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ['cpf', 'password', 'is_active', 'name', 'social_name', 'birth_date', 'is_professor', 'state', 'city']

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]
