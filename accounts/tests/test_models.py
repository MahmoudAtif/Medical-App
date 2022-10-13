from django.test import TestCase
from accounts.models import DoctorServices



class TestModels(TestCase):

    def setUp(self):
        self.service1=DoctorServices.objects.get(id=9)
    
    def test_doctor_slug(self):
        self.assertEquals(self.service1.clinic , 'mahmoud4')
