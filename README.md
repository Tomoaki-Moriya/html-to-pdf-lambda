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

sam deploy \
--stack-name slack-rembg-lambda-stack \
--region <your_region> \
--s3-bucket <your_s3_bucket> \
--capabilities CAPABILITY_NAMED_IAM \
--image-repository <your-account_id>.dkr.ecr.<your_region>.amazonaws.com/<your_repository_name> \
--profile <your_profile_name>
```
