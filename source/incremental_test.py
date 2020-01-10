#!/usr/local/bin/python3
###!/Users/zhiyang/anaconda3/bin/python3 
###!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
###	/usr/bin/python
###	/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
###	#!/usr/bin/python -mtimeit
#	/Library/Frameworks/Python.framework/Versions/3.6/bin/python3 ./incremental_test.py ./benchmarks/majority_netlist.json	./output/output-results
#	/Library/Frameworks/Python.framework/Versions/3.6/bin/python3 -mtimeit ./incremental_test.py ./benchmarks/majority_netlist.json	./output/output-results

"""
	This Python script is written by Zhiyang Ong to incrementally
		test features for my software designing noise-based logic
		circuits.


	Synopsis:
	Perform incremental software testing automatically for my
		research solution.

	This script can be executed as follows:
	./incremental_test.py




	Revision History:
	July 31, 2018			Version 0.1	Script.
"""

__author__ = 'Zhiyang Ong'
__version__ = '1.0'
__date__ = 'July 31, 2018'

#	The MIT License (MIT)

#	Copyright (c) <2018> <Zhiyang Ong>

#	Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

#	The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

#	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

#	Email address: echo "cukj -wb- 23wU4X5M589 TROJANS cqkH wiuz2y 0f Mw Stanford" | awk '{ sub("23wU4X5M589","F.d_c_b. ") sub("Stanford","d0mA1n"); print $5, $2, $8; for (i=1; i<=1; i++) print "6\b"; print $9, $7, $6 }' | sed y/kqcbuHwM62z/gnotrzadqmC/ | tr 'q' ' ' | tr -d [:cntrl:] | tr -d 'ir' | tr y "\n"	Che cosa significa?


###############################################################
"""
	Import modules from The Python Standard Library.
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
"""

import sys
import os
import os.path
#from pathlib import Path
from subprocess import call
import time
import warnings
import re



###############################################################
#	Import Custom Python Packages and Modules

# Statistics package.
"""
	Package and module to print statistics of software testing
		results.
"""
from statistics.test_statistics import statistical_analysis
# Package and module to check the validation of statistical analysis.
from statistics.test_statistics_tester import statistical_analysis_tester

"""
	Package and module to perform miscellaneous tasks in data
		analysis.
"""
from statistics.data_analysis_tool import data_analysis
"""
	Package and module to test the miscellaneous tasks in
		analyzing data. 
"""
from statistics.test_data_analysis_tool import data_analysis_tester



# Utilities package.
# Package and module to perform file I/O (input/output) operations.
from utilities.file_io import file_io_operations
# Package and module to test file I/O (input/output) operations.
from utilities.file_io_tester import file_io_operations_tester
# Package and module to process input arguments to the script/program.
# Package and module to perform date and time operations.
from utilities.date_time_processing import date_time_operations
# Package and module to test date and time operations.
from utilities.date_time_processing_tester import date_time_operations_tester
"""
	Module to generate the filename for storing the experimental
		results and simulation output.
"""
from utilities.generate_results_filename import generate_filename
"""
	Module to test if the generated filename (based on the
		then-current time stamp) conforms to the specified
		format.
"""
from utilities.generate_results_filename_tester import generate_filename_tester
# Module to test miscellaneous methods.
from utilities.miscellaneous import misc
from utilities.miscellaneous_tester import misc_tester

# Modules for user-defined error/exception.




# Modules for random number and random signal/"process" generation.
# Module to generate pseudorandom numbers.
from random_process_models.pseudorandom_number_generator import prng
# Module to generate pseudorandom numbers.
from random_process_models.pseudorandom_number_generator_tester import prng_tester






###############################################################

# Global variables.
#	Location to store simulation and/or experimental results.
#result_repository = "/Documents/ricerca/risultati_sperimentali/std-cell-library-characterization"


###############################################################
"""
	Module with methods that incrementally test features for my
		solution for designing noise-based logic circuits.
	It tests the following:
	+ Test the module to analyzing results from testing my software.
	+ Test the functions of the modules in the utilities module.
	+ Test the functions of the modules in the random_process_models module.
	+ Test the implementations for the noise-based logic circuits.
		- approximate circuit for calculating expectated value.
		- ???
"""
class incremental_test_automation:
	# (Static) variables.
	#	Location to store simulation and/or experimental results.
	result_repository = "~/Documents/ricerca/risultati_sperimentali/std-cell-library-characterization"
	# ============================================================










###############################################################
# Main method for the program.

#	If this is executed as a Python script,
if __name__ == "__main__":
	"""
	# Redirect standard output and standard error to an output file.
	results_file_object = file_io_operations.open_file_object_write_results()
	file_io_operations.redirect_std_op_to_file_obj(results_file_object)
	file_io_operations.redirect_std_err_to_file_obj(results_file_object)
	"""
	print("==================================================")
	print("Automating incremental regression testing of my software")
	print("	solution for genetic technology mapping.")
	print("")
	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
	# The real stuff begins here...
	print("-	-	-	-	-	-	-	-	-	-	-	-	-")
	print("=	Testing the statistical analysis package.")
	#	Insert test cases for statistical analysis package
	statistical_analysis_tester.test_statistical_analysis()
	# Test the miscellaneous tasks in analyzing data.
	data_analysis_tester.test_data_analysis()
	print("")
	print("-	-	-	-	-	-	-	-	-	-	-	-	-")
	# Insert test cases for testing the utilities package.
	print("")
	print("=	Testing the utilities package.")
	#	The original file I/O module has been rigorously tested.
	#file_io_operations_tester.test_file_io_operations()
	date_time_operations_tester.test_date_time_operations()
	generate_filename_tester.test_filename_generation_methods()
	misc_tester.test_miscellaneous_methods()
	print("-	-	-	-	-	-	-	-	-	-	-	-	-")
	# Insert test cases for testing the random_process_models package.
	print("")
	print("=	Testing the random_process_models package.")
	prng_tester.test_prng_methods()
	print("-	-	-	-	-	-	-	-	-	-	-	-	-")
	#	### TO-DO
	#	Test expr_configuration
#	incremental_test_automation.read_input_BibTeX_file(ip_file_obj,ip_filename)
	print("!	!	!	!	!	!	!	!	!	!	!")
	print(">>	Get statistics of the software testing process.")
	statistical_analysis.print_statistics_of_software_testing()
	# Close the file object for reading.
	#print("=	Close the file objects for reading (and writing).")
	#file_io_operations.close_file_object(ip_file_obj)
	"""
	file_io_operations.close_file_object(results_file_object)
	# Stop redirecting standard output and standard to an output file.
	file_io_operations.stop_redirecting_std_op()
	file_io_operations.stop_redirecting_std_err()
	"""
#	print("<<	I can see this in standard output, printed in the Terminal.")
	if misc.add_commit_push_updates_to_git_repository("Update build: Added access to Git repository"):
		print("Update repository of simulation/experimental results.")
	else:
		print("DID NOT update repository of simulation/experimental results.")
