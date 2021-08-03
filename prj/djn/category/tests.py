from django.test import TestCase, Client
from category.serializers import CategorySerializer

from category.fakers import CategoryFaker


# Create your tests here.

N_CATEGORIES = 3

class CategoryTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.categories = CategoryFaker.create_batch(N_CATEGORIES)
        [category.save() for category in self.categories]

    def test_list(self):
        response = self.client.get('/api/cat/list')
        expected = {'error': None, 'categories': CategorySerializer(self.categories, many=True).data}
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected)

    def test_nonexistentcategory(self):
        response = self.client.get('/api/cat/999999/items')
        expected = {"error": "Category doesn't exist"}
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), expected)

    def tearDown(self):
        pass