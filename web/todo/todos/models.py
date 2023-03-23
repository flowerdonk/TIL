from django.db import models

class Todo(models.Model):
    '''
    task = charfield # 업무
    isCompleted = False # 완료 여부
    created_at = datafield # 생성 시간
    completed_at = datafield # 완료 시간
    '''

    task         = models.CharField(max_length=300)
    isCompleted  = models.BooleanField(default=False)
    created_at   = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(auto_now=True)

    