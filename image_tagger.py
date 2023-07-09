import os
import re


def change_file_extension(filepath, new_extension):
    # Use regular expressions to replace the current extension with the new extension
    new_filepath = re.sub(r"\.[^.]+$", f".{new_extension}", filepath)

    # Rename the file
    os.rename(filepath, new_filepath)

    return new_filepath

# Example usage:
filepath = r"X:\Videos\Working with config files in Python.mp4"
new_extension = "mp3"

new_filepath = change_file_extension(filepath, new_extension)
print(f"File renamed to: {new_filepath}")
print(new_filepath)



# from transformers import pipeline
# from pprint import pprint
#
# from OpenSeq2Seq.open_seq2seq.data.text2text.t2t import _filter_max_length
#
# pipe = pipeline(task="image-to-text",model="nlpconnect/vit-gpt2-image-captioning")
#
#
# text = pipe(r"E:\images\images.jpg",_filter_max_length())
#
# pprint(text)
#
#
#



# import speech_recognition as sr
# import moviepy.editor as mp
# from pydub import AudioSegment
# from pprint import pprint
# from pathlib import Path
# from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
# from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_audio
#
# filepath = r'C:\Users\DELL\Downloads\ML.mp4'
# audio_path = r'C:\Users\DELL\Downloads\ML.mp3'
#
# video_clip = mp.VideoFileClip(filepath)
#
# video_clip.audio.write_audiofile(audio_path)
#
# r = sr.Recognizer()
#
#
# sound = AudioSegment.from_mp3(audio_path)
#
# len(sound)
#
# chunksize = 60*1000
#
#
# def audio_chunks(audio, chunksize=60000):
#     for i in range(0,len(audio),chunksize):
#         yield sound[i: i+chunksize]
#
# chunks = list(audio_chunks(audio_path, chunksize))
# print(f"{len(chunks)} chunks of {chunksize/1000}s each")
# len(chunks)
#
#
# r = sr.Recognizer()
# string_index = {}
#
#
# for index, chunk in enumerate(chunks):
#     chunk.export(r'C:\Users\DELL\Downloads\ML.wav', format='wav')
#     with sr.AudioFile(r'C:\Users\DELL\Downloads\ML.wav') as source:
#         audio = r.record(source)
#     s = r.recognize_google(audio)
#     print(s)
#     string_index[index] = s
#
#
#
#
# pprint(string_index)
#
#
#
#
#
# #
# # def process(filepath, chunksize=60000):
# #     #0: load mp3
# #     sound = AudioSegment.from_mp3(filepath)
# #
# #     #1: split file into 60s chunks
# #     def divide_chunks(sound, chunksize):
# #         # looping till length l
# #         for i in range(0, len(sound), chunksize):
# #             yield sound[i:i + chunksize]
# #     chunks = list(divide_chunks(sound, chunksize))
# #     print(f"{len(chunks)} chunks of {chunksize/1000}s each")
# #
# #     r = sr.Recognizer()
# #     #2: per chunk, save to wav, then read and run through recognize_google()
# #     string_index = {}
# #     for index,chunk in enumerate(chunks):
# #         #TODO io.BytesIO()
# #         chunk.export('/Users/mmaxmeister/Downloads/test.wav', format='wav')
# #         with sr.AudioFile('/Users/mmaxmeister/Downloads/test.wav') as source:
# #             audio = r.record(source)
# #         #s = r.recognize_google(audio, language="en-US") #, key=API_KEY) --- my key results in broken pipe
# #         s = r.recognize_google(audio, language="en-US")
# #         print(s)
# #         string_index[index] = s
# #         break
# #     return string_index
# #
# # text = process('/Users/mmaxmeister/Downloads/UUCM.mp3')
#
