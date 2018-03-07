#!/usr/bin/env python3
import argparse
import os

from shlex import quote


EXT = '.mp4'


def run(command):
    print("RUN COMMAND:\n    " + command)
    os.system(command)


def make_clip(args):
    fmt = {
        'crf': args.crf,
        'other': args.other,
    }
    vf = []

    if args.output:
        output = args.output
    else:
        # Auto name output file.
        prefix = '[GIF]{}'.format(os.path.basename(os.path.splitext(args.video)[0]))
        suffix = 1
        name = ''
        while True:
            name = '{} - {}{}'.format(prefix, suffix, EXT) 
            if not os.path.exists(name):
                break
            suffix += 1
        output = name

    fmt['time'] = ""
    if args.span and args.frame:
        raise RuntimeError("--span and --frame can't specified at the same time.")
    else:
        if args.span:
            fmt['time'] = '-ss {} -to {}'.format(*args.span)
        if args.frame:
            vf.append('select=between(n\,{}\,{}),setpts=PTS-STARTPTS'.format(*args.frame))

    if args.crop:
        vf.append('crop={}:{}:{}:{}'.format(*args.crop))

    fmt['an'] = '-an'
    if args.audio:
        fmt['an'] = ''

    scale = ''
    if args.scale:
        scale = 'scale={}:{}'.format(*args.scale)
    elif args.resize720:
        scale = 'scale=-1:720'
    if scale != '':
        vf.append(scale)

    if args.ass:
        vf.append('ass={}'.format(args.ass))

    if args.filter:
        vf.extend(args.filter)
    if len(vf) != 0:
        fmt['vf'] = '-vf {}'.format(quote(','.join(vf)))
    else:
        fmt['vf'] = ''

    run('ffmpeg -i {input} {time} -c:v libx264 -crf {crf} {vf}  -pix_fmt yuv420p -preset veryslow {other} {an} {output}'
        .format(input=quote(args.video), output=quote(output), **fmt))
    return output

def make_gif(args, input):
    gif_fps = 15
    run('ffmpeg -i {} -vf "fps={fps},{resize}:-1:flags=lanczos,palettegen" yibasuo_palette.png'
        .format(quote(input), resize=resize, fps=gif_fps))
    run('ffmpeg -i {input} -i yibasuo_palette.png -filter_complex'
        ' "fps={fps},{resize}:flags=lanczos[x];[x][1:v]paletteuse" {output}'
        .format(input=quote(input), output=quote('{}.gif'.format(os.path.splitext(os.path.basename(input))[0])),
                resize=resize, fps=gif_fps))
    run('rm yibasuo_palette.png')



def make_reverse(args):
    output = '[REVERSE]{}'.format(os.path.basename(args.video))
    run('ffmpeg -i {} -vf reverse {}'.format(quote(args.video), quote(output)))
    return output


def main():
    parser = argparse.ArgumentParser(description='Generate GIF-like MP4 video for Telegram/Twitter/etc.')
    parser.add_argument('video', type=str, help='The input video path.')
    parser.add_argument('--span', nargs=2, type=str, metavar=('START', 'END'), help='Specify cut time.')
    parser.add_argument('--frame', nargs=2, type=int, metavar=('START', 'END'), help='Specify cut frame.')
    parser.add_argument('--crop', nargs=4, type=str, metavar=('WIDTH', 'HEIGHT', 'X', 'Y'), help='Crop input video.')
    parser.add_argument('--crf', type=int, default=23, help='Specify the Constant Rate Factor of output video.')
    parser.add_argument('--720p', action='store_true', dest='resize720', help='Auto resize input video to 720P.')
    parser.add_argument('--audio', action='store_true', help="Don't remove input video audio track.")
    parser.add_argument('--with-gif', dest='gif', action='store_true', help="Generate addition .gif output file.")
    parser.add_argument('--gif', dest='gif_only', action='store_true', help="Convert input video to .gif file.")
    parser.add_argument('--reverse', action='store_true', help="ONLY reverse input video, other arguments invalid (except --gif).")
    parser.add_argument('--ass', type=str, help="Burn .ass subtitle into the video.")
    parser.add_argument('--scale', type=str, nargs=2, metavar=('W', 'H'), help='ffmepg -vf scale=W:H')
    parser.add_argument('--filter', type=str, nargs='+', help='ffmepg -vf ...')
    parser.add_argument('--other', type=str, default='', help='Other ffmepg arguments.')
    parser.add_argument('-o', '--output', metavar='output', type=str)
    args = parser.parse_args()

    if not os.path.isfile(args.video):
        raise RuntimeError('Wrong input video path.')

    if args.reverse:
        output = make_reverse(args)
    else:
        output = make_clip(args)
    
    if args.gif:
        make_gif(args, output)
    elif args.gif_only:
        make_gif(args, args.video)



if __name__ == '__main__':
    main()


