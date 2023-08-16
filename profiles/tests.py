from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Profile


class ProfileViewsTestCase(TestCase):
    """
    Test cases for profile views and models.
    Every test assert the correct status code and the template used.
    """

    def setUp(self):
        # Création de données de test
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.profile = Profile.objects.create(user=self.user, favorite_city="Metz")

    def test_profile_str(self):
        assert str(self.profile) == "testuser"

    def test_index_view(self):
        response = self.client.get(
            reverse("profiles:index")
        )  # En supposant que le nom du motif d'URL pour la vue index est 'profiles:index'
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/index.html")
        self.assertTrue("profiles_list" in response.context)
        self.assertEqual(len(response.context["profiles_list"]), 1)

    def test_profile_view(self):
        response = self.client.get(
            reverse("profiles:profile", args=[self.user.username])
        )  # En supposant que le nom du motif d'URL pour la vue profile est 'profiles:profile'
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/profile.html")
        self.assertEqual(response.context["profile"], self.profile)

        # Test avec un nom d'utilisateur non valide
        response = self.client.get(
            reverse("profiles:profile", args=["this_is_not_a_valid_username"])
        )  # En supposant que 'invalidusername' est un nom d'utilisateur non valide
        self.assertEqual(response.status_code, 404)
