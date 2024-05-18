import os
from Services.audio_recorder import AudioRecorder
from Services.tts_handler import TTSHandler
import whisper
import openai
from pydub import AudioSegment
from pydub.playback import play

# Initialize the OpenAI client
client = openai.OpenAI(
    base_url='http://192.168.1.169:11434/v1',
    api_key='ollama',  # required, but unused
)

# tts_handler_en = TTSHandler(language="EN")
tts_handler_es = TTSHandler(language="ES")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def record_audio(recorder):
    recorder.clear_file()
    print("ile cleared")
    print("--------------------------------------------------")
    print("Press Enter to start recording. Press Enter again to stop recording.")
    print("--------------------------------------------------")
    recorder.record()
    input("\nPress enter to finish the record:\n")
    recorder.stop_recording()
    print("--------------------------------------------------")
    print("Record Finished")
    recorder.save_to_file()

def transcribe_audio(audio_file):
    clear_screen()
    print("--------------------------------------------------")
    print("Transcribing audio...")
    model = whisper.load_model("small")


    # audio = whisper.load_audio(audio_file)
    # audio = whisper.pad_or_trim(audio)
    # mel = whisper.log_mel_spectrogram(audio).to(model.device)
    # _, probs = model.detect_language(mel)
    # language = max(probs, key=probs.get)

    result = model.transcribe(audio_file)
    print("--------------------------------------------------")
    print("Transcription:")
    print(result["text"])
    # return result["text"], language
    return result["text"], ''
    

def get_response(user_input):
    response = client.chat.completions.create(
        model="mane",
        messages=[
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message.content

def play_audio(audio_file):
    audio = AudioSegment.from_file(audio_file)
    play(audio)

def main():
    filename = "recorded_audio.wav"
    while True:
        record_audio(AudioRecorder(filename))
        transcription, language = transcribe_audio(filename)
        print("--------------------------------------------------")
        print("Chatbot response:")
        bot_response = get_response(transcription)
        print("\n" + bot_response)
        print("--------------------------------------------------")
        
        
        print("Generating TTS response...")
        # if language == "en":
        #     tts_output_path = tts_handler_en.tts_to_file(bot_response)
        # elif language == "es":
        #     tts_output_path = tts_handler_es.tts_to_file(bot_response)
        # else:
        #     print("Language not supported")
        #     break
        tts_output_path = tts_handler_es.tts_to_file(bot_response)

        
        
        print("Playing audio response...")
        play_audio(tts_output_path)

if __name__ == "__main__":
    main()
