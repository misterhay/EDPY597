# Drum loop six, another loop
beat_length = 0.5

4.times do
3.times do
  sample :drum_heavy_kick
  sample :drum_cymbal_closed
  sleep beat_length
end
sample :drum_snare_hard
sample :drum_cymbal_open
sleep beat_length
end
