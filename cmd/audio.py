import os
import subprocess

import click

from pydub import audio_segment as pydub, playback, silence


class Skip(Exception):
    pass


class Strings:
    SPLIT_INTRO = "Splitting audio..."
    SPLIT_OUTRO = "Done"

    REENCODE_INTRO = "Re-encoding audio files..."
    REENCODE_OUTRO = "Done"

    SKIP = "-"
    REPLAY = "?"

    NAME_PROMPT_OPTIONS = "(‘{replay}’ to listen again, ‘{skip}’ to skip)"
    NAME_PROMPT_OPTIONS = NAME_PROMPT_OPTIONS.format(replay=REPLAY, skip=SKIP)

    NAME_PROMPT = "Type a file name for this audio segment {options}"
    NAME_PROMPT = NAME_PROMPT.format(options=NAME_PROMPT_OPTIONS)

    SKIPPING_AUDIO = "Skipping audio segment..."
    NO_SILENCE_ERROR = "Couldn’t find any silent segments in the file to split on"


class SilenceConf:
    DEFAULT = "stricter"

    looser = dict(
        min_silence_len=150,
        silence_thresh=-30,
        keep_silence=300
    )
    stricter = dict(
        min_silence_len=125,
        silence_thresh=-40,
        keep_silence=300
    )

    @classmethod
    def get(cls, name):
        return getattr(cls, name)


def pad(s, bullet=True):
    b = "•" if bullet else " "
    return " {b} {str}".format(b=b, str=s)


def play_and_ask_for_name(segment):
    playback.play(segment)

    answer = click.prompt(pad(Strings.NAME_PROMPT))
    if answer == Strings.REPLAY:
        answer = play_and_ask_for_name(segment)
    if answer == Strings.SKIP:
        raise Skip()

    return answer


def export_segment_with_name(segment, out_folder, name):
    name = name if name.endswith(".m4a") else name + ".m4a"
    segment.export(os.path.join(out_folder, name), format="mp4")


def split_audio(audio_path, out_folder, silence_config):
    audio = pydub.AudioSegment.from_file(audio_path, "mp4")
    segments = silence.split_on_silence(audio, **silence_config)

    if not len(segments):
        raise click.ClickException(Strings.NO_SILENCE_ERROR)

    for segment in segments:
        try:
            name = play_and_ask_for_name(segment)
        except Skip:
            click.echo(pad(Strings.SKIPPING_AUDIO, bullet=False))
        else:
            export_segment_with_name(segment, out_folder, name)


def reencode_audio(in_folder, out_folder):
    for filename in os.listdir(in_folder):
        if filename.startswith("."):
            continue

        in_ = os.path.join(in_folder, filename)

        if os.path.isdir(in_):
            continue

        out = os.path.join(out_folder, filename)
        command = ["ffmpeg", "-i", in_, "-codec", "copy", out]

        subprocess.run(command, check=True)


@click.group()
def cli():
    pass


existing_path = lambda: click.Path(exists=True, resolve_path=True)


@cli.command()
@click.argument("audio_path", type=existing_path())
@click.argument("out_folder", type=existing_path())
@click.option("-s", "--silence", default=SilenceConf.DEFAULT)
def split(audio_path, out_folder, silence):
    click.echo(Strings.INTRO)
    split_audio(audio_path, out_folder, SilenceConf.get(silence))
    click.echo(Strings.OUTRO)


@cli.command()
@click.argument("in_folder", type=existing_path())
@click.argument("out_folder", type=existing_path())
def reencode(in_folder, out_folder):
    click.echo(Strings.REENCODE_INTRO)
    reencode_audio(in_folder, out_folder)
    click.echo(Strings.REENCODE_OUTRO)


if __name__ == "__main__":
    cli()