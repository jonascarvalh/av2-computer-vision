import requests, os
from decouple import config

UNSPLASH_ACCESS_KEY = config('UNSPLASH_ACCESS_KEY')
BASE_URL = 'https://api.unsplash.com/'
SAVE_DIR = 'images'

def download_images(query, qty, w=300):
    params = {
        'client_id': UNSPLASH_ACCESS_KEY,
        'query': query,  
        'count': qty,
    }

    response = requests.get(
        BASE_URL + 'photos/random',
        params=params
    )

    if response.status_code == 200:
        data = response.json()
        for i, photo in enumerate(data):
            img_url = photo['urls']['full']
            img_url = img_url+'&w=300'
            img_response = requests.get(img_url)

            if img_response.status_code == 200:
                with open(os.path.join(SAVE_DIR, f'morango_{i}.jpg'), 'wb') as file:
                    file.write(img_response.content)

                print(f'Image {i+1} has been saved.')
            else:
                print(f'Image {i+1} failed.')
    else:
        print('Error in request.')

if __name__ == '__main__':
    download_images('just strawberry', 30)