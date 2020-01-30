#!/usr/bin/python3

import pandas as pd
import numpy as np
import requests, sys
from itertools import combinations
#import seaborn as sns
from scipy import stats
import matplotlib.pyplot as plt
import pickle
from collections import Counter
from matplotlib.backends.backend_pdf import PdfPages
import copy
from scipy.stats import sem, t
from scipy import mean
import re
import os
from time import sleep

#Finally, we print the ouput in a new folders
with open(OUTPATH + "freqs_total.tsv", "r") as out_fh:
	print("{}\t{}\t{}".format("Combined_diseases", "Total_observed", "Exp_prob"), file=out_fh)
	for key in total_comb_pleios:
		if key in probs_pleios:
			print("{}\t{}\t{}".format(key, total_comb_pleios[key], probs_pleios[key]), file=out_fh)
		else:
			list2 = reversed(key.split("_"))
			key2 = list2.join("_")
			print("{}\t{}\t{}".format(key, total_comb_pleios[key], probs_pleios[key2]), file=out_fh)
	#print("{}\t{}\t{}".format("Rest", Rest_comb, Prob_none), file=out_fh)
