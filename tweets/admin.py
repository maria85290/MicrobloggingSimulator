from django.contrib import admin

from .models import *

admin.site.register(Participant)
admin.site.register(Mouse_tracking)
admin.site.register(Post)
admin.site.register(Hashtag)
admin.site.register(Action_type)
admin.site.register(Interaction)