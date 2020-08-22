#pip install pytube3
import pytube

url = "" #enter your link between the codes
download = pytube.YouTube(url).streams.first().download('location of download')
print(download)
