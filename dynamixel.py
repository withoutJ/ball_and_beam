# This example shows how to use the dynamixel AX-12A motor

port_name = 'COM4'

import serial

ser = serial.Serial(port_name, baudrate=1000000)

ref_position = 512
min_position = ref_position - 100
max_position = ref_position + 100

def set_position(pos):
	if pos < min_position: pos = min_position
	if pos > max_position: pos = max_position
	pos_l = pos & 0xff
	pos_h = pos >> 8
	header = [255, 255]
	msg = [1, 5, 3, 30, pos_l, pos_h]
	chkSum = [(~sum(msg)) & 0xff]
	instruction_packet = header + msg + chkSum
	ser.write(bytes(instruction_packet))

def set_speed(spd):
	spd_l = spd & 0xff
	spd_h = spd >> 8
	header = [255, 255]
	msg = [1, 5, 3, 32, spd_l, spd_h]
	chkSum = [(~sum(msg)) & 0xff]
	instruction_packet = header + msg + chkSum
	ser.write(bytes(instruction_packet))

set_position(512)