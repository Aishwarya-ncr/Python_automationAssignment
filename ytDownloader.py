'''The given application is for downloading youtube videos automatically
when their links are provided through a file.
This is done using a python dependency free library called pytube which is meant for
downloading youtube videos.
A function is created which is called upon for each link that downloads the videos and saves it in the given file path'''


from pytube import YouTube

def download_video(link):
    my_video=YouTube(link)  #creating an object for the video
    #getting highest resolution of the video setting the location (path) for the videos to download
    my_video=my_video.streams.get_highest_resolution()   
    location=r"C:\Users\pnrao\OneDrive\Desktop\automation_python"
    my_video.download(location) #download the video


with open("video_urls.txt") as f:
    urls=f.readlines()
    print(r"Initiating downloads...")
    print("Please wait")
    for i in urls:
        download_video(i)
print("Videos have been downloaded successfully")
