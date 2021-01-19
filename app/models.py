from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Article(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='article')
    text = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'Name - \"{self.name}\" Author - \"{self.author}\"'


class CommentToArticle(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_to_article')
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'Comment #{self.id} Article - \"{self.article.name}\" from \"{self.author}\"'


class LikeToArticle(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like_to_article')
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Like to article \"{self.article.name}\" from \"{self.author}\"'


class DislikeToArticle(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dislike_to_article')
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Dislike to article \"{self.article.name}\" from \"{self.author}\"'


class LikeToComment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like_to_comment')
    comment = models.ForeignKey(CommentToArticle, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Like to comment #{self.comment.id} from \"{self.author}\"'


class DislikeToComment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_dislike')
    comment = models.ForeignKey(CommentToArticle, on_delete=models.CASCADE, related_name='comments')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Dislike to comment #{self.comment.id} from \"{self.author}\"'


class CommentToComment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='authors_comment')
    comment = models.ForeignKey(CommentToArticle, on_delete=models.CASCADE, related_name='comments_to_comment')
    comment_to_comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'Comment to comment #{self.comment.id} from \"{self.author}\"'
