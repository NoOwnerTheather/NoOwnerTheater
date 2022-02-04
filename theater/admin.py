from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(ReleasedMovie)
admin.site.register(UnreleasedMovie)
admin.site.register(Review)
admin.site.register(CommentReview)
admin.site.register(CommentPreview)


