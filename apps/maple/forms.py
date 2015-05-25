from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Accounts

class AccountsCreationForm(forms.ModelForm):
	class Meta:
		model = Accounts
		fields = ('name', 'password')

	def save(self, *args, **kwargs):
		p = Accounts.objects.create_user(
			name=self.cleaned_data['name'],
			password=self.cleaned_data['password']
			)
		return p