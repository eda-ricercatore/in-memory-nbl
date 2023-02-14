#!/Users/zhiyang/anaconda3/bin/python3

"""
	This Python script is written by Zhiyang Ong to process and
		plot Xyce circuit simulation [XyceTeam2023] results.


	The objective of this script is to plot the values on the y-axis,
		for input or output voltage values, and the voltage value of
		intermediate nodes.

	Do not address the intervals between timestamps, and any possible
		differences in the intervals between timestamps.
	This is because each set of values for Vin, Vout, and V1
		(intermediate note) is assigned to each time instance.
		Hence, if the differences in the intervals are not uniform,
			it may affect the location of data points on the graphs/plots
			on the x-axis.
			However, it would not affect the shape of the graph/plot.


	Modify code to process Xyce circuit simulation results,
		for a circuit with:
	+ 1 input parameter
	+ 1 output parameter

	To extend this for more input and output signals of logic gates
		and circuits, and digital systems, add more plots or subplots
		to the end of this script.



	From [DrakeJr2016b, Built-in Types: Ranges], the input arguments to the
		function range() requires integer arguments.
		Or: https://docs.python.org/3/library/stdtypes.html
	Since the interval between timestamps is approximately the same,
		if not the same, we can just try to plot the graph for the
		elapsed time during simulation.
	


	Resources about colors for Matplotlib.pyplot:
	+ https://matplotlib.org/3.1.1/gallery/color/colormap_reference.html
	+ https://matplotlib.org/3.1.0/gallery/color/named_colors.html
	+ https://matplotlib.org/3.1.1/tutorials/colors/colors.html
	+ https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html




	References:
	+ \cite[From Lines, bars and markers: EventCollection Demo]{MatplotlibDevelopmentTeam2020a}
		- https://matplotlib.org/gallery/lines_bars_and_markers/eventcollection_demo.html;
			Last accessed on January 16, 2020.
	+ [Pankaj2022a]
		- Pankaj and Andrea Anderson, "How To Remove Spaces from a String In Python," DigitalOcean, LLC, New York, NY, December 12, 2022. Available online from *DigitalOcean: Community: Resources: Tutorials* at: https://www.digitalocean.com/community/tutorials/python-remove-spaces-from-string; February 13, 2023 was the last accessed date.
	+ [DrakeJr2016b]
		- Fred L. Drake, Jr., David Goodger, and Fredrik Lundh, "The Python Standard Library," Python Software Foundation, Beaverton, OR, March 23, 2016. Available online from *Welcome to Python.org: Python 3.5.1 documentation* at: https://docs.python.org/3/library/; April 1, 2016 was the last accessed date.
	+ [Naveen2021]
		- Naveen, "Pandas Drop Rows From DataFrame Examples," SparkByExamples.com, Irvine, CA, September 2, 2021. Available online from *Spark By Examples: Python Pandas Tutorial* at: https://sparkbyexamples.com/pandas/pandas-drop-rows-from-dataframe/; February 13, 2023 was the last accessed date.
	+ [ActiveStateSoftwareIncStaff2022]
		- ActiveState Software Inc. staff, "How To Delete A Column/Row From A DataFrame," ActiveState Software Inc., Vancouver, British Columbia, Canada, July 11, 2022. Available online from *ActiveState: Resources: Resource Library: Quick Reads* at: https://www.activestate.com/resources/quick-reads/how-to-delete-a-column-row-from-a-dataframe/; February 13, 2023 was the last accessed date.
	+ [Haire2023a]
		- Emma Carballal Haire, Irv Lustig, JHM Darbyshire, Joris Van den Bossche, Marc Garcia, Marco Edward Gorelli, MarcoGorelli, Matthew Roeschke, MeeseeksMachine, Natalia Mokeeva, Pandas Development Team, Patrick Hoefler, Richard Shadrach, Tsvika Shapira, William Ayd, aneesh98, jakirkham, jbrockmendel, and silviaovo, "API reference," NumFOCUS, Inc., Austin, TX, January 19, 2023. Available online from *PyData: pandas: Documentation: pandas documentation: API reference* as Version 1.5.3 at: https://pandas.pydata.org/docs/reference/index.html; February 10, 2023 was the last accessed date.
	+ [Kaur2022]
		- Simran Kaur, "Pandas Read\_Table()," Linux Hint LLC, Sunnyvale, CA, June, 2022. Available online from *Linux Hint: Python* at: https://linuxhint.com/pandas-read-table/; February 13, 2023 was the last accessed date.
	+ [Hunter2016a] John Hunter, Michael Droettboom, and Thomas A. Caswell (editors),
		"Pyplot tutorial," in Matplotlib, NumFOCUS, Inc., Austin, TX, September 20, 2016.
		Available online from *Matplotlib: docs: Overview, Release 1.5.3:
			User's Guide: Beginner's Guide* at: http://matplotlib.org/users/pyplot_tutorial.html;
			November 18, 2016 was the last accessed date.
	+ [Hunter2016]
		- John Hunter, Darren Dale, Eric Firing, Michael Droettboom, the Matplotlib development team, "Beginner's Guide: Matplotlib 1.5.3 documentation," NumFOCUS, Inc., Austin, TX, December 19, 2016. Available online from *Matplotlib: docs: Overview: User's Guide* at: https://matplotlib.org/users/beginner.html; December 11, 2018 was the last accessed date.
	+ [Berg2023]
		- Sebastian Berg, Ralf Gommers, Charles Harris, Stephan Hoyer, Inessa Pawson, Matti Picus, St{\'{e}}fan {van der Walt}, Melissa Weber Mendon{\c{c}}a, and Eric Wieser, "NumPy," NumFOCUS, Inc., Austin, TX, 2023. Available online at: https://numpy.org/; January 19, 2023 was the last accessed date.
	+ [NumPyDevelopers2018]
		- NumPy Developers, "NumPy," NumFOCUS, Inc., Austin, TX, 2018. Available online at: http://www.numpy.org/index.html; December 3, 2018 was the last accessed date.
	+ [Augspurger2018]
		- Tom Augspurger, Chris Bartak, Phillip Cloud, Andy Hayden, Stephan Hoyer, Wes McKinney, Jeff Reback, Chang She, Masaaki Horikoshi, and Joris Van den Bossche, "pandas: Python Data Analysis Library," NumFOCUS, Inc., Austin, TX, August, 2018. Available online from *PyData* at: http://pandas.pydata.org/; December 3, 2018 was the last accessed date.
	+ [Hunter2023] John Hunter, Michael Droettboom, and Thomas A. Caswell (editors),
		"Controlling style of text and labels using a dictionary," in Matplotlib,
		NumFOCUS, Inc., Austin, TX, September 20, 2016.
		Available online from *Matplotlib - Visualization with Python: Examples:
		Text, labels and annotations* at: https://matplotlib.org/stable/gallery/text_labels_and_annotations/text_fontdict.html#sphx-glr-gallery-text-labels-and-annotations-text-fontdict-py;
		January 17, 2023 was the last accessed date.
	+ [Hunter2023a] John Hunter, Michael Droettboom, and Thomas A. Caswell (editors),
		"Pyplot Mathtext," in Matplotlib, NumFOCUS, Inc., Austin, TX, September 20, 2016.
		Available online from *Matplotlib - Visualization with Python: Examples: pyplot* at:
		https://matplotlib.org/stable/gallery/pyplots/pyplot_mathtext.html#sphx-glr-gallery-pyplots-pyplot-mathtext-py;
		January 17, 2023 was the last accessed date.
	+ [Peitek2019a]
		- Norman Peitek, "05-save-as-file.py," GitHub, Inc., San Francisco, CA, July 26, 2019. Available online from *GitHub: Future Studio: matplotlib tutorials* at: https://github.com/futurestudio/matplotlib-tutorials/blob/master/05-save-as-file.py; January 18, 2023 was the last accessed date.
	+ [Peitek2019]
		- Norman Peitek, "Matplotlib -- Save Plots as File," Future Studio, Fellner, P{\"{o}}hls, Peitek GbR, Magdeburg, Saxony-Anhalt, Germany, August 5, 2019. Available online from *Future Studio: Future Studio Tutorials* at: https://futurestud.io/tutorials/matplotlib-save-plots-as-file; January 15, 2020 was the last accessed date.
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


# Import NumPy [NumPyDevelopers2018] [Berg2023]
import numpy as np
# Import pandas [Augspurger2018]
import pandas as pd
# Import Matplotlib [Hunter2016a].
import matplotlib.pyplot as plt
from matplotlib.collections import EventCollection
# Get the set of colors from: matplotlib.colors.TABLEAU_COLORS 
import matplotlib.colors as mcolors
# Import string package from the Python Standard Library.
import string






# Process the output file of Xyce circuit simulation results.
with open(simulation_results_filename, "r") as f_obj:
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

