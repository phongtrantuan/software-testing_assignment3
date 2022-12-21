from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.relative_locator import locate_with
from dotenv import *
from data import *
 
def prepareData(driver):
  try:
    driver.get("http://localhost/")
    driver.maximize_window()
    usersCreated = dataPreCondition['usersCreated']

    env = dotenv_values("./../.env")
    username_login = env["usernameAdmin"] 
    password_login = env["passwordAdmin"]
    login(driver, username_login, password_login)
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
    
    for user in usersCreated:
      addAccount(driver, user)
    
    logout(driver)
    
    login(driver, usersCreated[0]['username'], usersCreated[0]['password'])
  except :
    pass  

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

def addAccount(driver, account):
  # delete account if it's username or email has existed
  deleteAccount(driver, account)
  
  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//li[@data-key='siteadminnode']")))
  adminSite = driver.find_element(By.XPATH, "//li[@data-key='siteadminnode']")
  adminSite.click()
  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@href='#linkusers']")))
  adminUser = driver.find_element(By.XPATH, "//a[@href='#linkusers']")
  adminUser.click()
  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@href='http://localhost/user/editadvanced.php?id=-1']")))
  addUser = driver.find_element(By.XPATH, "//a[@href='http://localhost/user/editadvanced.php?id=-1']")
  addUser.click()
  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='id_username']")))
  addUsername = driver.find_element(By.XPATH, "//input[@id='id_username']")
  addUsername.send_keys(account["username"])
  addPasswordSelect = driver.find_element(By.XPATH, "//a[@href='#'][@class='form-control']")
  addPasswordSelect.click()
  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='id_newpassword']")))
  addPassword = driver.find_element(By.XPATH, "//input[@id='id_newpassword']")
  addPassword.send_keys(account["password"])
  addFirstname = driver.find_element(By.XPATH, "//input[@id='id_firstname']")
  addFirstname.send_keys(account["firstname"])
  addSurname = driver.find_element(By.XPATH, "//input[@id='id_lastname']")
  addSurname.send_keys(account["surname"])
  addEmail = driver.find_element(By.XPATH, "//input[@id='id_email']")
  addEmail.send_keys(account["email"])
  
  addAccountSubmit = driver.find_element(By.XPATH, "//input[@id='id_submitbutton']")
  addAccountSubmit.click()

def deleteAccount(driver, account):
  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//li[@data-key='siteadminnode']")))
  adminSite = driver.find_element(By.XPATH, "//li[@data-key='siteadminnode']")
  adminSite.click()
  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@href='#linkusers']")))
  adminCourse = driver.find_element(By.XPATH, "//a[@href='#linkusers']")
  adminCourse.click()
  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@href='http://localhost/admin/user.php']")))
  listUser = driver.find_element(By.XPATH, "//a[@href='http://localhost/admin/user.php']")
  listUser.click()
  
  # delete account have email of account
  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@href='#'][@class='moreless-toggler']")))
  moreFilter = driver.find_element(By.XPATH, "//a[@href='#'][@class='moreless-toggler']")
  moreFilter.click()
  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='id_email']")))
  checkEmail = driver.find_element(By.XPATH, "//input[@id='id_email']")
  checkEmail.send_keys(account["email"])
  checkEmailSelect = Select(driver.find_element(By.XPATH, "//select[@id='id_email_op']"))
  checkEmailSelect.select_by_value('2')
  
  addFilter = driver.find_element(By.XPATH, "//input[@id='id_addfilter']")
  addFilter.click()
  try:
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "td.cell a i.fa-cog")))
    listAccountHaveEmail = driver.find_elements(By.CSS_SELECTOR, "td.cell a i.fa-cog")
    lenListAccount = len(listAccountHaveEmail)
    for i in range(lenListAccount):
      WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "td.cell a i.fa-cog")))
      driver.find_elements(By.CSS_SELECTOR, "td.cell a i.fa-cog")[i].click();
      WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='id_email']")))
      emailInput = driver.find_element(By.XPATH, "//input[@id='id_email']").get_attribute("value")
      if account["email"] == emailInput:
        driver.back()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "td.cell a i.fa-trash")))
        listAccountHaveEmailDelete = driver.find_elements(By.CSS_SELECTOR, "td.cell a i.fa-trash")
        listAccountHaveEmailDelete[i].click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#modal-footer form .btn.btn-primary")))
        deleteConfirm = driver.find_element(By.CSS_SELECTOR, "#modal-footer form .btn.btn-primary")
        deleteConfirm.click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#id_removeall")))
        deleteFilter = driver.find_element(By.CSS_SELECTOR, "#id_removeall")
        deleteFilter.click()
        break
      driver.back()
  except :
    try:
      WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#id_removeall")))
      deleteFilter = driver.find_element(By.CSS_SELECTOR, "#id_removeall")
      deleteFilter.click()
    except :
      pass
  
  # delete account have username of account
  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@href='#'][@class='moreless-toggler']")))
  moreFilter = driver.find_element(By.XPATH, "//a[@href='#'][@class='moreless-toggler']")
  moreFilter.click()
  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='id_username']")))
  checkUsername = driver.find_element(By.XPATH, "//input[@id='id_username']")
  checkUsername.send_keys(account["username"])
  checkUsernameSelect = Select(driver.find_element(By.XPATH, "//select[@id='id_username_op']"))
  checkUsernameSelect.select_by_value('2')
  addFilter = driver.find_element(By.XPATH, "//input[@id='id_addfilter']")
  addFilter.click()
  
  try:
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "td.cell a i.fa-cog")))
    listAccountHaveUsername = driver.find_elements(By.CSS_SELECTOR, "td.cell a i.fa-cog")
    lenListAccount = len(listAccountHaveUsername)
    for i in range(lenListAccount):
      WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "td.cell a i.fa-cog")))
      driver.find_elements(By.CSS_SELECTOR, "td.cell a i.fa-cog")[i].click();
      WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='id_username']")))
      usernameInput = driver.find_element(By.XPATH, "//input[@id='id_username']").get_attribute("value")
      if account["username"] == usernameInput:
        driver.back()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "td.cell a i.fa-trash")))
        listAccountHaveUsernameDelete = driver.find_elements(By.CSS_SELECTOR, "td.cell a i.fa-trash")
        listAccountHaveUsernameDelete[i].click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#modal-footer form .btn.btn-primary")))
        deleteConfirm = driver.find_element(By.CSS_SELECTOR, "#modal-footer form .btn.btn-primary")
        deleteConfirm.click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#id_removeall")))
        deleteFilter = driver.find_element(By.CSS_SELECTOR, "#id_removeall")
        deleteFilter.click()
        break
      driver.back()
  except :
    try:
      WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#id_removeall")))
      deleteFilter = driver.find_element(By.CSS_SELECTOR, "#id_removeall")
      deleteFilter.click()
    except :
      pass

