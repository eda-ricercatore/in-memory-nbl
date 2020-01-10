#!/usr/local/bin/python3
###!/Users/zhiyang/anaconda3/bin/python3

"""
	This Python script is written by Zhiyang Ong to generate
		random signals/"processes" by calling pseudorandom number
		generators iteratively, using pseudorandom number
		generators (PRNG) from the Python Standard Library and
		other Python libraries.


	Synopsis:
	Generate random signals/"processes" in Python.

	This script can be executed as follows:
	./random_process_generator.py



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

# Module to generate pseudorandom numbers.
from random_process_models.pseudorandom_number_generator import prng



###############################################################
"""
	Module with methods that generate a digital random process,
		which consists of only "high" and/or "low" values, using
		the pseudorandom number generator from the Python
		Standard Library or other Python libraries.
"""
class rand_signal_generator:
	# (Static) variables.
	# Type of signal: bit-vector, BV.
	bv_signal = "bv"
	# Type of signal: random telegraph wave, RTW.
	rtw_signal = "rtw"
	# High and low values for a random telegraph wave, RTW.
	low_value_rtw = -1
	high_value_rtw = 1
	# High and low values for a bit vector (BV).
	low_value_bit_vector = 0
	high_value_bit_vector = 1
	# ============================================================
	##	Method to generate a discrete-time random signal/process
	#		for "n" values.
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
	#	@param n - number of discrete values used to represent the
	#				random signal/"process".
	#				Its default value is: 16.
	#	@return - Nothing.
	#	O(1) method.
	@staticmethod
	def gen_rand_signal_uniform_distributn(type_of_signal=rand_signal_generator.bv_signal, n=16):
		random_signal = []
		# Generate a random signal/"process" of n values.
		for x in range(n):
			"""
				###	TODO
				Check the output of psl_uniform(type_of_signal)
					complies with specifications, as an assertion.
			"""
			random_signal.append(psl_uniform(type_of_signal))
		"""
			###	TODO
			Check the random signal/"process" complies with
				specifications, as a postcondition.
		"""
	# ============================================================
	##	Method to generate a discrete-time random signal/process
	#		for "n" values.
	#
	#	Use the Python Standard Library's random module to call the
	#		random.getrandbits(k) function that is based on the
	#		MersenneTwister generator (or some other generators).
	#
	#	For the generated bit-vector (bv), it has a:
	#	- high value: "1"
	#	- low value: "0"
	#
	#	@param n - number of discrete values used to represent the
	#				random signal/"process".
	#				Its default value is: 16.
	#	@return - Nothing.
	#	O(1) method.
	@staticmethod
	def gen_bit_vector_getrandbits(n=16):
		return random.getrandbits(n)





