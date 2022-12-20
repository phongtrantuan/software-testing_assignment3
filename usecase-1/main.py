from selenium import webdriver
from selenium.webdriver.support.ui import Select
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
  
  dataCourses = dataPreCondition['coursesParticipate']
  dataCoursesNoParticipate = dataPreCondition['coursesNoParticipate']
  dataUsers = dataPreCondition['users']
  
  for course in dataCourses:
    addCourse(driver, course)
  
  for user in dataUsers:
    addAccount(driver, user)
  
  for course in dataCourses:
    addUserToCourse(driver, dataUsers[0], course)
    
  for course in dataCoursesNoParticipate:
    addCourse(driver, course)
    
  logout(driver)
    
  login(driver, dataUsers[0]['username'], dataUsers[0]['password'])
    
    

def ViewCourseByHome(driver, course):
  try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//li[@data-key='home']")))
    Home = driver.find_element(By.XPATH, "//li[@data-key='home']")
    Home.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@class='aalink']")))
    listCourse = driver.find_elements(By.XPATH, "//a[@class='aalink']")
    for courseItem in listCourse:
      if courseItem.text == course['courseName']:
        courseItem.click()
        closeBg(driver)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.nav-link.active.active_tree_node")))
        navActive = driver.find_elements(By.CSS_SELECTOR, "a.nav-link.active.active_tree_node")
        if len(navActive) > 0 and course['expect'] == 'success':
          print("Pass")
          return
        print("Fail")
        return
  except:
    print("Fail")

def ViewCourseByHomeNotJoin(driver, course):
  try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//li[@data-key='home']")))
    Home = driver.find_element(By.XPATH, "//li[@data-key='home']")
    Home.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@class='aalink']")))
    listCourse = driver.find_elements(By.XPATH, "//a[@class='aalink']")
    for courseItem in listCourse:
      if courseItem.text == course['courseName']:
        courseItem.click()
        closeBg(driver)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#notice")))
        notice = driver.find_element(By.CSS_SELECTOR, "#notice")
        if course['expect'] == 'error' and notice.text == course['message']:
          print("Pass")
          return
        print("Fail")
        return
  except:
    print("Fail")

def ViewCourseByMyCourses(driver, course):
  try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//li[@data-key='mycourses']")))
    MyCourses = driver.find_element(By.XPATH, "//li[@data-key='mycourses']")
    MyCourses.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[@class='multiline']")))
    listCourse = driver.find_elements(By.XPATH, "//span[@class='multiline']")
    for courseItem in listCourse:
      if courseItem.text == course['courseName']:
        courseItem.click()
        closeBg(driver)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.nav-link.active.active_tree_node")))
        navActive = driver.find_elements(By.CSS_SELECTOR, "a.nav-link.active.active_tree_node")
        if len(navActive) > 0 and course['expect'] == 'success':
          print("Pass")
          return
        print("Fail")
        return
  except:
    print("Fail")

def ViewCourseByMyCoursesFilter(driver, course):
  try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//li[@data-key='mycourses']")))
    MyCourses = driver.find_element(By.XPATH, "//li[@data-key='mycourses']")
    MyCourses.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[@class='multiline']")))
    SearchInput = driver.find_element(By.CSS_SELECTOR, "#searchinput")
    SearchInput.send_keys(course['courseName'])
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".searchbar .btn-clear .fa-times")))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[@class='multiline']")))
    try:
      WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, "//span[@class='multiline-none-view.none']")))
    except:
      pass
    listCourse = driver.find_elements(By.XPATH, "//span[@class='multiline']")
    for courseItem in listCourse:
      if courseItem.text == course['courseName']:
        courseItem.click()
        closeBg(driver)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.nav-link.active.active_tree_node")))
        navActive = driver.find_elements(By.CSS_SELECTOR, "a.nav-link.active.active_tree_node")
        if len(navActive) > 0 and course['expect'] == 'success':
          print("Pass")
          return
        print("Fail")
        return
  except:
    print("Fail")



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
  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.carousel-navigation-link.dropdown-item")))
  language = driver.find_element(By.CSS_SELECTOR, "a.carousel-navigation-link.dropdown-item")
  language.click()
  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div > div.items.h-100.overflow-auto > a:nth-child(1)")))
  languageEnglish = driver.find_element(By.CSS_SELECTOR, "div > div.items.h-100.overflow-auto > a:nth-child(1)")
  languageEnglish.click()
  
