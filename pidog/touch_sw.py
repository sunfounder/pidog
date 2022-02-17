#!/usr/bin/env python3
from robot_hat import Pin
from time import sleep

class TouchSW():
	def __init__ (self,sw1='D2',sw2='D3'):

		self.touch_1 = Pin(sw1)
		self.touch_2 = Pin(sw2)

	# def is_slide(self):
	# 	# print(self.touch_1.value(),self.touch_2.value())
	# 	if self.touch_1.value() == 0 and self.touch_2.value() == 1:
	# 		sleep(0.2)
	# 		if self.touch_2.value()== 0:
	# 			# print('Left slide')
	# 			return 'L'
	# 	elif self.touch_2.value() == 0 and self.touch_1.value() == 1 :
	# 		sleep(0.2)
	# 		if self.touch_1.value() == 0:
	# 			# print('Right slide')
	# 			return 'R'	

	# 	# print('no slide')	
	# 	return 'N'

	def is_slide(self):
		# print(self.touch_1.value(),self.touch_2.value())
		if self.touch_1.value() == 0:
			sleep(0.1)
			if self.touch_2.value()== 0:
				return 'LS'
			else:
				return 'L'
		elif self.touch_2.value() == 0:
			sleep(0.1)
			if self.touch_1.value() == 0:
				return 'RS'	
			else:
				return 'R'
		# if self.touch_1.value() == 0 or self.touch_2.value() == 0:
		# 	return 'P'

		return 'N'


if __name__ == "__main__":

	touch = TouchSW('D2','D3')

	while True:
		print(touch.touch_1.value(),touch.touch_2.value())
		print(touch.is_slide())
		sleep(0.05)
