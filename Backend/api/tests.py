from django.test import TestCase
from .models import MyModel

class MyModelTestCase(TestCase):
    def setUp(self):
        # Set up any initial data for the tests
        MyModel.objects.create(name="Test Name", value=10)

    def test_model_creation(self):
        # Test that a model instance can be created
        obj = MyModel.objects.get(name="Test Name")
        self.assertEqual(obj.value, 10)

    def test_model_update(self):
        # Test that a model instance can be updated
        obj = MyModel.objects.get(name="Test Name")
        obj.value = 20
        obj.save()
        self.assertEqual(obj.value, 20)

    def test_model_deletion(self):
        # Test that a model instance can be deleted
        obj = MyModel.objects.get(name="Test Name")
        obj.delete()
        self.assertEqual(MyModel.objects.count(), 0)
