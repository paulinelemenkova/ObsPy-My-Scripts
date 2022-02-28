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

st.plot(type="dayplot", interval=60,
    right_vertical_labels=False,
    vertical_scaling_range=5e3, one_tick_per_line=True,
    color=["k", "r", "b", "g"],dpi=100,
    show_y_UTC_label=False,
    events={"min_magnitude": 6.5},
    tick_rotation=15, tick_format="%H:%M:%S",
    number_of_ticks=8,
    bgcolor="white",face_color="red",transparent=True,
    draw=True,show=True)

# 1.4.6 Plotting a Record Section
st.plot(type="section")

    

# pip install cartoply
# import cartopy.crs as ccrs
from obspy import read_inventory
net = read_inventory()[0]
Network.plot(projection='global', resolution='l', continent_fill_color='0.9', water_fill_color='1.0', marker='v', size=225, label=True, color='#b15928', time=None, show=True, outfile=None, method=basemap, fig=None, **kwargs)[source]

