# ValveAirFlow
A 3D model designed in solidworks, which is then programmed with python to control the flow of air through the tube via a servo motor. The servo motor responds to a switch and switches between two positions on click of the push button. The start and end point can be determined by using two potentiometers and the ADS1115 ADC converter, code is set up for this and the commented out duty lines just need to be commented in. Otherwise the two positions can also be set through the code directly and without the need for Potentiometers (No Changes need to be made to run the code like this).
If you want to use this with potentiometers just comment in Line 38/39 and line 52/53 and comment out lines 40 and 54.
If you would like any information on the electrical wiring please feel free to message/email me (almaasshah@gmail.com).
The ADC converter used is and ADS1115.
The pwm pin is BCM pin 18 and the input pin for the switch is ADC pin 27 for this specific code.
