# yibasuo

Generate GIF-like video for Telegram/Twitter/etc.

## Requirement

* At least Python 3.2
* ffmpeg

## Usage

~~~
$ yibasuo.py --help
usage: yibasuo.py [-h] [--span START END] [--crop WIDTH HEIGHT X Y]
                  [--crf CRF] [--resize] [--scale W H] [-o output]
                  video

Generate GIF-like MP4 video for Telegram/Twitter/etc.

positional arguments:
  video                 The input video path.

optional arguments:
  -h, --help            show this help message and exit
  --span START END      Specify cut time.
  --crop WIDTH HEIGHT X Y
                        Crop input video.
  --crf CRF             Specify the Constant Rate Factor of output video.
  --resize              Auto resize input video to 720P.
  --scale W H           ffmepg -vf scale=W:H
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
