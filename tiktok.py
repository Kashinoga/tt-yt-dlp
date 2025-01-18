import json
import subprocess

# Path to your TikTok data JSON file
data_file = './user_data_tiktok.json'

# Load the JSON data
with open(data_file, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Extract liked videos
liked_videos = data.get('Activity', {}).get('Favorite Videos', []).get('FavoriteVideoList', [])

# Download each video using yt-dlp
for video in liked_videos:
    video_info = video.get('link', '')
    # video_id = video_info.get('ID', '')
    # play_addr = video_info.get('PlayAddr', '')
    # download_addr = video_info.get('DownloadAddr', '')
    # author_unique_id = video_info.get('Author', {}).get('UniqueId', '')

    print(video_info, 'video info')
    # Prioritize DownloadAddr, then PlayAddr, then construct URL with Video ID
    # if download_addr:
    #     print('VIDEO URL DOWNLOAD', download_addr)
    #     video_url = download_addr
    # elif play_addr:
    #     print('video url play addr', play_addr)
    #     video_url = play_addr
    # else:
    # video_url = 'https://www.tiktok.com/@{author_unique_id}/video/{video_id}'

    # Call yt-dlp to download the video
    subprocess.run(['yt-dlp', video_info])