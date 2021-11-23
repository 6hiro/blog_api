from django.contrib import admin
from .models import (
    CategoryModel,
    TagModel,
    PostModel
)

admin.site.register(CategoryModel)
admin.site.register(TagModel)
admin.site.register(PostModel)