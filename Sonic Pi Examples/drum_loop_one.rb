# Drum loop one, half notes
beat_length = 0.25

4.times do
sample :drum_heavy_kick
sleep beat_length
sample :drum_snare_hard
sleep beat_length
end