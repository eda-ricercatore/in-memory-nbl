#!/Users/zhiyang/anaconda3/bin/python3

"""
	This Python script is written by Zhiyang Ong to process and
		plot Xyce circuit simulation results.


	@modified by Zhiyang Ong, January 15, 2020.
	+ Modify code to process Xyce circuit simulation results,
		for a circuit with one input parameter.


	IMPORTANT NOTES:
	+ Computer bugs.
	January 16, 2020, 18:00 hrs, U.S. CST.
	Buggy computer did not save my file even though I had saved it,
		and the GUI of the IDE appeared to have saved it.
	That said, I noticed the "Terminal" application indicating
		the last modification time had not changed from 16:00 hrs
		till about 17:40 hrs.
	Hence, I lost an hour of work.
	Also, I noticed that the SSH authentication in the "Terminal"
		tab for the current working directory lapsed.
	However, commits to my "gulyas-scripts" repository still worked.



	Resources about colors for Matplotlib.pyplot:
	+ https://matplotlib.org/3.1.1/gallery/color/colormap_reference.html
	+ https://matplotlib.org/3.1.0/gallery/color/named_colors.html
	+ https://matplotlib.org/3.1.1/tutorials/colors/colors.html
	+ https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html




	References:
	+ \cite[From Lines, bars and markers: EventCollection Demo]{MatplotlibDevelopmentTeam2020a}
		- https://matplotlib.org/gallery/lines_bars_and_markers/eventcollection_demo.html;
			Last accessed on January 16, 2020.
"""




__author__ = 'Zhiyang Ong'
__version__ = '1.0'
__date__ = 'January 17, 2020'

#	The MIT License (MIT)

#	Copyright (c) <2020> <Zhiyang Ong>

#	Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

#	The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

#	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

#	Email address: echo "cukj -wb- 23wU4X5M589 TROJANS cqkH wiuz2y 0f Mw Stanford" | awk '{ sub("23wU4X5M589","F.d_c_b. ") sub("Stanford","d0mA1n"); print $5, $2, $8; for (i=1; i<=1; i++) print "6\b"; print $9, $7, $6 }' | sed y/kqcbuHwM62z/gnotrzadqmC/ | tr 'q' ' ' | tr -d [:cntrl:] | tr -d 'ir' | tr y "\n"	Che cosa significa?











###############################################################
#	Import packages and modules from the Python Standard Library.
import math


###############################################################
#	Import Custom Python Packages and Modules


###############################################################
#	Import packages and modules Python libraries
import matplotlib.pyplot as plt
from matplotlib.collections import EventCollection
# Get the set of colors from: matplotlib.colors.TABLEAU_COLORS 
import matplotlib.colors as mcolors
import numpy as np



nanosecond_threshold = 0.000000001
microsecond_threshold = 0.000001
millisecond_threshold = 0.001


# ============================================================
##	Method to scale for nanoseconds, microseconds, and milliseconds.
#
#	@param minimum_time_interval - Time interval/increment
#				indicating how much we should scale the time
#				field/column by.
#	@return the scaling factor (or scale factor) for the time
#				field/column.
#	O(1) method.
def scaling_factor_for_time_column(minimum_time_interval):
	if ( < minimum_time_interval)


# ============================================================
##	Method to determine the interval/increment between major ticks
#		for the x-axis and the y-axis (or y-axes).
#
#	@param for_y_axes - Boolean flag to indicate if two
#				intervals/increments between major ticks need to
#				be found for the y-axes.
#				This is used for multiple fields of data, such that
#					two scales may need to be used to plot the data.
#				If there exists more than two scales for the y-axis,
#					such requirement cannot be met.
#	@return - .
#	O(1) method.
def determine_interval_between_major_ticks_xy_axes(research_results_database,list_column_headers):
	x_minimum = min(research_results_database[list_column_headers[1]])
	x_maximum = max(research_results_database[list_column_headers[1]])
	x_major_increment = math.ceil((x_maximum - x_minimum)/10)
	print("x_major_increment is:",x_major_increment,".")
	x_range = range(x_minimum, x_maximum, x_major_increment)
	for current_column_header in list_column_headers[2:]:
		y_minimum = min(research_results_database[list_column_headers[current_column_header]])
		y_maximum = max(research_results_database[list_column_headers[current_column_header]])
		y_major_increment = math.ceil((x_maximum - x_minimum)/10)
		y_range = range(x_minimum, x_maximum, x_major_increment)
		y_ranges.append(y_range)
	return x_range, y_ranges






