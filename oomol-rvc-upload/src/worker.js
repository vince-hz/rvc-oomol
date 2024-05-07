/**
 * Welcome to Cloudflare Workers! This is your first worker.
 *
 * - Run "npm run dev" in your terminal to start a development server
 * - Open a browser tab at http://localhost:8787/ to see your worker in action
 * - Run "npm run deploy" to publish your worker
 *
 * Learn more at https://developers.cloudflare.com/workers/
 */

async function upload(url, data) {
  return fetch(url, {
    method: 'POST',
    body: data,
  });
}

export default {
	async fetch(request, env, ctx) {
		const r2 = env.r2; 

		switch (request.method) {
			case 'POST':
				const file = await request.arrayBuffer();
        // get uuid from timestamp.
        const uuid = Date.now().toString(36);
				await r2.put(uuid, file);
        const url = "https://oomol-rvc-upload.dajiba.club/" + uuid;
        return new Response(url, { status: 200 })
      case 'DELETE':
        const k = request.url.split('/').pop();
        await r2.delete(k);
        return new Response('ok', { status: 200 });
			default:
				const key = request.url.split('/').pop();
				const object = await r2.get(key);
				return new Response(object.body);
		}
	},
};
