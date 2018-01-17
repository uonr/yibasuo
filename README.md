# yibasuo

Generate GIF-like video for Telegram/Twitter/etc.

## Requirement

* At least Python 3.2
* ffmpeg

## Usage

~~~
usage: yibasuo.py [-h] [--span START END] [--frame START END]
                  [--crop WIDTH HEIGHT X Y] [--crf CRF] [--resize] [--audio]
                  [--scale W H] [--filter FILTER [FILTER ...]] [--other OTHER]
                  [-o output]
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
  --resize              Auto resize input video to 720P.
  --audio               Don't remove input video audio track.
  --scale W H           ffmepg -vf scale=W:H
  --filter FILTER [FILTER ...]
                        ffmepg -vf ...
  --other OTHER         Other ffmepg arguments.
  -o output, --output output
~~~

## Install


### Install via pip3

~~~
pip3 install yibasuo
~~~


### Install via git
~~~
git clone https://github.com/quanbrew/yibasuo
cd yibasuo
python3 setup.py install --user
~~~

### Download via cURL

~~~
curl https://raw.githubusercontent.com/quanbrew/yibasuo/master/yibasuo.py > yibasuo.py
chmod u+x yibasuo.py
~~~
