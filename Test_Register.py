import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import random
import string

class TestRegister(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_a_success_register(self): 
        # steps
        result_str = ''.join((random.choice('abcdxyzpqr') for i in range(5)))
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"signUp").click() # klik tombol sign in
        time.sleep(1)
        browser.find_element(By.ID,"name_register").send_keys(result_str) # isi email
        time.sleep(1)
        browser.find_element(By.ID,"email_register").send_keys(result_str+"@jagoqa.com") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"password_register").send_keys("testerjago") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signup_register").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('berhasil', response_data)
        self.assertEqual(response_message, 'created user!')

    
    def test_b_failed_empty_name_register(self): 
        # steps
        result_str = ''.join((random.choice(string.ascii_lowercase) for i in range(5)))
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"signUp").click() # klik tombol sign in
        time.sleep(1)
        browser.find_element(By.ID,"name_register").send_keys("") # isi email
        time.sleep(1)
        browser.find_element(By.ID,"email_register").send_keys(result_str+"@jagoqa.com") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"password_register").send_keys("testerjago") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signup_register").click() # klik tombol sign in
        time.sleep(1)

    def test_c_failed_exceed_max_character(self): 
        # steps
        result_str = ''.join((random.choice(string.ascii_lowercase) for i in range(40)))
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"signUp").click() # klik tombol sign in
        time.sleep(1)
        browser.find_element(By.ID,"name_register").send_keys(result_str) # isi email
        time.sleep(1)
        browser.find_element(By.ID,"email_register").send_keys(result_str+"@jagoqa.com") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"password_register").send_keys(result_str) # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signup_register").click() # klik tombol sign in
        time.sleep(1)

    def test_d_failed_empty_email_password(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"signUp").click() # klik tombol sign in
        time.sleep(1)
        browser.find_element(By.ID,"name_register").send_keys("") # isi email
        time.sleep(1)
        browser.find_element(By.ID,"email_register").send_keys("") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"password_register").send_keys("") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signup_register").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('sudah terdaftar', response_data)
        self.assertEqual(response_message, 'Gagal Register!')

        # validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('melebihi', response_data)
        self.assertEqual(response_message, 'Gagal Register!')

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()
