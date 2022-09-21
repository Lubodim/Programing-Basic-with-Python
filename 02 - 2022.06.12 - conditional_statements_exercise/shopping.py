bugget = float(input())
number_video_cards = int(input())
number_prosesores = int(input())
number_ram_memories = int(input())

one_video_card_price = 250
one_prosesor_price = one_video_card_price * number_video_cards * 0.35
one_ram_memory = one_video_card_price * number_video_cards * 0.10

total_sum = one_video_card_price * number_video_cards \
            + one_prosesor_price * number_prosesores \
            + one_ram_memory * number_ram_memories

if number_video_cards > number_prosesores:
    total_sum *= 0.85

something = abs(bugget - total_sum)

if total_sum <= bugget:
    print(f"You have {something:.2f} leva left!")
else:
    print(f"Not enough money! You need {something:.2f} leva more!")
