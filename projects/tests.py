from django.test import TestCase
from .models import Projects,Profile,Rates,Comments
# Create your tests here.

class TestProjects(TestCase):
    def setUp(self):

        self.new_project=Projects(name='Insta Clone',image='instagram.jpg',description='A clone of the website for the popular photo app Instagram built using Django Python framework.',link='https://instaclone-django.herokuapp.com/',screen1='home1.png',screen2='profile1.png')

    def test_instace(self):
        self.assertTrue(isinstance(self.new_project,Projects))

    def test_initialization(self):
        self.assertEqual(self.new_project.name,"Insta Clone")
        self.assertEqual(self.new_project.image,"instagram.jpg")
        self.assertEqual(self.new_project.description,"A clone of the website for the popular photo app Instagram built using Django Python framework.")
        self.assertEqual(self.new_project.link,"https://instaclone-django.herokuapp.com/")
        self.assertEqual(self.new_project.screen1,"home1.png")
        self.assertEqual(self.new_project.screen2,"profile1.png")

class TestProfile(TestCase):
    def setUp(self):
        self.new_profile=Profile(profile='Victor',bio='The Jig Is Up!',phone="0719890523")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile,Profile))

    def test_initialization(self):
        self.assertEqual(self.new_profile.profile,'Victor')
        self.assertEqual(self.new_profile.bio,'The Jig Is Up!')
        self.assertEqual(self.new_profile.phone,"0719890523")


class TestRating(TestCase):
    def setUp(self):
        self.new_rating=Rates(design=0,usability=0,content=0)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_rating,Rates))

    def test_initialization(self):
        self.assertEqual(self.new_rating.design,0)
        self.assertEqual(self.new_rating.usability,0)
        self.assertEqual(self.new_rating.content,0)
class TestComments(TestCase):
    def setUp(self):
        self.new_comment=Comments(comment="This is a sample comment.",pro_id=0)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment,Comments))

    def test_initialization(self):
        self.assertEqual(self.new_comment.comment,"This is a sample comment.")
        self.assertEqual(self.new_comment.pro_id,0)


# Create your tests here.
