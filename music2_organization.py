import os
import shutil
import pandas as pd

# Paths
base_path = r"D:\music2"
# train_metadata_path = os.path.join(base_path, "Metadata_Train.csv")
# train_data_path = os.path.join(base_path, "Train_submission")

test_data_path = os.path.join(base_path, "Test_submission")
test_metadata_path = os.path.join(base_path, "Metadata_Test.csv")

output_path = os.path.join(base_path, "Test_submission")

# Load metadata
print("Loading metadata...")
# train_metadata = pd.read_csv(train_metadata_path)

test_metadata = pd.read_csv(test_metadata_path)

metadata = pd.concat([test_metadata], ignore_index=True)

# Print metadata columns
print(f"Metadata columns: {metadata.columns}")

# Check unique instruments
if 'Class' not in metadata.columns or 'FileName' not in metadata.columns:
    raise ValueError("Metadata must have 'Class' and 'FileName' columns.")

print("Unique instruments found:", metadata['Class'].unique())

# Create folders for each instrument
os.makedirs(output_path, exist_ok=True)
for instrument in metadata['Class'].unique():  # Use 'Class' to create folders
    instrument_folder = os.path.join(output_path, instrument)
    os.makedirs(instrument_folder, exist_ok=True)
    print(f"Created folder: {instrument_folder}")

# Move files into respective folders
print("Organizing files...")
for _, row in metadata.iterrows():
    file_name = row['FileName']
    instrument = row['Class']
    
    # Determine the source path
    # src = os.path.join(train_data_path, file_name)
    # if not os.path.exists(src):
    src = os.path.join(test_data_path, file_name)
    
    # Log if the file is missing
    if not os.path.exists(src):
        print(f"File not found: {file_name}")
        continue
    
    # Destination path
    dst = os.path.join(output_path, instrument, file_name)
    shutil.move(src, dst)
    print(f"Moved {file_name} to {dst}")

print("Files organized successfully!")
