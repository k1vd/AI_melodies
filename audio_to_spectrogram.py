import os
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

# Paths
input_base_path = r"D:\music2"
output_base_path = r"D:\music2_spectrograms"

# Function to convert audio to spectrogram
def audio_to_spectrogram(audio_path, output_path):
    try:
        # Load audio file
        y, sr = librosa.load(audio_path, sr=None)
        
        # Generate Mel spectrogram
        mel_spectrogram = librosa.feature.melspectrogram(y=y, sr=sr, n_fft=2048, hop_length=512, n_mels=128)
        mel_spectrogram_db = librosa.power_to_db(mel_spectrogram, ref=np.max)
        
        # Plot and save the spectrogram
        plt.figure(figsize=(10, 4))
        librosa.display.specshow(mel_spectrogram_db, sr=sr, hop_length=512, x_axis='time', y_axis='mel')
        plt.colorbar(format='%+2.0f dB')
        plt.title('Mel Spectrogram')
        plt.tight_layout()
        plt.savefig(output_path, dpi=300, bbox_inches='tight', pad_inches=0)
        plt.close()
    except Exception as e:
        print(f"Error processing {audio_path}: {e}")

# Process each split (Train and Test)
for split in ["Train_submission", "Test_submission"]:
    input_split_path = os.path.join(input_base_path, split)
    output_split_path = os.path.join(output_base_path, split)
    
    # Process each instrument folder
    for instrument in os.listdir(input_split_path):
        instrument_input_path = os.path.join(input_split_path, instrument)
        instrument_output_path = os.path.join(output_split_path, instrument)
        os.makedirs(instrument_output_path, exist_ok=True)
        
        # Process each audio file
        for audio_file in os.listdir(instrument_input_path):
            if audio_file.endswith(".wav"):
                input_audio_path = os.path.join(instrument_input_path, audio_file)
                output_image_path = os.path.join(instrument_output_path, audio_file.replace(".wav", ".png"))
                
                print(f"Processing {input_audio_path} -> {output_image_path}")
                audio_to_spectrogram(input_audio_path, output_image_path)

print("Spectrogram generation completed!")
