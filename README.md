# in-memory-nbl

In-memory computing with noise-based logic



## Description of Repository's Contents

+ Jupyter notebook, *in_memory_nbl.ipynb*, contains experimental results.
	Or rather, simulation results.
+ source subdirectory
	- source code for the siumulation.
	- incremental_test.py
		* Used to perform automated regression testing of Python modules
			(for my hardware simulation, or simulation of NBL logic circuits)
		* Call the *Python* script as follows to perform automated regression
			testing: ***./incremental_test.py***.
	- doxygen.config
		* configuration file *Doxygen* to automatically produce/synthesize/generate
			documentation for the *Python*-based simulator. 
	- makefile
		* for build automationd
+ notes
	- guidelines
		* guidelines for collaboration
	- report
		* paper based on the NBL design.
