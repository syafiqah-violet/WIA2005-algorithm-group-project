import urllib.request, urllib.error, urllib.parse, obo
import plotly, plotly.graph_objects as go

url = 'https://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33'
# url = 'https://www.textise.net/showText.aspx?strURL=https://www.thestar.com.my/business/business-news/2015/01/05/citylink-mulls-main-market-listing-in-three-years#textiseTop'


# words without stop words
response = urllib.request.urlopen(url)
html = response.read()
text = obo.stripTags(html).lower()
fullwordlist = obo.stripNonAlphaNum(text)
wordlist = obo.removeStopwords(fullwordlist, obo.stopwords)
dictionary = obo.wordListToFreqDict(wordlist)
sorteddict = obo.sortFreqDict(dictionary)

for s in sorteddict: print(str(s))

# plot histogram of word frequency
for s in wordlist:
    x = [a for a in wordlist]
    y = [wordlist.count(p) for p in wordlist]

fig = go.Figure()
fig.add_trace(go.Histogram(histfunc="count", y=y, x=x, name="count"))

fig.show()



