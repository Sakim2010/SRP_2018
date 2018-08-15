
************Data Collection folder************

Contains code and results of data collection stage

We used the Scrapy library in Python to create a spider which would crawl through the Dawn Newspaper website’s archives and 
access the links to the articles. The archive pages were used to extract the categories, excerpts, and dates of the articles, 
whereas the actual article’s webpage was used to extract it’s headings and text. 

This required 2 spiders:
	news.py : for scraping the article’s webpage(Data Collection/scrapy project/news_crawler/news_crawler/spiders/news.py)
	cats_spider.py: for scraping archives (Data Collection/cats_spider.py)
	
	Notes:
	cats_spider.py was run locally, whereas news.py was uploaded online to Scrapy’s online Scrapinghub platform, 
		which run the spiders on their own servers.
	
	merge.py was then used to merge results from both spiders by based on the link of the articles. 
	The links were sometimes redirected, and thus for those links in the results from cats_spider.py that had no match, 
	the links were redirected to their using Python’s request library, and then matched.
	
	Finally, the file: ALL_complete.csv was created which included all articles on the Dawn Newspaper’s website from 1st July, 2017 to 31st May, 2018. 
	This was the dataset used to run and explore LDA and it’s possible uses for online Pakistani newspaper analysis.


***********LDA_gensim folder************
	
The following codes are run in the given order: 

create_docs.py: 
	sorts out the data from ALL_complete.csv according to the date, as well as remove any irrelevant categories, 
	given the kind of analysis you wish to do, hence creating data.csv which well then be used by the following code.

LDA_1.py: 
	uses the nltk and genism libraries to process the data by removing stopwords and punctuation, as well as stemming the words.

LDA_2.py: 
	runs the actual model on the corpus with varying number of topics (all even numbers between 2 and 40)

lda_choose.py: 
	finds the coherence values of the each LDA model and thus allows us 
	to choose the better models to use (the higher the coherence value, the better)

doc_to_topic_dist.py: 
	creates document to topic distribution, which has the perecentage representations of all topics for each document

lda_extract_topic_rep_csvs.py: 
	creates list of document headings along with the representation of a topic for that topic, 
	for all topics, with a separate csv file for each topic


***********Monthly LDA folder************

Contains results for Monthly LDA runs (one for November and the other for October)
Navigate to 'Labeled' folder to find csv files which contain the headings of articles, along with their respective topic representations


***********Guided LDA folder************

Contains guideddla.py which has all the needed code for running Guided LDA and storing the relevant results