"""
	@modified by Zhiyang Ong, January 15, 2020.

	Database list of circuit simulation results.
	Each entry in the list is a dictionary, where its key is the
		column header and its value is a list of data associated
		with that column in the output file of Xyce circuit
		simulation results. 
"""
#simulation_results_database = []
simulation_results_database = {}
temp_list_column_headers = []
# Path to Xyce circuit
filename = "inverter_transient.spice.prn"
# Process the output file of Xyce circuit simulation results.
with open(filename, "r") as f_obj:
	simulation_results = f_obj.readlines()
	# For each line in the output file.
	for current_line in simulation_results:
		# Is this line the first line?
		if "Index       TIME" in current_line:
			# Yes.
			print("Found first line of the Xyce circuit simulation results.")
			temp_list_column_headers = current_line.split()
			"""
				Enumerate the list of important columns.
				Ignore the "Index"/first column, and create a
					dictionary list for each column.
				That is, each column would be associated with a
					list ("value") by its column header ("key").
			"""
			print("	Enumerate columns headers.")
			for current_column_header in temp_list_column_headers[1:]:
				"""
					For each field, associate it with an empty
						list in a dictionary.
				"""
				print("	Current column header is:",current_column_header,".")
				"""
					Create a dictionary to store the data associated
						with this column.
					The key is the column header.
					The value is an intialized empty list that will
						store the data from that column in the
						output file for Xyce circuit simulation
						results.
				"""
				#temp_column = {current_column_header: []}
				#simulation_results_database.append(temp_column)
				#simulation_results_database.update({temp_column:[]})
				#simulation_results_database.setdefault(temp_column, [])
				simulation_results_database[current_column_header] = []
		# Is this the last line of the output file?
		elif "End of Xyce(TM) Simulation" in current_line:
			# Yes.
			print("Finish processing Xyce circuit simulation results.")
		# Else, process the next available line in the output file.
		else:
			# Current enumerated row of circuit simulation results.
			temp_row_of_cir_sim_res = current_line.split()
			"""
				Store the data for each column in this row into
					the appropriate dictionary in the database list
					of circuit simulation results.
			"""
			for index, (current_field_of_current_row,current_data_point_of_current_field,current_name_of_field) in enumerate(zip(temp_row_of_cir_sim_res[1:],simulation_results_database,temp_list_column_headers[1:])):
				# Demonstrate successful enumeration of columns/fields.
				"""
				print("	index=",index,"= associated value=",current_field_of_current_row,"=")
				print("	index=",index,"= current key-value pair=",current_data_point_of_current_field,"=")
				print("	index=",index,"= simulation_results_database[current_name_of_field]=",simulation_results_database[current_name_of_field],"=")
				"""
				"""
					Convert number in string data type to float
						data type before putting it into the database.
					This avoids data processing of the data as strings,
						instead of numbers.
				"""
				simulation_results_database[current_name_of_field].append(float(current_field_of_current_row))
# ========================================================
"""
	@modified by Zhiyang Ong, January 15, 2020.

	Ignore the following, since I have my own data to plot.
	The following generates random data to be plotted in this example.
# Fixing random state for reproducibility
np.random.seed(19680801)

# create random data
xdata = np.random.random([2, 10])

# split the data into two parts
xdata1 = xdata[0, :]
xdata2 = xdata[1, :]

# sort the data so it makes clean curves
xdata1.sort()
xdata2.sort()

# create some y data points
ydata1 = xdata1 ** 2
ydata2 = 1 - xdata2 ** 3
"""

