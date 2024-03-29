#	Xyce Circuit Simulation




## Xyce/SPICE Preliminaries

Input files for SPICE-like circuit simulators are referred to as SPICE decks [Weste2011, from Chapter 8 Circuit Simulation: \S8.2 A SPICE Tutorial, pp. 288].

A netlist is a representation of a circuit in textual form [Weste2011, from Chapter 1 Introduction: \S1.9 Circuit Design, pp. 42].
+ A SPICE netlist provides more details "for delay and power simulations" than Verilog netlists [or those in VHDL, SystemVerilog, or SystemC] [Weste2011, from Chapter 1 Introduction: \S1.9 Circuit Design, pp. 42]
+ Comparison of post-synthesis/postsynthesis gate-level netlist and transistor-level netlist [Weste2011, from Chapter 1 Introduction: \S1.11 Design Verification, pp. 53].
+ Discussion of extracted, transistor-level SPICE netlists [Weste2011, from Chapter 3 CMOS Processing Technology: \S3.5 Technology-Related CAD Issues: \S3.5.2 Circuit Extraction, pp. 133].
+ Transistor-level SPICE netlists can be extracted from schematics or IC layout designs [Weste2011, from Chapter 8 Circuit Simulation: \S8.2 A SPICE Tutorial, pp. 288].
	- Transistor-level SPICE netlists [Weste2011, from Chapter 15 Testing, Debugging, and Verification: \S15.9 Pitfalls and Fallacies, pp. 691].
+ Simulation netlists [Weste2011, from Chapter 8 Circuit Simulation: \S8.2 A SPICE Tutorial: \8.2.1 Sources and Passive Components, pp. 289] [Weste2011, from Chapter 8 Circuit Simulation: \S8.2 A SPICE Tutorial: \8.2.3 Inverter Transient Analysis, pp. 293-294] [Weste2011, from Chapter 8 Circuit Simulation: \S8.2 A SPICE Tutorial: \8.2.4 Subcircuits and Measurement, pp. 295-296] [Weste2011, from Chapter 8 Circuit Simulation: \S8.2 A SPICE Tutorial: \8.2.5 Optimization, pp. 297] [Weste2011, from Chapter 8 Circuit Simulation: \S8.3 Device Models: \8.3.5 Design Corners, pp. 302] [Weste2011, from Chapter 8 Circuit Simulation: \S8.4 Device Characterization: \8.4.4 Parasitic Capacitance, pp. 309] [Weste2011, from Chapter 8 Circuit Simulation: \S8.5 Circuit Characterization: \8.5.3 Logical Effort, pp. 316] [Weste2011, from Chapter 8 Circuit Simulation: \S8.6 Interconnect Simulation, pp. 321].
+ Use tools for version control, revision control, or software configuration management to backup SPICE decks that have been chracterized for the semiconductor manufacturing process technology that the IC design team is using; the characterization is done by characterizing simple circuits, such as fanout-of-4 (FO4) inverters [Weste2011, from Chapter 8 Circuit Simulation: \S8.7 Pitfalls and Fallacies, pp. 323].
+ structural gate-level netlists in HDL (e.g., Verilog or VHDL) [Weste2011, from Chapter 14 Design Methodology and Tools: \S14.4 Design Flows: \S14.4.1 Behavioral Synthesis Design Flow (ASIC Design Flow), pp. 638].
	- structural netlists in HDL [Weste2011, from Chapter 14 Design Methodology and Tools: \S14.4 Design Flows: \S14.4.1 Behavioral Synthesis Design Flow (ASIC Design Flow): \S14.4.1.3 Functional or Formal Verification, pp. 639] [Weste2011, from Chapter 14 Design Methodology and Tools: \S14.4 Design Flows: \S14.4.2 Automated Layout Generation, pp. 641].









##	Installing Xyce Circuit Simulator

port install gcc9 libgcc9
port install openmpi openmpi-gcc9 


https://wiki.helsinki.fi/display/HUGG/GNU+compiler+install+on+Mac+OS+X
https://wiki.helsinki.fi/display/HUGG/Open+MPI+install+on+Mac+OS+X

https://nanohub.org/resources/20605/watch?resid=20606

https://ultimateelectronicsbook.com/



Jaijeet Roychowdhury
+ https://pdfs.semanticscholar.org/99f3/e1ceae1f3df746c2e9e9c1699bb85a44cf22.pdf
	- has inverter example
	- jaijeet-roychowdhury
	- http://www.mos-ak.org/berkeley_2016/publications/T03_Wang_MOS-AK_Berkeley_2016.pdf

https://www.fabrice-salvaire.fr/en/about/

http://www-ise1.ist.osaka-u.ac.jp/~j-chen/
+ http://www-ise1.ist.osaka-u.ac.jp/~j-chen/EDA_Tool_Cookbook.pdf 






https://xyce.sandia.gov/downloads/Binaries.html

Silicon Integration Initiative, Inc.
+ Projects.Si2.org
	- Compact Model Coalition, CMC,
		* Public Models Releases
			+ CMC Standard Device Models
				- http://www.bdmc.berkeley.edu/
					* http://www.bdmc.berkeley.edu/model-download/bsim-bulkbdmc106-2-0-bdmc1/
		* CMC Open Standards/CMC Developers and Models: CMC Public Distributions: 
			+ https://projects.si2.org/cgi-bin/openeda.si2.org/download?group_id=87&file_id=2354&filename=CMC_StandardModelFileFormat_v0_0_0.pdf
	- Other Projects
		* Open Modeling Publications
			+ Statistical Methods For Semiconductor Chip Design V1.0:
	- LEF/DEF Downloads have been moved to www.si2.org/OpenAccess
		* Reference: https://projects.si2.org/other_projects_index.php
+ https://jpduarte.github.io/
	- My main interest is a fusion of the device, circuit, and system co-design areas. This integrated area has gained a major role in the current development of new hardware in machine learning applications. I received my B.Sc. and M.Sc. degrees from KAIST, South Korea. There, I had the pleasure to work with Professor Yang-Kyu Choi. While in Korea, I focused my education and research in semiconductor devices. Currently, I'm at my last semester under advisement of Professor Chenming Hu and also a member of the Professor Sayeef Salahuddin's group. 
+ NXP
	- SiMKit library
		* https://www.nxp.com/design/software/models/simkit/source-code-library:SOURCE-CODE-LIBRARY
		* https://www.nxp.com/design/software/models/simkit:SIMKIT
		* https://www.nxp.com/design/software/models/simkit/compact-models:COMPACT-MODELS
+ Mextram: http://mextram.ewi.tudelft.nl/page_Implementation.php
+ https://en.wikipedia.org/wiki/Transistor_model



Compact models:
+ https://www.taylorfrancis.com/books/9781315215181






##	Running Xyce Circuit Simulator


To run the *Xyce* circuit simulator from the command line interface (CLI), the Xyce executable would be run with the (circuit) netlist.


To customize this, we can use the UNIX shebang (or sharp-exclamation, sha-bang, hashbang, pound-bang, hash-piling) "#!" [WikipediaContributors2017a] to run the *Xyce* circuit simulator on this netlist as if this netlist were a script.

The command line arguments for *Xyce* are provided in [Keiter2022a, from Chapter 2, Section \S3, Table 3.1, pp. 765-766].
+ Avoid using the "-l" option (pp. 765) to store the log output into a specified (text) file.
	- It is easy for people to fail to update the path for the log file for each parameter configuration for the experiments involving *Xyce* circuit simulation.
	- However, for large circuits or other circuit simulation setup conditions that take a long time to simulate, this option allows us to record what happened and facilitate debugging. It also enables us to avoid printing a lot of information to the Terminal that can be hard to uniquely read and process when we run too many circuit simulations in a fairly short period of time.
	- ***Bottom line: When deciding whether to use this option, create a plan for updating the parameter value for this option.***
		* UNIX shebang approach: Use a script to update the UNIX shebang.
		* Build automation approach (e.g., Makefile): Use a script or *Make*-supported "for loop"s to iterate/enumerate a list of filenames.
