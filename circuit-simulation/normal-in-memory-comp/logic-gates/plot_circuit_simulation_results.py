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



	References:
	+ \cite[From Lines, bars and markers: EventCollection Demo]{MatplotlibDevelopmentTeam2020a}
		- https://matplotlib.org/gallery/lines_bars_and_markers/eventcollection_demo.html;
			Last accessed on January 16, 2020.
"""


###############################################################
#	Import packages and modules Python libraries
import matplotlib.pyplot as plt
from matplotlib.collections import EventCollection
# Get the set of colors from: matplotlib.colors.TABLEAU_COLORS 
import matplotlib.colors as mcolors
import numpy as np


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
				simulation_results_database[current_name_of_field].append(current_field_of_current_row)


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
	for index, (current_field_name,current_field_data,enumerated_color) in enumerate(zip(temp_list_column_headers[2:],simulation_results_database,mcolors.TABLEAU_COLORS)):
		print(":	current_field_name:",current_field_name,".")
		# Name of the field/column.
		print(":	temp_list_column_headers[index]:",temp_list_column_headers[index+1],".")
		# Data set for the field/column.
		print(":	simulation_results_database[current_field_name]:",simulation_results_database[current_field_name],".")
		print("	current color:",enumerated_color,".")
		ax.plot(temp_list_column_headers[1], simulation_results_database[current_field_name], enumerated_color)
		xevents1 = EventCollection(xdata1, color='tab:blue', linelength=0.05)
		yevents1 = EventCollection(ydata1, color='tab:blue', linelength=0.05, orientation='vertical')
		ax.add_collection(xevents1)
		ax.add_collection(yevents1)
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
	ax.set_xlim([0, 1])
	ax.set_ylim([0, 1])
	ax.set_title('line plot with data points')
	# display the plot
	plt.show()

