# tests.py (constants)
# !/usr/bin/env python3
# coding=utf-8
# young.daniel@epa.gov
# py-lint: disable=C0301

"""
This file houses test cases for the constants module.

Available functions:
- None
"""

from django.test import TestCase
from django.core.mail import EmailMultiAlternatives
from constants.utils import split_email_list, is_epa_email, non_epa_email_message, create_qt_email_message, xstr, \
    sort_rap_numbers, get_rap_fields, is_float


class TestUtils(TestCase):
    """Test utils."""

    def test_split_email_list_pass_one(self):
        """Runs the char split on an email that will be equal."""
        self.assertEqual(split_email_list("t;e,s\tt@t|est.com"), ['t', 'e', 's', 't@t', 'est.com'])

    def test_split_email_list_fail_one(self):
        """Runs the char split on an email that will not be equal."""
        self.assertNotEqual(split_email_list("t;e,s\tt@t|est.com"), ['t', 'e', 's', 't@test.com'])

    def test_is_epa_email_pass_one(self):
        """Runs the test to check if an email address is in the right format to be an epa email address."""
        self.assertEqual(is_epa_email("test@epa.gov"), True)

    def test_is_epa_email_fail_one(self):
        """Runs the test to check if an email address is in the right format to be an epa email address."""
        self.assertEqual(is_epa_email("test@test.com"), False)

    def test_is_epa_email_fail_two(self):
        """Runs the test to check if an email address is in the right format to be an epa email address."""
        self.assertEqual(is_epa_email("test@test.gov"), False)

    def test_is_epa_email_fail_three(self):
        """Runs the test to check if an email address is in the right format to be an epa email address."""
        self.assertEqual(is_epa_email("test@epa.com"), False)

    def test_is_epa_email_fail_seven(self):
        """Runs the test to check if an email address is in the right format to be an epa email address."""
        self.assertEqual(is_epa_email("test@Aepa.gov"), False)

    def test_is_epa_email_fail_eight(self):
        """Runs the test to check if an email address is in the right format to be an epa email address."""
        self.assertEqual(is_epa_email("test@repa.govR"), False)

    def test_is_epa_email_fail_nine(self):
        """Runs the test to check if an email address is in the right format to be an epa email address."""
        self.assertEqual(is_epa_email("test@4epa.gov"), False)

    def test_non_epa_email_message_fail_one(self):
        """Runs the test to check if an email address is not EPA that it sends the correct message."""
        self.assertIn(
            """Email list may only contain @epa.gov addresses.""", non_epa_email_message("test@test.com"), msg=None)

    def test_create_qt_email_message(self):
        """Returns EmailMultiAlternatives object."""
        to_emails = ["testTo@test.com"]
        self.assertIsInstance(
            create_qt_email_message("email Subject", "text content", "testFrom@test.com", to_emails, None, None),
            EmailMultiAlternatives, msg=None)

    def test_xstr_one(self):
        """Test the method that Checks for and replaces None objects with empty strings."""
        self.assertEqual(xstr(None), "")

    def test_xstr_two(self):
        """Test the method that Checks for and replaces None objects with empty strings."""
        self.assertEqual(xstr("test"), "test")

    def test_sort_rap_numbers(self):
        """Test the sort rap numbers."""
        raplist = {"15.42", "15.45", "12.12"}
        results = sort_rap_numbers(raplist)
        self.assertEqual(results, ["12.12", "15.42", "15.45"])

    def test_sort_rap_numbers_fail(self):
        """Test the sort rap numbers."""
        raplist = {"15.42", "test", "12.12"}
        results = sort_rap_numbers(raplist)
        # print(results)
        self.assertEqual(results, ["12.12", "15.42", "test"])

    def test_get_rap_fields(self):
        """Test the get rap fields with form."""
        fields = "form"
        results = get_rap_fields(fields)
        # print(results)
        self.assertEqual(results, [
            ['ace', 'ace_rap_numbers'], ['css', 'css_rap_numbers'],
            ['sswr', 'sswr_rap_numbers'], ['hhra', 'hhra_rap_numbers'],
            ['hsrp', 'hsrp_rap_numbers'], ['hsre', 'hsrp_rap_extensions'],
            ['shc', 'shc_rap_numbers']])

    def test_get_rap_fields_two(self):
        """Test the get rap fields without form."""
        fields = "notform"
        results = get_rap_fields(fields)
        # print(results)
        self.assertEqual(results, ['ace_rap_numbers', 'css_rap_numbers', 'sswr_rap_numbers', 'hhra_rap_numbers',
                                   'hsrp_rap_numbers', 'hsrp_rap_extensions', 'shc_rap_numbers'])

    def test_is_float_one(self):
        """Test the is float method with a float."""
        val_str = "1.2"
        results = is_float(val_str)
        # Print(results).
        self.assertEqual(results, True)

    def test_is_float_two(self):
        """Test the is float method with a char string."""
        val_str = "notAFloat"
        results = is_float(val_str)
        # Print(results).
        self.assertEqual(results, False)