"""
	List of named colors.

	References:
	+ \cite[From Color: List of named colors]{MatplotlibDevelopmentTeam2020a}
		- : {'tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan'}

	Check the number of fields in the Xyce circuit simulation results.
	print("	size of temp_list_column_headers:",len(temp_list_column_headers),".")
	print("	size of temp_list_column_headers[1:]:",len(temp_list_column_headers[1:]),".")
	
	Print the list of colors in matplotlib.colors.TABLEAU_COLORS.
	print("	mcolors.TABLEAU_COLORS:",mcolors.TABLEAU_COLORS,".")
	print("	mcolors.TABLEAU_COLORS[tab:gray]",mcolors.TABLEAU_COLORS['tab:gray'],".")
"""
# Ignore coloumn 1, which is the index (i.e., row number),
if len(temp_list_column_headers[2:]) >= len(mcolors.TABLEAU_COLORS):
	print("	WARNING!!! There are not enough colors in matplotlib.colors.TABLEAU_COLORS to plot each field with a unique color.")
else:
	# plot the data
	fig = plt.figure()
	ax = fig.add_subplot(1, 1, 1)
	"""
		The 1st column of temp_list_column_headers is always the row
			index of the Xyce circuit simulation results.
		The 2nd column of temp_list_column_headers is always the time
		stamp of the circuit simulation.
		Hence, enumerate the fields/columns of the Xyce circuit
			simulation results from column 2.
		Column 2 forms the data set for the x-axis, and the other
			columns are plotted in the x-y plane for the corresponding
			value of x (i.e., value of time instance).
		
		Create the events marking the x data points.
		Create the events marking the y data points.
		Add the events to the axis.

		ax.plot(temp_list_column_headers[1], ydata1, color='tab:blue')
		xevents1 = EventCollection(xdata1, color='tab:blue', linelength=0.05)
		yevents1 = EventCollection(ydata1, color='tab:blue', linelength=0.05, orientation='vertical')
		ax.add_collection(xevents1)
		ax.add_collection(yevents1)
		ax.plot(xdata2, ydata2, color='tab:orange')
		xevents2 = EventCollection(xdata2, color='tab:orange', linelength=0.05)
		yevents2 = EventCollection(ydata2, color='tab:orange', linelength=0.05, orientation='vertical')
		ax.add_collection(xevents2)
		ax.add_collection(yevents2)
	"""
	"""
	print("	temp_list_column_headers[1]:",temp_list_column_headers[1],".")
	print("	simulation_results_database[temp_list_column_headers[1]]:",simulation_results_database[temp_list_column_headers[1]],".")
	print("	temp_list_column_headers[2:]:",temp_list_column_headers[2:],".")
	"""
	print(":	temp_list_column_headers[1]:",temp_list_column_headers[1],".")
	print("	len(simulation_results_database[temp_list_column_headers[1]]):",len(simulation_results_database[temp_list_column_headers[1]]),".")
	#print("	simulation_results_database[temp_list_column_headers[1]]:",simulation_results_database[temp_list_column_headers[1]],".")
	data_for_y_axes_for_plotting = []
	for index, (current_field_name,current_field_data,enumerated_color) in enumerate(zip(temp_list_column_headers[2:],simulation_results_database,mcolors.TABLEAU_COLORS)):
		print(":	current_field_name:",current_field_name,".")
		# Name of the field/column.
		print(":	temp_list_column_headers[index]:",temp_list_column_headers[index+2],".")
		# Data set for the field/column.
		print("	len(simulation_results_database[current_field_name]):",len(simulation_results_database[current_field_name]),".")
		#print(":	simulation_results_database[current_field_name]:",simulation_results_database[current_field_name],".")
		print("	current color:",enumerated_color,".")
		"""
			Plot currently enumerated field (i.e., V_in or V_out)
				on the y-axis against time column/field on the x-axis.
		"""
		data_for_y_axes_for_plotting.append(plt.plot(simulation_results_database[temp_list_column_headers[1]],simulation_results_database[current_field_name], color=enumerated_color))
		#ax.plot(simulation_results_database[temp_list_column_headers[1]], simulation_results_database[current_field_name], color=enumerated_color)
		#xevents1 = EventCollection(simulation_results_database[temp_list_column_headers[1]], color=enumerated_color, linelength=0.05)
		#yevents1 = EventCollection(simulation_results_database[current_field_name], color=enumerated_color, linelength=0.05, orientation='vertical')
		#ax.add_collection(xevents1)
		#ax.add_collection(yevents1)
		"""
		ax.plot(temp_list_column_headers[1], ydata1, color='tab:blue')
		xevents1 = EventCollection(xdata1, color='tab:blue', linelength=0.05)
		yevents1 = EventCollection(ydata1, color='tab:blue', linelength=0.05, orientation='vertical')
		ax.add_collection(xevents1)
		ax.add_collection(yevents1)
		ax.plot(xdata2, ydata2, color='tab:orange')
		xevents2 = EventCollection(xdata2, color='tab:orange', linelength=0.05)
		yevents2 = EventCollection(ydata2, color='tab:orange', linelength=0.05, orientation='vertical')
		ax.add_collection(xevents2)
		ax.add_collection(yevents2)
		"""
	# set the limits
	#ax.set_xlim([0, 1])
	#ax.set_ylim([0, 1])
	# See https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.legend.html
	plt.legend(tuple(data_for_y_axes_for_plotting), ('V_in(V)', 'Vout(V)'))
	"""
		See https://matplotlib.org/api/axes_api.html#autoscaling-and-margins
		and https://matplotlib.org/api/pyplot_api.html
	"""
	"""
		Enumerate all fields/columns concurrently to find the minimum.
		Assume that the increment for each field/column (other than
			time) can be unique.
		See https://matplotlib.org/gallery/subplots_axes_and_figures/two_scales.html.
			\cite[From Subplots, axes and figures: Plots with different scales]{MatplotlibDevelopmentTeam2020a}
		See https://matplotlib.org/gallery/subplots_axes_and_figures/fahrenheit_celsius_scales.html
			\cite[From Subplots, axes and figures: Different scales on the same axes]{MatplotlibDevelopmentTeam2020a}
	"""
	"""
	number_of_rows = len(simulation_results_database[temp_list_column_headers[1]])
	index_of_last_row = number_of_rows - 1
	x_major_increment = math.ceil(index_of_last_row/10)
	y_min = float(min(simulation_results_database[temp_list_column_headers[1]]))
	print("	y_min is:",y_min,".")
	y_max = float(max(simulation_results_database[temp_list_column_headers[1]]))
	print("	y_max is:",y_max,".")
	y_major_increment = math.ceil((y_max - y_min)/10)
	print("	simulation_results_database[temp_list_column_headers[1]]",simulation_results_database[temp_list_column_headers[1]],".")
	x_major_ticks = range(0, number_of_rows,x_major_increment)
	y_major_ticks = range(y_min, y_max,y_major_increment)
	"""
	x_major_ticks, y_major_ticks = determine_interval_between_major_ticks_xy_axes(simulation_results_database,temp_list_column_headers)
	ax.set_xticks(x_major_ticks)
	ax.set_yticks(y_major_ticks)
	plt.xlabel('time (s)')
	plt.ylabel('V_in(V), Vout(V)')
	plt.title('Plot of Xyce circuit simulation results of V_in(V) and Vout(V) over time (s)')
	"""
		@modified by Zhiyang Ong, January 15, 2020.
		Save plot in PDF format.
		This save to PDF command has to appear before the .show()
			command;
			else, the PDF fuile would be empty.
		https://github.com/futurestudio/matplotlib-tutorials/tree/master/export_samples
		
		Reference:
			Norman Peitek, "Matplotlib — Save Plots as File", from
				{\it Future Studio: Future Studio Tutorials},
				{Fellner, P{\"{o}}hls, Peitek GbR}, Magdeburg,
				Saxony-Anhalt, Germany, August 5, 2019.
				Available at: https://futurestud.io/tutorials/matplotlib-save-plots-as-file;
					last accessed on January 15, 2019.
	"""
	plt.savefig(__file__+".pdf")
	# display the plot
	plt.show()

