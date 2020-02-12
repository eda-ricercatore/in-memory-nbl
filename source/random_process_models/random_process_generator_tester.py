#!/usr/local/bin/python3
###!/Users/zhiyang/anaconda3/bin/python3

"""
	This Python script is written by Zhiyang Ong to test the
		generator for random signals/"processes".


	Synopsis:
	Test the generator for random signals/"processes".

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

"""
	Package and module to print statistics of software testing
		results.
"""
from statistics_pkg.test_statistics import statistical_analysis
# Module to generate pseudorandom numbers.
from random_process_models.pseudorandom_number_generator import prng
# Module to generate random signals/"processes".
from random_process_models.random_process_generator import rand_signal_generator


###############################################################
##	Module that tests methods for random signal/"process" generation.
class rand_signal_generator_tester:
	## =========================================================
	#	Method to test the method that generates a discrete-time
	#		random signal/process for "n" values.
	#	@param - Nothing
	#	@return - Nothing.
	#	O(1) method.
	@staticmethod
	def test_gen_rand_signal_uniform_distributn():
		# Number of discrete values representing a random signal/"process".
		k = 16
		print("	Testing gen_rand_signal_uniform_distributn().")
		prompt = "	... Test: wrong type of signal.				{}"
		statistical_analysis.increment_number_test_cases_used()
		temp_rand_signal = rand_signal_generator.gen_rand_signal_uniform_distributn("whatever",k)
		if (k == len(temp_rand_signal)):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: type of signal = RTW.				{}"
		statistical_analysis.increment_number_test_cases_used()
		temp_rand_signal = rand_signal_generator.gen_rand_signal_uniform_distributn(rand_signal_generator.rtw_signal,k)
		"""
			Generated RTW signal of length k must have k
				values/digits.
			Each value/digit in the RTW signal should also be
				either -1 or 1 exclusively, and not any other
				value (e.g., 0, 1234, or 3.14).
		"""
		if (k == len(temp_rand_signal)) and ((-1 in temp_rand_signal) or (1 in temp_rand_signal)) and (not (0 in temp_rand_signal)) and (not (3.14 in temp_rand_signal)):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		"""
			Generated bit vector signal of length k must have k
				values/digits.
			Each value/digit in the bit vector should also be
				either 0 or 1 exclusively, and not any other
				value (e.g., 0, 1234, or 3.14).
		"""
		prompt = "	... Test: type of signal = bit vector.			{}"
		statistical_analysis.increment_number_test_cases_used()
		temp_rand_signal = rand_signal_generator.gen_rand_signal_uniform_distributn(rand_signal_generator.bv_signal,k)
		if (k == len(temp_rand_signal)) and ((0 in temp_rand_signal) or (1 in temp_rand_signal)) and (not (-1 in temp_rand_signal)) and (not (3.14 in temp_rand_signal)):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
	## =========================================================
	#	Method to test the method that generates a bit-vector
	#		-based discrete-time random signal/process for "n"
	#		values.
	#	@param - Nothing
	#	@return - Nothing.
	#	O(1) method.
	@staticmethod
	def test_gen_bit_vector_getrandbits():
		# Number of discrete values representing a random signal/"process".
		k = 8
		print("	Testing gen_rand_signal_uniform_distributn().")
		prompt = "	... Test: type of signal = bit vector.			{}"
		statistical_analysis.increment_number_test_cases_used()
		temp_rand_signal = rand_signal_generator.gen_bit_vector_getrandbits(k)
		if (k == len(temp_rand_signal)) and ((0 in temp_rand_signal) or (1 in temp_rand_signal)) and (not (-1 in temp_rand_signal)) and (not (3.14 in temp_rand_signal)):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
	## =========================================================
	#	Method to test the methods regarding random signal/"process".
	#	@param - Nothing
	#	@return - Nothing.
	#	O(1) method.
	@staticmethod
	def test_random_signal_generation_methods():
		print("")
		print("")
		print("==	Testing class: rand_signal_generator.")
		rand_signal_generator_tester.test_gen_rand_signal_uniform_distributn()
		rand_signal_generator_tester.test_gen_bit_vector_getrandbits()
