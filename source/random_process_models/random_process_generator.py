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
	#	@precondition - type_of_signal must belong to a supported
	#		type of signal.
	#		Default random process/signal type is: bit vector.
	#		Process unsupported random process/signal types as
	#			bit vectors.
	#	@assertion - Randomly generated values/digits to form
	#		the random process/signal must be a valid value for
	#		that random process/signal.
	#		E.g., each value/digital for a RTW signal is either
	#			a '-1' or a '1'.
	#		E.g., each value/digital for a bit vector is either
	#			a '0' or a '1'.
	#	@postcondition - Number of values/digits in the random
	#		process/signal is: "k".
	#	O(1) method.
	@staticmethod
	def gen_rand_signal_uniform_distributn(type_of_signal=bv_signal, n=16):
		"""
			Check if the type of the signal is supported.
			Is the type of the signal not a RTW signal?
		"""
		if type_of_signal != rand_signal_generator.rtw_signal:
			"""
				No. Make it a bit vector.
				Since the only types of supported signals are
					RTW signals and bit vectors, if a signal
					is not a RTW signal, it should be a bit
					vector.
				Treat all unsupported signals as a bit vector,
					which is the default signal type.
			"""
			type_of_signal = rand_signal_generator.bv_signal
		"""
			Initialize a 0-bit random signal that would be
				appended with randomly generated values/digits.
		"""
		random_signal = []
		# Generate a random signal/"process" of n values.
		for x in range(n):
			"""
				Checking for assertions.
				For specified type of random signal, is the
					generated pseudo-random number valid?
			"""
			random_value = prng.psl_uniform(type_of_signal)
			"""
				Is the random signal/process type a RTW signal
					with incorrect values?
			"""
			if (type_of_signal == rand_signal_generator.rtw_signal) and (not((-1 == random_value) or (1 == random_value))):
				# Yes. This value is not '-1' nor '1'.
				raise AssertionError("Values for RTW signals should only be '-1' or '1'.")
			#	Else, by default, treat it as a bit vector.
			#	Are its values are not '0' nor '1'?
			#	Triple "double quotes" (""") to demark block comments
			#		cause run-time interpretation problem.
			#	Hence, use single-line comments instead.
			elif (type_of_signal == rand_signal_generator.bv_signal) and (not((0 == random_value) or (1 == random_value))):
				# Yes, the value is not '0' nor '1'.
				raise AssertionError("Values for bit vectors should only be '0' or '1'.")
			#	Else, its values are correct for the specified
			#		type of random signal/process.
			#	Triple "double quotes" (""") to demark block comments
			#		cause run-time interpretation problem.
			#	Hence, use single-line comments instead.
			else:
				random_signal.append(random_value)
		"""
			Checking for postconditions.

			Does the length of the random signal match the number
				of specified values in the random signal?
		"""
		if n != len(random_signal):
			# No.
			raise AssertionError("Incorrect number of values generated to represent k-bit random signal.")
		"""
			Enumerate each value/digit in the random process/signal
				to determine if it is valid.
		"""
		for value_of_digit in random_signal:
			# Are the values/digits of a RTW signal '-1' or '1'?
			if (type_of_signal == rand_signal_generator.rtw_signal) and (not((-1 == value_of_digit) or (1 == value_of_digit))):
				# Yes. This value is not '-1' nor '1'.
				raise AssertionError("Values for RTW signals must be '-1' or '1'.")
			# Are the values/digits of a bit vector '0' or '1'?
			elif (type_of_signal == rand_signal_generator.bv_signal) and (not((0 == value_of_digit) or (1 == value_of_digit))):
				# Yes. This value is not '0' nor '1'.
				raise AssertionError("Values for bit vectors must be '0' or '1'.")
			elif (not (type_of_signal == rand_signal_generator.rtw_signal)) and (not (type_of_signal == rand_signal_generator.bv_signal)):
				print("!!!	type_of_signal is:",type_of_signal,".")
				raise AssertionError("Signal type is not supported.")
			"""
				Else, the currently enumerated value/digit of the
					signal is valid.
			"""
		return random_signal
	# ============================================================
	##	Method to generate a discrete-time random signal/process
	#		for "n" values, using another method from the random
	#		module of the Python Standard Library.
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






