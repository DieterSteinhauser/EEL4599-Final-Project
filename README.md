# EEL4599 Final Project
 

Dieter Steinhauser, Sean McNeil and Lucas Mueller.

EEL4599 Wireless Communications

4/2023

## Abstract

The Internet of Things (IoT) provides networks of interconnected devices for data exchange without human interference. Collecting and analyzing data in real-time enables many current and future microprocessor applications. The garage vehicle monitoring system incorporates IoT network systems to monitor carbon monoxide levels via a sensor module and transmit data to a central hub. The hub then uploads sensor data to ThingSpeak for analysis and notification of high CO levels. In addition to carbon monoxide, the system monitors car ports using ultrasonic sensors to simplify parking, alerting the user through a traffic light system. In this paper, we will explore the details of the garage vehicle monitoring system and how it incorporates IoT technology to improve safety and convenience. 

## Background 

<p  align="center">
<img src="Schematics\system operation diagram.drawio (1).png" alt="Circuit Block Diagram" title="">

Internet of Things (IoT) has revolutionized the way we interact with our surroundings, enabling devices to communicate without intervention. With the growth of IoT, new applications have emerged, transforming various industries. One such application is a garage vehicle monitoring system, integrating IoT technology to monitor carbon monoxide levels and parking spaces. This system uses a sensor module to detect carbon monoxide levels and transmit data to a central hub for interpretation and notification. Data is uploaded to ThingSpeak by the hub for CO data monitoring and analysis. Both local and remote alarms are activated upon arrival of unsafe CO levels. Additionally, the system uses ultrasonic sensors to monitor parking spaces, simplifying the parking process for users through a traffic light system.  

### Remote Circuit 1 & 2 (Configured Identically)
<p  align="center">
<img src="Schematics\remote_schematic_1.png" alt="Remote 1 Schematic" title="">

Our System accounts for two vehicles in a double car port garage. Remote devices are installed on the user's vehicle and draw 5V via USB. A remote device relies on an Arduino microprocessor and relays data to the central hub using a UART connected XBee. A carbon monoxide sensor, buzzer, and LEDs are also connected to the microprocessor for local data interpretation and preparation prior to XBee communication.  

### Local Circuit
<p  align="center">
<img src="Schematics\local_schematic.png" alt="Local Schematic" title="">

The central hub consists of a local XBee operating as a router for wireless transmissions. Additionally, this XBee is set in python API mode and configured through the Raspberry Pi. Once received data reaches the Pi, data is relayed to ThingSpeak and interpreted locally. Unsafe levels of carbon monoxide trigger the local alarm. The Pi has an audio amplifier connected to a speaker for a loud and effective alert. Ultrasonic sensors are connected to the Pi for distance data within the car port. Upon approach, the traffic light LED system indicates for the user to continue with green, slow down with yellow, and stop with red.  

##  XCTU Configuration

The XBee network is created using a single coordinator and two remote nodes, formatted in API mode. The network forming device requires a unique node identifier and defines the network ID and channel of communication for the entire system. Remote nodes also require unique identifiers and must share the network ID and channel with the coordinator for transmission. Sleep systems could also be employed at this stage. However, for debugging purposes it is best to avoid sleep cycles entirely. UART communication is developed using the DIN and DOUT pins on the XBee.  

The transmitters are configured to send API data without escapes [1]. They are configured to send and receieve UART data via their Tx and Rx pins at a baud rate of 9600.
 
The receiver is configured to receive API data without escapes [1]. It is configured to send and receieve UART data via its Tx and Rx pins at a baud rate of 9600.

## Arduino Configuration

The Arduinos are used to drive the remote modules in this project. For each of the two remote sensing modules, the following connections are made: All components are supplied power through the 3.3v and ground pins of the Arduino. To transmit data to the XBee two of the GPIO pins are used as TX and RX. This enables UART communication with the XBee. One of the Arduinos analog pins is used to receive data from the gas sensor. This data is then converted to digital with the microcontrollers onboard ADC. An additional 2 GPIO pins are used to control the piezo buzzer and LED indicators. 
 
In this project Arduino Uno boards were used in combination with a gas sensor, piezo speaker, LEDs, and an XBee device to operate the remote sensing modules. The program, written using the Arduino C++ library and uploaded to the Arduino board, configures the board in the following manner: analog data is read from the gas sensor and its value is used to determine the behavior of the piezo and an LED which act as audio and visual indicators when the carbon monoxide levels are unsafe. More specifically, when the carbon monoxide levels reach a dangerous concentration, the piezo will begin to play an 800Hz tone and the LED indicator will turn on. Using the software serial library, this data is then sent to the XBee using UART serial communication, the XBee then transmits this data to the base station. 
 

## Raspberry Pi Configuration

Inputs: Sink XBee device, Ultrasonic Sensor 1 and 2
Outputs: Thingspeak, Green/Yellow/Red LED, Speaker

The raspberry pi uses a python script to receieve and interpret data from the xbee device. the data from the xbee is sent via the UART Tx and Rx pins on the pi, with a baud rate of 9600. The pi separates the data by id and parses the data being recieved. If the carbon monoxide data reaches a preset theshold, audio will play from the connected speaker to signify danger.

The raspberry pi also receieves data from two ultrasonic sensors via the GPIO pins. the pi uses a python script to interpret the data and control the three LEDS - green, yellow, and red - depending on how close the car is to the sensor. The green LED will is lit until the car reaches a intermediate threshold. After that, the yellow LED is lit, and once the car passes the last threshold, the red LED will light up to let the driver know to stop.

The Raspberry Pi uses:
- the digi-xbee library (pip install digi-xbee) to interact with the xbee device
- the http.client and urllib libraries to send data to thingspeak
- the pygame library to output sound to the speaker
