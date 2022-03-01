import markdown
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter # 이 애너테이션을 적용하면 템플릿에서 해당 함수를 필터로 사용할 수 있게 해준다.
def sub(value, arg):
    return value - arg # 기존값 value에서 입력값 arg를 빼서 리턴한다.

@register.filter()
def mark(value):
    extensions = ['nl2br', 'fenced_code'] #마크다운의 확장기능. nl~ : 줄바꿈 문자를 <br>로, fen~ : 마크다운의 소스코드 표현
    return mark_safe(markdown.markdown(value, extensions=extensions))
