# Arthrex_Assignment

# How to test the code:
  + First make sure that all files are inside single folder
  + Delete the demo.log file (optional)
  + Then open these folder in any python IDE
  + First run LoggerModule.py file and make sure everything works finely
  + Then run App.py file to generate logs
  + Check whether logs gets added in the demo.log file
  + Testing.py file is created for tetsing automation

# Approach used to solve the problem
  + First created a custom logger module using python's built in logging library
  +  change the level og logger to DEBUG
  +  created handler to handle demo.log file
  +  created formatter to generate log according to given format
  +  created two functions in App.py file, add and divide
  +  on calling these functions they generate logs and logs gets saved in demo.log file
  +  created testing.py file to automate testing 
