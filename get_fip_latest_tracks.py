import requests
import deezer

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException
import selenium.webdriver.support.expected_conditions as EC
driver = webdriver.Firefox()

response = driver.get('https://connect.deezer.com/oauth/auth.php?app_id=508002&redirect_uri=https://arthursw.github.io/fipzer/index.html&perms=email,online_access')

# response = driver.get('https://connect.deezer.com/oauth/auth.php', params={'app_id': '508002', 'redirect_uri': 'https://arthursw.github.io/fipzer/index.html', 'perms': 'email,offline_access'})


wait = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])

# element = wait.until(EC.visibility_of((By.CSS_SELECTOR, "#dz-root")))
wait.until(EC.url_contains('arthursw.github.io/fipzer/index.html'))

print(driver.current_url)
print(driver.current_url.split('?')[1].split('=')[1])

access_token = driver.current_url.split('?')[1].split('=')[1]

client = deezer.Client(access_token=access_token)

print(client.search('Daft Punk'))
# response = requests.get('https://connect.deezer.com/oauth/access_token.php', params={'app_id':'508002', 'secret': '62a30a7740ee02f6b3e099313af2af75', 'code': 'fr705771abf21a4a3d3404388df5c2e1'})
# response = requests.get('https://connect.deezer.com/oauth/access_token.php', params={'app_id':'508002', 'secret': '62a30a7740ee02f6b3e099313af2af75', 'code': 'fr154eecba13033597ac2945c2c768dc'})
# access_token = str(response.content).split('&')[0].split('=')[1]


# response = requests.get('https://api.deezer.com/search?q=eminem', params={'access_token': access_token})

print(access_token)
print('creating fip test 1...')

response = requests.post('https://api.deezer.com/user/2734742/playlists/', params={'access_token': access_token, 'title': 'FIP test 1'})

import ipdb; ipdb.set_trace()

driver.get("file:///Users/Arthur/Projects/Tiny/Fipzer/index.html");


# driver.get("https://www.fip.fr/titres-diffuses?station=jazz")


# # elem = driver.find_element_by_name("q")
# refuse_button = driver.find_element(By.ID, 'didomi-notice-disagree-button')
# refuse_button.click()


# more_button = driver.find_element(
#     By.CSS_SELECTOR, 'button.button-base.button.tracklist-content-button-more')
# more_button.click()


# timeline = driver.find_element(By.CSS_SELECTOR, 'ul.list.timeline')
# timeline_items = timeline.find_elements(By.CLASS_NAME, 'timeline-item')


# for item in timeline_items:
#     title = item.find_element(By.CLASS_NAME, 'now-info-title')
#     artist = item.find_element(By.CLASS_NAME, 'now-info-subtitle')
#     album = item.find_elements(By.CLASS_NAME, 'now-info-details-value')[0]
#     label = item.find_elements(By.CLASS_NAME, 'now-info-details-value')[1]
#     print(title.get_attribute('innerHTML'), artist.get_attribute('innerHTML'),
#         album.get_attribute('innerHTML'), label.get_attribute('innerHTML'))
#     # import ipdb; ipdb.set_trace()

