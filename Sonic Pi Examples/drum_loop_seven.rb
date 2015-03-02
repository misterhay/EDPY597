# Drum loop seven, with parameters
def play_a_beat(chosen_sample, beat_length)
  sample chosen_sample
  sleep beat_length
end

4.times do
  play_a_beat(:drum_cymbal_closed,0.25)
end