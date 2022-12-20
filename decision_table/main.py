from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
import os
from dotenv import *
from data import *

# CODE JS
JS_DROP_FILES = "var k=arguments,d=k[0],g=k[1],c=k[2],m=d.ownerDocument||document;for(var e=0;;){var f=d.getBoundingClientRect(),b=f.left+(g||(f.width/2)),a=f.top+(c||(f.height/2)),h=m.elementFromPoint(b,a);if(h&&d.contains(h)){break}if(++e>1){var j=new Error('Element not interactable');j.code=15;throw j}d.scrollIntoView({behavior:'instant',block:'center',inline:'center'})}var l=m.createElement('INPUT');l.setAttribute('type','file');l.setAttribute('multiple','');l.setAttribute('style','position:fixed;z-index:2147483647;left:0;top:0;');l.onchange=function(q){l.parentElement.removeChild(l);q.stopPropagation();var r={constructor:DataTransfer,effectAllowed:'all',dropEffect:'none',types:['Files'],files:l.files,setData:function u(){},getData:function o(){},clearData:function s(){},setDragImage:function i(){}};if(window.DataTransferItemList){r.items=Object.setPrototypeOf(Array.prototype.map.call(l.files,function(x){return{constructor:DataTransferItem,kind:'file',type:x.type,getAsFile:function v(){return x},getAsString:function y(A){var z=new FileReader();z.onload=function(B){A(B.target.result)};z.readAsText(x)},webkitGetAsEntry:function w(){return{constructor:FileSystemFileEntry,name:x.name,fullPath:'/'+x.name,isFile:true,isDirectory:false,file:function z(A){A(x)}}}}}),{constructor:DataTransferItemList,add:function t(){},clear:function p(){},remove:function n(){}})}['dragenter','dragover','drop'].forEach(function(v){var w=m.createEvent('DragEvent');w.initMouseEvent(v,true,true,m.defaultView,0,0,0,b,a,false,false,false,false,0,null);Object.setPrototypeOf(w,null);w.dataTransfer=r;Object.setPrototypeOf(w,DragEvent.prototype);h.dispatchEvent(w)})};m.documentElement.appendChild(l);l.getBoundingClientRect();return l"

def drop_files(element, files, offsetX=0, offsetY=0):
    driver = element.parent
    isLocal = not driver._is_remote or '127.0.0.1' in driver.command_executor._url
    paths = []
    
    # ensure files are present, and upload to the remote server if session is remote
    for file in (files if isinstance(files, list) else [files]) :
        if not os.path.isfile(file) :
            raise FileNotFoundError(file)
        paths.append(file if isLocal else element._upload(file))
    
    value = '\n'.join(paths)
    elm_input = driver.execute_script(JS_DROP_FILES, element, offsetX, offsetY)
    elm_input._execute('sendKeysToElement', {'value': [value], 'text': value})

WebElement.drop_files = drop_files

def prepareData(driver):
  driver.get("http://localhost/")
  driver.maximize_window()
  usersCreated = dataPreCondition['usersCreated']

  env = dotenv_values(".env")
  username_login = env["usernameAdmin"] 
  password_login = env["passwordAdmin"]
  login(driver, username_login, password_login)
  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@id='user-menu-toggle']")))
  avatar = driver.find_element(By.XPATH, "//a[@id='user-menu-toggle']")
  avatar.click()
  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.carousel-navigation-link.dropdown-item")))
  language = driver.find_element(By.CSS_SELECTOR, "a.carousel-navigation-link.dropdown-item")
  language.click()
  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div > div.items.h-100.overflow-auto > a:nth-child(1)")))
  languageEnglish = driver.find_element(By.CSS_SELECTOR, "div > div.items.h-100.overflow-auto > a:nth-child(1)")
  languageEnglish.click()
  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//li[@data-key='siteadminnode']")))
  adminSite = driver.find_element(By.XPATH, "//li[@data-key='siteadminnode']")
  adminSite.click()
  
  for user in usersCreated:
    addAccount(driver, user)
  

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
  bgCourse = driver.find_elements(By.XPATH, "//div[@data-flexitour='backdrop']")
  if len(bgCourse) > 0:
    bgCourse[0].click()
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

def uploadImage(driver, imagesInput):
  try: 
    driver.get("http://localhost/")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@id='user-menu-toggle']")))
    avatar = driver.find_element(By.XPATH, "//a[@id='user-menu-toggle']")
    avatar.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@href='http://localhost/user/profile.php']")))
    profile = driver.find_element(By.XPATH, "//a[@href='http://localhost/user/profile.php']")
    profile.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "li.editprofile span a")))
    editProfile = driver.find_element(By.CSS_SELECTOR, "li.editprofile span a")
    editProfile.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".fp-btn-add .btn.btn-secondary")))
    
    dragProfileAvatar = driver.find_element(By.CSS_SELECTOR, ".fm-empty-container .dndupload-arrow.d-flex")
    # wait two second
    try:
      WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".fp-btn-add.btn.fail.btn-secondary-no-check")))
    except:
      pass
    
    listPath = []
    for link in imagesInput['links']:
      listPath.append(os.path.join(os.getcwd(), link))
    dragProfileAvatar.drop_files(listPath)
    if len(imagesInput['links']) == 1:
      if imagesInput['expect'] == 'error':
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#fp-msg-labelledby")))
        textError = driver.find_element(By.CSS_SELECTOR, "#fp-msg-labelledby").text
        if textError == imagesInput['message']:
          print('Pass')
          return
      if imagesInput['expect'] == 'success':
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".fp-filename-field .fp-filename")))
        fileName = driver.find_element(By.CSS_SELECTOR, ".fp-filename-field .fp-filename").text
        if fileName == imagesInput['links'][0]:
          print('Pass')
          return
      print('Fail')
      return
    if len(imagesInput['links']) > 1:
      if imagesInput['expect'] == 'error':
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#fp-msg-labelledby")))
        textError = driver.find_element(By.CSS_SELECTOR, "#fp-msg-labelledby").text
        if textError == imagesInput['message']:
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
  
  uploadImage(driver, dataTest['moreOne_FailFormat'])
  uploadImage(driver, dataTest['moreOne_TrueFailFormat'])
  uploadImage(driver, dataTest['moreOne_TrueFormat'])
  uploadImage(driver, dataTest['One_FailFormat'])
  uploadImage(driver, dataTest['One_TrueFormat'])
    
  
if __name__ == '__main__':
  main()