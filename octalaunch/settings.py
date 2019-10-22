import json

settings = {
    # default settings
    'drumPage': {
        'selectedAudioTrack': 0,
        'selectedMidiTrack': 0,
    },
    'notePage': {
        'selectedAudioTrack': 0,
        'selectedMidiTrack': 0,
    },
    'selectedPage': 'note',
    'trackChannels': {
        'audioTrackChannel': [0, 1, 2, 3, 4, 5, 6, 7],
        'midiTrackChannel': [8, 9, 10, 11, 12, 13, 14, 15]
    },
}

def save():
    with open('settings.json', 'w') as outfile:
        json.dump(settings, outfile, indent=4, sort_keys=True)

def load():
    try:
        with open('settings.json') as infile:
            # TODO validate input
            # TODO version the settings file
            data = json.load(infile)
            for key in data:
                settings[key] = data[key]
    except IOError:
        print("Can't read settings file, skipping.")