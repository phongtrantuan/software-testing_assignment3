dataPreCondition={
  "usersCreated":[
    {
      "username": "testpass", 
      "password": "Test@001", 
      "firstname": "Trần", 
      "surname": "Nguyễn",
      "email": "testpass1@gmail.com"
    }
  ]
}

data = {
  "passwordEmpty" : {
    "password": "",
    "newpassword": "Test@123",
    "newpasswordAgain": "Test@123",
    "errorField": ["password"],
    "error":"Required"
  },
  "passwordFail" : {
    "password": "abc",
    "newpassword": "Test@123",
    "newpasswordAgain": "Test@123",
    "errorField": ["password"],
    "error":"Invalid login, please try again"
  },
  "newPasswordEmpty" : {
    "password": "Test@001",
    "newpassword": "",
    "newpasswordAgain": "Test@123",
    "errorField": ["newpassword"],
    "error":"Required"
  },
  "newPasswordInvalid" : {
    "password": "Test@001",
    "newpassword": "abc",
    "newpasswordAgain": "abc",
    "errorField": ["newpassword", "newpasswordAgain"],
    "error":"""Passwords must be at least 8 characters long.
Passwords must have at least 1 digit(s).
Passwords must have at least 1 upper case letter(s).
The password must have at least 1 special character(s) such as as *, -, or #."""
  },
  "newPasswordAgainEmpty" : {
    "password": "Test@001",
    "newpassword": "Test@123",
    "newpasswordAgain": "",
    "errorField": ["newpasswordAgain"],
    "error":"Required"
  },
  "newPasswordAgainFail" : {
    "password": "Test@001",
    "newpassword": "Test@123",
    "newpasswordAgain": "Test@12",
    "errorField": ["newpassword", "newpasswordAgain"],
    "error":"These passwords do not match"
  }
}