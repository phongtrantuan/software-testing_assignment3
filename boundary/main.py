from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import *
from data import *
 
def prepareData(driver):
  driver.get("http://localhost/")
  driver.maximize_window()

  env = dotenv_values(".env")
  username_login = env["usernameAdmin"] 
  password_login = env["passwordAdmin"]
  login(driver, username_login, password_login)
  

def closeBg(driver):
  try:    
    WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, "//div[@data-flexitour='backdrop']")))
    bgCourse = driver.find_elements(By.XPATH, "//div[@data-flexitour='backdrop']")
    if len(bgCourse) > 0:
      bgCourse[0].click()
  except:
    pass

def login(driver, username, password):
  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@href='http://localhost/login/index.php']")))
  loginButton = driver.find_element(By.XPATH, "//a[@href='http://localhost/login/index.php']")
  loginButton.click()
  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@name='username']")))
  usernameInput = driver.find_element(By.XPATH, "//input[@name='username']")
  passwordInput = driver.find_element(By.XPATH, "//input[@name='password']")
  usernameInput.clear()
  passwordInput.clear()
  usernameInput.send_keys(username)
  passwordInput.send_keys(password)
  login = driver.find_element(By.XPATH, "//button[@id='loginbtn']")
  login.click()
  closeBg(driver)
  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@id='user-menu-toggle']")))
  avatar = driver.find_element(By.XPATH, "//a[@id='user-menu-toggle']")
  avatar.click()
  try: 
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.carousel-navigation-link.dropdown-item")))
    language = driver.find_element(By.CSS_SELECTOR, "a.carousel-navigation-link.dropdown-item")
    language.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div > div.items.h-100.overflow-auto > a:nth-child(1)")))
    languageEnglish = driver.find_element(By.CSS_SELECTOR, "div > div.items.h-100.overflow-auto > a:nth-child(1)")
    languageEnglish.click()
  except:
    avatar.click()
  
def logout(driver):
  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@id='user-menu-toggle']")))
  avatar = driver.find_element(By.XPATH, "//a[@id='user-menu-toggle']")
  avatar.click()
  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@class='dropdown-item']")))
  listManager = driver.find_elements(By.CSS_SELECTOR, "#carousel-item-main a.dropdown-item")
  logoutButton = listManager[len(listManager)-1]
  logoutButton.click()

def changePoint(driver, point):
  try: 
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//li[@data-key='siteadminnode']")))
    adminSite = driver.find_element(By.XPATH, "//li[@data-key='siteadminnode']")
    adminSite.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@href='#linkgrades']")))
    adminGrade = driver.find_element(By.XPATH, "//a[@href='#linkgrades']")
    adminGrade.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@href='http://localhost/admin/settings.php?section=gradessettings']")))
    adminGradeSetting = driver.find_element(By.XPATH, "//a[@href='http://localhost/admin/settings.php?section=gradessettings']")
    adminGradeSetting.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@name='s__gradepointmax']")))
    adminGradeMax = driver.find_element(By.XPATH, "//input[@name='s__gradepointmax']")
    adminGradeMax.clear()
    adminGradeMax.send_keys(point['max'])
    adminGradeDefault = driver.find_element(By.XPATH, "//input[@name='s__gradepointdefault']")
    adminGradeDefault.clear()
    adminGradeDefault.send_keys(point['default'])
    
    adminGradeSaveChange = driver.find_element(By.CSS_SELECTOR, "form .row button.btn.btn-primary")
    adminGradeSaveChange.click()
    
    # check
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.alert")))
    alertSuccess = driver.find_elements(By.CSS_SELECTOR, "div.alert.alert-success")
    if len(alertSuccess) > 0:
      if point['expect'] == "success":
        print('Pass')
      if point['expect'] == "error":
        print('Fail')
      return
    alertDanger = driver.find_elements(By.CSS_SELECTOR, "div.alert.alert-danger")
    if len(alertDanger) > 0:
      if point['expect'] == "error":
        textError = driver.find_element(By.CSS_SELECTOR, ".form-setting span.error").text
        if textError == point['result']:
          print('Pass')
          return
      print('Fail')
      return
  except :
    print('Fail')
def main():
  # create webdriver object
  driver = webdriver.Chrome()
  dataTest = data
  prepareData(driver)
  
  changePoint(driver, dataTest['dataMin-'])
  changePoint(driver, dataTest['dataMin'])
  changePoint(driver, dataTest['dataMin+'])
  changePoint(driver, dataTest['dataAverage'])
  changePoint(driver, dataTest['dataMax-'])
  changePoint(driver, dataTest['dataMax'])
  changePoint(driver, dataTest['dataMax+'])
  
if __name__ == '__main__':
  main()