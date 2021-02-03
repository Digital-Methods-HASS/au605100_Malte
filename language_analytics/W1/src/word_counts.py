# Importing packages
import os

from pathlib import Path
import pandas as pd

root_dir = Path.cwd()  # Setting root directory.

data_dir = root_dir / "data" / "100_english_novels" / "corpus"  # Setting data directory.

files = [file for file in data_dir.glob("*.txt") if file.is_file()]  # Using list comprehension to get all the file names if they are files.

# Creating empty lists

filename = []

total_words = []

unique_words = []

# Loop for iterating through the different files.
for file in files:

    novel_file_name = os.path.split(file)[-1]  # I take the last snippet of the path, which is the novel filename.

    filename.append(novel_file_name)  # Append each filename to the list.

    # Read each file.
    with open(file, encoding="utf-8") as f:

        novel = f.read()

        f.close()

    tokens = novel.split()  # I split the tokens by whitespace. Do note that to get a proper tokenization, more clever solutions could be applied. See fx NLTK's tokenizer.

    total_words.append(len(tokens))  # I append the length of the tokens from each novel.

    unique_tokens = set(tokens)  # Create a set of unique tokens.

    unique_words.append(len(unique_tokens))  # I append the number of unique tokens from each novel.

# Creating Python dictionary to use for pandas. If there are more efficient ways to create a pandas DataFrame from scratch - please let me know :-)
data_dict = {"filename": filename,
             "total_words": total_words,
             "unique_words": unique_words}

df = pd.DataFrame(data=data_dict)

df.to_csv("word_counts.csv")  # Writing data to csv.
