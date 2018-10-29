from django.contrib import admin

from organizer.models import Question, Resource, Thought, Answer

admin.site.register(Question)
admin.site.register(Resource)
admin.site.register(Thought)
admin.site.register(Answer)
