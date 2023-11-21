# I wrote this with ChatGPT as a collaborative effort

import os
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3, ID3NoHeaderError

def create_album(directory):
    for root, _, files in os.walk(directory):
        # Get the parent directory name to use as the album name
        album_name = os.path.basename(root)
        
        # Create a list to store the MP3 files
        mp3_files = [filename for filename in files if filename.endswith(".mp3")]
        
        # Sort the MP3 files based on their filenames
        mp3_files.sort()
        
        # Create a new album directory
        album_directory = os.path.join(root, album_name)
        os.makedirs(album_directory, exist_ok=True)
        
        # Set track number and add files to the album directory
        for track_number, mp3_file in enumerate(mp3_files, start=1):
            track_path = os.path.join(root, mp3_file)
            new_filename = f"{track_number:02d}_{mp3_file}"
            new_path = os.path.join(album_directory, new_filename)

            try:
                # Try to load ID3 tags for the MP3 file
                audio = EasyID3(track_path)
            except ID3NoHeaderError:
                print(f"Adding ID3 header for {mp3_file}")
                # Create a new ID3 header
                audio = EasyID3()
                
            # Update ID3 tags for the MP3 file
            audio['album'] = album_name
            audio['tracknumber'] = str(track_number)
            audio['title'] = os.path.splitext(os.path.basename(mp3_file))[0]  # Set title as the file name
            audio['artist'] = 'Unknown Artist'
            
            # Save the ID3 tags
            audio.save()

        # Remove empty folder after processing
        if not os.listdir(album_directory):
            os.rmdir(album_directory)

if __name__ == "__main__":
    # Specify the current directory
    current_directory = os.getcwd()
    
    # Call the function to create the album
    create_album(current_directory)
