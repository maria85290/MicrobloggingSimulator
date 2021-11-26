from django.contrib import admin
from django.contrib.admin.models import LogEntry, ADDITION, CHANGE
from .models import *


admin.site.register(Participant)
admin.site.register(Mouse_tracking)
admin.site.register(Post)
admin.site.register(Hashtag)
admin.site.register(Action_type)
admin.site.register(Interaction)
admin.site.register(Configuration)
admin.site.register(Environment)
