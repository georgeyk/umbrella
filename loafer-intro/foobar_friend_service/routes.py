from loafer.ext.aws.routes import SNSQueueRoute

from .handlers import FoobarFriendCreatedHandler


routes = (
    SNSQueueRoute(
        provider_queue='foobar-friend-created',
        provider_options={
            'endpoint_url': 'http://localhost:4100',
        },
        handler=FoobarFriendCreatedHandler(),
    ),
)
