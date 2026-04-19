from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from accounts.models import Profile
from teams.models import Team, Membership
from activities.models import Activity
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        self.stdout.write('Deleting existing data...')
        Activity.objects.all().delete()
        Membership.objects.all().delete()
        Profile.objects.all().delete()
        Team.objects.all().delete()
        User.objects.all().delete()

        self.stdout.write('Creating teams...')
        # Create a dummy user for created_by
        dummy = User.objects.create_user(username='dummy', email='dummy@test.com', password='pass')
        marvel = Team.objects.create(name='Marvel', description='Team of Marvel superheroes', created_by=dummy)
        dc = Team.objects.create(name='DC', description='Team of DC superheroes', created_by=dummy)

        self.stdout.write('Creating users and profiles...')
        # Marvel heroes
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='pass', first_name='Tony', last_name='Stark')
        cap = User.objects.create_user(username='captainamerica', email='cap@marvel.com', password='pass', first_name='Steve', last_name='Rogers')
        thor = User.objects.create_user(username='thor', email='thor@marvel.com', password='pass', first_name='Thor', last_name='Odinson')
        hulk = User.objects.create_user(username='hulk', email='hulk@marvel.com', password='pass', first_name='Bruce', last_name='Banner')
        blackwidow = User.objects.create_user(username='blackwidow', email='blackwidow@marvel.com', password='pass', first_name='Natasha', last_name='Romanoff')

        # DC heroes
        superman = User.objects.create_user(username='superman', email='superman@dc.com', password='pass', first_name='Clark', last_name='Kent')
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='pass', first_name='Bruce', last_name='Wayne')
        wonderwoman = User.objects.create_user(username='wonderwoman', email='wonderwoman@dc.com', password='pass', first_name='Diana', last_name='Prince')
        flash = User.objects.create_user(username='flash', email='flash@dc.com', password='pass', first_name='Barry', last_name='Allen')
        aquaman = User.objects.create_user(username='aquaman', email='aquaman@dc.com', password='pass', first_name='Arthur', last_name='Curry')

        # Profiles
        Profile.objects.create(user=ironman, bio='Genius billionaire playboy philanthropist', date_of_birth=date(1970, 5, 29), height=175, weight=75, fitness_goals='Save the world')
        Profile.objects.create(user=cap, bio='Super soldier', date_of_birth=date(1920, 7, 4), height=185, weight=95, fitness_goals='Protect freedom')
        Profile.objects.create(user=thor, bio='God of Thunder', height=198, weight=140, fitness_goals='Battle evil')
        Profile.objects.create(user=hulk, bio='Scientist turned monster', height=210, weight=400, fitness_goals='Control anger')
        Profile.objects.create(user=blackwidow, bio='Master spy', height=170, weight=60, fitness_goals='Fight injustice')
        Profile.objects.create(user=superman, bio='Man of Steel', height=190, weight=100, fitness_goals='Truth and justice')
        Profile.objects.create(user=batman, bio='Dark Knight', height=188, weight=95, fitness_goals='Protect Gotham')
        Profile.objects.create(user=wonderwoman, bio='Amazon warrior', height=183, weight=75, fitness_goals='Peace and equality')
        Profile.objects.create(user=flash, bio='Fastest man alive', height=180, weight=80, fitness_goals='Speed justice')
        Profile.objects.create(user=aquaman, bio='King of Atlantis', height=185, weight=90, fitness_goals='Protect oceans')

        self.stdout.write('Creating memberships...')
        # Marvel members
        for user in [ironman, cap, thor, hulk, blackwidow]:
            Membership.objects.create(user=user, team=marvel)
        # DC members
        for user in [superman, batman, wonderwoman, flash, aquaman]:
            Membership.objects.create(user=user, team=dc)

        self.stdout.write('Creating activities...')
        # Create some activities
        Activity.objects.create(user=ironman, activity_type='Running', duration=30, distance=5.0, calories_burned=300, notes='Morning run in suit')
        Activity.objects.create(user=superman, activity_type='Flying', duration=60, distance=1000.0, calories_burned=500, notes='Patrol around the world')
        Activity.objects.create(user=batman, activity_type='Training', duration=120, distance=0, calories_burned=800, notes='Nightly workout')
        Activity.objects.create(user=wonderwoman, activity_type='Combat training', duration=90, distance=0, calories_burned=600, notes='Amazon training')
        Activity.objects.create(user=flash, activity_type='Sprinting', duration=10, distance=100.0, calories_burned=200, notes='Speed practice')
        Activity.objects.create(user=thor, activity_type='Hammer throw', duration=15, distance=0, calories_burned=150, notes='Mjolnir practice')
        Activity.objects.create(user=hulk, activity_type='Smashing', duration=20, distance=0, calories_burned=1000, notes='Anger management')
        Activity.objects.create(user=cap, activity_type='Shield training', duration=60, distance=0, calories_burned=400, notes='Vibranium shield practice')
        Activity.objects.create(user=blackwidow, activity_type='Martial arts', duration=45, distance=0, calories_burned=350, notes='Spy training')
        Activity.objects.create(user=aquaman, activity_type='Swimming', duration=30, distance=10.0, calories_burned=250, notes='Ocean patrol')

        self.stdout.write('Database populated successfully!')