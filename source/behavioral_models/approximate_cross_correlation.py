#!/usr/local/bin/python3
###!/Users/zhiyang/anaconda3/bin/python3

"""
	This Python script is written by Zhiyang Ong to approximate
		cross-correlation to enable correlation-based machine
		learning.


	Synopsis:
	Approximate cross-correlation in Python.


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
# Module to generate random signals/"processes".
from random_process_models.random_process_generator import rand_signal_generator



###############################################################
"""
	Module with demonstrates how cross-correlation can be
		approximated, and implemented with in-memory computing.
"""
class approximate_cross_correlation:
	# ============================================================
	##	Method to demonstrate the generation and calculation of
	#		the cross correlation of RTW signals.
	#
	#	@param - None.
	#	@return - Nothing.
	#	O(1) method.
	@staticmethod
	def rtw_signal_generation_and_cross_correlation():
		# Number of discrete values for random signals/"processes".
		k=16
		# Generate a random signal of the type random telegraph wave (RTW).
		x_rtw_1 = rand_signal_generator.gen_rand_signal_uniform_distributn(rand_signal_generator.rtw_signal,k)
		print("x_rtw_1 is:",x_rtw_1,"=")
		# Generate another RTW.
		x_rtw_2 = rand_signal_generator.gen_rand_signal_uniform_distributn(rand_signal_generator.rtw_signal,k)
		# Find the cross-correlation between these two RTWs.




###############################################################
# Main method for the program.

#	If this is executed as a Python script,
if __name__ == "__main__":
	approximate_cross_correlation.rtw_signal_generation_and_cross_correlation()
