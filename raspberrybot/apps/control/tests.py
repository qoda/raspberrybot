from django.core.urlresolvers import reverse_lazy
from django.test import Client, TestCase


class ControlTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_view_command(self):
        self.client.get(reverse_lazy('control:command'))

    def tearDown(self):
        pass
