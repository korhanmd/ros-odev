#! /usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String

name = "Korhan Mutludogan"
no = 501831001

n_loop = no%10

rospy.init_node('publisher')

pub = rospy.Publisher('assignment', String, queue_size=1)
rate = rospy.Rate(1)

c = 0

while c <= n_loop:
	pub.publish(name)
	c += 1
	rate.sleep()
