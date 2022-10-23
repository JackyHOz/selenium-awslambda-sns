# Purpose

## Schedule to send deepracer leaderboard info (top3) via email

### Prerequisites
- AWS account
- Python 3.8
- AWS CLI
- AWS SAM
- Docker

### Architecture
!/images/architecture.jpg

### How to use: 
1. aws configure
- input your access key and secret key
2. git clone https://github.com/JackyHOz/selenium-awslambda-sns.git
3. cd selenium-awslambda-sns
4. sam build
5. sam deploy --guided
- then choose your prefer configure
6. Confirm subscription on your mailbox

### Example Sourcs
!/images/website_info.jpg

### Example output
!/images/output.jpg

### Doc:
- https://www.selenium.dev/documentation/
- https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html

### Ref: https://cloudbytes.dev/snippets/run-selenium-in-aws-lambda-for-ui-testing

### Delete
- delete the cloudformation stack that you created