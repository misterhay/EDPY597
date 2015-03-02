# Drum loop nine, in_thread
beat_length = 0.25

in_thread do
  loop do
  sample :drum_heavy_kick
  sample :drum_cymbal_closed
  sleep beat_length
  sample :drum_snare_hard
  sample :drum_cymbal_closed
  sleep beat_length
  end
end