import os

os.chdir("/usr/local/lib/python2.7/dist-packages/")
os.system("sudo rm RaPi.GPIO-0.0.1.egg-info")
os.system("sudo rm -r RaPi")

os.chdir("/home/rapi/RaPi.GPIO/")
os.system("python setup.py install")
os.system("sudo python setup.py install")

os.chdir("/home/rapi/RaPi.GPIO/test/")
os.system("sudo python led.py")
