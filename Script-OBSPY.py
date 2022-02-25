#!/usr/bin/env python
# coding: utf-8
python3
import os
os.chdir('/Users/polinalemenkova/Documents/Python/OBSPY')
# pip install obspy
from obspy import read
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
st = read("traces_UCC19540213Gal_E_0816.mseed")
print(st)

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

# 1.2.4 Exercises
