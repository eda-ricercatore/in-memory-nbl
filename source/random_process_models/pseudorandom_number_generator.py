#!/usr/local/bin/python3
###!/Users/zhiyang/anaconda3/bin/python3

"""
	This Python script is written by Zhiyang Ong to generate
		pseudorandom numbers deterministically in Python, using
		pseudorandom number generators (PRNG) from the Python
		Standard Library and other Python libraries.


	Synopsis:
	Generate pseudorandom numbers in Python.

	This script can be executed as follows:
	./pseudorandom_number_generator.py



	Revision History:
	September 6, 2019			Version 0.1	Script.
"""

__author__ = 'Zhiyang Ong'
__version__ = '1.0'
__date__ = 'September 6, 2019'

#	The MIT License (MIT)

#	Copyright (c) <2019> <Zhiyang Ong>

#	Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

#	The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

#	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

#	Email address: echo "cukj -wb- 23wU4X5M589 TROJANS cqkH wiuz2y 0f Mw Stanford" | awk '{ sub("23wU4X5M589","F.d_c_b. ") sub("Stanford","d0mA1n"); print $5, $2, $8; for (i=1; i<=1; i++) print "6\b"; print $9, $7, $6 }' | sed y/kqcbuHwM62z/gnotrzadqmC/ | tr 'q' ' ' | tr -d [:cntrl:] | tr -d 'ir' | tr y "\n"	Che cosa significa?


###############################################################
"""
	Import modules from the Python Standard Library.
	sys			Get access to any command-line arguments.
	os			Use any operating system dependent functionality.
	os.path		For pathname manipulations.

	subprocess -> call
				To make system calls.
	time		To measure elapsed time.
	warnings	Raise warnings.
	re			Use regular expressions.

	pathlib->Path
				For mapping a string to a path.
	datetime	To obtain information about the current date and time.
	time		To obtain information about the current time.
				time_ns version provides information about the
					current time with nanosecond accuracy.
	warnings	Provide warnings to users without terminating the
					program abruptly.
	random		For pseudorandom number generation.
"""

import sys
import os
import os.path
#from pathlib import Path
from subprocess import call
import time
import warnings
import re
import datetime
import random

###############################################################
#	Import Custom Python Packages and Modules






###############################################################
"""
	Module with methods that generate a "high" or "low" value
		for a digital random process, using the pseudorandom
		number generator from the Python Standard Library.
"""
class prng:
	# (Static) variables.
	# Type of signal: bit-vector, BV.
	bv_signal = "bv"
	# Type of signal: random telegraph wave, RTW.
	rtw_signal = "rtw"
	"""
		Default number for arbitrating a given pseudorandom number
			into a high value (i.e., "1") or a low value (i.e., "-1")
			for a random telegraph wave (RTW).
		The RTW arbiter shall use this value to determine if the
			generated pseudorandom number implies a high or low value
			for a RTW.
	"""
	rtw_arbitration_value = 0.0
	"""
		Default number for arbitrating a given pseudorandom number
			into a high value (i.e., "1") or a low value (i.e., "0")
			for a bit-vector (BV, i.e., boolean array/list).
		The bit-vector arbiter shall use this value to determine
			if the generated pseudorandom number implies a high or
			low value for a bit-vector.
	"""
	bit_vector_arbitration_value = 0.5
	# High and low values for a RTW.
	low_value_rtw = -1
	high_value_rtw = 1
	# High and low values for a bit vector.
	low_value_bit_vector = 0
	high_value_bit_vector = 1
	# ============================================================
	##	Method to generate a value for a random signal/process.
	#
	#	Use the Python Standard Library's random module to call the
	#		uniform function that is a PRNG based on a uniform
	#		distribution.
	#
	#	@param type_of_signal - Indicates if either of the following
	#				random signals (or random "processes") are used.
	#				* rtw, for a random telegraph wave
	#					- high value: "1"
	#					- low value: "-1"
	#				* bv, for a bit-vector
	#					- high value: "1"
	#					- low value: "0"
	#	@return - Nothing.
	#	O(1) method.
	@staticmethod
	def psl_uniform(type_of_signal="bv"):
		# Is the selected random signal/process a RTW?
		if type_of_signal == rtw_signal:
			"""
				Yes.
				Shall the generated pseudorandom number arbitrated
					to a high or low value?
			"""
			if random.uniform(low_value_rtw,high_value_rtw) >= rtw_arbitration_value:
				return high_value_rtw
			else:
				return low_value_rtw
		else:
			"""
				No. The random signal/process is treated as
					a bit vector by default.
				Shall the generated pseudorandom number arbitrated
					to a high or low value?
			"""
			if random.uniform(low_value_bit_vector,high_value_bit_vector) >= bit_vector_arbitration_value:
				return high_value_bit_vector
			else:
				return low_value_bit_vector


