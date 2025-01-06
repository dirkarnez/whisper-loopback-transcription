[whisper-loopback-transcription](https://github.com/dirkarnez/whisper-loopback-transcription)
=============================================================================================
Based on [tez3998/loopback-capture-sample: Sample code which records system (speaker) sounds (what you hear) in Python.](https://github.com/tez3998/loopback-capture-sample)

### Mono (`data=data[:, 0]`)
```python
    # record audio with loopback from default speaker.
    data = mic.record(numframes=SAMPLE_RATE*RECORD_SEC)
    
    # change "data=data[:, 0]" to "data=data", if you would like to write audio as multiple-channels.
    sf.write(file=OUTPUT_FILE_NAME, data=data[:, 0], samplerate=SAMPLE_RATE)
```

### Stereo (`data=data`)
```python
    # record audio with loopback from default speaker.
    data = mic.record(numframes=SAMPLE_RATE*RECORD_SEC)
    
    # change "data=data[:, 0]" to "data=data", if you would like to write audio as multiple-channels.
    sf.write(file=OUTPUT_FILE_NAME, data=data, samplerate=SAMPLE_RATE)
```

### Stereo Stream
```python
    while True:
        data = mic.record()
        print(data.size)
```

### Notes
- use libobs for loopback
    - [obs-studio/libobs/audio-monitoring at master · obsproject/obs-studio](https://github.com/obsproject/obs-studio/tree/master/libobs/audio-monitoring)
