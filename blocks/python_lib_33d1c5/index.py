from gradio_client import Client, file

# 人声推理。
# 输入：
# audioPath: 人声音频路径。
# dirName: 用于拼接输出人声音频路径。
# 输出：
# convertedPath: 推理后的人声音频路径。
def main(inputs: dict, context):
  audioPath = inputs['audioPath']
  dirName = inputs['dirName']
  storeDir = 'opt/' + dirName
  client = Client("http://34.142.159.33/")
  result = client.predict(
		sid=0,
		input_audio_path=audioPath,
		f0_up_key=0,
    f0_file=None,
		f0_method="rmvpe",
		file_index="",
		file_index2="logs/syz_01/added_IVF256_Flat_nprobe_1_syz_v2.index",
		index_rate=0.75,
		filter_radius=3,
		resample_sr=0,
		rms_mix_rate=0.25,
		protect=0.33,
    storeDir=storeDir,
		api_name="/infer_convert",
  )
  p = "/root/Retrieval-based-Voice-Conversion-WebUI/" + storeDir + "/converted.wav"
  context.output(p, "convertedPath", True)