#!/usr/local/bin/python3
###!/Users/zhiyang/anaconda3/bin/python3

"""
	This Python script is written by Zhiyang Ong to approximate
		cross-correlation to enable correlation-based machine
		learning.


	The definitions for calculating cross-correlation for
		periodic/deterministic signals, stochastic/random
		and random processes can be found in the following
		publications:
		+ \cite[\SA.2, pp. 364]{Chen2007c}
			- (Expectation of x and y, E[xy])/(sqrt(var(x)var(y)))
			- From https://en.wikipedia.org/wiki/Expected_value,
				expected value = \sum^{k}_{i=1} x_i*p_i;
				for equiprobable outcomes x_i (p_1 = p_2 = ... = p_k),
					which is true for x_i.
			- How to calculate E[XY]?
				* https://faculty.math.illinois.edu/~hildebr/408/408jointdiscrete.pdf
		+ \cite{Downey2015}
			- Chapter 7, 9, 12, 14
			- Chapter 7, pp. 85: Pearson's correlation (always
				between -1 and 1, inclusive).
		+ \cite{Downey2011}
			- Chapter 9, pp. 99: Pearson's correlation (always
			between -1 and 1, inclusive).
		+ \cite{Montgomery2014}
			- \S5.2, pp. 174-179.
				* pp. 176, Pearson's correlation, also defined
					as sigma_xy/(sigma_x*sigma_y) 
			- \S11.8, pp. 457-463.
		+ \cite{Bertsekas2008}
			- \S4.2, pp. 217, Pearson's correlation (not explicitly
				stated)
		+ \cite{Grimmett2001}
			- \S4.2, correlation coefficient and covariance, pp. 64,
				Pearson's correlation (not explicitly stated)
		+ \cite{Ross2004}
			- \S2.6, pp. 36, Pearson's correlation (not explicitly
				stated) for a pair of data (or data pairs, or pair
				of samples)
		+ \cite{Ross2010b}
			- \S7.9, pp. 371.
			- \S7.4, pp. 322, definition of covariance.
			- \S7.4, pp. 328, definition of correlation.



	Note that from https://en.wikipedia.org/wiki/Expected_value:
	+ Section on Basic Properties:
		- E[XY] = E[X]E[Y] if and only if (iff) X and Y are
			independent.

	From https://en.wikipedia.org/wiki/Cross-correlation,
	+ "After calculating the cross-correlation between the two
		signals, the maximum (or minimum if the signals are
		negatively correlated) of the cross-correlation function
		indicates the point in time where the signals are best
		aligned; i.e., the time delay between the two signals is
		determined by the argument of the maximum, or arg max of
		the cross-correlation" 
	+ 






	From https://docs.python.org/3/library/statistics.html






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
"""
	Testing scipy.signal.correlate2d;
	https://stackoverflow.com/questions/57111113/scipy-signal-correlate2d-does-not-seem-to-work-as-intended
	This method needs 2-D arrays as input arguments.


import scipy.signal as sig
signal_correlate_mode = ["full", "valid", "same"]
signal_correlate_boundary = ["fill", "wrap", "symm"]
cross_correlation_from_signal_correlate2D = sig.correlate2d(signal_x, signal_y)
print("SciPy-based cross-correlation using is:",cross_correlation_from_signal_correlate2D,"=")
"""

###############################################################
#	Import Custom Python Packages and Modules

# Module to generate pseudorandom numbers.
from random_process_models.pseudorandom_number_generator import prng
# Module to generate random signals/"processes".
from random_process_models.random_process_generator import rand_signal_generator
"""
	Package and module to perform miscellaneous tasks in data
		analysis.
"""
from statistics_pkg.data_analysis_tool import data_analysis
"""
	Package and module to print statistics of software testing
		results.
