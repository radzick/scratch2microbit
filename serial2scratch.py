#!/usr/bin/python
# --------------------------------------
# radzick 24-12-2016
#
# works only with Scratch 1.4
# --------------------------------------
# requirements:
# - scratchpy
# - pyserial
# --------------------------------------
# installation:
# $ easy_install-x.y pyserial
# $ pip install pyserial
# --------------------------------------
# usefull stuff:
# - https://pxt.microbit.org
# - https://github.com/pilliq/scratchpy
# - https://microbit-micropython.readthedocs.io
# - https://pythonhosted.org/pyserial
# - https://github.com/mu-editor/mu
# - enter microbit console:
#   $ python -m serial.tools.miniterm <>
# --------------------------------------

import scratch
import serial
import sys

# get the port location from arguments list
COM_PORT = sys.argv[1]
print('debug: com port = ' + repr(COM_PORT))

# init scratch connection & serve exceptions
scr = scratch.Scratch()
scr.broadcast('init scratch')
print('debug: scratch is on')

# init serial connections & serve exceptions
ser = serial.Serial(COM_PORT, 115200, bytesize=8, parity='N', stopbits=1, timeout=None)
if ser.is_open != True:
    ser.open()
ser.flushInput() 	#flush input buffer, discarding all its contents
ser.flushOutput()	#flush output buffer, aborting current output
print('debug: serial_open = ' + repr(ser.is_open))

# receive message(s) from scratch
def listen2scratch():
    i = 10
    while i > 0:
        try:
           yield scr.receive()
           i = i - 1
        except scratch.ScratchError:
           raise StopIteration

# receive message(s) from serial
def listen2serial():
    while ser.in_waiting > 0:
        try:
           yield ser.readline()
        except serial.SerialException:
           raise StopIteration

# main loop
while True:
    # parse messages from serial to scratch
    for ser_msg in listen2serial():
		print('debug: ' + ser_msg)
		# use only the first letter to drive scratch
		scr.broadcast(repr(ser_msg[0]))
