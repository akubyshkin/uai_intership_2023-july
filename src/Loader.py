import requests
import OfferPathBuilder as pb
import os


def read_from_disk(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def get_url(url):
    return requests.get(url)

def offer_images_downloader(root_dir, offer):
    i = 1
    paths = pb.OfferPathBuilders(root_dir).build_paths(offer)
    for picture_url in offer.picture_urls:
        if 'futlyr' in picture_url:
            continue
        response = requests.get(picture_url)

        for path in paths:
            if not os.path.exists(path.dir_name):
                print(f'directory {path.dir_name} not exists. Creating...')
                os.makedirs(path.dir_name)
                print(f'directory {path.dir_name} created')

            path_with_filename = os.path.join(
                path.dir_name, '{}_{}.jpg'.format(path.offer_id_prefix, i)
            )
            with open(path_with_filename, "wb") as out:
                out.write(response.content)
                print(f'{path_with_filename} saved')
            # print(f'{path_with_filename} saved')
        i += 1


