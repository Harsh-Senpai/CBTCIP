import sounddevice as sd
import wavio

def mic_record(loc_path, duration, samplerate=48000):
    print("Recording is in progress. Please Speak through your Microphone.")
    mic_config = sd.rec(int(samplerate * duration), samplerate=samplerate, channels=2, dtype='int16')
    sd.wait()
    wavio.write(loc_path, mic_config, samplerate, sampwidth=3)

def main():
    print("Welcome to Voice Recorder Program!")
    loc_path = input("Enter the file name with .wav extension to save the recording: ")

    try:
        duration = float(input("Please input the duration of the recording in seconds: "))
    except ValueError:
        print("Invalid input for duration. Please input in seconds.")
        return

    mic_record(loc_path, duration)
    print(f"Recording saved successfully at {loc_path}")

if __name__ == "__main__":
    main()
