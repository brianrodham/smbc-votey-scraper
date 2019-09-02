from scraper import Scraper

scraper = Scraper();
url = "https://www.smbc-comics.com/comic/2002-09-05"

while True:
    image_url = scraper.GetImageUrl(url)
    scraper.DownloadImage(image_url)
    print("Downloaded image: " + image_url)
    url = scraper.GetNextComicUrl(url)
    print(url)
    if url == "":
        print("Execution Finished")
        break
