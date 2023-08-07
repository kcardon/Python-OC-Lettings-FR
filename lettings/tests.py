from django.test import TestCase
from django.urls import reverse
from .models import Address, Letting


class LettingTestCases(TestCase):
    """
    Test cases for lettings:index, list views and models.
    Every test assert the correct status code, the template used and the context content.
    """

    def setUp(self):
        # Test data
        address = Address.objects.create(
            number=123,
            street="Test Street",
            city="Test City",
            state="TS",
            zip_code=12345,
            country_iso_code="TST",
        )
        self.letting = Letting.objects.create(title="Test Letting", address=address)

    def test_address_str(self):
        assert str(self.letting.address) == "123 Test Street"

    def test_letting_str(self):
        assert str(self.letting) == "Test Letting"

    def test_index_view(self):
        response = self.client.get(reverse("lettings:index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "lettings/index.html")
        self.assertTrue("lettings_list" in response.context)
        self.assertEqual(len(response.context["lettings_list"]), 1)

    def test_letting_view(self):
        response = self.client.get(reverse("lettings:letting", args=[self.letting.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "lettings/letting.html")
        self.assertEqual(response.context["title"], self.letting.title)
        self.assertEqual(response.context["address"], self.letting.address)

        # Test with an invalid letting ID
        response = self.client.get(
            reverse("lettings:letting", args=[9999])
        )  # Assuming 9999 is an invalid ID
        self.assertEqual(response.status_code, 404)
