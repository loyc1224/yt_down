import pytube
import ssl
from pytube import Playlist, YouTube
ssl._create_default_https_context = ssl._create_stdlib_context

def download_video(url, save_path):
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


# def download_list(url, save_path):      
#     try:
#         # Create a YouTube object for the given URL
#         youtube = pytube.YouTube(url)
        
#         if 'playlist' in url.lower():
#             # If the URL is a playlist, get all video URLs in the playlist
#             playlist = youtube.playlist()
#             video_urls = [video['url'] for video in playlist['videos']]
#         else:
#             # If the URL is a single video, use it directly
#             video_urls = [url]

#         # Download each video in the playlist
#         print(video_urls)
#         for video_url in video_urls:
#             video = pytube.YouTube(video_url)
            
#             # Select the stream (video quality) you want to download
#             stream = video.streams.get_highest_resolution()
            
#             # Download the video to the specified path
#             stream.download(output_path=save_path)
            
#             print(f"Downloaded video: {video.title}")

#         print("Download completed successfully!")
#     except Exception as e:
#         print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    video_url = "https://www.youtube.com/watch?v=4QlhNOVaY-E&list=PLE-R0uydm0uMPY7cu-kuEkcPHAM0M9Cby&index=31"
    #url_playlist="https://www.youtube.com/playlist?list=PLQp8cEU
    # Q8n-DfG6VGVYrxkkqmli1utAeU"
    
    save_directory = f"C:\code\yt_down\out"
   
    
    download_video(video_url, save_directory)
    #ownload_list(url_playlist, save_directory)

