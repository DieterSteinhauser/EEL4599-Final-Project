# EEL4599 Final Project
 

Dieter Steinhauser, Sean McNeil and Lucas Mueller.

EEL4599 Wireless Communications

4/2023

## Dependencies

None


<p  align="center">
<img src="images\fsm.png" alt="Assembled Sensor Circuit" title="">

## Abstract


Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

## Background 

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

<p  align="center">
<img src="Schematics\schematic_block.png" alt="Circuit Block Diagram" title="">

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

## Circuit Design

### Local Circuit
<p  align="center">
<img src="Schematics\local_schematic.png" alt="Local Schematic" title="">

### Remote Circuit 1 & 2 (Configured Identically)
<p  align="center">
<img src="Schematics\remote_schematic_1.png" alt="Remote 1 Schematic" title="">


##  XCTU Configuration

The XBee devices are either transmitters or a receiver.
 
The transmitters are configured to send API data without escapes [1]. They are configured to send and receieve UART data via their Tx and Rx pins at a baud rate of 9600.
 
The receiver is configured to receive API data without escapes [1]. It is configured to send and receieve UART data via its Tx and Rx pins at a baud rate of 9600.

## Arduino Configuration
 
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
 

## Raspberry Pi Configuration

Inputs: Sink XBee device, Ultrasonic Sensor 1 and 2
Outputs: Thingspeak, Green/Yellow/Red LED, Speaker

The raspberry pi uses a python script to receieve and interpret data from the xbee device. the data from the xbee is sent via the UART Tx and Rx pins on the pi, with a baud rate of 9600. The pi separates the data by id and parses the data being recieved. If the carbon monoxide data reaches a preset theshold, audio will play from the connected speaker to signify danger.

The raspberry pi also receieves data from two ultrasonic sensors via the GPIO pins. the pi uses a python script to interpret the data and control the three LEDS - green, yellow, and red - depending on how close the car is to the sensor. The green LED will is lit until the car reaches a intermediate threshold. After that, the yellow LED is lit, and once the car passes the last threshold, the red LED will light up to let the driver know to stop.

The Raspberry Pi uses:
- the digi-xbee library (pip install digi-xbee) to interact with the xbee device
- the http.client and urllib libraries to send data to thingspeak
- the pygame library to output sound to the speaker
