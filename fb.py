import facebook, requests
from facepy import GraphAPI

def facebook_info():
	token = 'access_token'
	graph = facebook.GraphAPI(access_token=token, version=2.7)
	profile = graph.get_object(id="me", fields='id,name,about,link,location,hometown,website', limit=100)
	friends = graph.get_connections(profile['id'],  
		connection_name='posts', 
		fields='caption,created_time,description,from,link,message,object_id,parent_id,permalink_url,picture,privacy,place,properties,shares,source,status_type,story,to,type,with_tags',
		 limit='100')

	#Or use the facepy library?...
	graph = GraphAPI('access_token')
	graph.get('page_id')

if __name__ == '__main__':
	facebook_info()