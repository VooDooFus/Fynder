import os
import chardet
from tqdm import tqdm

def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        rawdata = f.read()
    return chardet.detect(rawdata)['encoding']

def is_text_file(file_path):
    text_extensions = ['.txt', '.csv', '.log', '.md', '.py', '.json']  # Add more extensions if needed
    _, file_extension = os.path.splitext(file_path)
    return file_extension.lower() in text_extensions

def search_word_in_text_files(directory, target_word, max_results=None):
    found_files = []
    total_files = sum([len(files) for _, _, files in os.walk(directory)])
    with tqdm(total=total_files, desc="Searching files", unit="file") as pbar:
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                if os.path.isfile(file_path) and is_text_file(file_path):
                    try:
                        encoding = detect_encoding(file_path)
                        with open(file_path, 'r', encoding=encoding, errors='ignore') as f:
                            for line in f:
                                if target_word in line:
                                    found_files.append(file_path)
                                    pbar.write(f"Found '{target_word}' in: {file_path}")
                                    break
                    except Exception as e:
                        print(f"Error reading file {file_path}: {e}")
                pbar.update(1)
    print("\nSearch completed.")
    if found_files:
        print(f"Total text files found with '{target_word}': {len(found_files)}")
        if max_results:
            print(f"Displaying first {max_results} results:")
            for file_path in found_files[:max_results]:
                print(file_path)
        else:
            print("Text files:")
            for file_path in found_files:
                print(file_path)
    else:
        print(f"No text files found with '{target_word}'.")

# Usage example
directory_to_search = "D:"
target_word = "kink"
max_results = 10  # Set to None if you want to display all results

search_word_in_text_files(directory_to_search, target_word, max_results)
