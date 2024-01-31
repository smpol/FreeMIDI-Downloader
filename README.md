# FreeMIDI-Downloader

Simple Python Programme to download MIDI's from freemidi.org

This simple script written in python downloads files from the freemidi.org website and then parses the midi file and saves the information to a json file

## Example result of the programme

```json
[
  {
    "file": "1000.mid",
    "file_path": "/content/1000.mid",
    "genre": ["pop", "rock"],
    "key": "C# major",
    "meter": "4/4",
    "tempo": 80,
    "scale": "C# major",
    "instruments": [
      "Bass",
      "Harpsichord",
      "Horns",
      "Melody",
      "Piano",
      "Flute",
      "Flute"
    ],
    "url": "https://freemidi.org/download3-1000",
    "url_download": "https://freemidi.org/getter-1000"
  },
  {
    "file": "1001.mid",
    "file_path": "/content/1001.mid",
    "genre": ["pop", "rock"],
    "key": "F major",
    "meter": "12/8",
    "tempo": 185,
    "scale": "F major",
    "instruments": [
      "Melody",
      "BGround V",
      "Piano",
      "Harp/Bari/Harm/Tr",
      "Bass",
      "Bass (muted)",
      "Organ",
      "Banjo",
      "Big Drum",
      "Kick",
      "Hi Hat",
      "Tambourine",
      "Snare"
    ],
    "url": "https://freemidi.org/download3-1001",
    "url_download": "https://freemidi.org/getter-1001"
  },
  {
    "file": "1002.mid",
    "file_path": "/content/1002.mid",
    "genre": ["pop", "rock"],
    "key": "B major",
    "meter": "4/4",
    "tempo": 82,
    "scale": "B major",
    "instruments": [
      "Bass",
      "Harpsichord",
      "Harp",
      "Melody",
      "Oboe",
      "Flute",
      "Piano",
      "Guitar 1",
      "Piano 2",
      "Drums",
      "Timpani",
      "Sax",
      "Harpsichord 2"
    ],
    "url": "https://freemidi.org/download3-1002",
    "url_download": "https://freemidi.org/getter-1002"
  },
  {
    "file": "1003.mid",
    "file_path": "/content/1003.mid",
    "genre": ["rock", "pop"],
    "key": "G major",
    "meter": "4/4",
    "tempo": 144,
    "scale": "G major",
    "instruments": [
      "Std Drums",
      "Lead Organ 3",
      "Lead Gtr (Pkd Bass)",
      "Rythm 1 Muted Gtr",
      "Rythm 2 Nylon Bk32",
      "Fretless E. Bass"
    ],
    "url": "https://freemidi.org/download3-1003",
    "url_download": "https://freemidi.org/getter-1003"
  },
  {
    "file": "1004.mid",
    "file_path": "/content/1004.mid",
    "genre": ["rock", "pop"],
    "key": "G major",
    "meter": "4/4",
    "tempo": 144,
    "scale": "G major",
    "instruments": [
      "Std Drums",
      "Lead Organ 3",
      "Lead Gtr (Pkd Bass)",
      "Rythm 1 Muted Gtr",
      "Rythm 2 Nylon Bk32",
      "Fretless E. Bass"
    ],
    "url": "https://freemidi.org/download3-1004",
    "url_download": "https://freemidi.org/getter-1004"
  }
]
```

## Requirements

The programme requires the following pip libraries installed: music21 requests beautifulsoup4
