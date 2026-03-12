User session management means how the backend remembers who the user is across multiple requests.

Since HTTP is stateless, every request is independent. Sessions help the server know:

simple session flow 

User logs in
↓
Backend generates session
↓
User adds product to cart
↓
Backend identifies user from session
↓
Cart stored against user


- pydantic 
    - request validation 
    - consistent api response 
    - automatic openapi docs 

