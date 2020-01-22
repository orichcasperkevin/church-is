from django.test import TestCase
from django.urls import reverse


class GetDemoTestCase(TestCase):
    def setUp(self):
        print("setting uup")

    def test_get_demo_view(self):
        data = {
            "first_name": "demo",
            "last_name": "demolast",
            "email": "demo@gmail.com",
            "phone_number":"0713111882"
        }
        url = reverse("home")
        print(url)
        response = self.client.get(url)
        print(response)
