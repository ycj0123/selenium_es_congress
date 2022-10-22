from ffprobe import FFProbe
from ffprobe.exceptions import FFProbeError
from tqdm import tqdm
import nlp2

# Local file
# metadata=FFProbe('/mnt/storage2t/spanish_congress/10_000318_065_0_15781_578080.mp4')
# print(len(metadata.streams))
source_dir = '/mnt/storage2t/spanish_congress/'

test_videos = []
for i in tqdm(nlp2.get_files_from_dir(source_dir, match='mp4')):
    test_videos.append(i)
    # break

def test_video ():
    for test_video in test_videos:
        media = FFProbe(test_video)
        # print('File:', test_video)
        # print('\tStreams:', len(media.streams))
        for index, stream in enumerate(media.streams, 1):
            print('\tStream: ', index)
            try:
                if stream.is_video():
                    frame_rate = stream.frames() / stream.duration_seconds()
                    print('\t\tFrame Rate:', frame_rate)
                    # print('\t\tFrame Size:', stream.frame_size())
                # print('\t\tDuration:', stream.duration_seconds())
                # print('\t\tFrames:', stream.frames())
                # print('\t\tIs video:', stream.is_video())
            except FFProbeError as e:
                print(e)
            except Exception as e:
                print(e)

test_video()