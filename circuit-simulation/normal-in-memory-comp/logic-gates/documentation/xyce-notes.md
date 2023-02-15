#	Xyce Circuit Simulation



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
	- [Keiter2022, from Chapter 9 Results Output and Evaluation Options: \S9.1 Control of Results Output: \S9.1.1 .print Command] [Keiter2022, from Chapter 9 Results Output and Evaluation Options: \S9.1 Control of Results Output: \S9.1.3 Output File Redirection]
+ When using the "-o" option (pp. 765), check that the path of the output path is correct.
	- When doing experiments with *Xyce* circuit simulation, check that it (especially the filename) reflects the parameter configuration.




Guidelines and recommendations:
+ The use of asterisk indicates multiple instances of something (e.g., a parameter or device) [Keiter2022a, from Chapter 5 Introduction: \S 1.3 Typographical conventions, Table 1-1, pp. 20]
+ [Keiter2022a, from Chapter 5, Subsection \S 5.1.1, pp. 765--766] suggests using the same values for ***RELTOL*** and ***ABSTOL*** in the TIMEINT and NONLIN-TRAN .OPTIONS statements.
	- Choose the value of ***RELTOL***, so that *RELTOL = 1.0E-(m+1)* and *m* is the desired number of siginificant digits of accuracy.
	- Set *ABSTOL* to be the smallest value for components in the integrated circuit (IC).
	- Select ***ABSTOL < RELTOL***.
+ [Keiter2022a, from Chapter 2 Netlist Reference: \S 2.1 Netlist Commands: \S 2.1.37 .subckt (subcircuit), pp. 157-158].
	- ".subckt" statements begin with ".subckt" and ends with ".ends".
	- ".subckt" statements can be nested/embedded within other ".subckt" statements.
	- ".subckt" statements should only include device instantiations, and possibly the following statements (limited to use within the subcircuits).
		* ".model" statements for model definition.
		* ".param" statements for parameters.
		* ".func" statements for functions.
	- Format:
		* .subckt [name] [node]*
		* + [params: [param_name]=[param_value]]
		* .ends



















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


































#	Author Information

The MIT License (MIT)

Copyright (c) <2017> Zhiyang Ong

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Email address: echo "cukj -wb- 23wU4X5M589 TROJANS cqkH wiuz2y 0f Mw Stanford" | awk '{ sub("23wU4X5M589","F.d_c_b. ") sub("Stanford","d0mA1n"); print $5, $2, $8; for (i=1; i<=1; i++) print "6\b"; print $9, $7, $6 }' | sed y/kqcbuHwM62z/gnotrzadqmC/ | tr 'q' ' ' | tr -d [:cntrl:] | tr -d 'ir' | tr y "\n"		Don't compromise my computing accounts. You have been warned.

