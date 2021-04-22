import json
from datetime import timedelta


def acdc_tracks_duration():
    with open('acdc.json', 'r+') as file:
        dict_json = json.load(file)

        acdc_tracks = dict_json['album']['tracks']['track']
        total_tracks_duration = sum(int(track['duration']) for track in acdc_tracks)
        print(timedelta(seconds=total_tracks_duration))


acdc_tracks_duration()
