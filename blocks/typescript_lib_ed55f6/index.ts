import type { VocanaSDK } from "@vocana/sdk";

type Context = VocanaSDK<Inputs, Outputs>;
type Inputs = Readonly<{ in: unknown }>;
type Outputs = Readonly<{ out: unknown }>;

// 用一个 cf worker 完成数据上传。
// TODO: 最好是后面能把数据清理一下。
export default async function(inputs: Inputs, context: Context) {
  
  const base64data = inputs["binary"] as string;
  const binaryData =Buffer.from(base64data, 'base64');
  const url = 'https://oomol-rvc-upload.dajiba.club';
  const response = await fetch(url, {
    method: "POST",
    body: binaryData
  });
  const target = await response.text();
  context.output(target, "url" as any, true);
};