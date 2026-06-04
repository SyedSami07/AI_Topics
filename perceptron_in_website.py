logged_in = 1
likes_music = 1
has_money = 0

inputs = [logged_in, likes_music, has_money]
weights = [1, 1, 2]

threshold = 2

score = 0
for i in range(len(inputs)):
    score += inputs[i] * weights[i]

show_button = score > threshold

print("Show Buy Ticket button?", show_button)