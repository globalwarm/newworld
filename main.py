from ast import Num
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import random
from collections import Counter
import datetime


class FormBot():
    def __init__(
        self,
        link=None,
        country_code=None,
        time=0
    ) -> None:
        if link == None:
            print('Link Cannot be null.')

        a = 'https://docs.google.com/forms/d/e/1FAIpQLSd55dRV-YDI-klrgYwj0SaEok8A0twW51Hn-JA0V2CPsYW1qw/viewform'
        f = 'https://docs.google.com/forms/d/e/1FAIpQLSfbltArmRd-W3i49bY9pDc7FocN5OknS_tedFwaJMAS7ekmNQ/viewform'
        m = 'https://docs.google.com/forms/d/e/1FAIpQLSfvgQRSDh9liaOCnfW-l03x_TkSuJ8LCP0dlrnS30hOw0QRgA/viewform'
        if link == 'a':
            self.link = a
            print('Ahmad')
        elif link == 'f':
            self.link = f
            print('Feras')
        elif link == 'm':
            self.link = m
            print('Moayed')
        self.country_code = country_code
        if self.country_code:
            print('country code %s' % self.country_code)
        else:
            print('random country')
        
        self.time = time
        
        print('time between each submit is set to: %s' % self.time)

    # Functions
    def start(self, lang=0, nof=3):
        print('number of submit: %s' % nof)
        self.nof = nof
        for i in range(1, nof + 1):
            print(datetime.datetime.now())
            print('Start With Submit N.%s' % i)
            self.current_nof = i
            self.service = Service(
                'C:\Program Files (x86)\chromedriver_win32\chromedriver.exe')
            self.driver = webdriver.Chrome(service=self.service, options=self._options())
            self.driver.maximize_window()
            self.page_number = 1
            self.driver.get(self.link)

            sleep(2)
            self.language_page(lang)

    def _options(self):
        options = Options()
        options.add_argument("start-maximized")
        options.add_experimental_option("detach", False)
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        return options

    def next_page(self):
        sleep(1)
        if(self.page_number == 1):
            self.page_number += 1
            next_btn = self.driver.find_element(
                By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span')
            next_btn.click()
        elif(self.page_number == 2):
            next_btn = self.driver.find_element(
                By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div[2]/span')
            next_btn.click()

    # Pages
    def language_page(self, lang_flag):
        languages_select = self.driver.find_elements(
            By.CLASS_NAME, 'docssharedWizToggleLabeledContainer')
        sleep(1)
        languages_select[lang_flag].click()
        sleep(1)
        self.next_page()
        self.first_page()

    def first_page(self):
        all_answers = self.driver.find_elements(
            by=By.CLASS_NAME, value="docssharedWizToggleLabeledContainer")

        sleep(1)
        _gender = all_answers[:3]
        _gender_weighted = [0] * 49 + [1] * 49 + [2] * 1
        selected_gender = _gender[random.choice(_gender_weighted)]
        selected_gender.click()

        sleep(1)
        _age = all_answers[3:10]
        _age_weighted = [0] * 9 + [1] * 15 + [2] * 15 + \
            [3] * 20 + [4] * 20 + [5] * 12 + [6] * 9
        selected_age = _age[random.choice(_age_weighted)]
        selected_age.click()

        sleep(1)
        exp_sig, exp_mar, exp_div_sep, exp_widowed = 0, 0, 0, 0
        _marital = all_answers[10:14]
        if(selected_age.text == 'Below 20'):
            exp_sig, exp_mar, exp_div_sep, exp_widowed = 100, 0, 0, 0
        if(selected_age.text == '20-30'):
            exp_sig, exp_mar, exp_div_sep, exp_widowed = 60, 25, 15, 0
        if(selected_age.text == '31-40'):
            exp_sig, exp_mar, exp_div_sep, exp_widowed = 49, 35, 15, 1
        if(selected_age.text == '41-50'):
            exp_sig, exp_mar, exp_div_sep, exp_widowed = 37, 42, 18, 3
        if(selected_age.text == '51-60'):
            exp_sig, exp_mar, exp_div_sep, exp_widowed = 30, 42, 25, 3
        if(selected_age.text == '61-70'):
            exp_sig, exp_mar, exp_div_sep, exp_widowed = 25, 45, 27, 3
        if(selected_age.text == 'Above 70'):
            exp_sig, exp_mar, exp_div_sep, exp_widowed = 20, 47, 30, 3

        _marital_weighted = [0] * exp_sig + [1] * \
            exp_mar + [2] * exp_div_sep + [3] * exp_widowed
        selected_marital = _marital[random.choice(_marital_weighted)]
        selected_marital.click()
        sleep(1)

        nationality = self.driver.find_elements(
            by=By.CLASS_NAME, value="jgvuAb")
        sleep(1)
        nationality[0].click()

        # sleep(1)
        # nationalities = self.driver.find_elements(by=By.CLASS_NAME, value="oJeWuf")
        # nationalities = nationalities[190:-2]

        self._nationality_weighted = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 44, 45, 46, 47, 48, 49, 50,
                                      51, 53, 54, 55, 56, 57, 58, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60,
                                      60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 61, 62, 63, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64,
                                      64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 77, 78,
                                      79, 80, 81, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 83, 84, 85, 86, 87, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 100, 101, 102, 103, 104, 105, 107, 108, 110, 111, 112, 113, 114, 116, 117, 118, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 136, 137, 138, 139, 140, 141, 141, 141, 141, 141, 141, 141, 141, 141, 141, 141, 141, 141, 141, 141, 141, 141, 141, 141, 141, 141, 141, 141, 141, 141, 141, 141, 141, 141, 141, 141, 141, 141, 141, 141, 141, 141, 141, 141, 141, 141, 141, 141, 141, 141, 141, 141, 141, 141, 141, 142, 142, 142, 142, 142, 142, 142, 142, 142, 142, 142, 142, 142, 142, 142, 142, 142, 142, 142, 142, 142, 142, 142, 142, 142, 142, 142, 142, 142, 142, 142, 142, 142, 142, 142, 142, 142, 142, 142, 142, 142, 142, 142, 142, 142, 142, 142, 142, 142, 142, 143, 144, 145, 146, 147, 148, 149, 152, 153, 154, 156, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158,
                                      158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 158, 159, 160, 161, 162, 163, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178,
                                      178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 178, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 179, 180, 181, 182, 183, 184]

        # for idx, nationality in enumerate(nationalities):
        #     if(nationality.text in ['United States','United Kingdom','Spain','France',]):
        #         _nationality_weighted.extend([idx + 3] * 100)
        #     elif(nationality.text in ['Russia','Romania','Italy','India','Germany','Finland',]):
        #         _nationality_weighted.extend([idx + 3] * 50)
        #     elif(nationality.text in [
        #         'Syria','Somalia', 'Zimbabwe','Zambia','Yemen','Vietnam','Sri Lanka','Sierra Leone','Paraguay','Papua New Guinea','Myanmar (Burma)',
        #         'Mongolia','Libya','Kiribati','El Salvador','Cuba','Maldives','Marshall Islands','Seychelles',]):
        #         _nationality_weighted.extend([idx + 3] * 0)
        #     else:
        #         _nationality_weighted.append(idx + 3)

        if self.country_code:
            self.selected_nationality = self.country_code
        else:
            self.selected_nationality = random.choice(
                self._nationality_weighted)

        sleep(1)
        self.driver.find_element(
            By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[2]/div[%s]/span' % self.selected_nationality).click()

        self.next_page()
        self.second_page()

    def second_page(self):
        nationality = self.driver.find_elements(
            by=By.CLASS_NAME, value="jgvuAb")
        sleep(2)
        nationality[0].click()
        sleep(3)
        self.driver.find_element(
            By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[2]/div[%s]/span' % self.selected_nationality).click()

        self.next_page()
        self.third_page()

    def third_page(self):
        all_answers = self.driver.find_elements(
            by=By.CLASS_NAME, value="docssharedWizToggleLabeledContainer")
        sleep(1)
        _income = all_answers[:9]
        _income_weighted = [0] * 7 + [1] * 13 + [2] * 15 + [3] * \
            15 + [4] * 15 + [5] * 15 + [6] * 10 + [7] * 10 + [8] * 10
        selected_gender = _income[random.choice(_income_weighted)]
        selected_gender.click()

        sleep(1)
        _trip_line = all_answers[9:11]
        _trip_line_weighted = [0] * 85 + [1] * 15
        selected_trip_line = _trip_line[random.choice(_trip_line_weighted)]
        selected_trip_line.click()
        self.trip_line_str = selected_trip_line.text[3:]

        self.next_page()
        sleep(1)
        if(self.trip_line_str == 'No'):
            self.trip_line_multiple_page()
        elif(self.trip_line_str == 'Yes'):
            self.only_one_line_page()
        else:
            self.mode_page()

    def only_one_line_page(self):
        sleep(1)
        _jordan_days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, ]
        self.days_in_jordan = random.choice(_jordan_days)
        _daysjordan_contries = self.driver.find_element(
            by=By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
        _daysjordan_contries.send_keys(str(self.days_in_jordan))
        sleep(1)
        self.next_page()
        sleep(1)
        self.mode_page()

    def trip_line_multiple_page(self):
        all_answers = self.driver.find_elements(
            by=By.CLASS_NAME, value="docssharedWizToggleLabeledContainer")
        sleep(1)
        _other_contries = all_answers[:7]
        _other_contries_weighted = [0, 1, 2, 3, 4, 5]
        selected_other_contries = map(_other_contries.__getitem__, random.sample(
            _other_contries_weighted, random.randint(1, 3)))

        for contry in selected_other_contries:
            contry.click()

        sleep(1)
        na_pat = ['na'] * 10 + ['NA'] * 20 + ['N/A'] * 50 + ['N/a'] * 20
        _name_other_contries = self.driver.find_element(
            by=By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
        _name_other_contries.send_keys(random.choice(na_pat))

        sleep(1)
        _jordan_days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        self.days_in_jordan = random.choice(_jordan_days)
        _daysjordan_contries = self.driver.find_element(
            by=By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input")
        _daysjordan_contries.send_keys(str(self.days_in_jordan))

        sleep(1)
        _total_days = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, ]
        self.days_in_trip = random.choice(_total_days)
        _totaldays_contries = self.driver.find_element(
            by=By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input")
        _totaldays_contries.send_keys(str(self.days_in_trip))

        sleep(1)
        self.next_page()
        sleep(1)
        self.mode_page()

    def mode_page(self):
        all_answers = self.driver.find_elements(
            by=By.CLASS_NAME, value="docssharedWizToggleLabeledContainer")
        sleep(1)
        _modes = all_answers[:4]
        _modes_weighted = [0] + [1] + [2] + [3]
        selected_modes = map(_modes.__getitem__, random.sample(
            _modes_weighted, random.randint(1, 3)))

        for mode in selected_modes:
            mode.click()

        sleep(1)
        self.next_page()

        sleep(1)
        all_answers = self.driver.find_elements(
            by=By.CLASS_NAME, value="docssharedWizToggleLabeledContainer")

        sleep(1)
        _hear = all_answers[:9]
        _hear_weighted = [0, 1, 2, 3, 4, 5, 6, 7]
        selected_hear = map(_hear.__getitem__, random.sample(
            _hear_weighted, random.randint(1, 4)))

        for h in selected_hear:
            h.click()

        sleep(1)
        _arrange = all_answers[10:13]
        _arrange_weighted = [0] * 33 + [1] * 33 + [2] * 33
        selected_arrange = _arrange[random.choice(_arrange_weighted)]
        selected_arrange.click()
        self.selected_arrange_str = selected_arrange.text
        sleep(1)
        _when = all_answers[14:]
        if 'travel agency' in self.selected_arrange_str:
            _when_weighted = [0] * 33 + [1] * 0 + [2] * 0
        elif 'individual trip' in self.selected_arrange_str:
            _when_weighted = [0] * 33 + [1] * 33 + [2] * 0
        elif 'individually arrange' in self.selected_arrange_str:
            _when_weighted = [0] * 30 + [1] * 50 + [2] * 0
        selected_when = _when[random.choice(_when_weighted)]
        selected_when.click()

        sleep(1)
        self.next_page()

        sleep(1)
        all_answers = self.driver.find_elements(
            by=By.CLASS_NAME, value="docssharedWizToggleLabeledContainer")

        sleep(1)
        _where = all_answers[:4]
        if 'travel agency' in self.selected_arrange_str:
            _where_weighted = [0] * 0 + [1] * 50 + [2] * 30 + [3] * 0
        elif 'individual trip' in self.selected_arrange_str:
            _where_weighted = [0] * 25 + [1] * 25 + [2] * 15 + [3] * 5
        elif 'individually arrange' in self.selected_arrange_str:
            _where_weighted = [0] * 20 + [1] * 0 + [2] * 20 + [3] * 10
        selected_where = _where[random.choice(_where_weighted)]
        selected_where.click()

        sleep(1)
        _whom = all_answers[5:11]
        _whom_weighted = [0, 1, 2, 3, 4, 5]
        selected_whom = map(_whom.__getitem__, random.sample(
            _whom_weighted, random.randint(1, 1)))
        for h in selected_whom:
            h.click()

        sleep(1)
        _purpose = all_answers[12:25]
        _purpose_weighted = [0, 1, 2, 3, 4, 5, 6, 8, 10, 11]
        selected_purpose = map(_purpose.__getitem__, random.sample(
            _purpose_weighted, random.randint(1, 3)))
        for h in selected_purpose:
            h.click()

        sleep(1)
        _howget = all_answers[26:31]
        _howget_weighted = [[0], [2, 3, 4], [2, 4], [0, 3]]
        selected_howget = map(_howget.__getitem__,
                              random.choice(_howget_weighted))
        for h in selected_howget:
            h.click()

        sleep(1)
        _ticket = all_answers[32:36]
        if 'travel agency' in self.selected_arrange_str:
            _ticket_weighted = [0] * 25 + [1] * 25 + [2] * 50 + [3] * 0
        elif 'individual trip' in self.selected_arrange_str:
            _ticket_weighted = [0] * 25 + [1] * 25 + [2] * 25 + [3] * 25
        elif 'individually arrange' in self.selected_arrange_str:
            _ticket_weighted = [0] * 50 + [1] * 25 + [2] * 0 + [3] * 25
        selected_ticket = _ticket[random.choice(_ticket_weighted)]
        selected_ticket.click()

        sleep(1)
        _overnight = all_answers[38:]
        _overnight_weighted = [0] * 50 + [1] * 50
        selected_overnight = _overnight[random.choice(_overnight_weighted)]
        selected_overnight.click()
        self.stays_overnight_str = selected_overnight.text

        self.next_page()
        sleep(1)
        if(self.stays_overnight_str == 'Yes'):
            self.stays_overnight()
        elif(self.stays_overnight_str == 'No'):
            self.trip_map()

    def stays_overnight(self):
        sleep(1)
        all_answers = self.driver.find_elements(
            by=By.CLASS_NAME, value="docssharedWizToggleLabeledContainer")

        sleep(1)
        _nigthspetra = random.randint(1, (self.days_in_jordan))
        _nigthspetra_input = self.driver.find_element(
            by=By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
        _nigthspetra_input.send_keys(str(_nigthspetra))

        sleep(1)
        _accommodation = all_answers[:5]
        _accommodation_weighted = [0] * 30 + [1] * \
            30 + [2] * 20 + [3] * 10 + [4] * 10
        selected_accommodation = _accommodation[random.choice(
            _accommodation_weighted)]
        selected_accommodation.click()

        sleep(1)
        _accommodationclass = all_answers[6:11]
        _accommodationclass_weighted = [0] * 10 + \
            [1] * 30 + [2] * 25 + [3] * 25 + [4] * 10
        selected_accommodationclass = _accommodationclass[random.choice(
            _accommodationclass_weighted)]
        selected_accommodationclass.click()

        self.next_page()
        sleep(1)
        self.trip_map()

    def trip_map(self):
        sleep(1)
        all_answers = self.driver.find_elements(
            by=By.CLASS_NAME, value="docssharedWizToggleLabeledContainer")

        sleep(1)
        _enter = all_answers[:3]
        _enter_weighted = [0, 1, 2]
        selected_enter = map(_enter.__getitem__, random.sample(
            _enter_weighted, random.randint(1, 2)))
        for h in selected_enter:
            h.click()

        _spot = all_answers[4:19]
        _spot_weighted = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14]
        self.spot_selected = [0, 6] + \
            random.sample(_spot_weighted, random.randint(1, 5))
        selected_spot = map(_spot.__getitem__, self.spot_selected)
        for h in selected_spot:
            h.click()

        self.trail_path = [0, 1]
        if {9, } & set(self.spot_selected):
            self.trail_path.append(2)
        if {5, } & set(self.spot_selected):
            self.trail_path.append(3)
        if {8, } & set(self.spot_selected):
            self.trail_path.append(4)
        if {13, } & set(self.spot_selected):
            self.trail_path.append(5)

        sleep(1)
        _trail = all_answers[20:26]
        selected_trail = map(_trail.__getitem__, self.trail_path)
        for h in selected_trail:
            h.click()

        sleep(1)
        _fees = [50, 55, 60]
        _fees = [0, 0] + _fees + [i*random.choice(_fees) for i in range(1, 7)]
        _fees_input = self.driver.find_element(
            by=By.XPATH, value="/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input")
        _fees_input.send_keys(str(random.choice(_fees)))

        sleep(1)
        _feesguide = [0, 0, 0, 0, 100, 120, 150] + [i*40 for i in range(1, 7)]
        _feesguide_input = self.driver.find_element(
            by=By.XPATH, value="/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div[1]/div/div[1]/input")
        self.selected_feesguid = random.choice(_feesguide)
        _feesguide_input.send_keys(str(self.selected_feesguid))

        sleep(1)
        _souvenirs = [0, 0, 0, 0, 0, 0] + [i*5 for i in range(1, 50)]
        _souvenirs_input = self.driver.find_element(
            by=By.XPATH, value="/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div[1]/div/div[1]/input")
        self.selected_souvenirs = random.choice(_souvenirs)
        _souvenirs_input.send_keys(str(self.selected_souvenirs))

        sleep(1)
        _beverage = [i*5 for i in range(10, 25)]
        _beverage_input = self.driver.find_element(
            by=By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[11]/div/div/div[2]/div/div[1]/div/div[1]/input")
        _beverage_input.send_keys(str(random.choice(_beverage)))

        sleep(1)
        _accommodation = [0, 0, 0, 0, 0, 0]
        if self.stays_overnight_str == 'Yes':
            _accommodation += [i*5 for i in range(10, 25)]

        _accommodation_input = self.driver.find_element(
            by=By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[12]/div/div/div[2]/div/div[1]/div/div[1]/input")
        _accommodation_input.send_keys(str(random.choice(_accommodation)))

        sleep(1)
        _service = [i*5 for i in range(2, 10)]
        _service_input = self.driver.find_element(
            by=By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[13]/div/div/div[2]/div/div[1]/div/div[1]/input")
        _service_input.send_keys(str(random.choice(_service)))

        sleep(1)
        _activities = [0, 0, 0, 0, 0, 0] + [i*5 for i in range(5, 15)]
        _activities_input = self.driver.find_element(
            by=By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[14]/div/div/div[2]/div/div[1]/div/div[1]/input")
        _activities_input.send_keys(str(random.choice(_activities)))

        sleep(1)
        na_pat = [0] * 5 + ['nothing'] * 2 + ['clothes'] * 2 + ['na'] * 5 + ['NA'] * 5 + ['N/A'] * 10 + ['N/a'] * 5
        _h1 = random.choice(na_pat)
        _h1_input = self.driver.find_element(
            by=By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[15]/div/div/div[2]/div/div[1]/div/div[1]/input")
        _h1_input.send_keys(str(_h1))

        sleep(1)
        if _h1 == 'nothing' or _h1 == 'clothes':
            _h2 = [i*5 for i in range(5, 15)]
        else:
            _h2 = [0]
        _h2_input = self.driver.find_element(
            by=By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[16]/div/div/div[2]/div/div[1]/div/div[1]/input")
        _h2_input.send_keys(str(random.choice(_h2)))

        sleep(1)
        _value = all_answers[26:31]
        _value_weighted = [0] * 10 + [1] * 25 + [2] * 25 + [3] * 30 + [4] * 10
        selected_value = _value[random.choice(_value_weighted)]
        selected_value.click()

        sleep(1)
        flag = 20
        if self.selected_feesguid == 0:
            flag = 0
        _hire = all_answers[31:36]
        _hire_weighted = [0] * flag + [1] * flag + \
            [2] * flag + [3] * flag + [4] * 20
        selected_hire = _hire[random.choice(_hire_weighted)]
        selected_hire.click()

        sleep(1)
        _visit = all_answers[37:]
        _visit_weighted = [0] * 50 + [1] * 50
        selected_visit = _visit[random.choice(_visit_weighted)]
        selected_visit.click()

        self.visit_museum_str = selected_visit.text

        self.next_page()
        sleep(1)
        if(self.visit_museum_str == 'Yes'):
            self.visit_museum()
        elif(self.visit_museum_str == 'No'):
            self.use_soical_media()

    def visit_museum(self):
        all_answers = self.driver.find_elements(
            by=By.CLASS_NAME, value="docssharedWizToggleLabeledContainer")

        sleep(1)
        _whenmuseum = all_answers[:5]
        _whenmuseum_weighted = [0] * 15 + [1] * \
            15 + [2] * 15 + [3] * 15 + [4] * 0
        selected_whenmuseum = _whenmuseum[random.choice(_whenmuseum_weighted)]
        selected_whenmuseum.click()

        sleep(1)
        _time = all_answers[5:]
        _time_weighted = [0] * 15 + [1] * 15 + [2] * 15
        selected_time = _time[random.choice(_time_weighted)]
        selected_time.click()

        self.next_page()
        sleep(1)
        self.use_soical_media()

    def use_soical_media(self):
        all_answers = self.driver.find_elements(
            by=By.CLASS_NAME, value="docssharedWizToggleLabeledContainer")

        sleep(1)
        _use = all_answers
        _use_weighted = [0] * 15 + [1] * 15
        selected_use = _use[random.choice(_use_weighted)]
        selected_use.click()

        self.use_social_str = selected_use.text

        self.next_page()
        sleep(1)
        if(self.use_social_str == 'Yes'):
            all_answers = self.driver.find_elements(
                by=By.CLASS_NAME, value="docssharedWizToggleLabeledContainer")
            sleep(1)
            _platform = all_answers[:5]
            _platform_weighted = [0] * 20 + [1] * \
                20 + [2] * 20 + [3] * 20 + [4] * 20
            selected_platform = map(_platform.__getitem__, random.sample(
                _platform_weighted, random.randint(1, 3)))
            for mode in selected_platform:
                mode.click()

            self.next_page()
            sleep(1)
            self.other_visit_in_region()
        elif(self.use_social_str == 'No'):
            self.other_visit_in_region()

    def other_visit_in_region(self):
        all_answers = self.driver.find_elements(
            by=By.CLASS_NAME, value="docssharedWizToggleLabeledContainer")

        sleep(1)
        _use = all_answers
        _use_weighted = [0] * 15 + [1] * 15
        selected_use = _use[random.choice(_use_weighted)]
        selected_use.click()

        self.use_social_str = selected_use.text

        self.next_page()
        sleep(1)
        if(self.use_social_str == 'Yes'):
            all_answers = self.driver.find_elements(
                by=By.CLASS_NAME, value="docssharedWizToggleLabeledContainer")
            sleep(1)
            _platform = all_answers[:6]
            _platform_weighted = [0] * 20 + [1] * 20 + \
                [2] * 20 + [3] * 20 + [4] * 5 + [5] * 5
            selected_platform = map(_platform.__getitem__, random.sample(
                _platform_weighted, random.randint(1, 3)))
            for mode in selected_platform:
                mode.click()

            self.next_page()
            sleep(1)
            self.bring_phone()
        elif(self.use_social_str == 'No'):
            self.bring_phone()

    def bring_phone(self):
        all_answers = self.driver.find_elements(
            by=By.CLASS_NAME, value="docssharedWizToggleLabeledContainer")

        sleep(1)
        _use = all_answers
        _use_weighted = [0] * 15 + [1] * 15
        selected_use = _use[random.choice(_use_weighted)]
        selected_use.click()

        self.use_social_str = selected_use.text

        self.next_page()
        sleep(1)

        if(self.use_social_str == 'Yes'):
            all_answers = self.driver.find_elements(
                by=By.CLASS_NAME, value="docssharedWizToggleLabeledContainer")
            sleep(1)
            _use = all_answers
            _use_weighted = [0] * 15 + [1] * 15
            selected_use = _use[random.choice(_use_weighted)]
            selected_use.click()

            self.next_page()
            sleep(1)
            self.final_page()
        elif(self.use_social_str == 'No'):
            self.final_page()

    def final_page(self):
        sleep(1)
        five_ans = self.driver.find_elements(
            by=By.XPATH, value="//div[@role='radio' and @aria-setsize='5']")
        sleep(1)
        six_ans = self.driver.find_elements(
            by=By.XPATH, value="//div[@role='radio' and @aria-setsize='6']")

        end_point = 5
        temp = []
        for idx, six in enumerate(six_ans):
            temp.append(six)
            if idx == end_point:
                # 11-17 Souvenirs
                if end_point == 17:
                    if self.selected_souvenirs == 0:
                        sleep(1)
                        temp[0].click()
                        end_point += 6
                        temp = []
                        continue

                # 23-29 Tourguid
                if end_point == 29:
                    if self.selected_feesguid == 0:
                        sleep(1)
                        temp[0].click()
                        end_point += 6
                        temp = []
                        continue

                # 47-52 The Petra Museum visit
                if end_point == 53:
                    if self.visit_museum_str == 'No':
                        sleep(1)
                        temp[0].click()
                        end_point += 6
                        temp = []
                        continue

                # 53-58 Quality of accommodation services
                if end_point == 59:
                    if self.stays_overnight_str == 'No':
                        sleep(1)
                        temp[0].click()
                        end_point += 6
                        temp = []
                        continue

                # 65-71 Quality of souvenirs
                if end_point == 71:
                    if self.selected_souvenirs == 0:
                        sleep(1)
                        temp[0].click()
                        end_point += 6
                        temp = []
                        continue

                sleep(1)
                random.choice(temp).click()
                end_point += 6
                temp = []

        end_point = 4
        temp = []
        for idx, five in enumerate(five_ans):
            temp.append(five)
            if idx == end_point:
                sleep(1)
                random.choice(temp).click()
                end_point += 5
                temp = []

        all_answers = self.driver.find_elements(
            by=By.CLASS_NAME, value="docssharedWizToggleLabeledContainer")
        sleep(1)
        _platform = all_answers[:8]
        _platform_weighted = [0, 1, 2, 3, 4, 5, 6, 7]
        selected_platform = map(_platform.__getitem__, random.sample(
            _platform_weighted, random.randint(1, 3)))
        for mode in selected_platform:
            mode.click()

        sleep(1)
        self.next_page()
        sleep(2)
        if self.current_nof != self.nof:
            if self.time == 90:
                sleep(5400)
            elif self.time == 48:
                sleep(2880)
            elif self.time == 20:
                sleep(1200)
            elif self.time == 7:
                sleep(820)
            else:
                sleep(20)


# {60: 100, 158: 100, 178: 100, 179: 100, 59: 50, 64: 50, 76: 50, 82: 50, 141: 50, 142: 50, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1, 13: 1, 14: 1, 15: 1,
# 16: 1, 17: 1, 18: 1, 19: 1, 20: 1, 21: 1, 22: 1, 23: 1, 24: 1, 25: 1, 26: 1, 27: 1, 28: 1, 29: 1, 30: 1, 31: 1, 32: 1, 33: 1, 34: 1, 35: 1, 36: 1, 37: 1, 38: 1, 39: 1, 40: 1,
# 41: 1, 42: 1, 44: 1, 45: 1, 46: 1, 47: 1, 48: 1, 49: 1, 50: 1, 51: 1, 53: 1, 54: 1, 55: 1, 56: 1, 57: 1, 58: 1, 61: 1, 62: 1, 63: 1, 65: 1, 66: 1, 67: 1, 68: 1, 69: 1, 70: 1,
# 71: 1, 72: 1, 73: 1, 74: 1, 75: 1, 77: 1, 78: 1, 79: 1, 80: 1, 81: 1, 83: 1, 84: 1, 85: 1, 86: 1, 87: 1, 89: 1, 90: 1, 91: 1, 92: 1, 93: 1, 94: 1, 95: 1, 96: 1, 97: 1, 98: 1,
# 100: 1, 101: 1, 102: 1, 103: 1, 104: 1, 105: 1, 107: 1, 108: 1, 110: 1, 111: 1, 112: 1, 113: 1, 114: 1, 116: 1, 117: 1, 118: 1, 120: 1, 121: 1, 122: 1, 123: 1, 124: 1, 125: 1,
# 126: 1, 127: 1, 128: 1, 129: 1, 130: 1, 131: 1, 132: 1, 133: 1, 136: 1, 137: 1, 138: 1, 139: 1, 140: 1, 143: 1, 144: 1, 145: 1, 146: 1, 147: 1, 148: 1, 149: 1, 152: 1, 153: 1,
# 154: 1, 156: 1, 159: 1, 160: 1, 161: 1, 162: 1, 163: 1, 165: 1, 166: 1, 167: 1, 168: 1, 169: 1, 170: 1, 171: 1, 172: 1, 173: 1, 174: 1, 175: 1, 176: 1, 177: 1, 180: 1, 181: 1,
# 182: 1, 183: 1, 184: 1}

Number_of_submit = 4
cc = 64
t = 7

# sleep(10000)
fb = FormBot(
    # 'a',
    # 'f',
    'm',
    # country_code = cc,
    time = t
)
fb.start(nof=Number_of_submit)
