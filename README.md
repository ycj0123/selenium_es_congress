# Spanish Congress Dataset

This dataset contains videos recorded in the lower house of Spanish Congress. Data was scraped from the ofiicial website of "Congreso de los Diputados". All video has a resolution of 640*360, and frame rate ranges from 25 to 39 (mostly 25). The total length is about 12k hours.

## Metadata
Information including the title, date and the ID of the legislature of each video is given in `metadata.csv`.

## Date
Dates of the recordings span from 13/12/2011 to 07/07/2022.

## Naming Convention
The naming of the files does not follow any particular convention, instead follows the original filenames given on the website.

## File structure:
* s3://speechparacrawl/spanish_congress
    * video_name.mp4
    * metadata.csv
