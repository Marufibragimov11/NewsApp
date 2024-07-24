from modeltranslation.translator import register, TranslationOptions
from .models import News, Category


@register(News)
class NewsTranslationOption(TranslationOptions):
    fields = ('title', 'body')


@register(Category)
class CategoryTranslationOption(TranslationOptions):
    filter = ('name',)
