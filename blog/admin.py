from django.contrib import admin
from .models import Post

# Register your models here.

#registering the Post model with the admin page

admin.site.register(Post)
