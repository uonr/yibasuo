#!/usr/bin/env python3
import argparse
import os


EXT = '.mp4'


def run(command):
    # print(command)
    os.system(command)


def main():
    parser = argparse.ArgumentParser(description='Generate GIF-like MP4 video for Telegram/Twitter/etc.')
    parser.add_argument('video', type=str, help='The input video path.')
    parser.add_argument('--span', nargs=2, type=str, metavar=('START', 'END'), help='Specify cut time.')
    parser.add_argument('--frame', nargs=2, type=int, metavar=('START', 'END'), help='Specify cut frame.')
    parser.add_argument('--crop', nargs=4, type=str, metavar=('WIDTH', 'HEIGHT', 'X', 'Y'), help='Crop input video.')
    parser.add_argument('--crf', type=int, default=23, help='Specify the Constant Rate Factor of output video.')
    parser.add_argument('--resize', action='store_true', help='Auto resize input video to 720P.')
    parser.add_argument('--scale', type=str, nargs=2, metavar=('W', 'H'), help='ffmepg -vf scale=W:H')
    parser.add_argument('-o', '--output', metavar='output', type=str)
    args = parser.parse_args()

    if not os.path.isfile(args.video):
        raise RuntimeError('Wrong input video path.')

    fmt = {
        'crf': args.crf,
    }
    vf = []

    if args.output:
        fmt['output'] = args.output
    else:
        # Auto name output file.
        fmt['output'] = '[GIF]{}'.format(os.path.basename(os.path.splitext(args.video)[0]))
        prefix = 1
        new_name = fmt['output']
        while os.path.exists(new_name+EXT):
            prefix += 1
            new_name = '{} - {}'.format(fmt['output'], prefix)
        fmt['output'] = new_name

        fmt['output'] += EXT

    fmt['time'] = ''

    if args.span and args.frame:
        raise RuntimeError("--span and --frame can't specified at the same time.")
    else:
        if args.span:
            fmt['time'] = '-ss {} -to {}'.format(*args.span)
        if args.frame:
            vf.append('select=between(n\,{}\,{}),setpts=PTS-STARTPTS'.format(*args.frame))

    if args.crop:
        vf.append('crop={}:{}:{}:{}'.format(*args.crop))

    if args.scale:
        vf.append('scale={}:{}'.format(*args.size))
    elif args.resize:
        vf.append('scale=-1:720')

    fmt['vf'] = '-vf "{}"'.format(','.join(vf))

    run('ffmpeg -i "{}" -c:v libx264 -crf {crf} {vf} -pix_fmt yuv420p -preset veryslow -an "{output}"'
        .format(args.video, **fmt))


if __name__ == '__main__':
    main()


