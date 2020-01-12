#!/usr/local/bin/python3
###!/Users/zhiyang/anaconda3/bin/python3

"""
	This Python script is written by Zhiyang Ong to test the
		approximate cross-correlation approach.


	Synopsis:
	Test the approach to approximate cross-correlation in Python.


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
# Module to approximate cross-correlation.
from behavioral_models.approximate_cross_correlation import approx_cross_correlation
# Package and module to perform date and time operations.
from utilities.date_time_processing import date_time_operations

###############################################################
"""
	Module to test approach to approximate cross-correlation.
"""
class approx_cross_correlation_tester:
	# ============================================================
	##	Method to test the calculation of the cross-correlation
	#		of RTW signals.
	#
	#	For all methods to calculate/compute the cross-correlation,
	#		perform statistical analysis on the list of
	#			cross-correlation values.
	#	Write information about the following into an output file
	#		for further analysis/review.
	#	+ random signals (values of)
	#	+ value(s) of cross-correlation
	#	+ 
	#	 
	#
	#	@param - None.
	#	@return - Nothing.
	#	O(1) method.
	@staticmethod
	def test_rtw_signal_generation_and_cross_correlation():
		# Create a file object for writing.
		print("=	Create a file object for writing.")
		current_date_time = date_time_operations.get_current_date_time()
		op_filename = "results/cross-correlation-results-"+current_date_time+".text"
		op_file_obj = open(op_filename, 'w')
		# List of number of discrete values for random signals/"processes". 
		for k in [4, 8, 16, 32, 64, 128]:
			print("=	Testing random ", k, "-bit signals.")
			# Generate a random signal of the type random telegraph wave (RTW).
			x_rtw_1 = rand_signal_generator.gen_rand_signal_uniform_distributn(rand_signal_generator.rtw_signal,k)
			print("x_rtw_1 is:",x_rtw_1,"=")
			# Generate another RTW.
			x_rtw_2 = rand_signal_generator.gen_rand_signal_uniform_distributn(rand_signal_generator.rtw_signal,k)
			print("x_rtw_2 is:",x_rtw_2,"=")
			"""
				Find the cross-correlation between these two RTWs,
					using all approaches.
			"""
			[x_corr_list, std_dev_x_corr, var_x_corr, arith_mean_x_corr, ptp_x_corr, amax_x_corr, amin_x_corr] = approx_cross_correlation.cross_correlation_using_all_approaches(x_rtw_1,x_rtw_2)
			actual_list = [x_corr_list, std_dev_x_corr, var_x_corr, arith_mean_x_corr, ptp_x_corr, amax_x_corr, amin_x_corr]
			names_list = ["x_corr_list", "std_dev_x_corr", "var_x_corr", "arith_mean_x_corr", "ptp_x_corr", "amax_x_corr", "amin_x_corr"]
			for (name,metric) in enumerate(zip((names_list,actual_list))):
				#tempt_text = "=	Metric name="+name+"= with value ="+str(metric)+"="
				tempt_text = "=	Metric name="+str(name)+"= with value ="+str(metric)+"="
				op_file_obj.write(tempt_text)
				op_file_obj.write("\n")
			print("============================================")
		# Close the file object for writing.
		op_file_obj.close()
	## =========================================================
	#	Method to test the methods regarding approximating
	#		cross-correlation.
	#	@param - Nothing
	#	@return - Nothing.
	#	O(1) method.
	@staticmethod
	def test_random_signal_generation_methods():
		print("")
		print("")
		print("==	Testing class: approx_cross_correlation.")
		approx_cross_correlation_tester.test_rtw_signal_generation_and_cross_correlation()



