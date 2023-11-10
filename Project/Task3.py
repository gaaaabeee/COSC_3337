import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from matplotlib.colors import LogNorm

df_2004_5 = pd.read_csv('Solar_flare_RHESSI_2004_05.csv')
df_2015_16 = pd.read_csv('Solar_flare_RHESSI_2015_16.csv')

os.makedirs("Task3_outputs", exist_ok=True)

#plot the 2004-05 data frame
plt.scatter(df_2004_5["x.pos.asec"], df_2004_5["y.pos.asec"], s=5, alpha=0.2)
plt.tight_layout(pad=3.0)
plt.savefig(os.path.join("Task3_outputs", "spatial_2004_5.png"))
plt.clf()

#plot the 2015-16 data frame
plt.scatter(df_2015_16["x.pos.asec"], df_2015_16["y.pos.asec"], s=5, alpha=0.2)
plt.tight_layout(pad=3.0)
plt.savefig(os.path.join("Task3_outputs", "spatial_2015_16.png"))

#plot both dataframes over one another
plt.scatter(df_2004_5["x.pos.asec"], df_2004_5["y.pos.asec"], s=5, alpha=0.2)
plt.tight_layout(pad=3.0)
plt.savefig(os.path.join("Task3_outputs", "spatial_variation.png"))

#averages
print("                                 Averages for 2004-05 DF                        Averages for 2015-16 DF")
print(f'Duration of Flare:                  {sum(df_2004_5["duration.s"])/df_2004_5["duration.s"].count()}           '
      f'                  {sum(df_2015_16["duration.s"])/df_2015_16["duration.s"].count()}')

print(f'Peak Counts per Second:             {sum(df_2004_5["peak.c/s"])/df_2004_5["peak.c/s"].count()}                 '
      f'          {sum(df_2015_16["peak.c/s"])/df_2015_16["peak.c/s"].count()}')

print(f'Total Counts:                       {sum(df_2004_5["total.counts"])/df_2004_5["total.counts"].count()}          '
      f'                  {sum(df_2015_16["total.counts"])/df_2015_16["total.counts"].count()}')

print(f'XPos:                               {sum(df_2004_5["x.pos.asec"])/df_2004_5["x.pos.asec"].count()}             '
      f'              {sum(df_2015_16["x.pos.asec"])/df_2015_16["x.pos.asec"].count()}')

print(f'YPos:                               {sum(df_2004_5["y.pos.asec"])/df_2004_5["y.pos.asec"].count()}             '
      f'              {sum(df_2015_16["y.pos.asec"])/df_2015_16["y.pos.asec"].count()}')

print(f'Distance From Suns Center:          {sum(df_2004_5["radial"])/df_2004_5["radial"].count()}                       '
      f'     {sum(df_2015_16["radial"])/df_2015_16["radial"].count()}')
print("")

energyRanges04_05 = [0,0,0,0,0,0,0,0]
for val in df_2004_5["energy.kev"]:
    if val == "6-12":
        energyRanges04_05[0] += 1
    elif val == "12-25":
        energyRanges04_05[1] += 1
    elif val == "25-50":
        energyRanges04_05[2] += 1
    elif val == "50-100":
        energyRanges04_05[3] += 1
    elif val == "100-300":
        energyRanges04_05[4] += 1
    elif val == "300-800":
        energyRanges04_05[5] += 1
    elif val == "800-7000":
        energyRanges04_05[6] += 1
    elif val == "7000-20000":
        energyRanges04_05[7] += 1

energyRanges15_16 = [0,0,0,0,0,0,0,0]
for val in df_2015_16["energy.kev"]:
    if val == "6-12":
        energyRanges15_16[0] += 1
    elif val == "12-25":
        energyRanges15_16[1] += 1
    elif val == "25-50":
        energyRanges15_16[2] += 1
    elif val == "50-100":
        energyRanges15_16[3] += 1
    elif val == "100-300":
        energyRanges15_16[4] += 1
    elif val == "300-800":
        energyRanges15_16[5] += 1
    elif val == "800-7000":
        energyRanges15_16[6] += 1
    elif val == "7000-20000":
        energyRanges15_16[7] += 1

#counts
print("                                 Counts for 2004-05 DF                Counts for 2015-16 DF")
print(f'Total Flares:                        {df_2004_5["total.counts"].count()}                                {df_2015_16["total.counts"].count()}')
print(f'Total Count Sums:                    {sum(df_2004_5["total.counts"])}                         {sum(df_2015_16["total.counts"])}')
print("Energy Counts:")
print(f'6-12 kev:                            {energyRanges04_05[0]}                                {energyRanges15_16[0]}')
print(f'12-25 kev:                           {energyRanges04_05[1]}                                 {energyRanges15_16[1]}')
print(f'25-50 kev:                           {energyRanges04_05[2]}                                  {energyRanges15_16[2]}')
print(f'50-100 kev:                          {energyRanges04_05[3]}                                   {energyRanges15_16[3]}')
print(f'100-300 kev:                         {energyRanges04_05[4]}                                   {energyRanges15_16[4]}')
print(f'300-800 kev:                         {energyRanges04_05[5]}                                    {energyRanges15_16[5]}')
print(f'800-7,000 kev:                       {energyRanges04_05[6]}                                    {energyRanges15_16[6]}')
print(f'7,000-20,000 kev:                    {energyRanges04_05[7]}                                    {energyRanges15_16[7]}')