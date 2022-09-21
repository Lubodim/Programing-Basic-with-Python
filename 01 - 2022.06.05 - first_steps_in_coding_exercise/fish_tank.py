length = int(input())
width = int(input())
height = int(input())
procent = float(input())

volume_cm = length * width * height
volume_dm = volume_cm * 0.001

procent = procent * 0.01

litres_water = volume_dm - procent * volume_dm

print(litres_water)