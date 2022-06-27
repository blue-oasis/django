import markdown
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def sub(value, arg):
    return value - arg

# markdown 문법을 HTML으로 변환하는 필터 함수
@register.filter()
def mark(value):
    extensions = ["nl2br", "fenced_code"] #nl2br 줄바꿈 문자 <br> 변환, fenced_code 마크다운 소스코드 표현
    return mark_safe(markdown.markdown(value, extensions=extensions))