"""
from statistics_pkg.test_statistics import statistical_analysis

###############################################################
#	Import Python Packages and Modules from Python Libraries
# Import NumPy.
import numpy as np
# Import Matplotlib's pyplot module.
import matplotlib.pyplot as plt
import pycorrelate as pyc


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
	#
	#	@tested with the following method:
	#		+ cross_correlation_using_all_approaches_with_instrumentation()
	#
	#	References:
	#		\cite{NumPyContributors2019} describes the modes for the
	#			function.
	#		\cite{TheSciPyCommunity2019} shows an example.
	@staticmethod
	def cross_correlation_using_numpy(signal_x=[],signal_y=[],mode=numpy_correlate_mode_valid):
		return np.correlate(signal_x,signal_y,mode)
	# ============================================================
	##	Method to calculate the cross-correlation of two random
	#		signals, signal_x and signal_y, using all approaches
	#		that I learned.
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
	#	+ \cite{Legend2011} provides some methods to compute the
	#		cross-correlation between two random signals or vectors.
	#		https://stackoverflow.com/questions/6991471/computing-cross-correlation-function
	#	+ \cite{TheSciPyCommunity2019a} provides a list of statistical
	#		functions that I used a subset of.
	@staticmethod
	def cross_correlation_using_all_approaches(signal_x=[],signal_y=[]):
		# List of tuples storing results regarding cross-correlation.
		results = []
		"""
			Enumerate all modes of NumPy's correlate function.
			
			In the example from \cite{TheSciPyCommunity2019},
				the cross-correlation has values greater than 1;
				since the notes in \cite{TheSciPyCommunity2019}
					indicate that the definition for
					cross-correlation "is not unique," this can
					explain why the cross-correlation for the
					"valid" mode is >1.
		"""
		for current_mode in approx_cross_correlation.numpy_correlate_modes:
			# Determine the cross-correlation using the current mode.
			cross_correlation_from_numpy_correlate = approx_cross_correlation.cross_correlation_using_numpy(signal_x,signal_y,current_mode)
			#print("NumPy-based cross-correlation using",current_mode,"mode is:",cross_correlation_from_numpy_correlate,"=")
			"""
				Perform statistical analysis on the set of
					cross-correlation values.
			"""
			std_dev_cross_correlation = np.std(cross_correlation_from_numpy_correlate)
			#print("	NumPy-based cross-correlation's standard deviation using",current_mode,"mode is:",std_dev_cross_correlation,"=")
			var_cross_correlation = np.var(cross_correlation_from_numpy_correlate)
			#print("	NumPy-based cross-correlation's variance using",current_mode,"mode is:",var_cross_correlation,"=")
			arith_mean_cross_correlation = np.mean(cross_correlation_from_numpy_correlate)
			#print("	NumPy-based cross-correlation's arithmetic mean using",current_mode,"mode is:",arith_mean_cross_correlation,"=")
			ptp_cross_correlation = np.ptp(cross_correlation_from_numpy_correlate)
			#print("	NumPy-based cross-correlation's min and max values (or peak to peak) using",current_mode,"mode is:",ptp_cross_correlation,"=")
			amax_cross_correlation = np.amax(cross_correlation_from_numpy_correlate)
			#print("	NumPy-based cross-correlation's max value using",current_mode,"mode is:",amax_cross_correlation,"=")
			amin_cross_correlation = np.amin(cross_correlation_from_numpy_correlate)
			#print("	NumPy-based cross-correlation's min value using",current_mode,"mode is:",amin_cross_correlation,"=")
			#print("")
			results.append((current_mode, cross_correlation_from_numpy_correlate, std_dev_cross_correlation, var_cross_correlation, arith_mean_cross_correlation, ptp_cross_correlation, amax_cross_correlation, amin_cross_correlation))
		"""
		Matplotlib.pyplot's solution for correlation causes
			execution error
		
		(lags, c, line, b) = plt.xcorr(signal_x, signal_y,maxlags=4)
		print("Matplotlib.pyplot lags",lags,"=")
		print("Matplotlib.pyplot c",c,"=")
		print("Matplotlib.pyplot line",line,"=")
		print("Matplotlib.pyplot b",b,"=")
		"""
		cross_correlation_from_pycorrelate = pyc.ucorrelate(np.array(signal_x),np.array(signal_y))
		#print("Pycorrelate-based cross-correlation is:",cross_correlation_from_pycorrelate,"=")
		"""
			Perform statistical analysis on the set of
				cross-correlation values.
		"""
		std_dev_cross_correlation = np.std(cross_correlation_from_pycorrelate)
		print("	NumPy-based cross-correlation's standard deviation using",current_mode,"mode is:",std_dev_cross_correlation,"=")
		var_cross_correlation = np.var(cross_correlation_from_pycorrelate)
		print("	NumPy-based cross-correlation's variance using",current_mode,"mode is:",var_cross_correlation,"=")
		arith_mean_cross_correlation = np.mean(cross_correlation_from_pycorrelate)
		print("	NumPy-based cross-correlation's arithmetic mean using",current_mode,"mode is:",arith_mean_cross_correlation,"=")
		ptp_cross_correlation = np.ptp(cross_correlation_from_pycorrelate)
		print("	NumPy-based cross-correlation's min and max values (or peak to peak) using",current_mode,"mode is:",ptp_cross_correlation,"=")
		amax_cross_correlation = np.amax(cross_correlation_from_pycorrelate)
		print("	NumPy-based cross-correlation's max value using",current_mode,"mode is:",amax_cross_correlation,"=")
		amin_cross_correlation = np.amin(cross_correlation_from_pycorrelate)
		print("	NumPy-based cross-correlation's min value using",current_mode,"mode is:",amin_cross_correlation,"=")
		print("")
		results.append(("pyc.ucorrelate", cross_correlation_from_pycorrelate, std_dev_cross_correlation, var_cross_correlation, arith_mean_cross_correlation, ptp_cross_correlation, amax_cross_correlation, amin_cross_correlation))
		return results
	# ============================================================
	##	Method to calculate the cross-correlation of two random
	#		signals, signal_x and signal_y, using all approaches
	#		that I learned.
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
	#	IMPORTANT NOTES:
	#	This alternate method has instrumentation added to the
	#		method "cross_correlation_using_all_approaches()".
	#	Since the aforementioned method is so complicated, and
	#		the method cannot be encapsulated by a deterministic
	#		input/output behavior, instrumentation is added to
	#		indicate "test" outcomes (successful execution of
	#		the code).
	#	Correctness of the methods called from different
	#		*Python* libraries are not checked, since we assume
	#		that they have been thoroughly tested.
	#	However, the results from different method calls (using
	#		methods from different Python libraries) would be
	#		compared in the automated 
	#
	#	References:
	#	+ \cite{Legend2011} provides some methods to compute the
	#		cross-correlation between two random signals or vectors.
	#		https://stackoverflow.com/questions/6991471/computing-cross-correlation-function
	#	+ \cite{TheSciPyCommunity2019a} provides a list of statistical
	#		functions that I used a subset of.
	@staticmethod
	def cross_correlation_using_all_approaches_with_instrumentation(signal_x=[],signal_y=[]):
		# List of tuples storing results regarding cross-correlation.
		results = []
		"""
			Enumerate all modes of NumPy's correlate function.
			
			In the example from \cite{TheSciPyCommunity2019},
				the cross-correlation has values greater than 1;
				since the notes in \cite{TheSciPyCommunity2019}
					indicate that the definition for
					cross-correlation "is not unique," this can
					explain why the cross-correlation for the
					"valid" mode is >1.
		"""
		for current_mode in approx_cross_correlation.numpy_correlate_modes:
			prompt = "	... Testing NumPy-based cross-correlation's " + current_mode + " mode.		{}"
			statistical_analysis.increment_number_test_cases_used()
			# Determine the cross-correlation using the current mode.
			cross_correlation_from_numpy_correlate = approx_cross_correlation.cross_correlation_using_numpy(signal_x,signal_y,current_mode)
			#print("NumPy-based cross-correlation using",current_mode,"mode is:",cross_correlation_from_numpy_correlate,"=")
			"""
				Perform statistical analysis on the set of
					cross-correlation values.
			"""
			std_dev_cross_correlation = np.std(cross_correlation_from_numpy_correlate)
			#print("	NumPy-based cross-correlation's standard deviation using",current_mode,"mode is:",std_dev_cross_correlation,"=")
			var_cross_correlation = np.var(cross_correlation_from_numpy_correlate)
			#print("	NumPy-based cross-correlation's variance using",current_mode,"mode is:",var_cross_correlation,"=")
			arith_mean_cross_correlation = np.mean(cross_correlation_from_numpy_correlate)
			#print("	NumPy-based cross-correlation's arithmetic mean using",current_mode,"mode is:",arith_mean_cross_correlation,"=")
			ptp_cross_correlation = np.ptp(cross_correlation_from_numpy_correlate)
			#print("	NumPy-based cross-correlation's min and max values (or peak to peak) using",current_mode,"mode is:",ptp_cross_correlation,"=")
			amax_cross_correlation = np.amax(cross_correlation_from_numpy_correlate)
			#print("	NumPy-based cross-correlation's max value using",current_mode,"mode is:",amax_cross_correlation,"=")
			amin_cross_correlation = np.amin(cross_correlation_from_numpy_correlate)
			#print("	NumPy-based cross-correlation's min value using",current_mode,"mode is:",amin_cross_correlation,"=")
			#print("")
			results.append((current_mode, cross_correlation_from_numpy_correlate, std_dev_cross_correlation, var_cross_correlation, arith_mean_cross_correlation, ptp_cross_correlation, amax_cross_correlation, amin_cross_correlation))
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		"""
		Matplotlib.pyplot's solution for correlation causes
			execution error
		
		(lags, c, line, b) = plt.xcorr(signal_x, signal_y,maxlags=4)
		print("Matplotlib.pyplot lags",lags,"=")
		print("Matplotlib.pyplot c",c,"=")
		print("Matplotlib.pyplot line",line,"=")
		print("Matplotlib.pyplot b",b,"=")
		"""
		cross_correlation_from_pycorrelate = pyc.ucorrelate(np.array(signal_x),np.array(signal_y))
		#print("Pycorrelate-based cross-correlation is:",cross_correlation_from_pycorrelate,"=")
		"""
			Perform statistical analysis on the set of
				cross-correlation values.
		"""
		std_dev_cross_correlation = np.std(cross_correlation_from_pycorrelate)
		print("	NumPy-based cross-correlation's standard deviation using",current_mode,"mode is:",std_dev_cross_correlation,"=")
		var_cross_correlation = np.var(cross_correlation_from_pycorrelate)
		print("	NumPy-based cross-correlation's variance using",current_mode,"mode is:",var_cross_correlation,"=")
		arith_mean_cross_correlation = np.mean(cross_correlation_from_pycorrelate)
		print("	NumPy-based cross-correlation's arithmetic mean using",current_mode,"mode is:",arith_mean_cross_correlation,"=")
		ptp_cross_correlation = np.ptp(cross_correlation_from_pycorrelate)
		print("	NumPy-based cross-correlation's min and max values (or peak to peak) using",current_mode,"mode is:",ptp_cross_correlation,"=")
		amax_cross_correlation = np.amax(cross_correlation_from_pycorrelate)
		print("	NumPy-based cross-correlation's max value using",current_mode,"mode is:",amax_cross_correlation,"=")
		amin_cross_correlation = np.amin(cross_correlation_from_pycorrelate)
		print("	NumPy-based cross-correlation's min value using",current_mode,"mode is:",amin_cross_correlation,"=")
		print("")
		results.append(("pyc.ucorrelate", cross_correlation_from_pycorrelate, std_dev_cross_correlation, var_cross_correlation, arith_mean_cross_correlation, ptp_cross_correlation, amax_cross_correlation, amin_cross_correlation))
		return results
	# ============================================================
	##	Method to approximate the calculation of the cross-correlation
	#		of two random signals, signal_x and signal_y.
	#
	#	@param signal_x - A random signal.
	#	@param signal_y - Another random signal.
	#	@return - The approximate cross-correlation between signal_x
	#		and signal_y.
	#	O(1) method.
	#
	#
	#	References:
	#		\cite{???} describes the formula for calculating the
	#			cross-correlation function.
	#
	@staticmethod
	def approximate_cross_correlation_(signal_x=[],signal_y=[]):
		print("")
	## =========================================================
	#	Method to find the relative percentage difference between
	#		the methods regarding calculating cross-correlation.
	#	@param results - A list of list, where each list in the list
	#				contains results for each method.
	#	@return - A list of list, where each list is a comparison
	#				of results between any pair of methods, and the
	#				embedded list is a set of relative percentage
	#				difference comparing their results.
	#	O(1) method.
	@staticmethod
	def find_relative_percentage_difference(results=None):
		if results is None:
			return None
		else:
			results_size_per_dimension = len(results)
			temp_list_per_dimension_in_matrix = [0]*results_size_per_dimension
			matrix_tracking_comparisons = []
			for i in range(results_size_per_dimension):
				matrix_tracking_comparisons.append(temp_list_per_dimension_in_matrix)
			"""
				Use a boolean matrix to track comparisons between
					methods.
				
				An 0-initialized list per row in the 2-D list of
					lists containing results of the matrix.
			"""
			for list_in_results in range(results_size_per_dimension):
				for other_list_in_results in range(list_in_results+1,results_size_per_dimension):
					print("Comparing methods:",results[list_in_results][0]," and ",results[other_list_in_results][0],".")
					print("Relative difference for std_dev_x_corr",results[list_in_results][2]," and ",results[other_list_in_results][2],"is",data_analysis.get_relative_percentage_difference(results[list_in_results][2],results[other_list_in_results][2]),".")
					print("Relative difference for var_cross_correlation",results[list_in_results][3]," and ",results[other_list_in_results][3],"is",data_analysis.get_relative_percentage_difference(results[list_in_results][3],results[other_list_in_results][3]),".")
					print("Relative difference for arith_mean_cross_correlation",results[list_in_results][4]," and ",results[other_list_in_results][4],"is",data_analysis.get_relative_percentage_difference(results[list_in_results][4],results[other_list_in_results][4]),".")
					print("Relative difference for ptp_cross_correlationget_relative_difference_friendly_version",results[list_in_results][5]," and ",results[other_list_in_results][5],"is",data_analysis.get_relative_percentage_difference(results[list_in_results][5],results[other_list_in_results][5]),".")
					print("Relative difference for amax_cross_correlation",results[list_in_results][6]," and ",results[other_list_in_results][6],"is",data_analysis.get_relative_percentage_difference(results[list_in_results][6],results[other_list_in_results][6]),".")
					print("Relative difference for amin_cross_correlation",results[list_in_results][7]," and ",results[other_list_in_results][7],"is",data_analysis.get_relative_percentage_difference(results[list_in_results][7],results[other_list_in_results][7]),".")
					print("")












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
