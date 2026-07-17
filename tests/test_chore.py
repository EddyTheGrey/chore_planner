import unittest
import os
from src.chore_create import chore

'''
Tests for the chore class, which is used to create and manage chores.
'''

class TestChore(unittest.TestCase):
    def setUp(self):
            self.chore = chore(
                name="Test Chore",
            description="This is a test chore.",
            frequency="Daily",
            length=30,
            area="Kitchen"
        )

    def test_chore_creation(self):
        self.assertEqual(self.chore.name, "Test Chore")
        self.assertEqual(self.chore.description, "This is a test chore.")
        self.assertEqual(self.chore.frequency, "Daily")
        self.assertEqual(self.chore.length, 30)
        self.assertEqual(self.chore.area, "Kitchen")
        self.assertIsNotNone(self.chore.start_date)

    def test_chore_update(self):
        self.chore.update(name="Updated Chore", frequency="Weekly")
        self.assertEqual(self.chore.name, "Updated Chore")
        self.assertEqual(self.chore.frequency, "Weekly")

    def test_chore_str(self):
        expected_str = (
            "Chore: Test Chore\n"
            "Description: This is a test chore.\n"
            "Frequency: Daily\n"
            "Length: 30\n"
            "Area: Kitchen\n"
            "Start Date: " + str(self.chore.start_date) + "\n"
            "Last Completed: " + str(self.chore.last_completed) + "\n"
            "Next Due Date: " + str(self.chore.next_due_date)
        )
        self.assertEqual(str(self.chore), expected_str)

    def test_chore_get_info(self):
        info = self.chore.get_info()
        self.assertEqual(info["name"], "Test Chore")
        self.assertEqual(info["description"], "This is a test chore.")
        self.assertEqual(info["frequency"], "Daily")
        self.assertEqual(info["length"], 30)
        self.assertEqual(info["area"], "Kitchen")
        self.assertIsNotNone(info["start_date"])
        self.assertIsNone(info["last_completed"])
        self.assertIsNone(info["next_due_date"])
    
    def test_delete_chore(self):
        chore_to_delete = chore(
            name="Delete Chore",
            description="This chore will be deleted.",
            frequency="Weekly",
            length=15,
            area="Bathroom"
        )
        chore_to_delete.delete()
        with self.assertRaises(AttributeError):
            print(chore_to_delete.name)  # Accessing the name should raise an AttributeError since the object is deleted
