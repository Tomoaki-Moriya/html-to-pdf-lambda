# html-to-pdf-lambda

AWS Lambda to generate PDF from HTML

# Getting started

## Setup environment

```
pip install -r src/requirements.txt
```

## Deploy

```

sam build

```

```
aws s3api create-bucket --bucket <bucket_name> --region <region> --create-bucket-configuration LocationConstraint=<region> --profile <your_profile_name>
```

```
aws ecr create-repository --repository-name html-to-pdf-lambda --region <your_region> --profile <your_profile_name>
```

```

sam deploy \
--stack-name html-to-pdf-lambda-stack \
--region <your_region> \
--s3-bucket <your_s3_bucket> \
--capabilities CAPABILITY_NAMED_IAM \
--image-repository <your-account_id>.dkr.ecr.<your_region>.amazonaws.com/<your_repository_name> \
--profile <your_profile_name>
```
