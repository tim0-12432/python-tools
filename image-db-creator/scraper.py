#%%
import mechanicalsoup
import os
import wget

browser = mechanicalsoup.StatefulBrowser()
url = "https://www.google.com/imghp?hl=de"

browser.open(url)

search_term = input("What are you searching for?")

browser.get_current_page()

browser.select_form()

browser["q"] = search_term
response = browser.submit_selected()

new_url = browser.get_url()
print(f"getting images for url {new_url} ...")
browser.open(new_url)

page = browser.get_current_page()
all_images = page.find_all("img")

img_sources = []
for image in all_images:
    image = image.get("src")
    img_sources.append(image)

img_sources = [source for source in img_sources if source.startswith("https")]

path = os.getcwd()
path = os.path.join(path, "images", f"{search_term}s")
os.mkdir(path)

counter = 0
for source in img_sources:
    save_as = os.path.join(path, f"{search_term}-{counter}.png")
    print(f"downloading image {counter + 1} out of {len(img_sources)} ...")
    wget.download(source, save_as)
    counter += 1

print("Done!")
input()
# %%
