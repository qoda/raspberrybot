from django.core.urlresolvers import reverse_lazy
from django.test import Client, TestCase


class VisionTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def tearDown(self):
        pass
