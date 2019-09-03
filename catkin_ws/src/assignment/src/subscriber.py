#! /usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String

def callback(msg):
	rospy.loginfo(rospy.get_caller_id() + " I heard %s", msg.data)

rospy.init_node('subscriber')

sub = rospy.Subscriber('assignment', String, callback)

rospy.spin()