#!/usr/bin/env python
# coding: utf-8
python3
import os
os.chdir('/Users/polinalemenkova/Documents/Python/OBSPY')
# pip install obspy
#--------------------------------------------------#

# 1.2 UTCDateTime
# 1.2.1 Initialization
from obspy.core import UTCDateTime
UTCDateTime("2012-09-07T12:15:00")
UTCDateTime(2012, 9, 7, 12, 15, 0)
UTCDateTime("2012-09-07T12:15:00+02:00")

# 1.2.2 Attribute Access
time = UTCDateTime("2012-09-07T12:15:00")
time.year
time.julday
time.timestamp
time.weekday

# 1.2.3. Handling time differences
time = UTCDateTime("2012-09-07T12:15:00")
time2 = UTCDateTime(2012, 1, 1)
print(time - time2)

#--------------------------------------------------#
# 1.3 Reading Seismograms
from obspy import read
st = read("http://examples.obspy.org/RJOB_061005_072159.ehz.new")
# print(st)
st.plot()
#st = read("traces_UCC19540108Gal_N_0815.mseed")
#st = read("traces_UCC19540130Gal_N_0808.mseed")
#st = read("traces_UCC19540130Gal_E_0808.mseed")
#st = read("")
st = read("traces_UCC19540111Gal_N_0824.mseed")
print(st)
st = read("traces_UCC19540312Gal_E_0834.mseed")
print(st)
st = read("traces_UCC19540311Gal_E_0727.mseed")
print(st)
st = read("traces_UCC19540311Gal_E_0727.mseed")
print(st)
st = read("traces_UCC19540213Gal_N_0816.mseed")
print(st)
#
st = read("traces_UCC19540213Gal_E_0816.mseed")
st.plot()
print(st)

# 1.3.1 Accessing Meta Data (location, station, etc.)
tr = st[0] # assign first and only trace to new variable
print(tr)
print(tr.stats)
tr.stats.station
tr.stats.mseed.datatype

# 1.3.2 Accessing Waveform Data
# Retrieve the actual waveform data via the data keyword on each Trace:
tr.data
tr.data[0:3]
len(tr)

# 1.3.3 Data Preview
st.plot()

# 1.4 Waveform Plotting Tutorial
from obspy.core import read
singlechannel = read("https://examples.obspy.org/COP.BHZ.DK.2009.050")
print(singlechannel)
threechannels = read("https://examples.obspy.org/COP.BHE.DK.2009.050")
threechannels += read("https://examples.obspy.org/COP.BHN.DK.2009.050")
threechannels += read("https://examples.obspy.org/COP.BHZ.DK.2009.050")

# 1.4.1 Basic Plotting
singlechannel.plot()

import matplotlib.pyplot as plt
plt.plot(singlechannel)
plt.show()

# 1.4.2 Customized Plots
dt = singlechannel[0].stats.starttime
singlechannel.plot(color="red", number_of_ticks=7, tick_rotation=5, tick_format="%I:%M %p", starttime=dt + 60*60, endtime=dt + 60*60 + 120)
singlechannel.plot(color="purple", number_of_ticks=20, tick_rotation=10, tick_format="%I:%M %p", starttime=dt + 60*60, endtime=dt + 60*60 + 120)

# 1.4.3 Saving Plot to File
singlechannel.plot(outfile="/Users/polinalemenkova/Documents/Python/OBSPY/singlechannel.png")
singlechannel.plot(outfile="singlechannel.png")

# 1.4.4 Plotting multiple Channels
threechannels.plot(size=(800, 600))
# size in pixels: size=(1600, 1200)
threechannels.plot(outfile="threechannels_300_86.png",dpi=300,size=(1600, 1200))
threechannels.plot(outfile="threechannels_300_3200.png",dpi=300,size=(3200, 2400),title="Threechannels")

# 1.4.5 Creating a One-Day Plot
singlechannel.plot(type="dayplot")
singlechannel.plot(outfile="dayplot.png")

# Event information can be included in the plot as well (experimental feature, syntax might change):
from obspy import read
st = read("https://examples.obspy.org/GR.BFO..LHZ.2012.108")

