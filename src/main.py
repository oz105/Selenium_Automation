import re
import string
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



# This class contains all the info we should fill in the web before we click on submit
class UserInfo:

    def __init__(self, first_name, last_name, email, phone_number, question):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.my_question = question

    def to_dict(self):
        res = {'first_name': self.first_name,
               'last_name': self.last_name,
               'email': self.email,
               'phone_number': self.phone_number,
               'my_question': self.my_question,
               }
        return res

    def __str__(self):
        return str(self.to_dict())



class PopupWindow:

    def __init__(self, user_info):
        self.driver = None
        self.user_info = user_info

    def set_up(self):
        options = Options()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # will click on the book a demo to open the popup window
    def click_book_a_demo(self):
        try:
            book_a_demo_xpath = '//a[@data-popup="talkExperts" and @href = "#"]'
            book_a_demo_element = self.driver.find_element(By.XPATH, book_a_demo_xpath)
            book_a_demo_element.click()
            #to let the pop window up
            time.sleep(3)
        except Exception as ex:
            print("Error with click on book a demo")
            print(ex)
            self.driver.quit()
            exit()

    # will fill in the filed first name in the popup window
    def fill_in_first_name(self, first_name):
        if first_name.isalpha():
            try:
                first_name_xpath = '//input[@name="firstname" and @class="hs-input"]'
                first_name_element = self.driver.find_element(By.XPATH, first_name_xpath)
                first_name_element.send_keys(first_name)
            except Exception as ex:
                print("Error in first name fill in")
                print(ex)
        else:
            time.sleep(2)
            self.driver.quit()
            raise Exception("Error, Not a valid first name (should not contains numbers)")

    # will fill in the filed last name in the popup window
    def fill_in_last_name(self, last_name):

        if last_name.isalpha():
            try:
                last_name_xpath = '//input[@name="lastname" and @class="hs-input"]'
                last_name_element = self.driver.find_element(By.XPATH, last_name_xpath)
                last_name_element.send_keys(last_name)
            except Exception as ex:
                print("Error in last name fill in")
                print(ex)
        else:
            time.sleep(2)
            self.driver.quit()
            raise Exception("Error, Not a valid last name (should not contains numbers)")

    # will fill in the filed email in the popup window
    def fill_in_email(self, email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if re.fullmatch(regex, email):
            try:
                email_xpath = '//input[@name="email" and @class="hs-input"]'
                email_element = self.driver.find_element(By.XPATH, email_xpath)
                email_element.send_keys(email)
            except Exception as ex:
                print("Error in email fill in")
                print(ex)
        else:
            time.sleep(2)
            self.driver.quit()
            raise Exception("Error, Not a valid email")

    # will fill in the filed phone number name in the popup window
    def fill_in_phone_number(self, phone_number):
        allowed = set(string.digits + '+')
        if set(phone_number) <= allowed:

            try:
                phone_number_xpath = '//input[@name="phone" and @class="hs-input"]'
                phone_number_element = self.driver.find_element(By.XPATH, phone_number_xpath)
                phone_number_element.send_keys(phone_number)
            except Exception as ex:
                print("Error in phone number fill in")
                print(ex)
        else:

            time.sleep(2)
            self.driver.quit()
            raise Exception("Error, Not a valid phone number")

    # will select "Business Partner" in the combo box in the popup window
    def choose_company_type(self):
        try:
            company_type_dropbox_xpath = '//div[@class="selectedOption"]'
            drop_box_element = self.driver.find_element(by=By.XPATH, value=company_type_dropbox_xpath)
            drop_box_element.click()
            time.sleep(3)
            company_type_choose_xpath = '//*[@id="hsForm_1c6d7d5c-7237-45e2-961e-02c5a47fb283"]/div[5]/div/div/div/ul/li[4]'
            choose_element = self.driver.find_element(by=By.XPATH, value=company_type_choose_xpath)
            choose_element.click()
            time.sleep(3)
        except Exception as ex:
            print("Error in choose company type from dropbox")
            print(ex)

    # will fill the window that open after we select compant type
    def fill_in_open_help_note(self, question):
        try:
            note_to_know_xpath = '//*[@id="open_box_intent_for_forms-1c6d7d5c-7237-45e2-961e-02c5a47fb283"]'
            note_to_know_element = self.driver.find_element(By.XPATH, note_to_know_xpath)
            note_to_know_element.send_keys(question)

        except Exception as ex:
            print("Error in choose company type from dropbox")
            print(ex)

    # will select "Friend / Colleague" in the combo box in the popup window
    def fill_in_how_did_you_hear_dropbox(self):
        how_did_you_hear_dropbox_xpath = '//*[@id="hsForm_1c6d7d5c-7237-45e2-961e-02c5a47fb283"]/div[6]/div/div/div'
        drop_box_element = self.driver.find_element(by=By.XPATH, value=how_did_you_hear_dropbox_xpath)
        drop_box_element.click()
        time.sleep(3)

        how_did_you_hear_friend_xpath = '//*[@id="hsForm_1c6d7d5c-7237-45e2-961e-02c5a47fb283"]/div[6]/div/div/ul/li[2]'
        choose_element = self.driver.find_element(by=By.XPATH, value=how_did_you_hear_friend_xpath)
        choose_element.click()
        time.sleep(3)

    # click on submit
    def click_submit(self):
        try:
            submit_xpath = '//*[@id="hsForm_1c6d7d5c-7237-45e2-961e-02c5a47fb283"]/div[7]/div[2]/input'
            submit_element = self.driver.find_element(by=By.XPATH, value=submit_xpath)
            time.sleep(5)
            submit_element.click()
        except Exception as ex:
            print("Error with click on Submit")
            print(ex)
            self.driver.quit()
            exit()

    def fill_out_popup_window(self):
        driver = self.driver

        try:
            url = "https://agorareal.com/"
            driver.get(url)
            driver.maximize_window()
            # delay to let the page up.
            time.sleep(12)

        except Exception as ex:
            print("Error to get in the url")
            print(ex)
            exit()

        else:
            self.click_book_a_demo()
            self.fill_in_first_name(self.user_info.first_name)
            self.fill_in_last_name(self.user_info.last_name)
            self.fill_in_email(self.user_info.email)
            self.fill_in_phone_number(self.user_info.phone_number)
            self.choose_company_type()
            self.fill_in_open_help_note(self.user_info.my_question)
            self.fill_in_how_did_you_hear_dropbox()
            self.click_submit()
            # delay to see we click on submit before its close
            time.sleep(3)
            self.driver.quit()
            return True


if __name__ == '__main__':
    user_info = UserInfo("Bob", "cohen", "bob@gmail.com", "0508758263", "I have one")
    print(user_info)
    popup = PopupWindow(user_info)
    popup.set_up()
    popup.fill_out_popup_window()

