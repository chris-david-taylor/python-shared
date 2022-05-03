from urllib import response
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


class Slack:
    
    def __init__(self, token, channel):                           
        self.client = WebClient(token = token)
        self.channel = channel
 
      
    def __del__(self):
        pass  # destructor method for object 
  
                        
    def post_file(self, comment, file_name):
        try:
            self.client.files_upload(
                channels = self.channel,
                initial_comment = comment,
                file = file_name 
              )
        except SlackApiError as e:
            assert e.response["error"]
                      
