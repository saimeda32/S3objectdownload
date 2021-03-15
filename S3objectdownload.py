import boto3
from botocore.exceptions import ClientError
from csv import reader


bucket_name = 'Bucket_Name'
ACCESS_KEY = ''
SECRET_KEY = ''


def getobject(object):

 
    s3_file_path= object
    filename = object.split('/')[-1]

    s3 = boto3.client('s3',
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY)
    try:
        s3.download_file(bucket_name , s3_file_path, filename)
    except ClientError as e:
            print(e)


def main():

    with open('objects.csv', 'r') as read_obj:
         csv_reader = reader(read_obj)
         for row in csv_reader:
            object = row[0]
            print (object)
            download = getobject(object) 
            
         print ("Done !!!")




if __name__ == "__main__":
     main()
