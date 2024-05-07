from gradio_client import Client, file

# 分离人声和伴奏。 
# 从 'sourceDir' 中获取原始音频。
# 分离结果会导到一个服务器的本地路径。
# instruPath: 伴奏路径。
# vocalPath 人声路径。
# audioDirName: 透传。
def main(inputs: dict, context):
  sourceDir = inputs["sourceDir"]
  dirName = inputs["dirName"]
  client = Client("http://34.142.159.33/")
  result = client.predict(
		model_name="HP5_only_main_vocal",
		inp_root=sourceDir,
		save_root_vocal="opt" + "/" + dirName,
		paths=None,
		save_root_ins="opt" + "/" + dirName + "/instrument",
		agg=10,
		format0="flac",
		api_name="/uvr_convert"
  )
  vocalPath = "/root/Retrieval-based-Voice-Conversion-WebUI/opt/" + dirName + "/vocal_out.wav_10.flac"
  instruPath = "/root/Retrieval-based-Voice-Conversion-WebUI/opt/" + dirName + "/instrument/instrument_out.wav_10.flac"
  context.output(instruPath, "instruPath", False)
  context.output(dirName, "audioDirName", False)
  context.output(vocalPath, "vocalPath", True)