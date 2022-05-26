length = int(input())
width = int(input())
height = int(input())
occupied_volume = float(input()) / 100
volume_l = length * width * height * 0.001
wather = volume_l - volume_l * occupied_volume
print(wather)