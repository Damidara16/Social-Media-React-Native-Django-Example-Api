from django.core.files.uploadhandler import FileUploadHandler

def verify_following(f_user,c_user_uuid):
    return f_user.profile.following.filter(uuid=c_user_uuid).exists()

def upload_handler_chunk(f):
    fname = f'/media/new{f.name}'
    with open('new'+f.name, 'wb+') as den:
        CHUNK_SIZE = 1024 * 5
        chunk = f.multiple_chunks(CHUNK_SIZE)
        while chunk:
            den.write(chunk)
            chunck = f.multiple_chunks(CHUNK_SIZE)

"""class CustomHandler(FileUploadHandler):

    def __init__(self,*args,**kwargs):
        super(CustomHandler, self).__init__(*args,**kwargs)
        self.chunk_size = 64 * 2**16
    def receive_data_chunk(raw_data, start):
        pass
    def file_complete(file_size):
        pass"""

#FileUploadHandler handles the data from the client to server via http and then creates a file object to use in view
#with that object i can send to s3, stream to a denstination file, etc.
#i could create a custom handler to stream directly to s3 or to another client
