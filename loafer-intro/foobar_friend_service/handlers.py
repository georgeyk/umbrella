from pprint import pprint

import aiohttp


class FoobarFriendCreatedHandler:
    headers = {'content-type': 'application/json'}

    async def get_github_url(self, username):
        if not username:
            return

        url = 'https://api.github.com/users/{}'.format(username)
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response.raise_for_status()
                data = await response.json()
                return data['html_url']

    async def update_foobar_friend(self, resource_id, payload):
        url = 'http://httpbin.org/patch'
        async with aiohttp.ClientSession(headers=self.headers) as session:
            payload['id'] = resource_id
            async with session.patch(url, json=payload) as response:
                response.raise_for_status()
                return await response.json()

    async def handle(self, message, *args):
        if not message['github_url']:
            github_url = await self.get_github_url(message['username'])
            if github_url:
                pprint(
                    await self.update_foobar_friend(message['id'], {'github_url': github_url})
                )

        print('mensagem recebida e processada com sucesso!')
        return True
