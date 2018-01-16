#!/usr/bin/env python3
import argparse
import os


def main():
    parser = argparse.ArgumentParser(description='Generate GIF-like MP4 video for Telegram/Twitter/etc.')
    parser.add_argument('video', type=str, help='The input video path.')
    parser.add_argument('--span', nargs=2, type=str, metavar=('START', 'END'), help='Specify cut time.')
    parser.add_argument('--crop', nargs=4, type=str, metavar=('WIDTH', 'HEIGHT', 'X', 'Y'), help='Crop input video.')
    parser.add_argument('--crf', type=int, default=23, help='Specify the Constant Rate Factor of output video.')
    parser.add_argument('--resize', action='store_true', help='Auto resize input video to 720P.')
    parser.add_argument('--scale', type=str, nargs=2, metavar=('W', 'H'), help='ffmepg -vf scale=W:H')
    parser.add_argument('-o', '--output', metavar='output', type=str)
    args = parser.parse_args()

    if not os.path.isfile(args.video):
        raise RuntimeError('Wrong input video path.')

    output = ''
    if args.output:
        output = args.output
    else:
        # Auto name output file.
        p, _ = os.path.splitext(args.video)
        output = '[GIF]{}'.format(os.path.basename(p))
        if os.path.exists(output+'.mp4'):
            no = 2
            new_name = '{} - {}'.format(output, no)
            while os.path.exists(new_name + '.mp4'):
                no += 1
            output = new_name

        output += '.mp4'

    time = ''
    if args.span:
        time = '-ss {} -to {}'.format(*args.span)

    crop = ''
    if args.crop:
        crop = '-filter:v "crop={}:{}:{}:{}"'.format(*args.crop)

    scale = ''
    if args.scale:
        scale = '-vf scale={}:{}'.format(*args.size)
    elif args.resize:
        scale = '-vf scale=-1:720'

    os.system('ffmpeg -i "{}" -c:v libx264 -crf {crf} {scale} -pix_fmt yuv420p -preset veryslow -an {time} {crop} "{output}"'.format(args.video, time=time, crop=crop, crf=args.crf, scale=scale, output=output))


if __name__ == '__main__':
    main()


