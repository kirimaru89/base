import boto3
from django.conf import settings


class AwsService:
    @staticmethod
    def s3():
        return boto3.resource(
            "s3",
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        )

    @staticmethod
    def get_or_create_bucket(bucket_name):
        client = AwsService.s3()
        bucket = client.Bucket(bucket_name)
        if bucket.creation_date:
            return bucket

        try:
            client.create_bucket(Bucket=bucket_name)
            return client.Bucket(bucket_name)
        except Exception as e:
            print(repr(e))
            return None

    @staticmethod
    def upload_file(key, body):
        try:
            bucket_name = settings.AWS_BUCKET
            bucket = AwsService.get_or_create_bucket(settings.AWS_BUCKET)
            if not bucket:
                return False, None

            resource = AwsService.s3()
            resource.Bucket(bucket_name).put_object(Key=key, Body=body)
            params = {"Bucket": bucket_name, "Key": key}
            url = resource.meta.client.generate_presigned_url("get_object", Params=params)
            return True, url
        except Exception as e:
            print(repr(e))
            return False, None
