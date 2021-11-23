import uuid
from django.db import models
from django.contrib.auth import get_user_model


STATE = (('public', '公開'), ('private', '非公開'))


class CategoryModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField('登録日時', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at', ]


class TagModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField('登録日時', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at', ]


class PostModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    post = models.TextField('投稿')
    preview_content = models.TextField('プレビュー', blank=True, null=True)
    posted_by = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name='posted_by')
    is_public = models.CharField('公開・非公開', max_length=50, choices=STATE)
    created_at = models.DateTimeField('登録日時', auto_now_add=True)
    updated_at = models.DateTimeField('更新日時', auto_now=True)
    category = models.ForeignKey(
        CategoryModel, blank=True, null=True, on_delete=models.CASCADE)
    tags = models.ManyToManyField(TagModel, blank=True, related_name='tags')

    class Meta:
        ordering = ['-created_at', ]

    def __str__(self):
        return f"{self.title}-{self.category}"