def changPassword(driver, listPassword):
  try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@id='user-menu-toggle']")))
    avatar = driver.find_element(By.XPATH, "//a[@id='user-menu-toggle']")
    avatar.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@href='http://localhost/user/preferences.php']")))
    preferences = driver.find_element(By.XPATH, "//a[@href='http://localhost/user/preferences.php']")
    preferences.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".card-body .card-text div a")))
    changePass = driver.find_elements(By.CSS_SELECTOR, ".card-body .card-text div a")[1]
    changePass.click()
    
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#id_password")))
    currentPassword = driver.find_element(By.CSS_SELECTOR, "#id_password")
    currentPassword.clear()
    currentPassword.send_keys(listPassword['password'])
    currentPassword = driver.find_element(By.CSS_SELECTOR, "#id_newpassword1")
    currentPassword.clear()
    currentPassword.send_keys(listPassword['newpassword'])
    currentPassword = driver.find_element(By.CSS_SELECTOR, "#id_newpassword2")
    currentPassword.clear()
    currentPassword.send_keys(listPassword['newpasswordAgain'])
    currentPassword = driver.find_element(By.CSS_SELECTOR, "#id_submitbutton")
    currentPassword.click()
      
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#id_password")))
    cancel = driver.find_element(By.CSS_SELECTOR, "input#id_cancel")
    currentPasswordError = driver.find_elements(By.CSS_SELECTOR, "#id_error_password")
    if "password" in listPassword['errorField']:
      if listPassword['error'] in currentPasswordError[0].text:
        print('Pass')
        cancel.click()
        return
      print('Fail')
      cancel.click()
      return
    newPasswordError = driver.find_elements(By.CSS_SELECTOR, "#id_error_newpassword1")
    if len(listPassword['errorField']) < 2:
      if "newpassword" in listPassword['errorField']:
        if listPassword['error'] in newPasswordError[0].text:
          print('Pass')
          cancel.click()
          return
        print('Fail')
        cancel.click()
        return
    newPasswordAgainError = driver.find_elements(By.CSS_SELECTOR, "#id_error_newpassword2")
    if len(listPassword['errorField']) < 2:
      if "newpasswordAgain" in listPassword['errorField']:
        if listPassword['error'] in newPasswordAgainError[0].text:
          print('Pass')
          cancel.click()
          return
        print('Fail')
        cancel.click()
        return
    if len(listPassword['errorField']) == 2:
      check = 0
      if "newpassword" in listPassword['errorField']:
        if listPassword['error'] in newPasswordError[0].text:
          check += 1        
      if "newpasswordAgain" in listPassword['errorField']:
        if listPassword['error'] in newPasswordAgainError[0].text:
          check += 1
      if check == 2:
        print('Pass')
        cancel.click()
        return
      print('Fail')
      cancel.click()
  except :
    print('Fail')
    
def main():
  # create webdriver object
  driver = webdriver.Chrome()
  dataTest = data
  prepareData(driver)
  
  driver.get("http://localhost/")
  print('Test 1: ', end='')
  changPassword(driver, dataTest['passwordEmpty'])
  print('Test 2: ', end='')
  changPassword(driver, dataTest['passwordFail'])
  print('Test 3: ', end='')
  changPassword(driver, dataTest['newPasswordEmpty'])
  print('Test 4: ', end='')
  changPassword(driver, dataTest['newPasswordInvalid'])
  print('Test 5: ', end='')
  changPassword(driver, dataTest['newPasswordAgainEmpty'])
  print('Test 6: ', end='')
  changPassword(driver, dataTest['newPasswordAgainFail'])
  
if __name__ == '__main__':
  main()