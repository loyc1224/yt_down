os.system("cls")
p = Playlist(playlist_link)
path = "tester"
for video in p.video_urls:
	print(video)
	try:
		yt = YouTube(video,use_oauth=True,allow_oauth_cache=False)

		yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first().download(path)
	except pytube.exceptions.VideoPrivate as e:
		print(f"Error happend with {yt.title} err is {e}\n")
		continue
	except pytube.exceptions.VideoUnavailable as e:
		print(f"Error happend with {yt.title} err is {e}\n")
		continue
	except pytube.exceptions.AgeRestrictedError as e:
		print(f"Error happend with {yt.title} err is {e}\n")
		continue
	except Exception as err:
		print(f"\nSOMETHING UNSEEN HAS HAPPEND VIDEO = {yt.title} ERR = {err}\n")
		print(yt.streams.filter(progressive=True))
	print(f"Downloaded {yt.title}")
	time.sleep(15)`