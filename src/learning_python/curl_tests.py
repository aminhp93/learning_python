# curl -X POST -d 'email=minhpn.org.ec@gmail.com&password=Miamikki521' http://localhost:8000/api-token-auth/

# curl -X POST -H "Content-Type: application/json" -d '{"email":"minh@gmail.com", "password":"Miamikki521"}' http://localhost:8000/api-token-auth/


# curl -H "Content-Type: application/json" -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Im1pbmhwbi5vcmcuZWNAZ21haWwuY29tIiwiZXhwIjoxNTA1NzI0NTMyLCJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6Im1pbmhwbi5vcmcuZWNAZ21haWwuY29tIn0.5fghsxJ0CcEULNyIGGXf8US_L2Ll9nPR7KExiPL5WGw" http://localhost:8000/api/posts/

# curl -H "Content-Type: application/json" -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Im1pbmhwbi5vcmcuZWNAZ21haWwuY29tIiwiZXhwIjoxNTA0NDM0MzgxLCJlbWFpbCI6Im1pbmhwbi5vcmcuZWNAZ21haWwuY29tIn0.uH7rrnLlro1PHt6s-YrExsFiPT51WoykpUExahrlemA" -d '{"title": "book 6", "content": "test", "publish": "2017-03-03", "image": null}' http://localhost:8000/api/posts/create/

# curl -X POST -H "Content-Type: application/json" -d '{"token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Im1pbmhAZ21haWwuY29tIiwiZXhwIjoxNTAzNjMyNTMzLCJlbWFpbCI6Im1pbmhAZ21haWwuY29tIiwib3JpZ19pYXQiOjE1MDM2MzIyMzN9.vX_rnoDWLTBa9krBGHZvJjCaiWya5G9I6nC1I-a-qSs"}' http://localhost:8000/api-token-refresh/

# curl -X POST -H "Content-Type: application/json" -d '{"token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Im1pbmhAZ21haWwuY29tIiwiZXhwIjoxNTAzNjMyNTYxLCJlbWFpbCI6Im1pbmhAZ21haWwuY29tIiwib3JpZ19pYXQiOjE1MDM2MzIyMzN9.hifPO_kjlIXGWApNoIBQZ9hXO_LVks3n2oMZxzlozT8"}' http://localhost:8000/api-token-verify/