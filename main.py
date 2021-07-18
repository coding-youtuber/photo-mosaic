import requests


def download_image(url, file_path):
  r = requests.get(url, stream=True)

  if r.status_code == 200:
    with open(file_path, "wb") as f:
      f.write(r.content)

def main():

  with open("ids.txt", "r") as f:
    lines = [x.strip() for x in f.readlines()]
    print(lines)


  for video_id in lines:
    url = "http://img.youtube.com/vi/{}/maxresdefault.jpg".format(video_id)

    download_image(url=url, file_path="images/thumbnails/{}.jpg".format(video_id))



main()