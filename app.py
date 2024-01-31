from music21 import *
import json
import os
import requests
from bs4 import BeautifulSoup

def get_music_genre(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        element_genre = soup.find('li', string='genre')

        if element_genre:
            ol_element = element_genre.find_parent('ol')
            if ol_element:
                gatunki_muzyczne = [gatunek.text.strip() for gatunek in ol_element.find_all('a')]
                return gatunki_muzyczne
    except requests.exceptions.RequestException as e:
        print(f"Error from website: {e}")

    return None

def get_title_from_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        div_element = soup.find('div', {'class': 'download-title-container', 'style': 'display:none'})

        if div_element:
            return div_element.text.strip()
        else:
            return "Didn't Find Title."

    except requests.RequestException as e:
        return f"Error from website: {e}"

    except Exception as e:
        return f"Error: {e}"

def analyze_midi(file_path, type_of_analysis):
    midi_stream = converter.parse(file_path)

    if type_of_analysis == 'key':
        key = midi_stream.analyze('key')
        return key.tonic.name + " " + key.mode
    elif type_of_analysis == 'meter':
        meter = midi_stream.getTimeSignatures()[0]
        return meter.ratioString
    elif type_of_analysis == 'tempo':
        tempo = midi_stream.metronomeMarkBoundaries()[0][2]
        return tempo.number
    elif type_of_analysis == 'scale':
        scale = midi_stream.analyze('key').getScale()
        return scale.name
    elif type_of_analysis == 'instruments':
        instruments = []
        for part in midi_stream.parts:
            instruments.append(part.partName)
        return instruments

def download_midi(url_download, file_name):
    try:
        os.system(f'curl {url_download} --output "{file_name}"')
        return True
    except Exception as e:
        print(f"Error while downlaod midi. {e}")
        return False

results_list = []

# Set here how much files you want to download in for loop (this site has about 2000 files)
for i in range(1000, 20000):
    print(i)
    urllink = f"https://freemidi.org/download3-{i}"
    genre = get_music_genre(urllink)
    if not genre:
        continue
    else:
        url_download = f"https://freemidi.org/getter-{i}"
        name = f"{i}.mid"
        download_success = download_midi(url_download, name)

        if not download_success:
            continue

        file_path = os.path.abspath(name)

        try:
            title_result = get_title_from_website(urllink)
            key_result = analyze_midi(file_path, 'key')
            meter_result = analyze_midi(file_path, 'meter')
            tempo_result = analyze_midi(file_path, 'tempo')
            scale_result = analyze_midi(file_path, 'scale')
            instruments_result = analyze_midi(file_path, 'instruments')

            results_dict = {
                'file': name,
                'title': title_result,
                'genre': genre,
                'key': key_result,
                'meter': meter_result,
                'tempo': tempo_result,
                'scale': scale_result,
                'instruments': instruments_result,
                'genre': genre,
                'url': urllink,
                'url_download': url_download,
            }

            results_list.append(results_dict)

        except Exception as midi_exception:
            print(f"Błąd podczas analizy pliku MIDI {name}: {midi_exception}")
            os.remove(file_path)
            continue 

with open('results.json', 'w') as json_file:
    json.dump(results_list, json_file, indent=2)

print("Results saved in file: results.json")