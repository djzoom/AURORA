# Reference implementation — L03_spectrogram

> ⚠️ Please work through the exercises on your own first, then look at the reference implementation.

## Reference implementation 1

`predictions` — predicting the spectrogram shapes (sample answers; anything close in meaning is fine, there's no single correct answer for this exercise):

```python
predictions = {
    "sig_a_1000hz_pure": "One bright horizontal line at 1000 Hz, constant brightness all the way",
    "sig_b_decaying":    "One bright horizontal line at 1000 Hz, getting dimmer from left to right until it disappears",
    "sig_c_chord":       "Two bright horizontal lines, at 500 Hz and 1500 Hz, lasting the whole time",
}
```

## Reference implementation 2

`quiz_answers` — the spectrogram reading challenge (the check cell matches on keywords; an answer passes as long as it contains one of the keywords):

```python
quiz_answers = {
    "图A": "White noise — energy spread evenly across all frequencies and all moments",
    "图B": "Chord — C major triad C4+E4+G4 (three bright horizontal lines at 261/330/392 Hz)",
    "图C": "Sweep (glissando) — frequency climbs linearly from 200 Hz to 3000 Hz, corresponding to the slide performance technique",
    "图D": "Decaying pure tone — the frequency stays put, the energy (brightness) fades over time",
}
```

(The keys `"图A"`…`"图D"` mean Figure A…D; they are kept as is because the check cell in the notebook uses them.)

**Key points**
- The three spectrogram axes: horizontal = time, vertical = frequency, color brightness = energy.
- The four fingerprints: pure tone = one horizontal line; chord = several parallel horizontal lines; sweep = a diagonal line; white noise = the whole picture evenly bright.
- Brightness changing over time corresponds to the amplitude envelope — frequency fixed, brightness fading means a decaying pure tone.
