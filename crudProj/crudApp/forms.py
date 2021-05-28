from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post # 3. Post라는 모델을 참고하여 Form을 만들었음
        fields = ['title', 'writer', 'body'] # 4. Post라는 모델의 값 중 title과 writer, body라는 항목을 입력 받을 것
        # pub_date는 자동으로 기입되므로 받아올 필요 X