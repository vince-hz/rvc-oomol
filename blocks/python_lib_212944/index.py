from gradio_client import Client

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
  context.output(dirName, "dirName", False)
  context.output(dirPath, "dir", True)