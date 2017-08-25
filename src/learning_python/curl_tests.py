# curl -X POST -d 'email=minh@gmail.com&password=Miamikki521' http://localhost:8000/api-token-auth/

# curl -X POST -H "Content-Type: application/json" -d '{"email":"minh@gmail.com", "password":"Miamikki521"}' http://localhost:8000/api-token-auth/



# curl -H "Content-Type: application/json" -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Im1pbmhAZ21haWwuY29tIiwiZXhwIjoxNTAzNjM1MTUzLCJlbWFpbCI6Im1pbmhAZ21haWwuY29tIn0.1TGUaysBV9SDsR7KWj4t28dFL7-xov6tso59B7Uz8hI" http://localhost:8000/api/books/

# curl -H "Content-Type: application/json" -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Im1pbmhAZ21haWwuY29tIiwiZXhwIjoxNTAzNjM1NDY3LCJlbWFpbCI6Im1pbmhAZ21haWwuY29tIn0.DBYBL6wg6K7NC59VhrXtLmEB9jntrCcY78D3Mtlzxgk" -d '{"title": "book 6", "review": "review 4"}' http://localhost:8000/api/books/create/

# curl -X POST -H "Content-Type: application/json" -d '{"token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Im1pbmhAZ21haWwuY29tIiwiZXhwIjoxNTAzNjMyNTMzLCJlbWFpbCI6Im1pbmhAZ21haWwuY29tIiwib3JpZ19pYXQiOjE1MDM2MzIyMzN9.vX_rnoDWLTBa9krBGHZvJjCaiWya5G9I6nC1I-a-qSs"}' http://localhost:8000/api-token-refresh/

# curl -X POST -H "Content-Type: application/json" -d '{"token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Im1pbmhAZ21haWwuY29tIiwiZXhwIjoxNTAzNjMyNTYxLCJlbWFpbCI6Im1pbmhAZ21haWwuY29tIiwib3JpZ19pYXQiOjE1MDM2MzIyMzN9.hifPO_kjlIXGWApNoIBQZ9hXO_LVks3n2oMZxzlozT8"}' http://localhost:8000/api-token-verify/