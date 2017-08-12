# scratch2microbit
A simple way to connect micro:bit to your Scratch applications.

# Requirements:
- Scratch 1.4 
- Python 2 
- micro:bit board

# Pre-installation:
- $ pip install pyserial
- $ pip install scratch

# Usage
- Enable "Remote sensors connection" in Scractch 
- Flash the micro:bit board with dispatch2serial.pxt (or your own derivation)
- Run python script serial2scratch.py
- Play you Scratch script!

# Usefull links:
- https://wiki.scratch.mit.edu/wiki/Remote_Sensor_Connections
- https://wiki.scratch.mit.edu/wiki/Remote_Sensors_Protocol
- https://pxt.microbit.org
- https://github.com/pilliq/scratchpy
- https://microbit-micropython.readthedocs.io
- https://pythonhosted.org/pyserial
- https://github.com/mu-editor/mu
- enter microbit console: $ python -m serial.tools.miniterm <>

If you want to use Scratch 2.0, please refer to http://scratchx.org, the extensions might be helpful!
