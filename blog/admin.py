from django.contrib import admin
from .models import Post, Comment

# rejestracja istniejących w pliku models.py modeli
admin.site.register(Post)
admin.site.register(Comment)