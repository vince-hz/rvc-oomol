import type { VocanaSDK } from "@vocana/sdk";

type Context = VocanaSDK<Inputs, Outputs>;
type Inputs = Readonly<{ in: unknown }>;
type Outputs = Readonly<{ out: unknown }>;

export default async function(inputs: Inputs, context: Context) {
  const url = inputs["youtube_url"];
  if (typeof url === "string" && url.length > 0) {
    context.output(url, "youtube_url" as any, true)
  }
};