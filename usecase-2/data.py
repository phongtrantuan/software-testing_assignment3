dataPreCondition = {
  "usersCreated":[
    {
      "username": "testuser1", 
      "password": "Test@001", 
      "firstname": "Trần", 
      "surname": "Nguyễn",
      "email": "testuser1@gmail.com"
    }
  ],
  "usersAdd":[
    {
      "username": "testuser2", 
      "password": "Test@001", 
      "firstname": "Trần", 
      "surname": "Nguyễn",
      "email": "testuser2@gmail.com"
    },
    {
      "username": "testuser3", 
      "password": "Test@001", 
      "firstname": "Trần", 
      "surname": "Nguyễn",
      "email": "testuser3@gmail.com"
    },
    {
      "username": "testuser4", 
      "password": "Test@001", 
      "firstname": "Trần", 
      "surname": "Nguyễn",
      "email": "testuser4@gmail.com"
    },
    {
      "username": "testuser5", 
      "password": "Test@001", 
      "firstname": "Trần", 
      "surname": "Nguyễn",
      "email": "testuser5@gmail.com"
    },
    {
      "username": "testuser6", 
      "password": "Test@001", 
      "firstname": "Trần", 
      "surname": "Nguyễn",
      "email": "testuser6@gmail.com"
    },
    {
      "username": "testuser7", 
      "password": "Test@001", 
      "firstname": "Trần", 
      "surname": "Nguyễn",
      "email": "testuser7@gmail.com"
    },
    {
      "username": "testuser8", 
      "password": "Test@001", 
      "firstname": "Trần", 
      "surname": "Nguyễn",
      "email": "testuser8@gmail.com"
    },
    {
      "username": "testuser9", 
      "password": "Test@001", 
      "firstname": "Trần", 
      "surname": "Nguyễn",
      "email": "testuser9@gmail.com"
    },
    {
      "username": "testuser10", 
      "password": "Test@001", 
      "firstname": "Trần", 
      "surname": "Nguyễn",
      "email": "testuser10@gmail.com"
    },
    {
      "username": "testuser11", 
      "password": "Test@001", 
      "firstname": "Trần", 
      "surname": "Nguyễn",
      "email": "testuser11@gmail.com"
    }
  ]
}

data = {
  "dataInputTrue": {
    "username": "testuser2", 
    "password": "Test@001", 
    "firstname": "Trần", 
    "surname": "Nguyễn",
    "email": "testuser2@gmail.com",
    "fieldError": [],
    "message": "",
    "indexDataTrue": "2"
  },
  "dataInputLackFirstname": {
    "username": "testuser3", 
    "password": "Test@001", 
    "firstname": "", 
    "surname": "Nguyễn",
    "email": "testuser3@gmail.com",
    "fieldError": ["firstname"],
    "message": "Missing given name",
    "indexDataTrue": "3"
  },
  "dataInputLackSurname": {
    "username": "testuser4", 
    "password": "Test@001", 
    "firstname": "Trần", 
    "surname": "",
    "email": "testuser4@gmail.com",
    "fieldError": ["surname"],
    "message": "Missing surname",
    "indexDataTrue": "4"
  },
  "dataInputLackEmail": {
    "username": "testuser5", 
    "password": "Test@001", 
    "firstname": "Trần", 
    "surname": "Nguyễn",
    "email": "",
    "fieldError": ["email"],
    "message": "Required",
    "indexDataTrue": "5"
  },
  "dataInputEmailInvalid": {
    "username": "testuser6", 
    "password": "Test@001", 
    "firstname": "Trần", 
    "surname": "Nguyễn",
    "email": "abc",
    "fieldError": ["email"],
    "message": "Invalid email address",
    "indexDataTrue": "6"
  },
  "dataInputEmailExisted": {
    "username": "testuser7", 
    "password": "Test@001", 
    "firstname": "Trần", 
    "surname": "Nguyễn",
    "email": "testuser1@gmail.com",
    "fieldError": ["email"],
    "message": "This email address is already registered.",
    "indexDataTrue": "7"
  },
  "dataInputUsernameExisted": {
    "username": "testuser1", 
    "password": "Test@001", 
    "firstname": "Trần", 
    "surname": "Nguyễn",
    "email": "testuser8@gmail.com",
    "fieldError": ["username"],
    "message": "This username already exists, choose another",
    "indexDataTrue": "8"
  },
  "dataInputLackPassword": {
    "username": "testuser9", 
    "password": "", 
    "firstname": "Trần", 
    "surname": "Nguyễn",
    "email": "testuser9@gmail.com",
    "fieldError": ["password"],
    "message": "Required",
    "indexDataTrue": "9"
  },
  "dataInputPasswordInvalid1": {
    "username": "testuser10", 
    "password": "a", 
    "firstname": "Trần", 
    "surname": "Nguyễn",
    "email": "testuser10@gmail.com",
    "fieldError": ["password"],
    "message": """Passwords must be at least 8 characters long.
Passwords must have at least 1 digit(s).
Passwords must have at least 1 upper case letter(s).
The password must have at least 1 special character(s) such as as *, -, or #.""",
    "indexDataTrue": "10"
  },
  "dataInputPasswordInvalid2": {
    "username": "testuser11", 
    "password": "TEST@001", 
    "firstname": "Trần", 
    "surname": "Nguyễn",
    "email": "testuser11@gmail.com",
    "fieldError": ["password"],
    "message": "Passwords must have at least 1 lower case letter(s).",
    "indexDataTrue": "11"
  }
}