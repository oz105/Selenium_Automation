import time
import unittest

from src.main import UserInfo
from src.main import PopupWindow


class MyTestCase(unittest.TestCase):


    # check if the first name not contains only chars it will raise exception because we cant submit if the name contains numbers
    def test_first_name(self):
        user_info_test = UserInfo("123unvalid", "cohen", "test@gmail.com", "0508758263", "I have one")
        popup_test = PopupWindow(user_info_test)
        with self.assertRaises(Exception):
            popup_test.fill_in_first_name("123unvalid")

        with self.assertRaises(Exception):
            popup_test.fill_in_first_name("123456")

    # check if the last name not contains only chars it will raise exception because we cant submit if the last name contains numbers
    def test_last_name(self):

        user_info_test = UserInfo("bob", "123notvalid cohen", "test@gmail.com", "0508758263", "I have one")
        popup_test = PopupWindow(user_info_test)
        with self.assertRaises(Exception):
            popup_test.fill_in_last_name("123notvalid cohen")

        with self.assertRaises(Exception):
            popup_test.fill_in_last_name("123456")

    # check if the email not valid it will raise exception because we cant submit if the email not valid
    def test_email(self):
        user_info_test = UserInfo("bob", "123notvalid cohen", "test@gmail.com", "0508758263", "I have one")
        popup_test = PopupWindow(user_info_test)
        with self.assertRaises(Exception):
            popup_test.fill_in_email("bob.gmail.com")

        with self.assertRaises(Exception):
            popup_test.fill_in_email("bbb.google")

    # check if the phone number not valid it will raise exception because we cant submit if the phone number not contains only numbers
    def test_phone_number(self):
        user_info_test = UserInfo("bob", "123notvalid cohen", "test@gmail.com", "0508758263", "I have one")
        popup_test = PopupWindow(user_info_test)
        with self.assertRaises(Exception):
            popup_test.fill_in_email("a0508758263")

        with self.assertRaises(Exception):
            popup_test.fill_in_email("0508769044ba")

    # check that all good when the input are valid
    def test_for_valid_input(self):
        user_info = UserInfo("Bob", "cohen", "bob@gmail.com", "+972508758263", "I have one")
        popup_test = PopupWindow(user_info)
        popup_test.set_up()
        self.assertTrue(popup_test.fill_out_popup_window())

        time.sleep(5)

        user_info2 = UserInfo("valid", "valid", "bob@gmail.com", "0548859987", "I have two")
        popup_test = PopupWindow(user_info2)
        popup_test.set_up()
        self.assertTrue(popup_test.fill_out_popup_window())

        time.sleep(5)

        user_info3 = UserInfo("valid", "good", "bob@gmail.com", "058765878", "")
        popup_test = PopupWindow(user_info3)
        popup_test.set_up()
        self.assertTrue(popup_test.fill_out_popup_window())

        time.sleep(3)

    # check if the input is not valid we get an Exception (this test is on the web not on the func)
    def test_raise_ex(self):

        with self.assertRaises(Exception):
            user_info = UserInfo("123bobi", "cohen", "bob@gmail.com", "+972508758263", "I have one")
            popup_test = PopupWindow(user_info)
            popup_test.set_up()
            self.assertTrue(popup_test.fill_out_popup_window())

            time.sleep(5)

        with self.assertRaises(Exception):
            user_info = UserInfo("bobi", "9865cohen", "bob@gmail.com", "+972508758263", "I have one")
            popup_test = PopupWindow(user_info)
            popup_test.set_up()
            self.assertTrue(popup_test.fill_out_popup_window())

            time.sleep(5)

        with self.assertRaises(Exception):
            user_info = UserInfo("bobi", "9865cohen", "bob.google.com", "+972508758263", "I have one")
            popup_test = PopupWindow(user_info)
            popup_test.set_up()
            self.assertTrue(popup_test.fill_out_popup_window())

            time.sleep(5)



if __name__ == '__main__':
    unittest.main()
