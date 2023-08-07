from django.test import TestCase
from django.urls import reverse


class BaseViewsTestCases(TestCase):
    """
    Test cases for index and errors-handlers views.
    Every test assert the correct status code and the template used.
    """

    def test_status_code_index(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")

    def test_handler_404(self):
        response = self.client.get("/this-should-make-a-404-error")
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, "404.html")
