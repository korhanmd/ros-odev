#! /usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String

def checkNum(num):
	try:
		val = int(num)
	except ValueError:
		return False
	return True

name = raw_input("Ad Soyad: ")

no = raw_input("Öğrenci Numarası: ")

while not checkNum(no):
	no = raw_input("Girdi sayı değil! Öğrenci numarası: ")

n_loop = int(no)%10

rospy.init_node('publisher')

pub = rospy.Publisher('assignment', String, queue_size=1)
rate = rospy.Rate(1)

c = 0

while c <= n_loop:
	pub.publish(name)
	c += 1
	rate.sleep()
