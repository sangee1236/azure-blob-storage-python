import os
from azure.storage.blob import BlockBlobService, PublicAccess ,AppendBlobService

def azure_blob_storage():
    try:
        # To create a blob service or connection to azure blob storage 
        block_blob_service = BlockBlobService(account_name='account_name', account_key='account_key')

        # To create a container 
        container_name ='container_name'
        block_blob_service.create_container(container_name)

        # Set access to a container such as public ,readonly,private
        block_blob_service.set_container_acl(container_name, public_access=PublicAccess.Container)

        # Create a file to upload to azure blob storage 
        local_file_name ="Test.txt"
        path_to_file =os.path.join('local_path', local_file_name)

        # To write to the file  
        local_file = open(full_path_to_file,  'w')
        local_file.write("hi peoplee")
        local_file.close()

        # Upload the created file, use local_file_name for the blob name
        block_blob_service.create_blob_from_path(container_name, local_file_name, full_path_to_file)

        # To List all the blobs in the container 
        container_List = block_blob_service.list_blobs(container_name)
        for file in container_List:
            print("Blob name: "+{file.name})

        # Download the blob(s).
        download_file_path = os.path.join('local_path', 'local_file_name')
        block_blob_service.get_blob_to_path(container_name, local_file_name, download_file_path)

        #delete a blob 
        block_blob_service.delete_blob('container_name', 'blob_name')

        #Append to a blob service    
        append_blob_service = AppendBlobService(account_name='myaccount', account_key='mykey')

        # The same containers can hold all types of blobs
        append_blob_service.create_container('container_name')

        #To append file must exists 
        append_blob_service.create_blob('container_name', 'append_blob')

        #Append to a blob service    
        append_blob_service.append_blob_from_text('container_name', 'append_blob', 'Hello, world!')
        
        append_blob = append_blob_service.get_blob_to_text('container_name', 'append_blob')


        # Clean up resources. This includes the container and the temp files
        block_blob_service.delete_container(container_name)
    except Exception as e:
        #handle with care


# Main method.
if __name__ == '__main__':
    azure_blob_storage()


