const https = require('https')
const JSSoup = require('jssoup').default;
const xml2js = require('xml2js')

const domain = 'https://koding.work'
const hostname = 'koding.work'
const sitemapPost = '/post-sitemap.xml'
const sitemapPage = '/page-sitemap.xml'
const sitemapCategory = '/category-sitemap.xml'
const sitemapPaths = [sitemapPost, sitemapPage, sitemapCategory]

const cvPaths = ['/cv-en/', '/ch-zh/']

const headers = { 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36' }

// 取得所有網站上的 urls
async function getAllAvaliableUrls() {
	var paths = await parseSitemap()
	var pageNumPaths = await parseContainPageNum(paths)
	return paths.concat(pageNumPaths)
}

// 從 sitemap 中抓 url
async function parseSitemap() {
	var getBodyTasks = []
	for (let i in sitemapPaths) {
		getBodyTasks.push(getPageBody(sitemapPaths[i]))
	}
	var results = await Promise.all(getBodyTasks)

	var parseTasks = []
	for (let i in results) {
		parseTasks.push(xml2js.parseStringPromise(results[i]))
	}
	var parseResults = await Promise.all(parseTasks)
	console.log('parse sitemap finish')

	var paths = []
	for (let i in parseResults) {
		for (let j in parseResults[i].urlset.url) {
			paths.push(parseResults[i].urlset.url[j].loc[0].replace(domain, ''))
		}
	}
	return paths.concat(cvPaths)
}

// 從有分頁的網頁中爬出分頁 urls
async function parseContainPageNum(rootPaths) {
	var getBodyTasks = []
	for (let i in rootPaths) {
		if (rootPaths[i].includes('category') || rootPaths[i] == '/') {
			getBodyTasks.push(getPageBody(rootPaths[i]))
		}
	}
	var results = await Promise.all(getBodyTasks)

	var paths = []
	for (let i in results) {
		var soup = new JSSoup(results[i])
		var tags = soup.findAll('a', { 'class': 'page' })
		for (let j in tags) {
			paths.push(tags[j].attrs.href.replace(domain, '').replace('?preview=true', ''))
		}
	}
	console.log(`find ${paths.length} urls about page nums`)
	return paths
}

function getPageBody(path) {
	return new Promise(resolve => {
		var options = {
			hostname: hostname,
			path: path + '?preview=true',
			headers: headers
		}
		console.log(`start get ${domain}${path}?preview=true`)

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

module.exports = getAllAvaliableUrls