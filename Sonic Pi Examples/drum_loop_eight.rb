# Drum loop eight, nested functions
def cymbalClosed(beat_length)
  sample :drum_cymbal_closed
  sleep beat_length
end

def loop_this(n)
  n.times do
  cymbalClosed 0.25
  end
end

loop_this 16