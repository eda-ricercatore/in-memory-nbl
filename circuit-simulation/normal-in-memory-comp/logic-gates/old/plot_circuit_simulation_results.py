#!/Users/zhiyang/anaconda3/bin/python3

"""
	This Python script is written by Zhiyang Ong to process and
		plot Xyce circuit simulation results.


	@modified by Zhiyang Ong, January 15, 2020.
	+ Modify code to process Xyce circuit simulation results,
		for a circuit with one input parameter.


	References:
	+ \cite[From Lines, bars and markers: EventCollection Demo]{MatplotlibDevelopmentTeam2020a}
		- https://matplotlib.org/gallery/lines_bars_and_markers/eventcollection_demo.html;
			Last accessed on January 16, 2020.
"""



import matplotlib.pyplot as plt
from matplotlib.collections import EventCollection
import numpy as np


"""
	Database list of circuit simulation results.
	Each entry in the list is a dictionary, where its key is the
		column header and its value is a list of data associated
		with that column in the output file of Xyce circuit
		simulation results. 
"""
simulation_results_database = []
# Path to Xyce circuit
filename = "inverter_transient.spice.prn"
with open(filename, "r") as f_obj:
	simulation_results = f_obj.readlines()
	for current_line in simulation_results:
		if "Index       TIME" in current_line:
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
				temp_column = {current_column_header: []}
				simulation_results_database.append(temp_column)
		elif "End of Xyce(TM) Simulation" in current_line:
			print("Finish processing Xyce circuit simulation results.")
		else:
			# Current enumerated row of circuit simulation results.
			temp_row_of_cir_sim_res = current_line.split()
			"""
				Store the data for each column in this row into
					the appropriate dictionary in the 
			"""
			for current_column_header in temp_list_column_headers[1:]:
	print("=	Circuit simulation results:")
	print(simulation_results_database)


"""
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

# plot the data
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(xdata1, ydata1, color='tab:blue')
ax.plot(xdata2, ydata2, color='tab:orange')

# create the events marking the x data points
xevents1 = EventCollection(xdata1, color='tab:blue', linelength=0.05)
xevents2 = EventCollection(xdata2, color='tab:orange', linelength=0.05)

# create the events marking the y data points
yevents1 = EventCollection(ydata1, color='tab:blue', linelength=0.05,
                           orientation='vertical')
yevents2 = EventCollection(ydata2, color='tab:orange', linelength=0.05,
                           orientation='vertical')

# add the events to the axis
ax.add_collection(xevents1)
ax.add_collection(xevents2)
ax.add_collection(yevents1)
ax.add_collection(yevents2)

# set the limits
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])

ax.set_title('line plot with data points')

# display the plot
plt.show()
"""
