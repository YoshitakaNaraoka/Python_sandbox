import pyaudio

def get_mic_index(pa):
  """マイクチャンネルを取得する関数"""
  
  # マイクチャンネル一覧をリストに追加する
  mic_list = []
  for i in range(pa.get_device_count()):
    device_info = pa.get_device_info_by_index(i)
    num_of_imput_ch = device_info['maxInputChannels']
    
    if num_of_imput_ch > 0:
      mic_list.append(device_info['index'])
      
      return mic_list[0]
    
# PyAudio を準備する
pa = pyaudio.PyAudio()

# マイクチャンネルを自動取得
index = get_mic_index(pa)
print(index)