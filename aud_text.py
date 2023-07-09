from transformers import pipeline
from moviepy.editor import VideoFileClip
from keybert import KeyBERT
from utol import stop_ffmpeg
import time
import os
import re
from keyphrase_vectorizers import KeyphraseTfidfVectorizer
from pprint import pprint

kw = KeyBERT()
currentpath = os.getcwd()


# Load the video file
# video = VideoFileClip(r"D:\Downloads\Mojo 🔥 — a new programming language for AI developers (first look).mp4")
# # Extract the audio track as a WAV file
# audio = video.audio
# audio.write_audiofile(r"X:\testings\trial_1.mp3")
# # Close the video file
# video.close()
# # file = open(r"E:\testing_3.wav", 'r', encoding="latin1")
# pipe = pipeline(task='automatic-speech-recognition', model=r"facebook/wav2vec2-base-960h")
# print("finished")
# output = pipe(r"X:\testings\trial_1.mp3", chunk_length_s=10, stride_length_s=(4, 2))
# pprint(output)
# type(output)
# keywords = kw.extract_keywords(output['text'], use_mmr=True,keyphrase_ngram_range=(1, 2), top_n=20)
# pprint(keywords)


def change_file_extension(filepath, new_extension):
    # Use regular expressions to replace the current extension with the new extension
    new_filepath = re.sub(r"\.[^.]+$", f".{new_extension}", filepath)

    # Rename the file
    # os.rename(filepath, new_filepath)

    return new_filepath


# Example usage:
# filepath = r"X:\Videos\Working with config files in Python.mp4"
# new_extension = "mp3"
#
# new_filepath = change_file_extension(filepath, new_extension)
# print(f"File renamed to: {new_filepath}")
# print(new_filepath)


def audio_tags_generator(filepath):
    pipe = pipeline(task='automatic-speech-recognition', model=r"openai/whisper-tiny")
    output = pipe(filepath, chunk_length_s=10, stride_length_s=(4, 2))
    tags = kw.extract_keywords(output['text'], vectorizer=KeyphraseTfidfVectorizer(), top_n=20)
    return tags


def video_tags_generator(filepath):
    new_extension = "mp3"
    video = VideoFileClip(filepath)
    audio = video.audio
    # old_file_name = Path(filepath).name
    # extension = extension_finder(filepath)
    new_file_path = change_file_extension(filepath, new_extension)
    print(new_file_path)
    audio.write_audiofile(new_file_path)
    audio.close()
    time.sleep(4)
    audio = None
    pipe = pipeline(task='automatic-speech-recognition', model=r"openai/whisper-tiny")
    output = pipe(new_file_path, chunk_length_s=10, stride_length_s=(4, 2))
    pprint(output['text'])
    tags = kw.extract_keywords(output['text'], vectorizer=KeyphraseTfidfVectorizer(), top_n=20)
    video.reader.close()
    stop_ffmpeg()
    os.remove(new_file_path)

    return tags

# Example usage
# process_id = 8944
# result = stop_process(process_id)
#
# if result:
#     print(f"Process {process_id} has been terminated.")
# else:
#     print(f"Process {process_id} could not be found.")


#
# def get_pid_for_file_windows(filepath):
#     for proc in psutil.process_iter(['pid', 'name']):
#         try:
#             file_handles = proc.open_files()
#             for handle in file_handles:
#                 if handle.path == filepath:
#                     return proc.pid
#         except (psutil.AccessDenied, psutil.NoSuchProcess):
#             pass
#     return None
