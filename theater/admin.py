from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Movie)

admin.site.register(Review)
admin.site.register(CommentReview)
admin.site.register(CommentPreview)
admin.site.register(Business)


