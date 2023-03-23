from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta): # Meta도 상속받기 때문에
        model = get_user_model() # settings - auth user model에서 가져옴, 현재 프로젝트에서 활성화된 User 모델을 리턴
        

class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta): # Meta도 상속받기 때문에
        model = get_user_model() # settings - auth user model에서 가져옴
        fields = ('username', 'email', 'first_name', 'last_name', ) # 원하는 정보만 가져옴