const startPreload = require('./preloader')
const getAllAvaliableUrls = require('./parse_sitemap')

function splitPath(paths, pageMaxPathsLen = 10) {
	var splits = []
	for (let i = 0; i < paths.length; i += pageMaxPathsLen) {
		splits.push(paths.slice(i, i + pageMaxPathsLen))
	}
	return splits
}

exports.handler = async (event) => {
	var urls = await getAllAvaliableUrls()
	var pagedPaths = splitPath(urls)
	for (let i in pagedPaths) {
		await startPreload(pagedPaths[i])
	}

	return {
		statusCode: 200,
		body: JSON.stringify('Finish!'),
	};
};

// exports.handler()