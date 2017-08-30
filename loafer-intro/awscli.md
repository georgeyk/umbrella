## [awscli](https://github.com/aws/aws-cli)

```bash
# create topic
aws --endpoint-url http://localhost:4100 sns create-topic --name friend-created

# create queue
aws --endpoint-url http://localhost:4100 sqs create-queue --queue-name foobar-friend-created

# subscribe queue to topic
aws --endpoint-url http://localhost:4100 sns subscribe --topic-arn arn:aws:sns:local:000000000000:friend-created \
 --protocol sqs --notification-endpoint http://localhost:4100/queue/foobar-friend-created

# publish the contents of 'test_user.json' to topic
aws --endpoint-url http://localhost:4100 sns publish \
 --topic-arn arn:aws:sns:local:000000000000:friend-created \
 --message file://test_user.json
```
