from django.contrib import admin
from .models import Team, Membership, Leaderboard

admin.site.register(Team)
admin.site.register(Membership)
admin.site.register(Leaderboard)