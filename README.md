# daq_tools_installer
A bash script to install tools useful for a DAQ computer running Linux Mint 20.3+

This set of tools is meant to be helpful for people involved in hardware design in its exploratory phase when the final requirements are not stable/known yet. The programming language of choice here is Python3 to control the different DAQ devices for the acquisition of raw measurement data and to gather them in a CSV file to take a first look at the data-set with Paraview. Paraview is a highly optimized data visualisation application that is very handy when one wants to take a quick look at data sets with many data points.

## Supported DAQ devices

[Labjack U6](https://labjack.com/products/u6) *tested*

[PicoScope 5444D](https://www.picotech.com/oscilloscope/5000/flexible-resolution-oscilloscope) *tested*

## Sensors used
[Temperature LM35](https://www.ti.com/lit/ds/symlink/lm35.pdf)
The LM35 is a linear temperature sensor that comes in a SOIC8, TO-92 and TO-220 package and is very easy to use with its analog output of 10mV/°C. 

## Scripts
[daq_tools_installer.sh](https://github.com/DeadBugEngineering/daq_tools_installer/blob/main/daq_tools_installer.sh)
This script is meant to be used on a freshly setup Linux Mint 20.3+ install.
[tempLoggerU6_14xLM35.py](https://github.com/DeadBugEngineering/daq_tools_installer/blob/main/tempLoggerU6_14xLM35.py)
This script logs the temperature of up to 14 LM35 sensors using a U6 Labjack. 
