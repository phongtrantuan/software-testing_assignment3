data = {
  "dataMin-" : {
    "max": 0,
    "default": 1,
    "expect": "error",
    "result": "This setting must be an integer between 1 and 10000."
  },
  "dataMin" :{
    "max": 1,
    "default": 1,
    "expect": "success",
    "result": "Changes saved"
  },
  "dataMin+" :{
    "max": 2,
    "default": 1,
    "expect": "success",
    "result": "Changes saved"
  },
  "dataAverage" :{
    "max": 5000,
    "default": 1,
    "expect": "success",
    "result": "Changes saved"
  },
  "dataMax-" :{
    "max": 9999,
    "default": 1,
    "expect": "success",
    "result": "Changes saved"
  },
  "dataMax" :{
    "max": 10000,
    "default": 1,
    "expect": "success",
    "result": "Changes saved"
  },
  "dataMax+" :{
    "max": 10001,
    "default": 1,
    "expect": "error",
    "result": "This setting must be an integer between 1 and 10000."
  }
}