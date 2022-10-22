import pandas as pd
import argparse
from tqdm import tqdm

df = pd.read_csv("/home/itk0123/selenium_es_congress/metadata_cal.csv", index_col=0)

df = df[df['downloaded'] == 1]

df.to_csv('metadata_filtered.csv', index=False)