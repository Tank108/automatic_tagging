from torch.onnx.symbolic_opset11 import chunk
from transformers import pipeline
from moviepy.editor import *
from pprint import pprint
from keybert import KeyBERT
from keyphrase_vectorizers import KeyphraseCountVectorizer
from tqdm import tqdm
kw = KeyBERT()
# Load the video file
video = VideoFileClip(r"D:\Downloads\Mojo 🔥 — a new programming language for AI developers (first look).mp4")

# Extract the audio track as a WAV file
audio = video.audio

audio.write_audiofile(r"X:\testings\trial_1.mp3")

# Close the video file
video.close()

# file = open(r"E:\testing_3.wav", 'r', encoding="latin1")

pipe = pipeline(task='automatic-speech-recognition', model=r"facebook/wav2vec2-base-960h")

print("finished")

output = pipe(r"X:\testings\trial_1.mp3", chunk_length_s=10, stride_length_s=(4, 2))

pprint(output)

type(output)


keywords = kw.extract_keywords(output['text'], use_mmr=True,keyphrase_ngram_range=(1, 2), top_n=20)
pprint(keywords)


