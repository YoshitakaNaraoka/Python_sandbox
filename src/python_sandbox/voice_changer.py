import pyaudio

# PyAudio を準備する
pa = pyaudio.PyAudio()

# 音声デバイス一覧を表示する
for i in range(pa.get_device_count()):
    device_info = pa.get_device_info_by_index(i)
    print(device_info)