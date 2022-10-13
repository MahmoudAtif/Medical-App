from urllib import response
from django.test import TestCase , Client
from django.urls import reverse



class TestView(TestCase):


    def setUp(self):
        self.client=Client()
        self.index_url =reverse('index')
        self.appointment_url=reverse('appointment', args=['some-slug'])
        # self.doctor_detail_url=reverse('doctor_detail',args=['some-slug'])

    def test_index_get(self):
        response=self.client.get(self.index_url)
        self.assertEquals(response.status_code , 200)
        self.assertTemplateUsed(response , 'user/index.html')
        print('test_index_get----> Done')
        print(response)

    

    def test_appointment_get(self):
        response=self.client.get(self.appointment_url)
        self.assertEquals(response.status_code , 302)
        # self.assertTemplateUsed(response , 'user/appointment.html')
        print('test_appointment_get----> Done')

    
    def test_appointment_post(self):
        response=self.client.post(self.appointment_url , {
            'doctor':'test-doctor',
            'patient':'test-patient',
            })
        self.assertEquals(response.status_code, 302)
        print('test_appointment_post----> Done')

    # def test_doctor_detail_get(self):
    #     response=self.client.get(self.doctor_detail_url)
    #     self.assertEquals(response.status_code ,302)
    #     self.assertTemplateUsed(response , 'user/doctors_detail.html')
    #     print('test_doctor_detail_get----> Done')

