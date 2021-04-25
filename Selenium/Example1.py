from selenium import webdriver

url = "https://www.youtube.com/c/vahrehvah/videos";

driver = webdriver.Chrome('/Users/bhaagi/dev/LearningPythonBasics/Selenium/chromedriver')
driver.get(url)

videos = driver.find_elements_by_class_name('style-scope ytd-grid-video-renderer')

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

print(len(videos))

for video in videos:
    title = video.find_element_by_xpath('.//*[@id="video-title"]')
    print(title.text)