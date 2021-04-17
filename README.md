# 一把梭

Generate GIF-like video for Telegram/Twitter/etc.

## Requirement

* At least Python 3.2
* ffmpeg

## Usage

```
usage: yibasuo.py [-h] [--span START END] [--frame START END]
                  [--crop WIDTH HEIGHT X Y] [--crf CRF] [--720p] [--audio]
                  [--with-gif] [--gif] [--reverse] [--ass ASS] [--scale W H]
                  [--filter FILTER [FILTER ...]] [--other OTHER] [-o output]
                  video

Generate GIF-like MP4 video for Telegram/Twitter/etc.

positional arguments:
  video                 The input video path.

optional arguments:
  -h, --help            show this help message and exit
  --span START END      Specify cut time.
  --frame START END     Specify cut frame.
  --crop WIDTH HEIGHT X Y
                        Crop input video.
  --crf CRF             Specify the Constant Rate Factor of output video.
  --720p                Auto resize input video to 720P.
  --audio               Don't remove input video audio track.
  --with-gif            Generate addition .gif output file.
  --gif                 Convert input video to .gif file.
  --reverse             ONLY reverse input video, other arguments invalid
                        (except --gif).
  --ass ASS             Burn .ass subtitle into the video.
  --scale W H           ffmepg -vf scale=W:H
  --filter FILTER [FILTER ...]
                        ffmepg -vf ...
  --other OTHER         Other ffmepg arguments.
  -o output, --output output
```

## Install

```
git clone https://github.com/quanbrew/yibasuo
pip3 install -e ./yibasuo
```

or nix:

```
nix -if .
```
