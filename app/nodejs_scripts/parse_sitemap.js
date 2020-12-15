const https = require('https')
const xml2js = require('xml2js')

const hostname = 'koding.work'
const sitemapPost = '/post-sitemap.xml'
const sitemapPage = '/page-sitemap.xml'
const sitemapCategory = '/category-sitemap.xml'
const sitemaps = [sitemapPost, sitemapPage, sitemapCategory]

const cvPaths = ['/cv-en/', '/ch-zh/']

const headers = { 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36' }


async function parseSitemap() {
	var sitemapTasks = []
	for (i in sitemaps) {
		sitemapTasks.push(getSitemap(sitemaps[i]))
	}
	var results = await Promise.all(sitemapTasks)

	var parseTasks = []
	for (i in results) {
		parseTasks.push(xml2js.parseStringPromise(results[i]))
	}
	var parseResults = await Promise.all(parseTasks)

}

function getSitemap(path) {
	return new Promise(resolve => {
		var options = {
			hostname: hostname,
			path: path + '?preview=true',
			headers: headers
		}
		console.log(options)

		https.get(options, (res) => {
			let body = ''
			res.on('data', data => {
				body += data
			})

			res.on('end', () => {
				resolve(body)
			})
		});
	})
}

parseSitemap()