def logout(driver):
  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@id='user-menu-toggle']")))
  avatar = driver.find_element(By.XPATH, "//a[@id='user-menu-toggle']")
  avatar.click()
  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@class='dropdown-item']")))
  listManager = driver.find_elements(By.CSS_SELECTOR, "#carousel-item-main a.dropdown-item")
  logoutButton = listManager[len(listManager)-1]
  logoutButton.click()
  
  
def addUserToCourse(driver, user, course):
  siteCourse = driver.find_element(By.XPATH, "//a[@href='http://localhost/my/courses.php']")
  siteCourse.click()
  
  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@data-flexitour='backdrop']")))
  bgCourse = driver.find_element(By.XPATH, "//div[@data-flexitour='backdrop']")
  bgCourse.click()
  
  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[@class='multiline']")))
  listCourse = driver.find_elements(By.XPATH, "//span[@class='multiline']")
  for courseItem in listCourse:
    if courseItem.text == course['courseName']:
      courseItem.click()
      WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@data-flexitour='backdrop']")))
      bgCourse = driver.find_element(By.XPATH, "//div[@data-flexitour='backdrop']")
      bgCourse.click()
      WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//li[@data-key='participants']")))
      participants = driver.find_element(By.XPATH, "//li[@data-key='participants']")
      participants.click()
      WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//form[@id='enrolusersbutton-1']")))
      participantsEnrol = driver.find_element(By.XPATH, "//form[@id='enrolusersbutton-1']")
      participantsEnrol.click()
      WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[@class='form-autocomplete-downarrow position-absolute p-1']")))
      participantsSearch = driver.find_element(By.XPATH, "//span[@class='form-autocomplete-downarrow position-absolute p-1']")
      participantsSearch.click()
      WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "li[role='option'] span small")))
      participantsSelect = driver.find_elements(By.CSS_SELECTOR, "li[role='option'] span small")
      for liParticipant in participantsSelect:
        if liParticipant.text == user['email']:
          liParticipant.click()
          break
      WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".badge.badge-secondary")))
      participantsAdd = driver.find_element(By.CSS_SELECTOR, ".modal-footer button.btn.btn-primary")
      participantsAdd.click()
      break
  

