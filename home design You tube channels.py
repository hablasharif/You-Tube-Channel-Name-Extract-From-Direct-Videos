import re
import requests
from bs4 import BeautifulSoup

def get_video_id(url):
    """Extract the video ID from a YouTube URL."""
    pattern = re.compile(r'(?:v=|\/)([0-9A-Za-z_-]{11}).*')
    match = pattern.search(url)
    return match.group(1) if match else None

def get_channel_name_and_url(video_url):
    """Get the channel name and URL of a YouTube video by scraping the video page."""
    response = requests.get(video_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        channel_name_tag = soup.find('link', itemprop='name')
        channel_url_tag = soup.find('link', itemprop='url')
        if channel_name_tag and channel_url_tag:
            return channel_name_tag['content'], channel_url_tag['href']
    return None, None

def main(urls):
    """Main function to process a list of YouTube video URLs and save the output as markdown."""
    processed_channels = set()
    with open('Home Design Youtube Channels.md', 'w', encoding='utf-8') as file:
        for url in urls:
            video_id = get_video_id(url)
            if video_id:
                channel_name, channel_url = get_channel_name_and_url(url)
                if channel_name and channel_url:
                    if channel_name not in processed_channels:
                        file.write(f"URL: {url}\nChannel Name: [{channel_name}]({channel_url})\n\n")
                        processed_channels.add(channel_name)
                else:
                    file.write(f"URL: {url}\nChannel Name: Not Found\n\n")
            else:
                file.write(f"URL: {url}\nError: Invalid URL\n\n")

if __name__ == "__main__":
    youtube_urls = [
"https://www.youtube.com/watch?v=5u0ryaR6mvQ&pp=ygU64Kas4Ka-4Kah4Ka84Ka_IOCmpOCniOCmsOCmvyDgppXgprDgpr4g4Kah4Ka_4Kac4Ka-4KaH4KaoIA%3D%3D",
"https://www.youtube.com/watch?v=RHQOpTY-Lsg&pp=ygU64Kas4Ka-4Kah4Ka84Ka_IOCmpOCniOCmsOCmvyDgppXgprDgpr4g4Kah4Ka_4Kac4Ka-4KaH4KaoIA%3D%3D",
"https://www.youtube.com/watch?v=cetxXC9baFI&pp=ygU64Kas4Ka-4Kah4Ka84Ka_IOCmpOCniOCmsOCmvyDgppXgprDgpr4g4Kah4Ka_4Kac4Ka-4KaH4KaoIA%3D%3D",
"https://www.youtube.com/watch?v=7gscw0fM0YQ&pp=ygU64Kas4Ka-4Kah4Ka84Ka_IOCmpOCniOCmsOCmvyDgppXgprDgpr4g4Kah4Ka_4Kac4Ka-4KaH4KaoIA%3D%3D",
"https://www.youtube.com/watch?v=UtBCglSpilA&pp=ygU64Kas4Ka-4Kah4Ka84Ka_IOCmpOCniOCmsOCmvyDgppXgprDgpr4g4Kah4Ka_4Kac4Ka-4KaH4KaoIA%3D%3D",
"https://www.youtube.com/watch?v=s7BW_9OmNcE&pp=ygU64Kas4Ka-4Kah4Ka84Ka_IOCmpOCniOCmsOCmvyDgppXgprDgpr4g4Kah4Ka_4Kac4Ka-4KaH4KaoIA%3D%3D",
"https://www.youtube.com/watch?v=c6wCrJ8naIM&pp=ygU64Kas4Ka-4Kah4Ka84Ka_IOCmpOCniOCmsOCmvyDgppXgprDgpr4g4Kah4Ka_4Kac4Ka-4KaH4KaoIA%3D%3D",
"https://www.youtube.com/watch?v=oFzaHZd5vfY&t=638s&pp=ygU64Kas4Ka-4Kah4Ka84Ka_IOCmpOCniOCmsOCmvyDgppXgprDgpr4g4Kah4Ka_4Kac4Ka-4KaH4KaoIA%3D%3D",
"https://www.youtube.com/watch?v=TH8AXH5GJEY&pp=ygU64Kas4Ka-4Kah4Ka84Ka_IOCmpOCniOCmsOCmvyDgppXgprDgpr4g4Kah4Ka_4Kac4Ka-4KaH4KaoIA%3D%3D",
"https://www.youtube.com/watch?v=CPW2QHFbbZ0&pp=ygU64Kas4Ka-4Kah4Ka84Ka_IOCmpOCniOCmsOCmvyDgppXgprDgpr4g4Kah4Ka_4Kac4Ka-4KaH4KaoIA%3D%3D",
"https://www.youtube.com/watch?v=Cw_jxlSc_jM&pp=ygU64Kas4Ka-4Kah4Ka84Ka_IOCmpOCniOCmsOCmvyDgppXgprDgpr4g4Kah4Ka_4Kac4Ka-4KaH4KaoIA%3D%3D",
"https://www.youtube.com/watch?v=U67s-YI8yec&pp=ygU64Kas4Ka-4Kah4Ka84Ka_IOCmpOCniOCmsOCmvyDgppXgprDgpr4g4Kah4Ka_4Kac4Ka-4KaH4KaoIA%3D%3D",
"https://www.youtube.com/watch?v=z6OWFBdlDnQ&pp=ygU64Kas4Ka-4Kah4Ka84Ka_IOCmpOCniOCmsOCmvyDgppXgprDgpr4g4Kah4Ka_4Kac4Ka-4KaH4KaoIA%3D%3D",
"https://www.youtube.com/watch?v=l90Wjg2Z8T8&pp=ygU64Kas4Ka-4Kah4Ka84Ka_IOCmpOCniOCmsOCmvyDgppXgprDgpr4g4Kah4Ka_4Kac4Ka-4KaH4KaoIA%3D%3D",
"https://www.youtube.com/watch?v=EOXJGqiyKjE&pp=ygU64Kas4Ka-4Kah4Ka84Ka_IOCmpOCniOCmsOCmvyDgppXgprDgpr4g4Kah4Ka_4Kac4Ka-4KaH4KaoIA%3D%3D",
"https://www.youtube.com/watch?v=veOiToA1G7k&pp=ygU64Kas4Ka-4Kah4Ka84Ka_IOCmpOCniOCmsOCmvyDgppXgprDgpr4g4Kah4Ka_4Kac4Ka-4KaH4KaoIA%3D%3D",
"https://www.youtube.com/watch?v=ETwl27HpO2I&pp=ygU64Kas4Ka-4Kah4Ka84Ka_IOCmpOCniOCmsOCmvyDgppXgprDgpr4g4Kah4Ka_4Kac4Ka-4KaH4KaoIA%3D%3D",
"https://www.youtube.com/watch?v=MbU-i3IXrUY&pp=ygU64Kas4Ka-4Kah4Ka84Ka_IOCmpOCniOCmsOCmvyDgppXgprDgpr4g4Kah4Ka_4Kac4Ka-4KaH4KaoIA%3D%3D",
"https://www.youtube.com/watch?v=oTJ4lSFIkPk&pp=ygU64Kas4Ka-4Kah4Ka84Ka_IOCmpOCniOCmsOCmvyDgppXgprDgpr4g4Kah4Ka_4Kac4Ka-4KaH4KaoIA%3D%3D",
"https://www.youtube.com/watch?v=QYMTi17c3WU&pp=ygU64Kas4Ka-4Kah4Ka84Ka_IOCmpOCniOCmsOCmvyDgppXgprDgpr4g4Kah4Ka_4Kac4Ka-4KaH4KaoIA%3D%3D",
"https://www.youtube.com/watch?v=VwfcYL3wN24&pp=ygU64Kas4Ka-4Kah4Ka84Ka_IOCmpOCniOCmsOCmvyDgppXgprDgpr4g4Kah4Ka_4Kac4Ka-4KaH4KaoIA%3D%3D",
"https://www.youtube.com/watch?v=q_EnK1702gE&pp=ygU64Kas4Ka-4Kah4Ka84Ka_IOCmpOCniOCmsOCmvyDgppXgprDgpr4g4Kah4Ka_4Kac4Ka-4KaH4KaoIA%3D%3D",
"https://www.youtube.com/watch?v=9R2SRLtTK3w&pp=ygU64Kas4Ka-4Kah4Ka84Ka_IOCmpOCniOCmsOCmvyDgppXgprDgpr4g4Kah4Ka_4Kac4Ka-4KaH4KaoIA%3D%3D",
"https://www.youtube.com/watch?v=Ryli6JFe47Q&pp=ygU64Kas4Ka-4Kah4Ka84Ka_IOCmpOCniOCmsOCmvyDgppXgprDgpr4g4Kah4Ka_4Kac4Ka-4KaH4KaoIA%3D%3D",
"https://www.youtube.com/watch?v=v2GovcTneSw&pp=ygU64Kas4Ka-4Kah4Ka84Ka_IOCmpOCniOCmsOCmvyDgppXgprDgpr4g4Kah4Ka_4Kac4Ka-4KaH4KaoIA%3D%3D",
"https://www.youtube.com/watch?v=7OTCoadDsas&pp=ygU64Kas4Ka-4Kah4Ka84Ka_IOCmpOCniOCmsOCmvyDgppXgprDgpr4g4Kah4Ka_4Kac4Ka-4KaH4KaoIA%3D%3D",
"https://www.youtube.com/watch?v=SKvju1nymac&pp=ygU64Kas4Ka-4Kah4Ka84Ka_IOCmpOCniOCmsOCmvyDgppXgprDgpr4g4Kah4Ka_4Kac4Ka-4KaH4KaoIA%3D%3D",
"https://www.youtube.com/watch?v=7r6cSStMb04&pp=ygU64Kas4Ka-4Kah4Ka84Ka_IOCmpOCniOCmsOCmvyDgppXgprDgpr4g4Kah4Ka_4Kac4Ka-4KaH4KaoIA%3D%3D",
"https://www.youtube.com/watch?v=M1L_eFZ73IQ&pp=ygU64Kas4Ka-4Kah4Ka84Ka_IOCmpOCniOCmsOCmvyDgppXgprDgpr4g4Kah4Ka_4Kac4Ka-4KaH4KaoIA%3D%3D",
"https://www.youtube.com/watch?v=PlVwFXUlgs8&pp=ygU64Kas4Ka-4Kah4Ka84Ka_IOCmpOCniOCmsOCmvyDgppXgprDgpr4g4Kah4Ka_4Kac4Ka-4KaH4KaoIA%3D%3D",
"https://www.youtube.com/watch?v=NFu_sU-xwk8&pp=ygU64Kas4Ka-4Kah4Ka84Ka_IOCmpOCniOCmsOCmvyDgppXgprDgpr4g4Kah4Ka_4Kac4Ka-4KaH4KaoIA%3D%3D",
"https://www.youtube.com/watch?v=PCutQoWHVtk&pp=ygU64Kas4Ka-4Kah4Ka84Ka_IOCmpOCniOCmsOCmvyDgppXgprDgpr4g4Kah4Ka_4Kac4Ka-4KaH4KaoIA%3D%3D",
"https://www.youtube.com/watch?v=ljuKTa_JfAM&pp=ygU64Kas4Ka-4Kah4Ka84Ka_IOCmpOCniOCmsOCmvyDgppXgprDgpr4g4Kah4Ka_4Kac4Ka-4KaH4KaoIA%3D%3D",
"https://www.youtube.com/watch?v=4mR_aSBj_Io&pp=ygU64Kas4Ka-4Kah4Ka84Ka_IOCmpOCniOCmsOCmvyDgppXgprDgpr4g4Kah4Ka_4Kac4Ka-4KaH4KaoIA%3D%3D",
"https://www.youtube.com/watch?v=spMWAfOI3QQ&pp=ygU64Kas4Ka-4Kah4Ka84Ka_IOCmpOCniOCmsOCmvyDgppXgprDgpr4g4Kah4Ka_4Kac4Ka-4KaH4KaoIA%3D%3D",
"https://www.youtube.com/shorts/1ToG0aY2akE",
"https://www.youtube.com/watch?v=Pgw9AkdY60Y&pp=ygU64Kas4Ka-4Kah4Ka84Ka_IOCmpOCniOCmsOCmvyDgppXgprDgpr4g4Kah4Ka_4Kac4Ka-4KaH4KaoIA%3D%3D",
"https://www.youtube.com/shorts/X069cOeuWKI",
"https://www.youtube.com/watch?v=uJAuB68MlJo&pp=ygU64Kas4Ka-4Kah4Ka84Ka_IOCmpOCniOCmsOCmvyDgppXgprDgpr4g4Kah4Ka_4Kac4Ka-4KaH4KaoIA%3D%3D",
"https://www.youtube.com/watch?v=QzDESB3T0Jk&pp=ygU64Kas4Ka-4Kah4Ka84Ka_IOCmpOCniOCmsOCmvyDgppXgprDgpr4g4Kah4Ka_4Kac4Ka-4KaH4KaoIA%3D%3D",
"https://www.youtube.com/watch?v=FR0O3GPGnDU&pp=ygU64Kas4Ka-4Kah4Ka84Ka_IOCmpOCniOCmsOCmvyDgppXgprDgpr4g4Kah4Ka_4Kac4Ka-4KaH4KaoIA%3D%3D",
"https://www.youtube.com/watch?v=gFu1_36XNH0&pp=ygU64Kas4Ka-4Kah4Ka84Ka_IOCmpOCniOCmsOCmvyDgppXgprDgpr4g4Kah4Ka_4Kac4Ka-4KaH4KaoIA%3D%3D",
"https://www.youtube.com/watch?v=3sNuydO2Pd8&pp=ygU64Kas4Ka-4Kah4Ka84Ka_IOCmpOCniOCmsOCmvyDgppXgprDgpr4g4Kah4Ka_4Kac4Ka-4KaH4KaoIA%3D%3D",

    ]
    main(youtube_urls)
