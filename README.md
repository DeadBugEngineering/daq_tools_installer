# daq_tools_installer
A bash script to install tools useful for a DAQ computer running Linux Mint 20.3+

This set of tools is meant to be helpful for people involved in hardware design in its exploratory phase when the final requirements are not stable/known yet. The programming language of choice here is Python3 to control the different DAQ devices for the acquisition of raw measurement data and to gather them in a CSV file to take a first look at the data-set with Paraview. Paraview is a highly optimized data visualisation application that is very handy when one wants to take a quick look at data sets with many data points.

## Supported DAQ devices

[Labjack U6](https://labjack.com/products/u6) *tested*

[PicoScope 5444D](https://www.picotech.com/oscilloscope/5000/flexible-resolution-oscilloscope) *tested*
