dataPreCondition = {
  "coursesParticipate": [
    {
      'courseName': 'Kiểm tra phần mềm',
      'courseId': 'CO3015'
    },
    {
      'courseName': 'Hệ quản trị cơ sở dữ liệu',
      'courseId': 'CO3021'
    }
  ],
  "coursesNoParticipate": [
    {
      'courseName': 'Kỹ thuật lập trình',
      'courseId': 'CO1027'
    }
  ],
  "users":[{
    "username": "testcourse1", 
    "password": "Test@001", 
    "firstname": "Trần", 
    "surname": "Nguyễn", 
    "email": "testcourse1@gmail.com"
  }]
}

data = {
  "testByHome" : {
    'courseName': 'Kiểm tra phần mềm',
    'courseId': 'CO3015',
    'expect': 'success',
    'message': ''
  },
  "testByMyCourses" : {
    'courseName': 'Kiểm tra phần mềm',
    'courseId': 'CO3015',
    'expect': 'success',
    'message': ''
  },
  "testByMyCoursesFilter" : {
    'courseName': 'Kiểm tra phần mềm',
    'courseId': 'CO3015',
    'expect': 'success',
    'message': ''
  },
  "testByHomeNotJoin" : {
    'courseName': 'Kỹ thuật lập trình',
      'courseId': 'CO1027',
    'expect': 'error',
    'message': 'You cannot enrol yourself in this course.'
  }
}