from selenium import webdriver
import random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

url = "https://10ff.net/login"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
driver.get(url=url)

time.sleep(0.2)
finger_name = driver.find_element(By.XPATH, '//*[@id="username"]')
finger_name.click()
finger_name.send_keys("Femboy Sock >w<", Keys.ENTER)

start_bot = False
players_found = False

waiting_for_players = driver.find_element(By.XPATH, '//*[@id="game"]/div[2]/div[2]').text.split()
if waiting_for_players[-1] != 'players.':
    players_found = True

count_down = "10"

while count_down != ["1"]:
    count_down = driver.find_element(By.XPATH, '//*[@id="game"]/div[2]/div').text.split()
    print(count_down)
    time.sleep(1)

start_bot = True


if start_bot:
    time.sleep(1)
    # Word automation
    type_in_word = driver.find_element(By.XPATH, '//*[@id="game"]/div[3]/div[2]/div[2]/div[1]/input')
    number = 2
    root = f'//*[@id="game"]/div[3]/div[2]/div[1]/div/span[{number}]'
    words = driver.find_element(By.XPATH, '//*[@id="game"]/div[3]/div[2]/div[1]/div/span[1]')
    print(words.text)

    type_in_word.send_keys(words.text, Keys.SPACE)

    for num in range(80):
        time.sleep(0.18)
        word_that_should_be_sent = driver.find_element(By.XPATH,
                                                       f'//*[@id="game"]/div[3]/div[2]/div[1]/div/span[{number}]').text
        print(word_that_should_be_sent)
        type_in_word.send_keys(word_that_should_be_sent, Keys.SPACE)
        number += 1

