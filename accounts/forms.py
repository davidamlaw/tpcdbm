from django.forms import ModelForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class AddUserForm(UserCreationForm):

    class Meta:
        fields = ('email', 'username', 'first_name', 'last_name', 'password1',
                  'password2', 'employment_supports', 'day_hab', 'specialized_supports',
                  'cbds', 'role', 'date_joined')
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Username:'
        self.fields['email'].label = 'Email Address:'

class UserUpdateForm(ModelForm):

    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'first_name', 'last_name', 'is_active', 'is_admin', 'employment_supports', 'day_hab', 'specialized_supports',
        'cbds', 'role', 'date_joined')
