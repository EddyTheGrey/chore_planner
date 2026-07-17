import unittest
import os
from src.chore_storage import load_chores_from_csv, save_chores_to_csv
from src.chore_create import chore

'''
Tests for the chore storage module, which handles saving and loading chores to and from a CSV file.
'''

class TestChoreStorage(unittest.TestCase):
    def setUp(self):
        self.test_filename = "csv_files/test_chores.csv"
        self.chores = [
            chore("Chore 1", "Description 1", "Daily", 30, "Kitchen"),
            chore("Chore 2", "Description 2", "Weekly", 60, "Bathroom")
        ]
        save_chores_to_csv(self.chores, self.test_filename)
        
    def tearDown(self):
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)
            
    def test_load_chores_from_csv(self):
        loaded_chores = load_chores_from_csv(self.test_filename)
        self.assertEqual(len(loaded_chores), len(self.chores))
        for original, loaded in zip(self.chores, loaded_chores):
            self.assertEqual(original.name, loaded.name)
            self.assertEqual(original.description, loaded.description)
            self.assertEqual(original.frequency, loaded.frequency)
            self.assertEqual(original.length, loaded.length)
            self.assertEqual(original.area, loaded.area)
    
    def test_save_chores_to_csv(self):
        new_chore = chore("Chore 3", "Description 3", "Monthly", 90, "Living Room")
        self.chores.append(new_chore)
        save_chores_to_csv(self.chores, self.test_filename)
        loaded_chores = load_chores_from_csv(self.test_filename)
        self.assertEqual(len(loaded_chores), len(self.chores))
        self.assertEqual(loaded_chores[-1].name, new_chore.name)
        self.assertEqual(loaded_chores[-1].description, new_chore.description)
        self.assertEqual(loaded_chores[-1].frequency, new_chore.frequency)
        self.assertEqual(loaded_chores[-1].length, new_chore.length)
        self.assertEqual(loaded_chores[-1].area, new_chore.area)