

# 1.Whisper 라이브러리 불러오기
import whisper

# 2.모델 로드하기
model = whisper.load_model("small")  # tiny, base, small, medium, large

# 3.음성 파일을 읽어들여 변환 .wav, .mp3, .m4a, .webm, .ogg, .flac 등
audio = r"/Users/jun/Documents/깃/ktcloud_genai/아동-영어1.wav"
result = model.transcribe(audio, fp16=False)  # fp16=False 옵션은 CPU 환경에서 필요
print(result["text"])


# 4.결과 출력 또는 저장
with open("output_eng.txt", "w", encoding="utf-8") as f:
    f.write(result["text"])