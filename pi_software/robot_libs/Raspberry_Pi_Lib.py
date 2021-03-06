#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" This module is used for Raspberry Pi Specific functions and classes"""
#
# Copyright (c) 2021 Rob Probin.
# All original work.
#
# This is licensed under the MIT License. Please see LICENSE.

import os

RPI_file = "/sys/firmware/devicetree/base/model"

def is_raspberry_pi():
	"""
	Checks a specific file to see this is likely to be a Raspberry Pi.
	Assumes you've checked Linux with sys.platform.
	:return: True is file looks like a Raspberry Pi
	""" 
	if os.path.isfile(RPI_file):
		f = open(RPI_file, "r")
		data = f.read()
		f.close()
		if data.find("Raspberry") != -1:
			return True
	return False

