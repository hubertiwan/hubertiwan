from pytube import YouTube

link = input("Podaj link do nagrania: ")
video = YouTube(link).streams.get_highest_resolution()

# Pobierz film do wskazanej lokalizacji, umieść między " "
video.download(output_path=" ")
print("Film został pobrany!")