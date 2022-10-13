from django.test import SimpleTestCase , TestCase , Client
from django.urls import reverse , resolve
from accounts.views import *



class TestUrl(SimpleTestCase):

   def test_doctor_list_url(self):
       url=reverse('doctor_list')
    #    print(resolve(url))
       self.assertEquals(resolve(url).func, doctor_list)
       print('test_doctor_list_url ---> Done')


   def test_index_url(self):
       url=reverse('index')
       self.assertEquals(resolve(url).func,index)
       print('test_index_url ---> Done')


   def test_appointment_url(self):
       url=reverse('appointment',args=['test-slug'])
       self.assertEquals(resolve(url).func , appointment)
       print('test_appointment_url ---> Done')
    



    
    