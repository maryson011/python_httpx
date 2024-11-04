import httpx

response = httpx.get('https://httpbin.org/get')
#print('text')
#print(response.text)
#print('json')
#print(response.json)
#print('content')
#print(response.content)
#print(response.status_code)
#print(response.cookies)

#response2 = httpx.post(
#    'https://httpbin.org/post',
    #params={},
    #json={},
    #headers={},
    #auth={}
#)

## timeout e redirect
# from httpx import get
r = httpx.get(
    'https://httpbin.org/redirect/10',
    #'https://httpbin.org/delay/10',
    follow_redirects=True,
    timeout=5.0
)

print(r.history)
print(r.history[0].text)

from httpx import Client as Session

with Session() as session:
    response = session.get(
        'https://httpsbin.org/delay/10'
    )
print(response)

with Session(base_url='https://httpsbin.org') as session:
    response = session.get(
        '/delay/10'
    )
print(response)