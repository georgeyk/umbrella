import asyncio

from .handlers import FoobarFriendCreatedHandler


loop = asyncio.get_event_loop()

handler = FoobarFriendCreatedHandler()
message = {'invalid': 'message'}
loop.run_until_complete(handler.handle(message))
loop.close()
# Execute: python -m foobar_friend_service.manual_run
