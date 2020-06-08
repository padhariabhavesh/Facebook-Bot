# @ Bhavesh Padharia

# Facebook post on feed using GraphAPI

import facebook

#Token generated from GraphAPI

token = 'Enter your access token '
fb = facebook.GraphAPI(access_token=token)

fb.put_object(parent_object='me', connection_name='feed', message='Hello this is test post on feed ')
