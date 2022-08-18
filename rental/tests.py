from django.test import TestCase
from .models import CustomUser, Tool, RentalDetails


# Create your tests here.


class RentTest(TestCase):
    def setUp(self) -> None:
        self.user = CustomUser.objects.create_user(first_name="hamza", last_name="seif", username='hamzaseif1',
                                                   email='hamza@hamza.com')
        self.tool = Tool.objects.create(owner=self.user, name='screw driver', description='best driver', price=5)

        self.secondUser = CustomUser.objects.create_user(first_name="moha", last_name="seif", username='mohaseif1',
                                          email='hamza@hamza.com')
    def test_rent_own_tool(self):
        self.assertFalse(self.tool.rent(self.user, 4))

    def test_rent_a_rented_tool(self):
        self.tool.rent(self.secondUser, 5)
        self.assertFalse(self.tool.rent(self.secondUser, 5))

    def test_rent_tool(self):
        self.assertTrue(self.tool.rent(self.secondUser,5))
    def test_test(self):
        self.assertEqual(5,5)


