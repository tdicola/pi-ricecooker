# Raspberry Pi Rice Cooker
### Tony DiCola (tony@tonydicola.com)

## Requirements

To run the raspberry pi rice cooker code you must have the following installed on your raspberry pi:
* Python 2.7
* [Flask](http://flask.pocoo.org/)
* [RPi.GPIO](https://pypi.python.org/pypi/RPi.GPIO)
* Photocell hooked up to pin 18, as per this [Adafruit tutorial](http://learn.adafruit.com/basic-resistor-sensor-reading-on-raspberry-pi/overview)

If all the requirements are satisfied, copy the files to a directory on your pi and run the server with the following command:
`sudo python server.py`

From a web browser access http://<ip of your raspberry pi>:5000/ to see the rice cooker status.

## Acknowledgements

The raspberry pi rice cooker is possible with help from:
* [Raspberry Pi](http://www.raspberrypi.org/)
* [Flask](http://flask.pocoo.org/)
* [RPi.GPIO](https://pypi.python.org/pypi/RPi.GPIO)
* [Adafruit Raspberry Pi Tutorials](http://learn.adafruit.com/category/raspberry-pi)
* [Bootstrap](http://getbootstrap.com/)
* [jQuery](http://jquery.com/)
* [flot](http://www.flotcharts.org/)
* [HTML5 Boilerplate](http://html5boilerplate.com/)