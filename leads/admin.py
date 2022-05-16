from django.contrib import admin

from leads.models import Agent, Category, Lead, User, UserProfile,FollowUp

# Register your models here.
admin.site.register(User)
admin.site.register(Lead)
admin.site.register(Agent)
admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(FollowUp)
