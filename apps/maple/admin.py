from django.contrib import admin
from .models import Accounts
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django import forms
from .forms import AccountsCreationForm

class AccountChangeForm(forms.ModelForm):
	class Meta:
		model = Accounts
		fields = ('id', 'name', 'password', 'pic', 'loggedin', 'nxcredit', 'characterslots', 'is_staff')

@admin.register(Accounts)
class AccountAdmin(admin.ModelAdmin):
	form = AccountChangeForm
	add_form = AccountsCreationForm
	list_display = ('name', 'loggedin')
	list_filter = ('gm','is_staff', 'loggedin')
	fieldsets = (
		(None, {'fields': ('name', 'email', 'gm', 'loggedin')}),
	)
	# add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
	# overrides get_fieldsets to use this attribute when creating a user.
	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('name', 'password', 'email', 'gm')}
		),
	)
	search_fields = ('gm', 'name')
	filter_horizontal = ()
