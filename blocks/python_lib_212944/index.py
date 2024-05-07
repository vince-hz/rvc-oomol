from gradio_client import Client

# 从 youtube 地址下载原始内容, 导出音频。
# audioDirName: 音频的文件夹名。
# audioDirPath: 音频文件夹路径。
def main(inputs: dict, context):
  url = inputs["url"]
  client = Client("http://34.142.159.33/")
  result = client.predict(
		url=url,
		api_name="/download_video"
  )
  r = eval(result)
  dirPath = r["path"]
  dirName = r["dirName"]
  context.output(dirName, "audioDirName", False)
  context.output(dirPath, "audioDirPath", True)