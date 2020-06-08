# @ Bhavesh Padharia

# Facebook post on feed using GraphAPI

import facebook

#Token generated from GraphAPI

token = 'EAAnXnU7Ylt4BALVHRPYrqxg9wZBVpYeKZAI1911WFTQn45CAcbuueWydsZAMdZAhXCa4enpwzbcjsUkxmlVxs0ZAPuVHa04P7Uivn1b0WbZCz6OfmgfHAvzFXll52Q6qLJNDFz5LeIFH7LpMQAZBciC5zIS9fuY9oZAI9hYCZBH4ikWKRHBuB72k9SjXYWI1etkRaWb3n2AwDqQZDZD'
fb = facebook.GraphAPI(access_token=token)

fb.put_object(parent_object='me', connection_name='feed', message='Hello this is my fourth test for fb page')
