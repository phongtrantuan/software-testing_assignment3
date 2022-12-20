dataPreCondition={
  "usersCreated":[
    {
      "username": "testupload", 
      "password": "Test@001", 
      "firstname": "Trần", 
      "surname": "Nguyễn",
      "email": "testupload1@gmail.com"
    }
  ]
}

data = {
  "moreOne_FailFormat" : {
    "links": ["pdf1.pdf","pdf2.pdf"],
    "expect": "error",
    "message": "You are allowed to attach a maximum of 1 file(s) to this item"
  },
  "moreOne_TrueFailFormat" : {
    "links": ["pdf1.pdf","image1.png"],
    "expect": "error",
    "message": "You are allowed to attach a maximum of 1 file(s) to this item"
  },
  "moreOne_TrueFormat" : {
    "links": ["image1.png","image2.png"],
    "expect": "error",
    "message": "You are allowed to attach a maximum of 1 file(s) to this item"
  },
  "One_FailFormat" : {
    "links": ["pdf2.pdf"],
    "expect": "error",
    "message": "PDF document filetype cannot be accepted."
  },
  "One_TrueFormat" : {
    "links": ["image1.png"],
    "expect": "success",
    "message": ""
  }
}