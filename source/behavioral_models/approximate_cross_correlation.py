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
#	Import Python Packages and Modules from Python Libraries
import numpy as np



###############################################################
"""
	Module with demonstrates how cross-correlation can be
		approximated, and implemented with in-memory computing.
"""
class approx_cross_correlation:
	# Modes for the NumPy correlate function
	numpy_correlate_mode_valid = "valid"	# Default option
	numpy_correlate_mode_same = "same"
	numpy_correlate_mode_full = "full"
	# List of modes for the NumPy correlate function
	numpy_correlate_modes = [numpy_correlate_mode_valid,numpy_correlate_mode_same,numpy_correlate_mode_full]
	# ============================================================
	##	Method to calculate the cross-correlation of two random
	#		signals, signal_x and signal_y.
	#
	#	@param signal_x - A random signal.
	#	@param signal_y - Another random signal.
	#	@return - The cross-correlation between signal_x and signal_y.
	#	O(1) method.
	@staticmethod
	def cross_correlation_using_numpy(signal_x=[],signal_y=[],mode=numpy_correlate_mode_same):
		return np.correlate(signal_x,signal_y,mode)
	# ============================================================
	##	Method to calculate the cross-correlation of two random
	#		signals, signal_x and signal_y, using all approaches
	#		that I learned.
	#
	#	The definitions for calculating cross-correlation for
	#		periodic/deterministic signals, stochastic/random
	#		and random processes can be found in the following
	#		publications:
	#		+ \cite{Chen2007c}
	#		+ \cite{Downey2015}
	#		+ \cite{Downey2011}
	#		+ \cite{Montgomery2014}
	#		+ \cite{Bertsekas2008}
	#		+ \cite{Grimmett2001}
	#		+ \cite{Ross2004}???
	#		+ \cite{Ross2010b}
	#
	#	There exists different implementations, among Python
	#		libraries, of functions to compute cross-correlation,
	#		and some implementations have different "modes";
	#		hence, there exists different definitions for
	#			calculating cross-correlation. 
	#
	#	There exists different implementations, among Python
	#		libraries, of functions to compute cross-correlation,
	#		and some implementations have different "modes";
	#		hence, there exists different definitions for
	#			calculating cross-correlation. 
	#
	#	@param signal_x - A random signal.
	#	@param signal_y - Another random signal.
	#	@return - The cross-correlation between signal_x and signal_y.
	#	O(1) method.
	#
	#	References:
	#		\cite{Legend2011} provides some methods to compute the
	#			cross-correlation between two random signals or
	#			vectors.
	#			https://stackoverflow.com/questions/6991471/computing-cross-correlation-function
	@staticmethod
	def cross_correlation_using_all_approaches(signal_x=[],signal_y=[]):
		###
			Enumerate all modes of NumPy's correlate function.
			
			In the example from \cite{TheSciPyCommunity2019},
				the cross-correlation has values greater than 1;
				since the notes in \cite{TheSciPyCommunity2019}
					indicate that the definition for
					cross-correlation "is not unique," this can
					explain why the cross-correlation for the
					"valid" mode is >1.
		###
		for current_mode in approx_cross_correlation.numpy_correlate_modes:
			# Determine the cross-correlation using the current mode.
			cross_correlation_from_numpy_correlate = approx_cross_correlation.cross_correlation_using_numpy(signal_x,signal_y,current_mode)
			print("Cross-correlation using",current_mode,"mode is:",cross_correlation_from_numpy_correlate,"=")
			"""
				Perform statistical analysis on the set of
					cross-correlation values.
			"""
		# 





###############################################################
# Main method for the program.


"""
	If executed from the "source" directory, it cannot locate the
		custom Python modules that are imported at the top of
		this Python script/program. 
"""
#	If this is executed as a Python script,
"""
if __name__ == "__main__":
	approximate_cross_correlation.rtw_signal_generation_and_cross_correlation()
"""
