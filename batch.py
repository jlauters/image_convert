import os
from subprocess import call

# Get Images from directory
#
# For Simplicity I would structure this so that you have
# ( ~ == home directory )
# ~/python_apps/img_convert/images/
# Where this file lives at
# ~/python_apps/img_convert/batch.py

img_path = 'images/'

for filename in os.listdir(img_path):
  
  print "Filename: "
  print filename

  print "convert name: "
  print img_path + filename

  # Edit this to how you like, to change the "fixed" filename
  ret_code = call("convert " + img_path + filename + " -fuzz 42% -fill 'rgb(248,241,221)' -opaque red fixed/" + filename, shell=True)
  
  print "return code:"
  print ret_code
  
  
