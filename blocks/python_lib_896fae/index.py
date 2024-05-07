from gradio_client import Client

# 音频合并。
# s1, s2 代表任意两个音频。 mergeDir 用于拼接导出的文件路径。
# 输出：
# fileName： 文件名
# downloadUrl: 音频下载地址

def main(inputs: dict, context):
  s1 = inputs["s1"]
  s2 = inputs["s2"]
  dirName = inputs["mergeDir"]
  client = Client("http://34.142.159.33/")
  result = client.predict(
		s1=s1,
		s2=s2,
		dir=dirName,
		api_name="/merge_video"
  )
  dict = eval(result)
  path = dict["path"]
  downloadPath = 'http://34.142.159.33/' + path
  context.output(dirName + ".wav", "fileName", False)
  context.output(downloadPath, "downloadUrl", True)