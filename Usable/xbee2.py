# Copyright 2017, Digi International Inc.
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

from digi.xbee.devices import XBeeDevice
import parse
import ultrasonic_module as us

# TODO: Replace with the serial port where your local module is connected to.
PORT = "/dev/serial0"
# TODO: Replace with the baud rate of your local module.
BAUD_RATE = 9600


def main(sensor1, sensor2):
    print(" +-----------------------------------------+")
    print(" | XBee Python Library Receive Data Sample |")
    print(" +-----------------------------------------+\n")

    device = XBeeDevice(PORT, BAUD_RATE)

    try:
        device.open()

        def data_receive_callback(xbee_message):
            print("From %s >> %s" % (xbee_message.remote_device.get_64bit_addr(),
                                     xbee_message.data.decode()))
            parse.parseID(xbee_message.remote_device.get_64bit_addr(), xbee_message.data.decode())
            print(f'sensor 1 data: {sensor1.distance()}')
            print(f'sensor 2 data: {sensor2.distance()}')
            #print(sensor1.distance())
            
        device.add_data_received_callback(data_receive_callback)

        print("Waiting for data...\n")
        input()
        

    finally:
        if device is not None and device.is_open():
            device.close()


if __name__ == '__main__':
    sensor1 = us.sensor(18, 17)
    sensor2 = us.sensor(23, 22)
    main(sensor1, sensor2)
