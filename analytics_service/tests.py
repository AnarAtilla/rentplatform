class AnalyticsTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='user@example.com', password='password123')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.property = Property.objects.create(
            title='Test Property',
            description='Test description',
            location='Test location',
            price=1000.00,
            owner=self.user,
            property_type='apartment',
            rooms=2,
            bathrooms=1
        )

    def test_create_property_view(self):
        response = self.client.get(reverse('property_detail', kwargs={'pk': self.property.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(PropertyView.objects.count(), 1)

    def test_create_search_query(self):
        response = self.client.get(reverse('property_search'), {'q': 'Test'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(SearchQuery.objects.count(), 1)