def clearCourse(driver, courseInput):
  # clear course have course's name
  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//li[@data-key='siteadminnode']")))
  adminSite = driver.find_element(By.XPATH, "//li[@data-key='siteadminnode']")
  adminSite.click()
  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@href='#linkcourses']")))
  adminCourse = driver.find_element(By.XPATH, "//a[@href='#linkcourses']")
  adminCourse.click()
  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@href='http://localhost/course/management.php']")))
  adminCourseManager = driver.find_element(By.XPATH, "//a[@href='http://localhost/course/management.php']")
  adminCourseManager.click()
  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@name='search'][@class='form-control']")))
  searchCourse = driver.find_element(By.XPATH, "//input[@name='search'][@class='form-control']")
  searchCourse.send_keys(courseInput['courseName'])
  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@class='btn  btn-primary search-icon'][@type='submit']")))
  searchButton = driver.find_element(By.XPATH, "//button[@class='btn  btn-primary search-icon'][@type='submit']")
  searchButton.click()
  try:
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".listitem-course a.coursename.aalink")))
    listCourseHaveId = driver.find_elements(By.CSS_SELECTOR, ".listitem-course a.coursename.aalink")
    index = -1
    for course in listCourseHaveId:
      index = index + 1
      if course.text == courseInput['courseName']:
        deleteCourse = driver.find_elements(By.XPATH, "//a[@class='action-delete']")
        deleteCourse[index].click();
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "form .btn.btn-primary")))
        deleteConfirm = driver.find_element(By.CSS_SELECTOR, value="form .btn.btn-primary")
        deleteConfirm.click()
        break
  except:
    pass
  
  # clear course have course's id
  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//li[@data-key='siteadminnode']")))
  adminSite = driver.find_element(By.XPATH, "//li[@data-key='siteadminnode']")
  adminSite.click()
  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@href='#linkcourses']")))
  adminCourse = driver.find_element(By.XPATH, "//a[@href='#linkcourses']")
  adminCourse.click()
  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@href='http://localhost/course/management.php']")))
  adminCourseManager = driver.find_element(By.XPATH, "//a[@href='http://localhost/course/management.php']")
  adminCourseManager.click()
  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@name='search'][@class='form-control']")))
  searchCourse = driver.find_element(By.XPATH, "//input[@name='search'][@class='form-control']")
  searchCourse.send_keys(courseInput['courseId'])
  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@class='btn  btn-primary search-icon'][@type='submit']")))
  searchButton = driver.find_element(By.XPATH, "//button[@class='btn  btn-primary search-icon'][@type='submit']")
  searchButton.click()
  try:
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//a[@class='action-edit']")))
    listCourseHaveId = driver.find_elements(By.XPATH, "//a[@class='action-edit']")
    index = -1
    for course in listCourseHaveId:
      index = index + 1
      course.click();
      WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@name='shortname']")))
      courseIdInput = driver.find_element(By.XPATH, "//input[@name='shortname']").get_attribute("value")
      if courseInput['courseId'] == courseIdInput:
        driver.back()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@class='action-delete']")))
        deleteCourse = driver.find_elements(By.XPATH, "//a[@class='action-delete']")
        deleteCourse[index].click();
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "form .btn.btn-primary")))
        deleteConfirm = driver.find_element(By.CSS_SELECTOR, value="form .btn.btn-primary")
        deleteConfirm.click()
        break
      driver.back()
  except:
    pass
  
def addCourse(driver, course):
  # clear course if it's id has existed
  clearCourse(driver, course)
  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//li[@data-key='siteadminnode']")))
  adminSite = driver.find_element(By.XPATH, "//li[@data-key='siteadminnode']")
  adminSite.click()
  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@href='#linkcourses']")))
  adminCourse = driver.find_element(By.XPATH, "//a[@href='#linkcourses']")
  adminCourse.click()
  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@href='http://localhost/course/edit.php?category=0']")))
  addCourse = driver.find_element(By.XPATH, "//a[@href='http://localhost/course/edit.php?category=0']")
  addCourse.click()
  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@name='fullname'][@id='id_fullname']")))
  addCourseName = driver.find_element(By.XPATH, "//input[@name='fullname'][@id='id_fullname']")
  addCourseName.send_keys(course["courseName"])
  addCourseId = driver.find_element(By.XPATH, "//input[@id='id_shortname']")
  addCourseId.send_keys(course["courseId"])
  addCourseSubmit = driver.find_element(By.XPATH, "//input[@type='submit'][@name='saveanddisplay']")
  addCourseSubmit.click()
  closeBg(driver)
  

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


def main():
  # create webdriver object
  driver = webdriver.Chrome()
  prepareData(driver)
  
  dataTest = data
  ViewCourseByHome(driver, dataTest['testByHome'])
  ViewCourseByMyCourses(driver, dataTest['testByMyCourses'])
  ViewCourseByMyCoursesFilter(driver, dataTest['testByMyCoursesFilter'])
  ViewCourseByHomeNotJoin(driver, dataTest['testByHomeNotJoin'])
  
if __name__ == '__main__':
  main()