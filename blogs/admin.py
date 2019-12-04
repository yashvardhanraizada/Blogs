from django.contrib import admin
from .models import User, Blog, Blogger, Stream

admin.site.register(User)
admin.site.register(Blog)
admin.site.register(Blogger)
admin.site.register(Stream)