+ When using the "-o" option (pp. 765), check that the path of the output path is correct.
	- When doing experiments with *Xyce* circuit simulation, check that it (especially the filename) reflects the parameter configuration.
	- Information on using the ".print" statement [Keiter2022, from Chapter 9 Results Output and Evaluation Options: \S9.1 Control of Results Output: \S9.1.1 .print Command, pp. 154-158] to specify printing circuit simulation results to the output file.
		* Table 9-2 (page 156) indicates how to use this parameter to print/save the circuit simulation results in output file(s). It also specifies the output file format that we can save the circuit simulation results [Keiter2022, from Chapter 9 Results Output and Evaluation Options: \S9.1 Control of Results Output: \S9.1.1 .print Command, Table 9-2, pp. 156].
		* Output file formats (specified in Table 9-2, on page 156) are [Keiter2022a, from Chapter 2 Netlist Reference: \S2.1 Netlist Commands: \S2.1.31 ".print" (Print output): Comments, pp. 127-128] [Keiter2022, from Chapter 9 Results Output and Evaluation Options: \S9.1 Control of Results Output: \S9.1.1 .print Command, Table 9-3, pp. 156]:
			+ Default file format: NOINDEX, ".prn"
			+ CSV file format: ".csv"
			+ RAW file format: ".raw"
			+ TECPLOT file format: ".dat"
			+ PROBE file format: ".csd"
		* [Keiter2022, from Chapter 9 Results Output and Evaluation Options: \S9.1 Control of Results Output: \S9.1.3 Output File Redirection, pp. 159-161]
			+ When both "-o" and "-r" command line arguments/options are used, the "-r" command line argument/option would only use its value to store the Xyce circuit simulation in the raw/binary format [Keiter2022, from Chapter 9 Results Output and Evaluation Options: \S9.1 Control of Results Output: \S9.1.3 Output File Redirection: \S9.1.3.1 "-r" Output, pp. 160].
			+ The "-r" command line argument/option cannot override the Xyce netlist [Keiter2022, from Chapter 9 Results Output and Evaluation Options: \S9.1 Control of Results Output: \S9.1.3 Output File Redirection: \S9.1.3.1 "-r" Output, pp. 160].
			+ If the ".print sens" statement, ".print homotopy" statement, and the "-o" command line argument/option will have a greater priority over the "-r" command line argument/option, and would prevent usage of the "-r" command line argument/option [Keiter2022, from Chapter 9 Results Output and Evaluation Options: \S9.1 Control of Results Output: \S9.1.3 Output File Redirection: \S9.1.3.1 "-r" Output, pp. 160].
				- This is because the ".print sens" statement and the ".print homotopy" statement do not support raw file output in their analysis types.
				- The ***set of analyses that can be done by the Xyce circuit simulator*** is provided in [Keiter2022a, from Chapter 2 Netlist Reference: \S2.1 Netlist Commands: \S2.1.31 ".print" (Print output), pp. 126-142].
					* AC analysis [Keiter2022a, from Chapter 2 Netlist Reference: \S2.1 Netlist Commands: \S2.1.31 ".print" (Print output): \S2.1.31.1 Print AC Analysis, pp. 134-135].
					* DC analysis [Keiter2022a, from Chapter 2 Netlist Reference: \S2.1 Netlist Commands: \S2.1.31 ".print" (Print output): \S2.1.31.2 Print DC Analysis, pp. 135].
					* harmonic balance analysis [Keiter2022a, from Chapter 2 Netlist Reference: \S2.1 Netlist Commands: \S2.1.31 ".print" (Print output): \S2.1.31.3 Print Harmonic Balance Analysis, pp. 136-137].
					* noise analysis [Keiter2022a, from Chapter 2 Netlist Reference: \S2.1 Netlist Commands: \S2.1.31 ".print" (Print output): \S2.1.31.4 Print Noise Analysis, pp. 138].
					* transient analysis [Keiter2022a, from Chapter 2 Netlist Reference: \S2.1 Netlist Commands: \S2.1.31 ".print" (Print output): \S2.1.31.5 Print Transient Analysis, pp. 138].
					* homotopy [Keiter2022a, from Chapter 2 Netlist Reference: \S2.1 Netlist Commands: \S2.1.31 ".print" (Print output): \S2.1.31.6 Print Homotopy, pp. 139].
					* sensitivity [Keiter2022a, from Chapter 2 Netlist Reference: \S2.1 Netlist Commands: \S2.1.31 ".print" (Print output): \S2.1.31.7 Print Sensitivity, pp. 139-141].
					* embedded sampling analysis [Keiter2022a, from Chapter 2 Netlist Reference: \S2.1 Netlist Commands: \S2.1.31 ".print" (Print output): \S2.1.31.8 Print Embedded Sampling Analysis, pp. 141].
					* Intrusive PCE analysis [Keiter2022a, from Chapter 2 Netlist Reference: \S2.1 Netlist Commands: \S2.1.31 ".print" (Print output): \S2.1.31.9 Print Intrusive PCE analysis, pp. 142].
					* This is also summarized in Table 9-1 of [Keiter2022, from Chapter 9 Results Output and Evaluation Options: \S9.1 Control of Results Output: \S9.1.1 .print Command, Table 9-1, pp. 155]
	- Additional information on the command line argument "-o" is found at: [Keiter2022, from Chapter 9 Results Output and Evaluation Options: \S9.1 Control of Results Output: \S9.1.3 Output File Redirection: \S9.1.3.2 "-o" Output, pp. 160].
		* Xyce does not allow this command line argument to override the Xyce netlist.
	- The command line argument "-r" saves the output file in the raw file format [Keiter2022a, from Chapter 2 Netlist Reference: \S2.1 Netlist Commands: \S2.1.31 ".print" (Print output): Comments, pp. 132], and its combined usage with the "-a" option stores Xyce circuit simulation results in ASCII characters.
		* This can be used to specify an output file for each type/mode of analysis [Keiter2022a, from Chapter 2 Netlist Reference: \S2.1 Netlist Commands: \S2.1.31 ".print" (Print output): pp. 126-127], such as AC and HB [Keiter2022a, from Chapter 2 Netlist Reference: \S2.1 Netlist Commands: \S2.1.31 ".print" (Print output): Comments, pp. 128].
			+ The AC and harmonic balance analysis types/modes can produce multiple files for each analysis type/mode [Keiter2022, from Chapter 9 Results Output and Evaluation Options: \S9.1 Control of Results Output: \S9.1.3 Output File Redirection: \S9.1.3.4 Multi-File Output for AC and HB Analysis, pp. 161].
	- When the CSV FORMAT is specified, and the "-o" command line argument/option is indicated, it will still print to a ".prn" output file (in the print-to-file format) with the ".prn" file extension added to the filename/path specified by the "-o" command line argument/option.
	- When the CSV FORMAT is specified, without specification of the "-o" command line argument/option, it will print to a ".csv" output file (in the CSV format) in the location/directory of the netlist.
	- ***To print the output file in the CSV format in the desired location, do not use the "-o" command line argument/option, and use the file argument of the ".print" statement to print the CSV output file in the specified location.***












***Guidelines and recommendations***:
+ The use of asterisk indicates multiple instances of something (e.g., a parameter or device) [Keiter2022a, from Chapter 5 Introduction: \S1.3 Typographical conventions, Table 1-1, pp. 20]
+ [Keiter2022a, from Chapter 5, Subsection \S5.1.1, pp. 765--766] suggests using the same values for ***RELTOL*** and ***ABSTOL*** in the TIMEINT and NONLIN-TRAN .OPTIONS statements.
	- Choose the value of ***RELTOL***, so that *RELTOL = 1.0E-(m+1)* and *m* is the desired number of siginificant digits of accuracy.
	- Set *ABSTOL* to be the smallest value for components in the integrated circuit (IC).
	- Select ***ABSTOL < RELTOL***.
+ [Keiter2022a, from Chapter 2 Netlist Reference: \S2.1 Netlist Commands: \S2.1.37 .subckt (subcircuit), pp. 157-158].
	- ".subckt" statements begin with ".subckt" and ends with ".ends".
	- ".subckt" statements can be nested/embedded within other ".subckt" statements.
	- ".subckt" statements should only include device instantiations, and possibly the following statements (limited to use within the subcircuits).
		* ".model" statements for model definition.
			+ Use ".model" statements to include user-defined models of semiconductor devices [Keiter2022, \S4.2, pp. 42].
		* ".param" statements for parameters.
		* ".func" statements for functions.
	- Format:
		* .subckt [name] [node]*
		* + [params: [param_name]=[param_value]]
		* .ends
	- Use ".subckt" statements for macromodels, such as circuit models of semiconductor devices, or actual subcircuits (or subsystems to be incorporated into electronic/electrical systems) [Keiter2022, \S4.2, pp. 42].
+ Global parameters can be defined using the ".GLOBAL_PARAM" statement [Keiter2022a, from Chapter 2 Netlist Reference: \S2.1 Netlist Commands: \S2.1.12 .GLOBAL_PARAM (Global parameter), pp. 43-44].
	- "Reserved words that [cannot] be used as names for parameters":
		* Time
		* Freq
		* Hertz
		* Vt
		* Temp
		* Temper
		* GMIN
	- Global parameters cannot be redefined (p.. 44).
	- Definitions of ".PARAM" at "the top level netlist is equivalent to" those of ".GLOBAL_PARAM" definitions (pp. 43).
+ Parameters can be defined using the ".PARAM" statement [Keiter2022a, from Chapter 2 Netlist Reference: \S2.1 Netlist Commands: \S2.1.26 .PARAM (Parameter), pp. 118-119].
	- While parameters can be redefined, the last parameter definition would be used. Warnings are not provided for this, unless specified with the "*-redefined_param* command line option".
	- Interpolators can use data stored in a file for numerical interpolation (pp. 118).
	- "Reserved words that [cannot] be used as names for parameters" (pp. 118-119):
		* Time
		* Freq
		* Hertz
		* Vt
		* Temp
		* Temper
		* GMIN
	- Definitions of ".PARAM" at "the top level netlist [or 'main circuit netlist'] is equivalent to" those of ".GLOBAL_PARAM" definitions, and can be accessed by the main circuit and all subcircuits (pp. 119).
	- ".PARAM" definitions in subcircuits are limited to the scope of these subcircuits and nested/embedded subcircuits (pp. 119).
	- From [Keiter2022, from Chapter 4 Netlist Basics: \S4.3 Parameters and Expressions, pp. 44-47], parameters and expressions can only specify numeric values [Keiter2022, from Chapter 4 Netlist Basics: \S4.3 Parameters and Expressions, pp. 44] [Keiter2022, from Chapter 4 Netlist Basics: \S4.3 Parameters and Expressions: \S4.3.1 Parameters, pp. 44]
