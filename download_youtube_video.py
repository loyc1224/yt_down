import pytube

def download_youtube_video(url, save_path):
    try:
        # Create a YouTube object for the given URL
        youtube = pytube.YouTube(url)
        
        # Select the stream (video quality) you want to download
        stream = youtube.streams.get_highest_resolution()
        
        # Download the video to the specified path
        stream.download(output_path=save_path)
        
        print("Download completed successfully!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    video_url = "https://www.youtube.com/watch?v=lxvx8gS90ag"
    save_directory = "c:/code/tmp"
    
    download_youtube_video(video_url, save_directory)
