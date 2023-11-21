# MP3 Metadata Updater

This script recursively processes MP3 files in a given directory, creating albums and setting metadata using the Mutagen library.

## Usage

1. Ensure you have Python installed on your system.
2. Install the required library using:

    ```bash
    pip install mutagen
    ```

3. Copy the script to the directory containing your MP3 files.
4. Open a terminal and navigate to the directory containing the script.
5. Run the script:

    ```bash
    python script_name.py
    ```

## Functionality

- The script processes all MP3 files in the specified directory and its subdirectories.
- It organizes the files into albums named after the direct parent folder.
- Track titles are set as the corresponding file names.
- The artist is set to "Unknown Artist" for all tracks.
- Empty folders are removed after processing.

## Dependencies

- Python 3
- Mutagen library

## Note

Make sure to back up your data before running the script, especially if it will modify your file structure.

Feel free to customize the script to suit your specific needs.