+ ***Information about the description of components, including subcircuits and semiconductor devices, including their prefixes for their variable names*** [Keiter2022a, from Chapter 2 Netlist Reference: \S2.3 Devices, Table 2-34, pp. 174-175].
	- Information about the *Xyce* circuit simulation features that are supported by a list of *Xyce* device models, such as MOSFETs and memristors [Keiter2022a, from Chapter 2 Netlist Reference: \S2.3 Devices, Table 2-35, pp. 176-179]:
		* branch current
		* power
		* analytic sensitivity
		* stationary noise
	- Supported multigate MOSFET transistors, or multigate devices, or multigate field-effect transistors (MuGFET)
		* ***Determine how to implement the following***:
			+ ***FinFETs***, non-planar transistors or 3-D transistors
				- The inverter example shows how it works.
				- ***Determine how to scale it to smaller dimensions***, such as 10 nm FinFETs and 5 nm FinFETs.
			+ ***gate-all-around field-effect transistor, GAAFET*** (preferred) or GAA FET, non-planar transistors or 3-D transistors
			+ ***multiple-independent-gate field-effect transistor (MIGFET)***
				- Can support advanced data structures for logic synthesis and verification based on XOR gates and majority gates.
					* They are more efficient representations of boolean functions.
					* majority-inverter graphs, MIGs
					* XOR-AND graphs, XAGs
					* XOR-majority graphs, XMGs
					* majority-inverter graphs, MIGs
		* [Keiter2022a, from Chapter 2 Netlist Reference: \S2.3 Devices: \S2.3.20 MOS Field Effect Transistor (MOSFET): \S2.3.20.13 Level 110 MOSFET Tables (BSIM CMG version 110.0.0), pp. 562-598] is the preferred multi-gate MOSFET device.
			+ Indicated as a FinFET device on page 562.
			+ Use MOSFET (Level 110) [Keiter2022a, from Chapter 2 Netlist Reference: \S2.3 Devices, Table 2-35, pp. 178]
		* [Keiter2022a, from Chapter 2 Netlist Reference: \S2.3 Devices: \S2.3.20 MOS Field Effect Transistor (MOSFET): \S2.3.20.14 Level 107 and 108 MOSFET Tables (BSIM CMG versions 107.0.0 and 108.0.0), pp. 598-662].
			+ Indicated as a FinFET device on page 599 (BSIM CMG versions 107.0.0).
			+ Indicated as a FinFET device on page 629 (BSIM CMG versions 108.0.0).
+ To use multiple instances of the same device, see [Keiter2022, from Chapter 4 Netlist Basics: \S4.4 Device Multiplier M, Table 4-3, pp. 47]
+ Use subcircuits to facilitate reading and maintenance of SPICE decks [Weste2011, from Chapter 8 Circuit Simulation: \S8.2 A SPICE Tutorial: \8.2.4 Subcircuits and Measurement, pp. 295]
+ Include (extracted) SPICE simulation netlists as (sub)circuits to be included in the main SPICE decks (use the .include statement) [Weste2011, from Chapter 8 Circuit Simulation: \S8.2 A SPICE Tutorial: \8.2.4 Subcircuits and Measurement, pp. 295]












