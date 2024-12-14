from django import forms
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

from .models import Category, Husband, TagPost, Women


# @deconstructible
# class RussianValidator:  # Для общей проверки + в поле добавить validators=[RussianValidator(),]
#
#
#     ALLOWED_CHARS = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯабвгдеёжзийклмнопрстуфхцчшщбыъэюя0123456789- "
#     code = 'russian'
#
#     def __init__(self, message=None):
#         self.message = message if message else "Должны присутствовать только русские символы, дефис и пробел."
#
#     def __call__(self, value, *args, **kwargs):
#         if not (set(value) <= set(self.ALLOWED_CHARS)):
#             raise ValidationError(self.message, code=self.code)


class AddPostForm(forms.ModelForm):  # Форма связанная с моделью Women
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='Категория не выбрана', label='Категории')
    husband = forms.ModelChoiceField(queryset=Husband.objects.all(), empty_label='Не замужем', required=False,
                                     label='Муж')

    class Meta:
        model = Women
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat', 'husband', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 50, 'rows': 5})
        }

    def clean_title(self):  # Для частной проверки
        title = self.cleaned_data['title']
        # ALLOWED_CHARS = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯабвгдеёжзийклмнопрстуфхцчшщбыъэюя0123456789- "
        #
        # if not (set(title) <= set(ALLOWED_CHARS)):
        #     raise ValidationError("Должны присутствовать только русские символы, дефис и пробел.")
        if len(title) > 50:
            raise ValidationError("Длина превышает 50 символов")
        return title


    # title = forms.CharField(max_length=255, min_length=3, label='Заголовок',
    #                         widget=forms.TextInput(attrs={'class': 'form-input'}),
    #                         error_messages={
    #                             'min_length': 'Слишком короткий заголовок, минимум 3 символа',
    #                             'required': 'Заполните заголовок'
    #                         })
    # # slug = forms.SlugField(max_length=255, label='URL')
    # content = forms.CharField(widget=, required=False, label="Контент")
    # is_published = forms.BooleanField(required=False, initial=True, label='Статус')
    #
    # tags = forms.ModelMultipleChoiceField(queryset=TagPost.objects.all(), required=False, label='Теги')
    #

class UploadFileForm(forms.Form):
    file = forms.ImageField(label='Файл')
