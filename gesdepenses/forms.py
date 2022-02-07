from django.forms import ModelForm
from django.contrib.auth.models import User

from .models import Charge


class userForm(ModelForm):
	class Meta:
		model = User
		fields = [ 'username', 'email', 'first_name',
		]

class prod(ModelForm):
	class Meta:
		model = Charge
		fields = ['owner', 'amount', 'desc'
		]