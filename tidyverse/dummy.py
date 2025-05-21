print('Importing tidyverse')
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotnine as pn
import tqdm
import collections
import toolz
# export fonts in matplotlib correctly,
# see https://stackoverflow.com/questions/34387893/output-matplotlib-figure-to-svg-with-text-as-text-not-curves
plt.rcParams['svg.fonttype'] = 'none'
