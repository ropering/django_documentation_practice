from django.contrib import admin

from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3  # 선택 가능 폼 갯수 (추가 가능)


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice_text', 'votes', 'question')


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {
            'fields': ['pub_date'],
            'classes': ['collapse']  # 감추기
        }),
    ]
    inlines = [ChoiceInline]  # 작성 페이지에 Choice 추가하기
    list_display = ('question_text', 'pub_date', 'was_published_recently')  # display 항목
    list_filter = ['pub_date']  # 필터 메뉴 (우측)
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
