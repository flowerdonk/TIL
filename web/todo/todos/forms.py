from django import forms
from .models import Todo

'''
Django Form VS ModelForm
Form : html 렌더링, 유효성 검사 <- 귀찮음, django가 대신 해줌
ModelForm : 어차피 form 객체 DB와 같이 사용 -> 필드도 model 기반으로 생성
'''

class TodoForms(forms.ModelForm):
    class Meta:
        model = Todo # 이 모델 기반으로 Form 형성
        fields = ('task', ) # 모든 필드를 받음
        # exclude, fields 둘 중 하나