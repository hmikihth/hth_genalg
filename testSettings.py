#!/usr/bin/env python3

import unittest

import Settings

class SettingTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print("Testing settings module")
        self.settings = Settings.Settings()
    
    @classmethod
    def tearDown(self):
        print("Settings module testing is complete")
    
    def test(self):
        print (self.settings)
