#!/bin/bash
#
# Use this shell script to compile (if necessary) your code and then execute it. Below is an example of what might be found in this file if your program was written in Python
#
#python ./src/donation_analytics.py ../../donation-analytics/FEC_input/by_date/itcont_2018_20070823_20170529.txt ./input/percentile.txt ./output/repeat_donors.txt
python ./src/donation_analytics.py ./input/itcont.txt ./input/percentile.txt ./output/repeat_donors.txt
python -m pytest -v ./src/unit_test1.py
#py.test -v ./src/unit_test1.py
 

