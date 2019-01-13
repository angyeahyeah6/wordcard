from django.contrib import admin
from .models import Word, Phrase, Relate, Card
# Register your models here.
admin.site.register(Word)
admin.site.register(Phrase)
admin.site.register(Relate)
admin.site.register(Card)