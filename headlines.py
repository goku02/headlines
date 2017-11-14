from flask import Flask, render_template, request
import feedparser

BBC_FEED = 'http://feeds.bbci.co.uk/news/rss.xml'
RSS_FEED = {
	'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
	'cnn': 'http://rss.cnn.com/rss/edition.rss',
	'fox': 'http://feeds.foxnews.com/foxnews/latest',
	'iol': 'http://www.iol.co.za/cmlink/1.640'
}

app = Flask(__name__)

@app.route('/')
def get_news(publication='bbc'):
	try:
		query = request.args.get("publication")
		if not query or query.lower() not in RSS_FEED:
			publication = 'bbc'
		else:
			publication = query.lower()
		feed = feedparser.parse(RSS_FEED[publication])
		#print(feed['entries'][0])
		first_article = feed['entries'][0]
		title = first_article.get('title')
		published = first_article.get('published')
		summary = first_article.get('summary')
	except IndexError:
		return render_template('error_notFound.html')
	#return render_template('home.html')
	return render_template('home.html', articles=feed['entries'])


if __name__ == "__main__":
	app.run(port=5000, debug=True)