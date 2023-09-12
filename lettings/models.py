from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator

# This module defines the Address and Letting models for the application.


class Address(models.Model):
    """
    Model representing a physical address.

    Attributes:
        number (PositiveIntegerField): The street number of the address, limited to a maximum value of 9999.
        street (CharField): The name of the street, with a maximum length of 64 characters.
        city (CharField): The city where the address is located, with a maximum length of 64 characters.
        state (CharField): The state or region code of the address, with a minimum length of 2 characters.
        zip_code (PositiveIntegerField): The ZIP code of the address, limited to a maximum value of 99999.
        country_iso_code (CharField): The ISO country code of the address, with a length of 3 characters.

    """

    class Meta:
        verbose_name_plural = "Addresses"

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(
        max_length=3, validators=[MinLengthValidator(3)]
    )

    def __str__(self):
        return f"{self.number} {self.street}"


class Letting(models.Model):
    """
    Model representing a property letting.

    Attributes:
        title (CharField): The title or name of the property letting, with a maximum length of 256 characters.
        address (OneToOneField): A reference to the associated Address object, establishing a one-to-one relationship
            between Letting and Address models.

    """

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