#https://docs.obspy.org/packages/autogen/obspy.core.stream.Stream.plot.html#obspy.core.stream.Stream.plot

from obspy import read
#st.plot(type="section", dist_degree=True)
st = read("https://examples.obspy.org/GR.BFO..LHZ.2012.108")
st.filter("lowpass", freq=0.1, corners=2)

# minimal example
st.plot(type="dayplot", interval=60,
    right_vertical_labels=False, vertical_scaling_range=5e3,
    one_tick_per_line=True, color=["k", "r", "b", "g"], show_y_UTC_label=False, events={"min_magnitude": 6.5})

# my example
st.plot(type="dayplot", interval=15,
    vertical_scaling_range=5e3, one_tick_per_line=True,
    color=["purple", "r", "b", "g"], dpi=100, size=(800, 600),
    show_y_UTC_label=True,
    events={"min_magnitude": 6.5},
    tick_rotation=15, tick_format="%H:%M:%S",
    number_of_ticks=12,
    bgcolor="white",face_color="red",transparent=True,
    starttime=None,endtime=None,
    localization_dict={'time in': "temps en", 'seconds': "secondes", 'minutes': "minutes", 'hours': "heures"}, data_unit="$\\frac{m}{s}$",
    x_labels_size=9, y_labels_size=9, title_size=11,
    subplots_adjust_left=0.10, subplots_adjust_right=0.92,
    subplots_adjust_top=0.93,subplots_adjust_bottom=0.1,
    right_vertical_labels=False,
    grid_color="gray", grid_linewidth=0.5,grid_linestyle=":",
#    title="My Title",
    draw=True,show=True)

# 1.4.6 Plotting a Record Section
st.plot(type="section")
# To plot a record section the ObsPy header trace.stats.distance (Offset) must be defined in meters

# 1.4.7 Plot & Color Options
# 1.4.8 Custom Plotting using Matplotlib
import matplotlib.pyplot as plt
from obspy import read
st = read("https://examples.obspy.org/GR.BFO..LHZ.2012.108")
tr = st[0]
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(tr.times("matplotlib"), tr.data, "b-")
ax.xaxis_date()
fig.autofmt_xdate()
plt.show()


# 1.5 Retrieving Data from Data Centers
# 1.5.1 The FDSN Web Services
# 1.5.2 ArcLink
# 1.5.3 IRIS Web Services
# 1.5.4 Earthworm Wave Server
# 1.5.5 NERIES Web Services
# 1.5.6 NEIC
# 1.5.7 SeedLink
# 1.5.8 Syngine Service

# 1.6 Filtering Seismograms
import numpy as np
import matplotlib.pyplot as plt
import obspy

# Read the seismogram
st = obspy.read("https://examples.obspy.org/RJOB_061005_072159.ehz.new")
# There is only one trace in the Stream object, let’s work on that trace...
tr = st[0]
# Filtering with a lowpass on a copy of the original Trace
tr_filt = tr.copy()
tr_filt.filter("lowpass", freq=1.0, corners=2, zerophase=True)

# Now let’s plot the raw and filtered data...
t = np.arange(0, tr.stats.npts / tr.stats.sampling_rate, tr.stats.delta)
plt.subplot(211)
plt.plot(t, tr.data, "blue")
plt.ylabel("Raw Data")
plt.subplot(212)
plt.plot(t, tr_filt.data, "red")
plt.ylabel("Lowpassed Data")
plt.xlabel("Time [s]")
plt.suptitle(tr.stats.starttime)
plt.show()

st.filter("lowpass", freq=0.1, corners=2)
st.filter("highpass", freq=0.1, corners=2)
st.filter("bandpass", freqmin=0.1, freqmax=0.4, corners=4)
# Butterworth-Bandstop Filter
st.filter("bandstop", freqmin=0.1, freqmax=0.4, corners=4)
st.filter("lowpass_cheby_2", freq=0.1)

