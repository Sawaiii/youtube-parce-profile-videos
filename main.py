import youtube_dl

def get_video_links(channel_url):
    ydl_opts = {
        'quiet': True,
        'extract_flat': True,
        'skip_download': True,
        'force_generic_extractor': True,
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(channel_url, download=False)
    
    video_links = []
    if 'entries' in result:
        for entry in result['entries']:
            if 'url' in entry:
                video_links.append(f"https://www.youtube.com/watch?v={entry['url'].split('/')[-1]}")
    else:
        if 'url' in result:
            video_links.append(f"https://www.youtube.com/watch?v={result['url'].split('/')[-1]}")
    
    return video_links

def save_links_to_file(links, filename='links.txt'):
    with open(filename, 'w') as file:
        for link in links:
            file.write(f"{link}\n")

if __name__ == "__main__":
    channel_url = input("Введите ссылку на YouTube канал: ")
    video_links = get_video_links(channel_url)
    save_links_to_file(video_links)
    print(f"Ссылки на видео сохранены в файл 'links.txt'. Общее количество видео: {len(video_links)}.")