***Suggested reading***:
+ [Logic Synthesis for Digital In-Memory Computing](http://www.cs.utsa.edu/~jha/papers/2022_Jha_ICCAD_LogicSynthesisInMemoryComputingHybrid.pdf)
+ [Logic Synthesis for Established and Emerging Computing](https://si2.epfl.ch/~demichel/publications/archive/2019/08478240.pdf)
	- https://si2.epfl.ch/~demichel/research/logic.html
+ [New Logic Synthesis as Nanotechnology Enabler](https://infoscience.epfl.ch/record/210272?ln=en)
	- BBDD, biconditional binary decision diagrams, biconditional BDDs
	- SWD, spin-wave devices
	- area-delay-power product, ADP product
+ FO4 inverter, Fanout-of-4 inverters
	- schematic design of FO4 inverters [Weste2011, from Chapter 4 Delay: \S4.3 RC Delay Model: \4.3.5 Elmore Delay, Example 4.6, pp. 151]
	- circuit delay of FO4 inverters is $5\tau$ [Weste2011, from Chapter 4 Delay: \S4.3 RC Delay Model: \4.3.5 Elmore Delay, pp. 152]
		* $\tau$ refers to the RC delay of a first-order RC circuit, and is used to estimate the propagation delay (Equation 4.9 on page 149) [Weste2011, from Chapter 4 Delay: \S4.3 RC Delay Model: \4.3.4 Transient Response, pp. 148-149]
			+ Estimate "process parameter" (that estimates transistor delay) [Sutherland1999, from Chapter 1 The Method of Logical Effort: \S1.1 Delay in a logic gate, pp. 3] or time $\tau$ from the characteristics of the semiconductor manufacturing process based on the following characteristics [Sutherland1999, from Chapter 3 Deriving the Method of Logical Effort: \S3.2 Delay in a logic gate, pp. 45]:
				- transistor length
				- transistor width
				- gate oxide thickness
				- mobility
				- "other [semiconductor manufacturing] process parameters"
				- IC designers can use SPICE-like circuit simulation of a transistor-level IC implementation of an inverter to characterize the value of $\tau$ and the parasitic delay of an inverter $p_{inv}$ [Sutherland1999, from Chapter 5 Calibrating the Model: \S5.1 Calibration technique, pp. 81]. This process is also known as inverter characterization [Sutherland1999, from Chapter 5 Calibrating the Model: \S5.1 Calibration technique, pp. 82].
			[Sutherland1999, from Chapter 5 Calibrating the Model: \S5.1 Calibration technique, pp. 81-83]
		* Inverter delay is estimated to be 0.2 FO4 inverter delay [Weste2011, from Chapter 4 Delay: \S4.4 Linear Delay Model: \4.4.3 Delay in a Logic Gate, Example 4.10, pp. 158]
			+ FO4 delay, or FO4 inverter delay, is cited for "typical process parameters and worst-case environments (low power supply voltage and high temperature)" [Weste2011, from Chapter 4 Delay: \S4.4 Linear Delay Model: \4.4.3 Delay in a Logic Gate, pp. 158]
			+ FO4 delay, or FO4 inverter delay, is approximately 1/3 or 1/2 the drawn channel length [Weste2011, from Chapter 4 Delay: \S4.4 Linear Delay Model: \4.4.3 Delay in a Logic Gate, pp. 158]
		* Comparisons of FO4 inverter delay across semiconductor manufacturing process technologies by different companies, from 2 um to 65 nm [Weste2011, from Chapter 8 Circuit Simulation: \S8.4 Device Characterization: \8.4.6 Comparison of Processes, Table 8.5, pp. 312] 
			+ Comparisons of FO4 inverter delay and $\tau$ [Weste2011, from Chapter 8 Circuit Simulation: \S8.5 Circuit Characterization: \8.5.3 Logical Effort, Table 8.8, pp. 318]
			+ Determine statistical delay distribution of FO4 inverter delay via Monte Carlo simulation or other parameter sweep approaches [Weste2011, from Chapter 8 Circuit Simulation: \S8.5 Circuit Characterization: \8.5.6 Monte Carlo Simulation, pp. 319]
				- Good semiconductor device models have parameters to account for inter-die semiconductor manufacturing process variations (or, die-to-die process variations) and/or intra-die semiconductor manufacturing process variations (or, within-die process variations) [Weste2011, from Chapter 8 Circuit Simulation: \S8.5 Circuit Characterization: \8.5.6 Monte Carlo Simulation, pp. 319]
		* The delay of unloaded inverters is about 0.2 (or 20%) of FO4 inverter delay; hence, delay estimation/analysis via SPICE simulation need to specify the estimated load of the final stage [Weste2011, from Chapter 8 Circuit Simulation: \S8.7 Pitfalls and Fallacies: Applying inappropriate output loading, pp. 323]
		* Used for characterizing sequential elements, such as flip-flops [Weste2011, from Chapter 10 Sequential Circuit Design: \S10.4 Static Sequencing Element Methodology: \S10.4.2 Characterizing Sequencing Element Delays, pp. 405]
		* For characterizing circuits in the data path:
			+ static CMOS full adders, 2-3 FO4 inverter delay [Weste2011, from Chapter 11 Datapath Subsystems: \S11.2 Addition/Subtraction: \S11.2.1 Single-Bit Addition, pp. 434]
			+ domino CMOS full adders, 1.5 FO4 inverter delay [Weste2011, from Chapter 11 Datapath Subsystems: \S11.2 Addition/Subtraction: \S11.2.1 Single-Bit Addition, pp. 434]
			+ good 64-bit domino adder, 7-9 FO4 inverter delay [Weste2011, from Chapter 11 Datapath Subsystems: \S11.2 Addition/Subtraction: \S11.2.2 Carry-Propagate Addition: \S11.2.2.13 Summary, pp. 457]
			+ static adders, 13 FO4 inverter delay, 1/3 to 10% of energy consumption by dynamic adders, trade-off between energy efficiency and delay [Weste2011, from Chapter 11 Datapath Subsystems: \S11.2 Addition/Subtraction: \S11.2.2 Carry-Propagate Addition: \S11.2.2.13 Summary, pp. 457]
			+ 32-bit tree adders, pre-layout delays of 7 FO4 inverter delay [Weste2011, from Chapter 11 Datapath Subsystems: \S11.2 Addition/Subtraction: \S11.2.2 Carry-Propagate Addition: \S11.2.2.13 Summary, pp. 458]
			+ 64-bit tree adders, pre-layout delays of 8.5 FO4 inverter delay [Weste2011, from Chapter 11 Datapath Subsystems: \S11.2 Addition/Subtraction: \S11.2.2 Carry-Propagate Addition: \S11.2.2.13 Summary, pp. 458]
		* ***SPICE deck/netlist for simulating FO4 inverter***, and alternate schematic for FO4 inverter (pp. 295) [Weste2011, from Chapter 8 Circuit Simulation: \S8.2 A SPICE Tutorial: \8.2.4 Subcircuits and Measurement, Figure 8.10, pp. 296] [Weste2011, from Chapter 8 Circuit Simulation: \S8.2 A SPICE Tutorial: \8.2.4 Subcircuits and Measurement, pp. 294-296]
	- Reference: [Hrishikesh2002] explains the optimal logic depth for each pipeline stage







##	Output Files


+ The user guide [Keiter2022, from Table 7-4, pp.81, \S7.3.8] provides options to print the Xyce circuit simulation results in different formats.
	- E.g., we can use the option to print the Xyce circuit simulation results in CSV format, instead of the default ".prn" (print-to-file) format.
+ \cite[\S7.4.6., pp. 73, "Output files" section]{Keiter2019a}
	- "The output data, as specified by a .PRINT line, however, goes to a single (*.prn) file. For convenience, Xyce also creates a second auxilliary file with the *.res suffix."
	- "Figure 7-3 shows an example file named clip.cir, which when run will produce fildes clip.cir.res and clip.cir.prn. The file clip.cir.res contains one line for each step, showing what parameter value was used on that step. clip.cir.prn is the familiar output format, but the INDEX field recycles to zero each time a new step begins."
	- "As the default behavior distinguishes each step’s output only by recycling the INDEX field to zero, it can be beneficial to add the sweep parameters to the .PRINT line. For the default file format (format=std), Xyce will not automatically include these sweep parameters, so for plotting it is usually best to specify them by hand."
	- "If using the default .prn file format (format=std), the resulting .STEP simulation output file will be a simple concatenation of each step’s underlying analysis output. If using format=probe, the data for each execution of the circuit will be in distinct sections of the file, and it should be easy to plot the results using PROBE."
+ \cite[\S7.5.8., pp. 79-80, "Output files" section]{Keiter2019a}
	- pp. 79, "Figure 7-5 shows an example file named clip.cir, which when run will produce files clip.cir.res and clip.cir.prn. The file clip.cir.res contains one line for each step, showing what parameter value was used on that step. clip.cir.prn is the familiar output format, but the INDEX field recycles to zero each time a new step begins. As the default behavior distinguishes each step’s output only by recycling the INDEX field to zero, it can be beneficial to add the sampling parameters to the .PRINT line. For the default file format (format=std), Xyce will not automatically include these sampling parameters, so for plotting it is usually best to specify them by hand."
	- pp. 80, "Note that for sampling calculations involving a really large number of sample points, the single output file can become prohibitively large. Be careful when using .PRINT if the number of samples is large. If the number is really large (thousands) consider excluding any .PRINT output statements and just rely on statistical outputs, described next in section 7.5.9. Similarly, the generation of the measure output can be suppressedwith.OPTIONS MEASURE MEASPRINT."







##	Power Analysis

+ \cite[\S6.1.8, pp. 579]{Keiter2019a} describes how to measure power dissipation
	in a circuit/device.
+ https://www.researchgate.net/post/Is_it_possible_to_calculate_the_static_dynamic_power_dissipation_using_the_data_exported_from_SPICE_Deck
 + \cite[\S2.3, pp. 142-145, Table 2-31]{Keiter2019a}
	- Indicates whether each component in the Xyce device library supports
		power analysis. 













##	Netlists

+ https://github.com/Xyce
+ https://github.com/Xyce/Xyce_Regression/tree/master/Netlists
+ https://github.com/Xyce/Xyce/releases







##	Model Binning


From https://edadocs.software.keysight.com/pages/viewpage.action?pageId=5683982#
+ "BinModel allows you to sweep a parameter (usually a geometry, such as gate length), then enable the simulator to automatically select between different model cards. If a circuit contains nonlinear devices for circuit simulation, each device should be associated with one device model through schematic or netlist editing. However, modern processes require multiple models for different device sizes to improve simulation accuracy."
	- "Bin Model (Bin Model for Automatic Model Selection)"
		* From {\it Knowledge Center: ADS Support Home: ADS Documentation (all releases): Documentation: ADS 2008 Update 1: Introduction to Circuit Components: Circuit Components}.
		* From {\it Keysight Technologies: Technical Support Contact Center and Knowledge Base: Keysight EEsof EDA Knowledge Center: Advanced Design System Support Home: Advanced Design System Product Documentation: EEsof Advanced Design System 2008 Update 1 Documentation: Introduction to Circuit Components: Circuit Components}.
		* Keysight Technologies: Santa Rosa, CA.
		* 2019.
+ Automated Model Binning
	- "Automated Model Binning" article"
		* Simulation Standard, Volume 8, Number 1, January 1997
			+ Journal title: Simulation Standard.
		* https://www.silvaco.com/tech_lib_TCAD/simulationstandard/1997/jan/a3/a3.html
		* Silvaco, Inc.: Santa Clara, {CA}
		* 2020
		* "An automated SPICE model binning feature has been implemented in UTMOST III. Binning is used when the user decides to generate a separate model for each device and then combine them into groups by introducing L, W and P (WxL) parameters in a final combined model."
		* "The binning method is widely used for empirical models. Even though BSIM3v3 is a physical model, it also supports binning. It is possible to generate a single BSIM3v3 model which can be used for all geometries. The overall error of a single model may not be as low as binned models. However the single model is compact, easy to maintain and more physical than binned models. Both methods have advantages and disadvantages and users can choose between these two methods."
		* "Technical Library, Publications": https://www.silvaco.com/tech_lib/index.html
			+ Simulation Standard - 1997: https://www.silvaco.com/tech_lib_TCAD/simulationstandard/1997/index.html
			+ Simulation Standard - 2019: https://www.silvaco.com/tech_lib_TCAD/simulationstandard/2019/index.html
			+ Analog & Mixed Signal Recommended Textbooks: https://www.silvaco.com/tech_lib_EDA/kbase/AMS/recommendedTextbooks.html
			+ TCAD Recommended Textbooks: https://www.silvaco.com/tech_lib_TCAD/whitePapers/recommendedTextbooks.html
			+ Books Written Referencing Silvaco Software: https://www.silvaco.com/tech_lib_TCAD/books.html
			+ Digital CAD Recommended Textbooks: https://www.silvaco.com/tech_lib_EDA/kbase/logicVerification/recommendedTextbooks.html
			+ Silvaco Support
		* Silvaco: Silvaco Support: Technical Library, Publications
	- "Automated Model Binning" with Xyce
		* "Model binning is supported for MOSFET models. For model binning, the netlist contains a set of similar .MODEL cards which correspond to different sizing information (length and width). They are similar in that they are for the same model (and same LEVEL number), and have the same prefix. They are different in that they have different lmin,lmax,wmin,wmax parameters, and the name suffix will be the bin number. For a MOSFET device instance, Xyce will automatically select the appropriate binned model, based on the L and W parameters of that instance. It will only seach the models with matching name prefixes, and can only work if all the binned models have specified all the lmin,lmax,wmin,wmax parameters."
			+ \cite[\S2.1.18.2, pp. 65, subsubsubsection on, "Model Binning"]{Keiter2019a}
				- "Model binning is not enabled by default. To enable it, it is necessary to specify '.options parser model_binning=true.'"
				- Sample code for model card and simulating it.
			+ ".model" command for inductor, pp. 155.
		* \cite[\S6.1.6.2., "Model Parameter Sweeps", pp. 579]{Keiter2019a}
		* \cite[\S6.1.10, "Model Statements", pp. 580]{Keiter2019a}
	- \cite[\S5.4, "Model Interpolation", pp. 48-49]{Keiter2019}
+ Binning
	- Auto Model Selection: https://www.ee.columbia.edu/~harish/uploads/2/6/9/2/26925901/spectre_reference.pdf
		* "Spectre Circuit Simulator User Guide", Product Version 5.0, January 2004
		* Chapter 5, "Parameter Specification and Modeling Features"
		* "Binning is the process of partitioning a device with different sizes into different models. BeforeBSIM 3v3, it was very difficult to fit all the devices with a singlemodel statement over verywide ranges of device sizes. To improve fitting accuracy, you might characterize devices intoseveral models with each model valid only for a limited range of device sizes.", pp. 107, Chapter 5, Section on Binning, and Subsection on "Auto Model Selection". 
	









##	Additional Information

Sensitivity analysis and uncertainty quantification (UQ):
+ https://www.osti.gov/servlets/purl/1504833
+ https://www.osti.gov/servlets/purl/1244466





























#	Technology Libraries






##	Default/Built-in Importing Technology Library


List of tables in https://prod-ng.sandia.gov/techlib-noauth/access-control.cgi/2016/165198.pdf
+ Chapter/Section 2 has information about BSIM3, BSIM4, and BSIM6 device models, as well as memristor TEAM device models, and BSIM-CMG FinFETs (Table 2.88 and 2.89)



##	Instantiating Components


+ \cite[\S2.3, pp. 140-141, Table 2-30]{Keiter2019a}
	- Provides Information about how to instantiate components in Xyce's
		device/technology library.
+ \cite[\S4.2, pp. 35-37, Table 4-2]{Keiter2019}
	- Also, provides Information about how to instantiate components in Xyce's
	device/technology library.
+ Using FinFETs
	- \cite[\S2.3.20.12, pp. 431-432, Table 2-102]{Keiter2019a} describes the
		device instance parameters of the BSIM-CMG FinFETs.
		* The default feature size of the FinFET is 30 nm (3e-08 m).
		* \cite[\S2.3.20.12, pp. 431-432, Table 2-102]{Keiter2019a}






##	Importing Technology Libraries and Subcircuits


+ include
	- Location of process models for FinFET devices:
		* /Applications/apps/eda/technology_lib/pdk/ASAP7_PDKandLIB_v1p6/asap7PDK_r1p6/models/hspice
	- Location of extracted SPICE netlists of logic cells/gates:
		* /Applications/apps/eda/technology_lib/pdk/ASAP7_PDKandLIB_v1p6/lib_release_191006/asap7_7p5t_library/rev25/CDL/xAct3D_extracted/Extracted_netlists
	- \cite[\S5.3.2., pp. 46-47, "Model Library Configuration using .INCLUDE" section]{Keiter2019a}
		* ".include \[name of model library\]"
		* "Xyce uses model libraries by inserting an .INCLUDE statement into a netlist. Once a file is included, its contents become available to the netlist just as if the entire contents had been inserted directly into the netlist."
	- \cite[\S5.3.3., pp. 47, "Model Library Configuration using .LIB" section]{Keiter2019a}
		* "With .LIB, a library file can contain multiple versions of a model and specific versions may be selected at the top level using a keyword on the .LIB line."
			+ "There are two different uses for the .LIB command. In the main netlist, .LIB functions in a similar manner to .INCLUDE: it reads in a file. Inside that file, .LIB and .ENDL are used to specify blocks of model code that may be included independently of other parts of the same file."
				- I do not understand this statement.
	- \cite[\S2.1.14, pp. 39]{Keiter2019a}
		* .inc \[name of model library, or path to model library\]
		* .include \[name of model library, or path to model library\]
		* .inc '\[name of model library, or path to model library\]'
		* .include '\[name of model library, or path to model library\]'
		* .inc "\[name of model library, or path to model library\]"
		* .include "\[name of model library, or path to model library\]"
+ import
	- Note: *Xyce* commands ***do not correspond to the term, "import".***
+ .save statements
	- \cite[\12.5, pp. 160]{Keiter2019a}
		* consists/comprised of:
			+ .IC statements
			+ .nodeset statements
		* If user-specified output filename is not provided, *Xyce* uses the following
			filename: netlist.cir.ic.
		* Examples:
			+ .save type=ic 
	- \cite[]{}
		* To be completed.






##	Sizing FinFET Devices: Comparing Parameters of FinFETs and MOSFETs



As researchers continue to pursue the ongoing reduction/shrinking of the "minimum feature size" [Weste2011, from Chapter 1 Introduction: \S1.1 A Brief History, pp. 4] [Weste2011, from Chapter 1 Introduction: \S1.5 CMOS Fabrication and Layout, \S1.5.3 Layout Design Rules, pp. 25] in semiconductor manufacturing technology, and self-fulfill the Moore's law [Moore1965] [Moore1998] prophecy [Weste2011, from Chapter 1 Introduction: \S1.1 A Brief History, pp. 4], they are exploring different transistor architectures, such as FinFETs [Chauhan2015] and gate-all-around transistors (***Cite this!!!***).
+ We can add more devices to this paragraph.
+ [Another paraphrased expression] As researchers continue to pursue the ongoing reduction/shrinking of the "minimum feature size" [Weste2011, from Chapter 1 Introduction: \S1.1 A Brief History, pp. 4] [Weste2011, from Chapter 1 Introduction: \S1.5 CMOS Fabrication and Layout, \S1.5.3 Layout Design Rules, pp. 25] in semiconductor manufacturing technology, and abide by the self-fulfilling prophecy [Weste2011, from Chapter 1 Introduction: \S1.1 A Brief History, pp. 4] of Moore's law [Moore1965] [Moore1998], they are exploring different transistor architectures and devices, such as FinFETs [Chauhan2015] and gate-all-around transistors (***Cite this!!!***).



These new semiconductor devices can lead to new circuit designs (***Cite this!!!***), architecture designs (***Cite this!!!***), and enable design-technology co-optimization (DTCO) (***Cite this!!!***) and system-technology co-optimization (STCO) (***Cite this!!!***). DTCO and STCO can be supported by incorporating semiconductor device models, or compact models [Gildenblat2010], for these new/emerging semiconductor devices in circuit simulation tools. Consequently, these circuit simulation with these compact models can characterize macromodels of VLSI system architectures, processor architectures [Binkert2011] [gem5developers2014], and domain-specific architectures (or hardware accelerators).


To map circuit designs based on planar, bulk MOSFET devices to those using non-planar MOSFET devices, I would map the defining characteristics/properties/parameters of the former to the latter. Planar, bulk MOSFET devices are defined by the length and width of the MOSFET devices [Sutherland1999, from Chapter 1 The Method of Logical Effort: \S1.1 Delay in a logic gate, pp. 5] [Weste2011, from Chapter 1 Introduction: \S1.5 CMOS Fabrication and Layout, \S1.5.3 Layout Design Rules, pp. 26], while FinFET devices are defined by ... (***Complete This!!!***)
+ The defining quantifiable characteristics of MOSFET transistors are
[Weste2011, from Chapter 1 Introduction: \S1.5 CMOS Fabrication and Layout, \S1.5.3 Layout Design Rules, pp. 26] [Weste2011, from Chapter 1 Introduction: \S1.9 Circuit Design, pp. 45]:
	- length
	- width
	- These characteristics are used to specify the dimensions of MOSFET devices in schematics [Weste2011, from Chapter 1 Introduction: \S1.9 Circuit Design, pp. 43] [Weste2011, from Chapter 8 Circuit Simulation: \S8.2 A SPICE Tutorial, pp. 288] and transistor-level SPICE netlists [Weste2011, from Chapter 15 Testing, Debugging, and Verification: \S15.9 Pitfalls and Fallacies, pp. 691], which can be extracted from schematics of transistor-level circuit designs [Weste2011, from Chapter 8 Circuit Simulation: \S8.2 A SPICE Tutorial, pp. 288] or layout designs of integrated circuits [Weste2011, from Chapter 3 CMOS Processing Technology: \S3.5 Technology-Related CAD Issues: \S3.5.2 Circuit Extraction, pp. 133] [Weste2011, from Chapter 8 Circuit Simulation: \S8.2 A SPICE Tutorial, pp. 288] [Weste2011, from Chapter 8 Circuit Simulation: \S8.2 A SPICE Tutorial: \S8.2.4 Subcircuits and Measurement, pp. 295]
		* "Circuits [are] represented as schematic[s] [or] netlist[s]" [Weste2011, from Chapter 1 Introduction: \S1.9 Circuit Design, pp. 42]
		* schematic entry [Brodersen1992, from Chapter 4, pp. 35-44] [Jansen2003, from Chapter 3, pp. 52-83] (***Add more references for the term, "schematic entry" or "schematic capture", rather than just "schematics"!!!***)
	- Additional characteristics/parameters of bulk MOSFET devices are:
		* area and perimeter for the diffusion regions [Weste2011, from Chapter 2 MOS Transistor Theory: \S2.3 C-V Characteristics: \S2.3.1 Simple MOS Capacitance Models, pp. 69-70] [Weste2011, from Chapter 1 Introduction: \S1.5 CMOS Fabrication and Layout: \S1.5.1 Inverter Cross-Section, pp. 20] [Weste2011, from Chapter 2 MOS Transistor Theory: \S2.3 C-V Characteristics: \S2.3.3 Detailed MOS Diffusion Capacitance Model, pp. 72-73] [Weste2011, from Chapter 3 CMOS Processing Technology: \S3.3 Layout Design Rules: \S3.3.1 Design Rule Background: \S3.3.1.2 Transistor Rules, pp. 114] for the source and drain [Weste2011, from Chapter 1 Introduction: \S1.3 MOS Transistors, pp. 7-8] [Weste2011, from Chapter 1 Introduction: \S1.5 CMOS Fabrication and Layout: \S1.5.1 Inverter Cross-Section, pp. 19-20] [Weste2011, from Chapter 1 Introduction: \S1.5 CMOS Fabrication and Layout: \S1.5.2 Fabrication Process, pp. 21, 23] [Weste2011, from Chapter 2 MOS Transistor Theory: \S2.1 Introduction, pp. 62] [Weste2011, from Chapter 2 MOS Transistor Theory: \S2.3 C-V Characteristics: \S2.3.3 Detailed MOS Diffusion Capacitance Model, pp. 72] [Weste2011, from Chapter 4 Delay: \S4.3 RC Delay Model: \S4.3.2 Gate and Diffusion Capacitance, pp. 147] of the MOSFET devices [Sutherland1999, from Chapter 5 Calibrating the Model: \S5.2 Designing test circuits: \S5.2.3 Parasitic capacitance, pp. 87] [Keiter2022a, from Chapter 2 NetlistReference: \S2.3 Devices: \S2.3.20 MOS Field Effect Transistor (MOSFET), pp. 290-291]
			+ AS, area of the source diffusion region of the MOSFET device [Weste2011, from Chapter 2 MOS Transistor Theory: \S2.3 C-V Characteristics: \S2.3.3 Detailed MOS Diffusion Capacitance Model, pp. 72]
			+ AD, area of the drain diffusion region of the MOSFET device
			+ PS, perimeter of the source diffusion region of the MOSFET device
			+ PD, perimeter of the drain diffusion region of the MOSFET device
			+ Additional notes:
				- "Junction leakage is caused by current through the p-n junction between the source/drain diffusions and the body." [Weste2011, from Chapter 2 MOS Transistor Theory: \S2.4 Nonideal I-V Effects: \S2.4.4 Leakage, pp. 80]	
				- "Junction leakage occurs when a source or drain diffusion region is at a different potential from the substrate." [Weste2011, from Chapter 5 Power: \S5.3 Static Power: \S5.3.1 Static Power Sources: \S5.3.1.3 Junction Leakage, pp. 196]
				- During SPICE-like circuit simulation, "the junction leakage current" is determined from "the diffusion area and perimeter" [Weste2011, from Chapter 8 Circuit Simulation: \S8.3 Device Models: \S8.3.4 Diffusion Capacitance Models, pp. 302]
				- To determine the gate capacitance with SPICE-like circuit simulation, "set[ the] diffusion area and perimeter to 0" [Weste2011, from Chapter 8 Circuit Simulation: \S8.4 Device Characterization: \S8.4.3 Gate Capacitance, pp. 302]
		+ "gate, source, and drain regions" of MOSFET devices based on the silicon on insulator (SOI) semiconductor manufacturing process [Weste2011, from Chapter 3 CMOS Processing Technology: \S3.4 CMOS Process Enhancements: \S3.4.1 Transistors: \S3.4.1.2 Silicon on Insulator, pp. 120]



Weste2011
length
pp. 45


Defining (quantifiable) characteristics/properties/parameters of FinFET devices are:
+ Additional information about FinFET devices:
	- Fin-like source/drain regions on the silicon surface of FinFET devices [Weste2011, from Chapter 3 CMOS Processing Technology: \S3.4 CMOS Process Enhancements: \S3.4.4 Beyond Conventional CMOS, pp. 129]














Since "the capacitance of the transistor gate is proportional to its [cross-sectional] area," the gate capacitance is in turn dependent on the length and the width of the transistor [Sutherland1999, from Chapter 1 The Method of Logical Effort: \S1.1 Delay in a logic gate, pp. 5]. By setting the transistor length to the "minimum feature size" for the semiconductor manufacturing process technology chosen to implement the integrated circuit design, the gate capacitance effectively/essentially becomes proportional to the transistor width [Sutherland1999, from Chapter 1 The Method of Logical Effort: \S1.1 Delay in a logic gate, pp. 5] [Sutherland1999, from Chapter 1 The Method of Logical Effort: \S1.2 Multi-stage logic networks, Example 1.7, pp. 15] [Sutherland1999, from Chapter 4 Calculating the Logical Effort of Gates: \S4.3 Calculating logical effort, pp. 62].



An aside: Since logic gates are connected together in a logic circuit, where a logic gates that are not (primary) output gates would drive at least one other logic gate, the logic gate input capacitance and logic gate output capacitance can be expressed in terms of the transistor widths. This is because the transistor width is proportional to gate capacitance, assuming that all transistors are designed to have "minimum transistor length" [Sutherland1999, from Chapter 1 The Method of Logical Effort: \S1.1 Delay in a logic gate, pp. 5] [Sutherland1999, from Chapter 1 The Method of Logical Effort: \S1.2 Multi-stage logic networks, Example 1.7, pp. 15] [Weste2011, from Chapter 1 Introduction: \S1.5 CMOS Fabrication and Layout, \S1.5.3 Layout Design Rules, pp. 25] (or "minimum drawn transistor channel length") [Weste2011, from Chapter 1 Introduction: \S1.5 CMOS Fabrication and Layout, \S1.5.3 Layout Design Rules, pp. 24]. Here, the output capacitance of a logic gate `$C_{out}$` refers to the external load of the logic gate, and depends on the transistor sizes/widths connected to the input pins of logic gates connected to the output pin of the logic gate (or fan-out cone of the logic gate). Similarly, the input capacitance of a logic gate `$C_{in}$` refers to "the capacitance presented by the logic gate at ... its input terminals", and depends on the transistor sizes/widths [Sutherland1999, from Chapter 1 The Method of Logical Effort: \S1.1 Delay in a logic gate, pp. 5].
+ "minimum drawn transistor channel length" is defined and described in [Weste2011, from Chapter 1 Introduction: \S1.5 CMOS Fabrication and Layout, \S1.5.3 Layout Design Rules, pp. 24].
	- it is the "minimum polysilicon width", or "minimum width of a polysilicon wire"
	- consequently, the transistor length is the "minimum polysilicon width"
+ minimum "feature size refers to minimum transistor length" [Weste2011, from Chapter 1 Introduction: \S1.5 CMOS Fabrication and Layout, \S1.5.3 Layout Design Rules, pp. 25]
+ The minimum feature size determines the minimum gate length of the MOSFET device, since it is the "minimum allowable size" [Sutherland1999, Chapter 12 Conclusions: \S12.3 A design procedure, pp. 195].
	- Similarly, the IC (standard) cell library [Doman2012] [Ha2009] [Lee2012] [Golshan2007] [Keating2007] [Yu2014a] [Gupta2007] [Salem2007] [Clein2000] [Sicard2007a] [Sicard2007b] [Yeap1998] [Sicard2007] [Mukherjee2007] [Jansen2003] [Hu2007] [Hu2009] [Chiang2007] [Lavagno2016a] [Scheffer2006a] selected for the IC design process would specify the limited discrete transistor sizes that we can use in IC designs [Sutherland1999, Chapter 12 Conclusions: \S12.3 A design procedure, pp. 195]
		* keyphrases used interchangeably for cell library
			+ VLSI design libraries
			+ cell library
			+ design libraries
			+ standard cell library
			+ standard-cell libraries













The (CMOS) semiconductor manufacturing process is described by its "minimum feature size" [Weste2011, from Chapter 1 Introduction: \S1.1 A Brief History, pp. 4] [Weste2011, from Chapter 1 Introduction: \S1.5 CMOS Fabrication and Layout, \S1.5.3 Layout Design Rules, pp. 25] (***Add More References!!!***), which is the smallest dimension of a transistor feature/dimension (e.g., gate length [Keshavarzi2007] [Weste2011, from Chapter 1 Introduction: \S1.5 CMOS Fabrication and Layout, \S1.5.3 Layout Design Rules, pp. 25]) that can be manufactured with consistently with "process reliability" (***Add Citations for "process reliability", especially for semiconductor manufacturing***!!!) [Weste2011, from Chapter 1 Introduction: \S1.1 A Brief History, pp. 4]
It is also referred to as the "minimum drawn channel" length", denoted as `2 \times \lambda` [Sutherland1999, Chapter 5 Calibrating the Model, \S5.2 Designing test circuits, \S5.2.3 Parasitic capacitance, pp. 89] [Weste2011, from Chapter 1 Introduction: \S1.5 CMOS Fabrication and Layout, \S1.5.3 Layout Design Rules, pp. 25]
- Alternatively, `\lambda` refers to "half [of] the [minimum] feature size" [Weste2011, from Chapter 1 Introduction: \S1.5 CMOS Fabrication and Layout, \S1.5.3 Layout Design Rules, pp. 25]
[Weste2011]


An aside: Other features of MOSFETs include widths, separations, and overlaps [Weste2011, from Chapter 3 CMOS Processing Technology, \S3.3 Layout Design Rules, pp. 113] 







To simplify our analysis of transistors and circuits, we assume that for any given integrated circuit, or dies cut from from a wafer, all the transistors are chosen to have the minimum "length [Sutherland1999", from Chapter 1 The Method of Logical Effort: \S1.1 Delay in a logic gate, pp. 5] [Sutherland1999, from Chapter 1 The Method of Logical Effort: \S1.2 Multi-stage logic networks, Example 1.7, pp. 15], so that we can have faster switching transistor and faster circuits (or digital circuits with smaller delays and better performance) [Weste2011, from Chapter 4 Delay: \S4.8 Historical Perspective, pp. 175] (***Add More References!!!***).
+ "transistors are typically chosen to have the minimum possible length because short-channel transistors are faster, smaller, and consume less power" [Weste2011, from Chapter 1 Introduction: \S1.5 CMOS Fabrication and Layout, \S1.5.3 Layout Design Rules, pp. 26]


According to the method of logical effort [Sutherland1999, from Chapter 1 The Method of Logical Effort, pp. 1], the delay of a logic gate can be estimated as `$d = g \cdot h + p$` [Sutherland1999, from Chapter 1 The Method of Logical Effort: \S1.1 Delay in a logic gate, Equation 1.2 on pp. 2 and Equation 1.5 on pp. 3], and `$d$` [Sutherland1999, from Chapter 1 The Method of Logical Effort: \S1.1 Delay in a logic gate, Equation 5 on pp. 3], where `$d$` is the unitless delay unit of a logic gate that is independent of the semiconductor manufacturing process, `$g$` is the logical effort representing the characteristics of a logic gate and `$h$` is the electrical effort that estimates the load characteristics [Sutherland1999, from Chapter 1 The Method of Logical Effort: \S1.1 Delay in a logic gate, Equation 1.3, pp. 2], and `$p$` [Sutherland1999, from Chapter 1 The Method of Logical Effort: \S1.1 Delay in a logic gate, Equations 1.2 and 1.3 on pp. 2 and Equation 1.5 on pp. 3].
+ The method of logical effort does not adequate model interconnect delay, and can use the unified logical effort method in [Morgenshtein2010] to model interconnect delay.
+ While IC designers can use the method of logical effort to optimize/maximize the performance (or minimize the circuit delay) of a digital integrated circuit delay, the IC designers cannot use the method to minimize the energy area and consumption of the digital IC [Sutherland1999, from Chapter 12 Conclusions: 12.5 Shortcomings of logical effort, pp. 198].





Since the electrical effort is typically described as ratio of transistor widths rather than capacitances of a given transistor and the "minimum sized inverter", and the capacitance of a MOSFET transistor is porportional to its (planar) area, by assuming that the length of a MOSFET is sized to be the "minimum feature size" [Weste2011, from Chapter 1 Introduction: \S1.1 A Brief History, pp. 4] [Sutherland1999, from Chapter 12 Conclusions: \S12.3 A design procedure, Figure 12.1, pp. 194], we can estimate the capacitance of a MOSFET by its area, and consequently its width [Sutherland1999, from Chapter 1 The Method of Logical Effort: \S1.1 Delay in a logic gate, pp. 5] [Sutherland1999, from Chapter 1 The Method of Logical Effort: \S1.2 Multi-stage logic networks, Example 1.7, pp. 15] [Sutherland1999, from Chapter 4
Calculating the Logical Effort of Gates: \S4.3 Calculating logical effort, pp. 62]. Hence, the size of a transistor can effectively be described by its width. Since the width of the transistor is proportional to the capacitance of the MOSFET [Sutherland1999, from Chapter 1 The Method of Logical Effort: \S1.1 Delay in a logic gate, pp. 7], 





An aside from the subsection on "Xyce/SPICE Preliminaries":
+ Transistor-level SPICE netlists [Weste2011, from Chapter 15 Testing, Debugging, and Verification: \S15.9 Pitfalls and Fallacies, pp. 691] can be extracted from schematics or IC layout designs [Weste2011, from Chapter 8 Circuit Simulation: \S8.2 A SPICE Tutorial, pp. 288], and can be described as "extracted, transistor-level SPICE netlists" [Weste2011, from Chapter 3 CMOS Processing Technology: \S3.5 Technology-Related CAD Issues: \S3.5.2 Circuit Extraction, pp. 133]. These netlists can be used for SPICE-like circuit simulation, and are also referred to as SPICE simulation netlists [Weste2011, from Chapter 8 Circuit Simulation: \S8.2 A SPICE Tutorial: \8.2.1 Sources and Passive Components, pp. 289] [Weste2011, from Chapter 8 Circuit Simulation: \S8.2 A SPICE Tutorial: \8.2.3 Inverter Transient Analysis, pp. 293-294] [Weste2011, from Chapter 8 Circuit Simulation: \S8.2 A SPICE Tutorial: \8.2.4 Subcircuits and Measurement, pp. 295-296] [Weste2011, from Chapter 8 Circuit Simulation: \S8.2 A SPICE Tutorial: \8.2.5 Optimization, pp. 297] [Weste2011, from Chapter 8 Circuit Simulation: \S8.3 Device Models: \8.3.5 Design Corners, pp. 302] [Weste2011, from Chapter 8 Circuit Simulation: \S8.4 Device Characterization: \8.4.4 Parasitic Capacitance, pp. 309] [Weste2011, from Chapter 8 Circuit Simulation: \S8.5 Circuit Characterization: \8.5.3 Logical Effort, pp. 316] [Weste2011, from Chapter 8 Circuit Simulation: \S8.6 Interconnect Simulation, pp. 321].











minimum
+ [x] [Sutherland1999]





[Sutherland1999, from Chapter 1 The Method of Logical Effort: \S1.1 Delay in a logic gate, pp. 5]
"minimum feature size"
+ [x] [Weste2011]




[Chen2007]
"minimum feature"



feature:
+ [x] [Weste2011]
+ [x] [Sutherland1999]
	- word is not found in the book
	







length
+ [ ] [Weste2011]






width
+ [ ] [Weste2011]


size
+ [ ] [Weste2011]



sizing
+ [ ] [Weste2011]




gate sizing by width of transistor 
length
width
size
sizing
[Sutherland1999]


semiconductor manufacturing process
+ [ ] [Weste2011]




semiconductor manufacturing process technology
+ [ ] [Weste2011]



process technology
+ [ ] [Weste2011]



scaling
+ [ ] [Weste2011]







region, for (source/drain) region(s)
+ [x] [Weste2011]






diffusion
+ [x] [Weste2011]









(correlation and) causation between size of transistor and switching speed of the transistor, which affects the ability of the logic gates to be able to switch its output pin between logic high/"1"/true and low/"0"/false accordingly (***CITE THIS!!!***). The faster the transistor can switch, the faster the logic gates can form a short circuit between the output pin and the voltage source that would charge, or or ground that would discharge, the output pin (***CITE THIS!!!***)


Other effects of minimum feature downsizing, and consequently transistor downsizing.
+ ***Use appropriate equations of MOSFET transistors to justify the following facts.***
+ increase in leakage current, and consequently leakage power [Weste2011, from Chapter 5 Power: \S5.7 Historical Perspective: Summary, pp. 209]
+ As the minimum feature size decreases, the transistor gate lengths decreases and consequently decreases the switching delay of the transistors [Weste2011, from Chapter 6 Interconnect: \S6.6 Pitfalls and Fallacies: Summary, pp. 238]
	- "Switch faster, dissipate less power, and are cheaper to manufacture" [Weste2011, from Chapter 7 Robustness: \S7.4 Scaling, pp. 254-255]
	- On the other hand, as the minimum feature size decreases, the interconnect/wire delays do not decrease [Weste2011, from Chapter 6 Interconnect: \S6.6 Pitfalls and Fallacies: Summary, pp. 238]
+ End of Dennard scaling [Dennard1974] in the early or mid- 2000s [Weste2011, from Chapter 1 Introduction: \S1.1 A Brief History, pp. 4].
	- impact on delay, voltage and power supply, and power consumption,  [Weste2011, from Chapter 7 Robustness: \S7.4 Scaling: \S7.4.1 Transistor Scaling, pp. 255-257]
	- impact on interconnect scaling [Weste2011, from Chapter 7 Robustness: \S7.4 Scaling: \S7.4.2 Interconnect Scaling, pp. 257-258]
+ minimum feature size becomes smaller than the wavelength of light used for the photolithography step in semiconductor manufacturing [Weste2011, from Chapter 12 Array Subsystems: \S12.2 SRAM: \S12.2.1 SRAM Cells: \S12.2.1.4 Physical Design, pp. 504] [Weste2011, from Chapter 1 Introduction: \S1.5 CMOS Fabrication and Layout: \S1.5.2 Fabrication Process, pp. 23] [Weste2011, from Chapter 3 CMOS Processing Technology: \S3.2 CMOS Technologies: \S3.2.2 Photolithography, pp. 101-103]
+ additional references for photolithography:
	- [Weste2011, from Chapter 1 Introduction: \S1.5 CMOS Fabrication and Layout: \S1.5.2 Fabrication Process, pp. 20]
	- "193 nm double-patterning lithography" [Weste2011, from Chapter 3 CMOS Processing Technology: \S3.6 Manufacturing Issues: \S3.6.3 Resolution Enhancement Rules, pp. 36]
	- [Weste2011, from Chapter 7 Robustness: \S7.2 Variability: \S3.6.3 Process Variation, pp. 243]
		* "Channel length variations are caused by photolithography proximity effects"
		* "Line width and spacing, like channel length, depend on photolithography and etching proximity effects"
	- the size of the transistor is dependent on multiple factors, including photolithography [Weste2011, from Chapter 7 Robustness: \S7.4 Scaling: \S7.4.4 Impacts on Design: \S7.4.4.6 Physical Limits, pp. 262]
	- "subwavelength lithography" [Weste2011, from Chapter 7 Robustness: \S7.5 Statistical Analysis of Variability: \S7.5.2 Variation Sources: \S7.5.2.1 Channel Length, pp. 267]
	- causes for "systematic across- chip linewidth variation (ACLV)" [Weste2011, from Chapter 7 Robustness: \S7.5 Statistical Analysis of Variability: \S7.5.2 Variation Sources: \S7.5.2.1 Channel Length, pp. 267]:
		* photolithography
		* pattern-dependent etch rates
	- photolithography is also known as "optical lithography" (***Cite This!!!***)



Definitions:
+ "technology generation", "technology node" [Weste2011, from Chapter 7 Robustness: \S7.4 Scaling: \S7.4.3 International Technology Roadmap for Semiconductors, pp. 258]




When layout designs of circuits are not available, circuit designers should use floorplanning to estimate wire lengths and wiring congestions [Weste2011, from Chapter 1 Introduction: \S1.10 Physical Design: \S1.10.1 Floorplanning, pp. 45]. This can help IC designers estimate if the layout design of the "proposed [IC] design" can fit into allocated IC design area budget (or "the chip area budgeted") [Weste2011, from Chapter 1 Introduction: \S1.10 Physical Design: \S1.10.1 Floorplanning, pp. 45]. In addition, it can help IC designers estimate the impact of the interconnect delays, and parasitic resistance and capacitance using appropriate interconnect models, on circuit delay, energy consumption, and crosstalk noise due to capacitive coupling [Weste2011, from Chapter 6 Interconnect: 6.2 Interconnect Modeling, pp. 213-229]
schematic, 319

















Similarly, extend this for the following semiconductor devices:
+ "gate-all-around (GAA) FET, abbreviated GAAFET" (from the Wikipedia entry for multigate device, multi-gate MOSFET, multi-gate field-effect transistor, or MuGFET)
	- multiple-independent-gate field-effect transistor, MIGFET
+ ferroelectric field-effect transistor, Fe FET
	- used in ferroelectric RAM, FeRAM, F-RAM, or FRAM






Explore operations with the following:
+ high bandwidth memory, HBM
+ wafer-scale computing
	- wafer-level packaging
		* wafer-level chip-scale packaging, WLCSP
+ 3-D IC design and manufacturing
	- 2.5-D IC design and manufacturing
+ chiplet-based computing
+ resistive random-access memory, ReRAM, or RRAM
+ non-volatile random-access memory, NVRAM
+ magnetoresistive random-access memory, MRAM
	- MTJ families
		* field-induced magnetic switching
		* thermally-assisted switching
		* spin-transfer-torque switching
+ phase-change memory, PRAM, PCM, PCME, PRAM, PCRAM
	- or OUM, ovonic unified memory
	- chalcogenide RAM, C-RAM, CRAM
+ spin-transfer torque RAM, STT-RAM
+ ferroelectric RAM, FeRAM, F-RAM, FRAM
	- ferroelectric memory, which is different from FeRAM???
		* FeFET
		* FTJ, ferroelectric tunnel junction
+ metal oxide resistive memory, OxRAM
	- filamentary-oxide-based resistive memory technology, OxRAM
	- oxide-based (Ox) RAM, OxRAM
	- oxide resistive memory, OxRAM
+ conductive bridging RAM, CBRAM
	- conductive bridge RAM, CBRAM
+ macromolecular memory
+ Mott memory
+ massive storage devices








Wikipedia
+ Memory cell
	- D. Tang, Denny; Lee, Yuan-Jen (2010). Magnetic memory: Fundamentals and technology. Cambridge University Press. p. 91. 
	- Li, Hai; Chen, Yiran (19 April 2016). Nonvolatile memory design: Magnetic, resistive, and phase change. CRC press
	- Jacob, Bruce; Ng, Spencer; Wang, David (28 July 2010). Memory systems: Cache, DRAM, disk. Morgan Kaufmann. p. 355
	- Siddiqi, Muzaffer A. (19 December 2012). Dynamic RAM: Technology advancements. CRC Press
+ DRAM
	- Keeth, Brent; Baker, R. Jacob; Johnson, Brian; Lin, Feng (2007). DRAM Circuit Design: Fundamental and High-Speed Topics. Wiley.
	- Wang, David Tawei (2005). Modern DRAM Memory Systems: Performance Analysis and a High Performance, Power-Constrained DRAM-Scheduling Algorithm (PDF) (PhD). University of Maryland, College Park. hdl:1903/2432. Retrieved 2007-03-10. A detailed description of current DRAM technology.
+ RAM
	- Sze, Simon M. (2002). Semiconductor Devices: Physics and Technology (PDF) (2nd ed.). Wiley. p. 214. ISBN 0-471-33372-7.
	- Rainer Waser (2012). Nanoelectronics and Information Technology. John Wiley & Sons.
	- Pimbley, J. (2012). Advanced CMOS Process Technology. Elsevier.






























#	Resources


+ https://xyce.sandia.gov/documentation/index.html
+ https://digitalops.sandia.gov/Mediasite/Play/24aace4429fc450fb5b38cdbf424a66e1d
+ https://digitalops.sandia.gov/Mediasite/Play/c4d3f65bbef74067bebb4c36788dc2931d




Not-so-good references:
+ http://www.unm.edu/~pzarkesh/ECE523/tspice.pdf
+ Ngsice: http://ftp.icm.edu.pl/packages/linux-gentoo/distfiles/ngspice-27-manual.pdf
	- "Ngspice Users ManualVersion 27(Describes ngspice-27 release version)Holger Vogt, Marcel Hendrix, Paolo Nenziš, September 10, 2017.
		* "Holger Vogt and Marcel Hendrix and Paolo Nenzi", September 10, 2017










#	References


+ Unknown source of netlist
+ [Keiter2022a]
	- Eric R. Keiter, Thomas V. Russo, Richard L. Schiek, Heidi K. Thornquist, Ting Mei, Jason C. Verley, Karthik V. Aadithya, and Joshua D. Schickling, "Xyce$^\texttrademark$ Parallel Electronic Simulator: Reference Guide, Version 7.6," number SAND2022-14886, Sandia National Laboratories, Albuquerque, NM and Livermore, CA, November, 2022. Available online from Sandia National Laboratories: Research: Research Foundations: Engineering Science: Advanced Simulation and Computing (ASC): Xyce: Documentation & Tutorials at: https://xyce.sandia.gov/files/xyce/Xyce_Reference_Guide_7.6.pdf; February 9, 2023 was the last accessed date.
+ [Keiter2022]
	- Eric R. Keiter, Thomas V. Russo, Richard L. Schiek, Heidi K. Thornquist, Ting Mei, Jason C. Verley, Karthik V. Aadithya, and Joshua D. Schickling, "Xyce$^\texttrademark$ Parallel Electronic Simulator: Users' Guide, Version 7.6," number SAND2022-14885, Sandia National Laboratories, Albuquerque, NM and Livermore, CA, November, 2022. Available online from Sandia National Laboratories: Research: Research Foundations: Engineering Science: Advanced Simulation and Computing (ASC): Xyce: Documentation & Tutorials at: https://xyce.sandia.gov/files/xyce/Xyce_Users_Guide_7.6.pdf; February 9, 2023 was the last accessed date.
+ [Keiter2023]
	- Eric 'Karlsefni2012' Keiter, Tom 'tvrusso' Russo, peshola, Heidi 'hkthorn' Thornquist, rich1149, Jason 'TBird2001' Verley, Paul 'kuberry' Kuberrys, Zack 'zackgalbreath' Galbreath, Joseph 'josephsnyder' Snyder, and David 'dc-snl' Collins, Gary J. 'gjtempl' Templet, and loulawrence, "The Xyce$^\texttrademark$ Parallel Electronic Simulator," GitHub, Inc., San Francisco, CA, January 31, 2023. Available online from GitHub: Xyce at: https://github.com/Xyce/Xyce; February 9, 2023 was the last accessed date.
+ [XyceTeam2023b]
	- Xyce team, "Executables," Sandia National Laboratories, Albuquerque, NM, 2023. Available online from Sandia National Laboratories: Research: Research Foundations: Engineering Science: Advanced Simulation and Computing (ASC): Xyce: Downloads: Executables at: https://xyce.sandia.gov/downloads/executables/; February 5, 2023 was the last accessed date.
+ [XyceTeam2023]
	- Xyce team, "Xyce: Parallel Electronic Simulation," Sandia National Laboratories, Albuquerque, NM, 2023. Available online from Sandia National Laboratories: Research: Research Foundations: Engineering Science: Advanced Simulation and Computing (ASC) at: https://xyce.sandia.gov/; February 5, 2023 was the last accessed date.
+ [XyceTeam2023e]
	- Xyce team, "Xyce Regression Suite," Sandia National Laboratories, Albuquerque, NM, 2022. Available online from Sandia National Laboratories: Research: Research Foundations: Engineering Science: Advanced Simulation and Computing (ASC): Xyce: Downloads: Source Code at: https://xyce.sandia.gov/files/xyce/Xyce_Regression-7.6.tar.gz and https://xyce.sandia.gov/downloads/source-code/; February 9, 2023 was the last accessed date.
+ peshola2023,
	- peshola, Eric 'Karlsefni2012' Keiter, Tom 'tvrusso' Russo, rich1149, Heidi 'hkthorn' Thornquist, Paul 'kuberry' Kuberry, and Jason 'TBird2001' Verley, "The Xyce$^\texttrademark$ Regression Test Suite," GitHub, Inc., San Francisco, CA, January 31, 2023. Available online from GitHub: Xyce at: https://github.com/Xyce/Xyce_Regression; February 9, 2023 was the last accessed date.
+ [WikipediaContributors2017a]
	- Wikipedia contributors, "Shebang (Unix)," Wikimedia Foundation, San Francisco, CA, April 24, 2017. Available online from Wikipedia, The Free Encyclopedia: Unix at: https://en.wikipedia.org/wiki/Shebang_(Unix); May 1, 2017 was the last accessed date.
+ [Sutherland1999]
	- Ivan Sutherland, Bob Sproull, and David Harris, "Logical Effort: Designing Fast CMOS Circuits," Morgan Kaufmann, San Francisco, CA, 1999.
+ [Weste2011]
	- Neil H. E. Weste and David Money Harris, "CMOS VLSI Design: A Circuits and Systems Perspective," Fourth edition, Pearson Education, Boston, MA, 2011.
+ [Moore1965]
	- Gordon E. Moore, "Cramming More Components Onto Integrated Circuits," in Electronics, Volume 38, Number 8, pp. 114--117, McGraw-Hill, New York, NY, April 19, 1965. Available online from *Intel: Newsroom: Moore's Law -- Now and in the Future* at: https://newsroom.intel.com/wp-content/uploads/sites/11/2018/05/moores-law-electronics.pdf; February 17, 2023 was the last accessed date.
+ [Moore1998]
	- Gordon E. Moore, "Cramming More Components Onto Integrated Circuits," in *Proceedings of the IEEE*, Volume 86, Number 1, pp. 82-85, IEEE Press, Piscataway, NJ, January, 1998. DOI: https://dx.doi.org/10.1109/JPROC.1998.658762.
+ [Chauhan2015]
	- Yogesh Singh Chauhan, Darsen Duane Lu, Sriramkumar Venugopalan, Sourabh Khandelwal, Juan Pablo Duarte, Navid Paydavosi, Ali Niknejad, and Chenming Hu, "FinFET Modeling for IC Simulation and Design: Using the BSIM-CMG Standard," Academic Press, San Diego, CA, 2015.
+ [Gildenblat2010]
	- Gennady Gildenblat, "Compact Modeling: Principles, Techniques and Applications," Springer Science+Business Media B.V., Dordrecht, The Netherlands, 2010. DOI: https://dx.doi.org/10.1007/978-90-481-8614-3.
+ [gem5developers2014]
	- gem5 developers, "The gem5 Simulator System: A modular platform for computer system architecture research," October 27, 2014. Available online at: http://www.gem5.org/Main_Page; self-published; October 9, 2014 was the last accessed date.
+ [Binkert2011]
	- Nathan Binkert, Bradford Beckmann, Gabriel Black, Steven K. Reinhardt, Ali Saidi, Arkaprava Basu, Joel Hestness, Derek R. Hower, Tushar Krishna, Somayeh Sardashti, Rathijit Sen, Korey Sewell, Muhammad Shoaib, Nilay Vaish, Mark D. Hill, and David A. Wood, "The gem5 Simulator," ACM SIGARCH Computer Architecture News, Volume 39, Number 2, pp. 1-7, ACM Press, New York, NY, May, 2011. DOI: https://dx.doi.org/10.1145/2024716.2024718.
+ [Chen2007]
	- Wai-Kai Chen (editor), "The VLSI Handbook," Second edition, in The Electrical Engineering Handbook Series, CRC Press, Boca Raton, FL, 2007.
+ [Keshavarzi2007]
	- Ali Keshavarzi, "\S21.2.1 Device Performance and Energy Scaling," in The VLSI Handbook: Section 3 Low Power Electronics and Design: Chapter 21 Technology Scaling and Low-Power Circuit Design: \S21.2 Technology Scaling Challenges, Second edition, in The Electrical Engineering Handbook Series, pp. 21-1 -- 21-25, CRC Press, Boca Raton, FL, 2007.
	- part of the book [Chen2007].
	- 



concatenate these to put in the input CSV file to generate Markdown format citations, using my BibTeX-to-Markdown translations
Morgenshtein2010
Doman2012
Ha2009
Lee2012
Golshan2007
Keating2007
Yu2014a
Gupta2007
Salem2007
Clein2000
Sicard2007b
Sicard2007a
Yeap1998
Sicard2007
Mukherjee2007
Jansen2003
Hu2007
Hu2009
Chiang2007
Lavagno2016a
Scheffer2006a






















The main references for the Xyce circuit simulator are:
+ [Keiter2022]
+ [Keiter2022a]









#	Author Information

The MIT License (MIT)

Copyright (c) <2017> Zhiyang Ong

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Email address: echo "cukj -wb- 23wU4X5M589 TROJANS cqkH wiuz2y 0f Mw Stanford" | awk '{ sub("23wU4X5M589","F.d_c_b. ") sub("Stanford","d0mA1n"); print $5, $2, $8; for (i=1; i<=1; i++) print "6\b"; print $9, $7, $6 }' | sed y/kqcbuHwM62z/gnotrzadqmC/ | tr 'q' ' ' | tr -d [:cntrl:] | tr -d 'ir' | tr y "\n"		Don't compromise my computing accounts. You have been warned.