# my example
st.plot(type="dayplot", interval=15,
    vertical_scaling_range=5e3, one_tick_per_line=True,
    color=["purple", "r", "b", "g"], dpi=100, size=(800, 600),
    show_y_UTC_label=True,
    events={"min_magnitude": 6.5},
    tick_rotation=15, tick_format="%H:%M:%S",
    number_of_ticks=12,
    bgcolor="white",face_color="red",transparent=True,
    starttime=None,endtime=None,
    localization_dict={'time in': "temps en", 'seconds': "secondes", 'minutes': "minutes", 'hours': "heures"}, data_unit="$\\frac{m}{s}$",
    x_labels_size=9, y_labels_size=9, title_size=11,
    subplots_adjust_left=0.10, subplots_adjust_right=0.92,
    subplots_adjust_top=0.93,subplots_adjust_bottom=0.1,
    right_vertical_labels=False,
    grid_color="gray", grid_linewidth=0.5,grid_linestyle=":",
#    title="My Title",
    draw=True,show=True)

# pip install cartoply
# import cartopy.crs as ccrs
from obspy import read_inventory
net = read_inventory()[0]
Network.plot(projection='global', resolution='l', continent_fill_color='0.9', water_fill_color='1.0', marker='v', size=225, label=True, color='#b15928', time=None, show=True, outfile=None, method=basemap, fig=None, **kwargs)[source]

# 1.7 Downsampling Seismograms
import numpy as np
import matplotlib.pyplot as plt
import obspy
# Read the seismogram
st = obspy.read("https://examples.obspy.org/RJOB_061005_072159.ehz.new")
# There is only one trace in the Stream object, let’s work on that trace...
tr = st[0]

# Decimate the 200 Hz data by a factor of 4 to 50 Hz. Note that this
# automatically includes a lowpass filtering with corner frequency 20 Hz.
# We work on a copy of the original data just to demonstrate the effects of # downsampling.
tr_new = tr.copy()
tr_new.decimate(factor=4, strict_length=False)

# For comparison also only filter the original data (same filter options as in automatically applied filtering during downsampling, corner frequency
# 0.4 * new sampling rate)
tr_filt = tr.copy()
tr_filt.filter("lowpass", freq=0.4 * tr.stats.sampling_rate / 4.0)

# Now let’s plot the raw and filtered data...
t = np.arange(0, tr.stats.npts / tr.stats.sampling_rate, tr.stats.delta)
t_new = np.arange(0, tr_new.stats.npts / tr_new.stats.sampling_rate, tr_new.stats.delta)

plt.plot(t, tr.data, "k", label="Raw", alpha=0.3)
plt.plot(t, tr_filt.data, "b", label="Lowpassed", alpha=0.7)
plt.plot(t_new, tr_new.data, "r", label="Lowpassed/Downsampled", alpha=0.7)
plt.xlabel("Time [s]")
plt.xlim(82, 83.5)
plt.suptitle(tr.stats.starttime)
plt.legend()
plt.show()

# 1.8 Merging Seismograms
import numpy as np
import matplotlib.pyplot as plt
import obspy

# Read in all files starting with dis.
st = obspy.read("https://examples.obspy.org/dis.G.SCZ.__.BHE")
st += obspy.read("https://examples.obspy.org/dis.G.SCZ.__.BHE.1")
st += obspy.read("https://examples.obspy.org/dis.G.SCZ.__.BHE.2")

# sort
st.sort(["starttime"])
# start time in plot equals 0
dt = st[0].stats.starttime.timestamp

# Go through the stream object, determine time range in julian seconds and plot the data with a shared x axis
ax = plt.subplot(4, 1, 1) # dummy for tying axis
for i in range(3):
    plt.subplot(4, 1, i + 1, sharex=ax)
    t = np.linspace(st[i].stats.starttime.timestamp - dt,
                    st[i].stats.endtime.timestamp - dt,
                    st[i].stats.npts)
    plt.plot(t, st[i].data)
# Merge the data together and show plot in a similar way
st.merge(method=1)
plt.subplot(4, 1, 4, sharex=ax)
t = np.linspace(st[0].stats.starttime.timestamp - dt,
                st[0].stats.endtime.timestamp - dt,
                st[0].stats.npts)
plt.plot(t, st[0].data, "r")
plt.show()
