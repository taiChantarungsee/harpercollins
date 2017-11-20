import os

"""Tweet function that gets called by the following two functions, each of which uses it in a different
	way. Takes image url and looks up appropiate image, then tweets it with text. """
def tweet(df, img_url,mypath,row):
	auth, api = twitter_cred()
	if isinstance(img_url, str):
		for root, dirs, files in os.walk(mypath + '\static'):
			for name in files:
				if name in img_url:
					filename = name
					img = mypath + '\static\\' + filename							
					api.update_with_media(img, status=row['post_text'])
			else:
				api.update_status(row['post_text'])
				

class Tweet(object):
	#Function to share twitter credentials:
	def twitter_cred():
		auth = tweepy.OAuthHandler('consumer key', 'consumer secret')
		auth.set_access_token('access token','access token secret')
		api = tweepy.API(auth)
		return auth, api
	
	"""Should be refactored using filter and the itertools library. Tweets out text from spreadsheet, for only 
	those entries categorized for twitter."""
	def tweet_bulk(df):
		dirpath = os.getcwd()
		mypath = dirpath
		
		for index,row in df.iterrows():
			if df.loc[index,'socialmedia_channel'] == 'Twitter':
				img_url = row['post_img']
				tweet(df,img_url,mypath,row)
	
	
	"""This one is for use with the scheduler function. Tweet out specific post instead of all of them.
	Should be merged with the previous function. """
	def single_tweet(_index, df):
		dirpath = os.getcwd()
		mypath = dirpath
	
		#Could also be refactored to make use of filter.
		for index,row in df.iterrows():
			if df.loc[index,'socialmedia_channel'] == 'Twitter' and index == _index:
				img_url = row['post_img']
				tweet(df,img_url,mypath,row)	

if __name__ == '__main__':
    tweet()