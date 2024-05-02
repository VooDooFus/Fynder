# Fynder
File Content Searcher
This Python script allows you to efficiently search for a specific word or phrase within the content of files in a given directory. 
It provides support for detecting file encodings, ensuring compatibility across various file types.

Features:
Flexible Search: Specify the directory to search and the target word or phrase.
Encoding Detection: Automatically detects and handles different file encodings to ensure accurate search results.
Progress Tracking: Utilizes tqdm for displaying progress bars, keeping you informed about the search progress.
Customization: Optionally limit the number of search results displayed.

Usage:
Set the directory_to_search variable to the directory path containing the files you want to search.
Define the target_word variable with the word or phrase you're searching for.
Optionally, set max_results to limit the number of displayed results. Set to None for all results.

Requirements:
chardet
tqdm

/VooDooFus/
