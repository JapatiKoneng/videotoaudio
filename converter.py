import subprocess
import sys
import os

def get_ffmpeg_path():
    if getattr(sys, 'frozen', False):
        return os.path.join(sys._MEIPASS, "ffmpeg.exe")
    return os.path.join(os.path.dirname(__file__), "ffmpeg.exe")

def convert_to_mp3(input_path: str, output_path: str, bitrate: str = "192k"):
    ffmpeg_path = get_ffmpeg_path()
    print(f"Using FFmpeg: {ffmpeg_path}")
    print(f"FFmpeg exists: {os.path.exists(ffmpeg_path)}")
    print(f"Input: {input_path}")
    print(f"Output: {output_path}")

    command = [
        ffmpeg_path,
        "-i", input_path,
        "-vn",                  # no video
        "-ab", bitrate,         # audio bitrate
        "-ar", "44100",         # sample rate
        "-y",                   # overwrite output
        output_path
    ]

    print(f"Command: {command}")

    try:
        result = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        print(f"Return code: {result.returncode}")
        print(f"STDOUT: {result.stdout.decode(errors='ignore')}")
        print(f"STDERR: {result.stderr.decode(errors='ignore')}")

        if result.returncode == 0:
            return True, None
        else:
            err = result.stderr.decode(errors='ignore')
            return False, err

    except Exception as e:
        print(f"Exception: {str(e)}")
        return False, str(e)