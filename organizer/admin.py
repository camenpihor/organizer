from django.contrib import admin

from organizer.models import Question, Resource, Random, Thought, Answer

admin.site.register(Question)
admin.site.register(Resource)
admin.site.register(Random)
admin.site.register(Thought)
admin.site.register(Answer)
