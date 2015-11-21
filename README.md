RaPi.GPIO README

RaPi.GPIO is a GPIO library that can support Banana Pro/Pi, Roseapple Pi. The API is the compatible with RPi.GPIO for Raspberry Pi. [RPi.GPIO](https://pypi.python.org/pypi/RPi.GPIO).

You can donwload the RaPi.GPIO from:
https://github.com/xapp-le/RaPi.GPIO.
## Support Hardware
    Banana Pro/Pi
    Roseapple Pi 

## Download
    git clone https://github.com/xapp-le/RaPi.GPIO

## Installation
    sudo apt-get update
    sudo apt-get install python-dev
    cd /RaPi.GPIO
    python setup.py install                 
    sudo python setup.py install
    
Please be attention that you need use both python and sudo pytohn to make the RaPi.GPIO work well.

## Remove
    cd /usr/local/lib/python2.7/dist-packages/
    sudo rm -r RaPi
    
Note that the RaPi library might be under /usr/lib/python2.7/dist-packages/, depending your system path setup. Remove the folder RaPi and the python egg info file.

## Extra
This version supports a new addressing mode "RAW" which enables you to use any GPIO pin. Below is an example which sets PD10 (which is pin 29 on the LCD connector) to a high level.

    import LMK.GPIO as GPIO
    GPIO.setmode(GPIO.RAW)
    GPIO.setup(GPIO.PD+10, GPIO.OUT)
    GPIO.output(GPIO.PD+10, 1)

## Examples
Under source/test directory, there are some examples.
D
D
D
D
D
D
under the source/test directory, there are some eaxmples for reference.
