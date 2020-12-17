const https = require('https')

const hostname = 'koding.work'
const headers = { 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36' }

function startRequest(path) {
	return new Promise(resolve => {
		var options = {
			hostname: hostname,
			path: path,
			headers: headers
		}

		var t = new Date();
		https.get(options, (res) => {
			let headers = res.headers

			res.on('data', data => { })

			res.on('end', () => {
				let totalTime = (new Date() - t);
				console.log(`prefetch finish => cache status: ${headers['cf-cache-status']}, age: ${headers['age']}, response time: ${totalTime}ms, url: https://${hostname}${path}`)
				resolve(true)
			})
		});
	})
}

async function startPreload(paths) {
	console.log('preload 20 batch start')
	await Promise.all(paths.map(p => startRequest(p)))
	console.log('finish')
}

module.exports = startPreload


