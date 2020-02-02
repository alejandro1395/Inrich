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

#First we read both input files before manipulating them

pd.options.mode.chained_assignment = None  # default='warn'
gwas_catalog_snps = pd.read_csv("../input_files/reference.snps", sep='\t', header = None)#first database creation
LD_snps = pd.read_csv('../input_files/CEU_mod.csv', sep='\t', header = 0)
Outfile = "../input_files/merged_ref.snps"

#First, let's assign the column names to the gwas_catalog
# subset of SNPS

gwas_catalog_snps.columns = ["Chr", "POS", "SNPID"]
print(gwas_catalog_snps[1:5])

#Then let's merge both DF according to the criteria
# where SNPID is in same row
merged_df_SNP1 = gwas_catalog_snps.merge(LD_snps, how='inner',
left_on='SNPID', right_on='SNP1')
merged_df_SNP2 = gwas_catalog_snps.merge(LD_snps, how='inner',
left_on='SNPID', right_on='SNP2')
#retrieve set of single SNPs for each memeber of pleiotropies pairs

#Then, we retrieve just the subset of columns for each one we want
selected_columns1 = ["Chr", "POS1"]
selected_columns2 = ["Chr", "POS2"]
merged_df_SNP1 = merged_df_SNP1[selected_columns1]
merged_df_SNP2 = merged_df_SNP2[selected_columns2]
total_merged = pd.concat([merged_df_SNP1, merged_df_SNP2.rename(columns={'POS2':'POS1'})],
ignore_index=True, sort= False)
unique_total_merged = total_merged.drop_duplicates()

unique_total_merged.to_csv(Outfile, sep="\t",
index = False)
