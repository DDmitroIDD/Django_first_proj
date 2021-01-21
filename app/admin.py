from django.contrib import admin

# Register your models here.
from app.models import Article, DislikeToComment, LikeToComment, DislikeToArticle, \
    LikeToArticle, CommentToArticle

admin.site.register(Article)
admin.site.register(CommentToArticle)
admin.site.register(LikeToArticle)
admin.site.register(DislikeToArticle)
admin.site.register(LikeToComment)
admin.site.register(DislikeToComment)