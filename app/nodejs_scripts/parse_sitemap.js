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
	let paths = await parseSitemap()
	let pageNumPaths = await parseContainPageNum(paths)
	return [...paths, ...pageNumPaths]
}

// 從 sitemap 中抓 url
async function parseSitemap() {
	let getBodyTasks = sitemapPaths.map(path => getPageBody(path))
	let results = await Promise.all(getBodyTasks)

	let parseTasks = results.map(r => xml2js.parseStringPromise(r))
	let parseResults = await Promise.all(parseTasks)
	console.log('parse sitemap finish')

	let paths = []
	for (let i in parseResults) {
		for (let j in parseResults[i].urlset.url) {
			paths.push(parseResults[i].urlset.url[j].loc[0].replace(domain, ''))
		}
	}
	return [...paths, ...cvPaths]
}

// 從有分頁的網頁中爬出分頁 urls
async function parseContainPageNum(rootPaths) {
	let getBodyTasks = rootPaths.reduce((result, path) => {
		if (path.includes('category') || path == '/') {
			result.push(getPageBody(path))
		}
		return result
	}, [])

	let results = await Promise.all(getBodyTasks)

	let paths = []
	results.forEach(result => {
		let soup = new JSSoup(result)
		let tags = soup.findAll('a', { 'class': 'page' })
		tags.forEach(tag => {
			paths.push(tag.attrs.href.replace(domain, '').replace('?preview=true', ''))
		})
	})
	console.log(`find ${paths.length} urls about page nums`)
	return paths
}

function getPageBody(path) {
	return new Promise(resolve => {
		let options = {
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