from django.contrib import admin

from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3  # 선택 가능 폼 갯수 (추가 가능)


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {
            'fields': ['pub_date'],
            'classes': ['collapse']  # 감추기
        }),
    ]
    inlines = [ChoiceInline]  # Choice 추가하기
    list_display = ('question_text', 'pub_date', 'was_published_recently')


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
