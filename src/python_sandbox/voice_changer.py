import pyaudio

# PyAudio を準備する
pa = pyaudio.PyAudio()

# マイクチャンネル一覧をリストに追加する
mic_list = []
for i in range(pa.get_device_count()):
    device_info = pa.get_device_info_by_index(i)
    num_of_imput_channels = device_info['maxInputChannels']
    
    if num_of_imput_channels > 0:
        mic_list.append(device_info['index'])
print(mic_list)

# [0, 1, 4, 5, 9, 10, 14] -> 7 つのマイクチャンネルが発見！