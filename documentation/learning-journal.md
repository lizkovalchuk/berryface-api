# BerryFace Backend Learning Journal
## Documentation of Lessons

1. [ Development Cycle ](#development-cycle)
2. [ AWS Integration ](#aws-integration)
3. [ Deploying to Lambda ](#deploying-to-lambda)

<a name="development-cycle"></a>

### ___Development Cycle___

1. update
2. test
3. push and commit to remote repo
4. then deploy
5. then test

<a name="aws-integration"></a>

### ___AWS Integration___

1. Download AWS CLI on machine
    - create user on AWS web app
    - AWS CLI config asks for AWS user creds (command to access/write/update AWS creds is `aws configure`.)
    - user credentials for AWS CLI are set globally.
    - Your AWS credentials enable deploying to Lambda from CLI.
2. To deploy to Lambda, Lambda expects a .zip that contains the function itself along with all its dependencies. The link to documentation on how to deploy to Lambda via the CLI is:

https://docs.aws.amazon.com/lambda/latest/dg/python-package.html

3. Check your deploy by accessing the API endpoint Amazon provides for your lambda. 
    - For example, below is our lambda function as of June 6th, 2020.
    - It takes an event as a param and prints a message.
    - Check the success of your lambda by accessing: https://e8rugc1lb0.execute-api.us-east-2.amazonaws.com/default/berryface-flask?first_name=test&last_name=123
    - See image Example 1: Lambda Return below

```python
from flask import Flask

def lambda_handler(event, context):
    first_name = event['queryStringParameters']['first_name']
    last_name = event['queryStringParameters']['last_name']
    message = 'Hello {} {}!'.format(first_name, last_name)
    return { 
        'message' : message
    }
```

##### __Example 1: Lambda Return__


![alt text](/documentation/images/lambda.png)

<a name="deploying-to-lambda"></a>

### ___Deploying to Lambda___

- If your function has dependencies, you will need to bunble them into a zip and include them in your deploy. 
- For this reason, you must first run `make_lib.sh` and then `deploy.sh`


--------------

## Next Course of Action

### Structure

1. Have Raspberry Pi use `boto3` python package to write to Amazon SQS topic.

https://boto3.amazonaws.com/v1/documentation/api/latest/guide/sqs-example-sending-receiving-msgs.html

2. Next we will develop 3 seperate Lambda functions
    - Lambda 1: Subscribes to AWS SQS and writes queued content to Redis (Amazon Elasticache).
    - Lambda 2: ReadOnly Flask application. It Queries Elasticache and has seperate endpoints foreach filtered result/aggregation.
    - Lambda 3: Subscribes to SQS and writes results into DynamoDB for achival purposes.

3. ReactJS app makes requests to Lambda 2 to populate graph

### Helpful Links

1. https://redis.io/topics/data-types-intro#redis-keys
    - How you structure keys is essential for queries and aggregations.



