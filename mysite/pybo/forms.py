from django import forms
from pybo.models import Question

#장고 폼. ModleForm 모델폼 Form 폼 상속
#모델폼 내부에는 반드시 Meta 클래스가 있어야 함. 모델 폼이 사용할 모델과 모델의 필드 적기

class QuestionForm(forms.ModelForm) :
    class Meta:
        model = Question
        fields = ['subject', 'content']
        #부트스트랩 적용
        """widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        }"""
        #라벨 이름 바꾸기
        labels = {
            'subject': '제목',
            'content': '내용',
        }



