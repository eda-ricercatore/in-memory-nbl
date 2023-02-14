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


	Use the user guide [Keiter2022, Table 7-4, pp.81, \S7.3.8] and
		reference guide [Keiter2022a] to`generate CSV files, instead
		of ".prn" files, which is difficult to process [Keiter2022a].

	This is because the default ".prn" (print-to-file) format stores
		data in columns that are not uniformly separated from each other.
	E.g., for each row, the whitespace between a pair of columns is
		different from another pair of columns.
	Hence, printing the Xyce circuit simulation results to a format
		with standardized separation between the columns, such as a
		comma, tab, or fixed amount of character space (or whitespace
		characters) makes input file processing a lot easier.




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






"""
	Process the input file containing Xyce circuit simulation results.

	Store the results in a pandas DataFrame.
"""
df = pd.read_table("./input-files/invert1.cir.csv", delimiter=",")
print(df)


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
#if len(temp_list_column_headers[2:]) >= len(mcolors.TABLEAU_COLORS):
#	print("	WARNING!!! There are not enough colors in matplotlib.colors.TABLEAU_COLORS to plot each field with a unique color.")




"""
	Plot the circuit simulation results [Hunter2016].

	When we plot the input and output signals, Vin and Vout, of the
		inverter on the same set of axes, they will overlap and make
		it hard to read the graphs/plots/functions separately.

	Consequently, we choose to use subplots to stack the graphs/plots/functions
		vertically, so that they would be easier to analyze/study/examine
		[TheMatplotlibDevelopmentTeam2023a, API Reference: matplotlib.pyplot: matplotlib.pyplot.subplots: Date tick labels].
"""
#fig, axs = plt.subplots(2,1)
fig, axs = plt.subplots(2,1, figsize=(10,10))
axs[0].plot(df["TIME"], df["{V(IN)+1.0}"], label="inverter $V_{in}$")
axs[1].plot(df["TIME"], df["{V(VOUT)+1.0}"], label="inverter $V_{out}$")


# Add the titles to the plots [Hunter2023].
axs[0].set_title('Plot of $V_{in}$ (V) against time $t$ (s)')
axs[1].set_title('Plot of $V_{out}$ (V) against time $t$ (s)')
# Add mathematical text to the plot [Hunter2023] [Hunter2023a].
#axs[0].text(300, 0.65, r'$V_{out}$ = $\neg$ $V_{in}$')
#axs[1].text(300, 0.65, r'$V_{out}$ = $\neg$ $V_{in}$')
fig.text(300, 0.65, r'$V_{out}$ = $\neg$ $V_{in}$')
# Label the y-axis for both subplots.
axs[0].set_ylabel('$V_{in}$ (V)')
axs[1].set_ylabel('$V_{out}$ (V)')
# Label the x-axis for both subplots.
axs[0].set_xlabel('time $t$ (s)')
axs[1].set_xlabel('time $t$ (s)')
# Add a legend to both subplots [Hunter2023b].
axs[0].legend(title='Function plotted:')
axs[1].legend(title='Function plotted:')
"""
  Save plot in PDF format [Peitek2019] [Peitek2019a].
	This "save to PDF" command has to appear before the .show() command;
		else, the PDF file would be empty.
"""
plt.savefig("output-files/"+"cmos-inverter-vout-vin"+".pdf")
# Show the plot via GUI representation and the file plot.
plt.show()