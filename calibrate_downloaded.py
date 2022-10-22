import pandas as pd
import argparse
from tqdm import tqdm

def calibrate_log(cal_source, cal_target):
    downloaded = []
    with open(cal_source, 'r') as f:
        for l in f.readlines():
            downloaded.append(l.strip())

    downloaded = [l.split()[-1] for l in downloaded]
    downloaded = [l.split('/')[-1] for l in downloaded]

    log = pd.read_csv(cal_target, index_col=0)
    links = log['link'].tolist()
    count = [0 for _ in links]
    for f in tqdm(downloaded):
        for i, l in enumerate(links):
            if f in l:
                count[i] = 1
                break

    log['downloaded'] = count
    log.to_csv(f'{cal_target[:-4]}_cal.csv')


def compare_numbers(target):
    origianl = pd.read_csv(target, index_col=0)
    calibrated = pd.read_csv(f'{target[:-4]}_cal.csv', index_col=0)
    downloaded_ori = origianl['downloaded'].to_numpy()
    downloaded_cal = calibrated['downloaded'].to_numpy()
    n_down_ori = downloaded_ori.sum()
    n_down_cal = downloaded_cal.sum()
    for i, d in enumerate(downloaded_ori):
        if d != downloaded_cal[i]:
            if d == 1:
                print(origianl.loc[i, 'link'], "file missing")
            else:
                print(origianl.loc[i, 'link'], "file present")
    print(f"Before Calibration: {n_down_ori}/{len(downloaded_ori)}")
    print(f"After Calibration: {n_down_cal}/{len(downloaded_cal)}")

def count_videos(dir='video_downloaded.csv'):
    df = pd.read_csv(dir, index_col=0)
    downloaded = df['downloaded'].to_numpy()
    n_down = downloaded.sum()
    print(f"{n_down}/{len(downloaded)}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--calibrate', action='store_true')
    parser.add_argument('-s', '--source', default='output.txt')
    parser.add_argument('-t', '--target', default='metadata.csv')
    parser.add_argument('-v', '--compare', action='store_true')
    parser.add_argument('-n', '--count', action='store_true')
    args = parser.parse_args()
    if args.calibrate:
        print('Start calibrating...')
        calibrate_log(args.source, args.target)
        print('Calibrated log saved.')
    if args.compare:
        print('Comparing number of videos...')
        compare_numbers(args.target)
    if args.count:
        print('Counting number of videos...')
        count_videos()