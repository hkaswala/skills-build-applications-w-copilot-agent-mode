from django.test import TestCase
from django.contrib.auth.models import User
from .models import Team, Membership, Leaderboard

class TeamTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.team = Team.objects.create(name='Test Team', created_by=self.user)

    def test_team_creation(self):
        self.assertEqual(self.team.name, 'Test Team')
        self.assertEqual(self.team.created_by.username, 'testuser')

class MembershipTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.team = Team.objects.create(name='Test Team', created_by=self.user)
        self.membership = Membership.objects.create(user=self.user, team=self.team)

    def test_membership_creation(self):
        self.assertEqual(self.membership.user.username, 'testuser')
        self.assertEqual(self.membership.team.name, 'Test Team')

class LeaderboardTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.team = Team.objects.create(name='Test Team', created_by=self.user)
        self.leaderboard = Leaderboard.objects.create(team=self.team, user=self.user, points=100)

    def test_leaderboard_creation(self):
        self.assertEqual(self.leaderboard.points, 100)
        self.assertEqual(self.leaderboard.user.username, 'testuser')