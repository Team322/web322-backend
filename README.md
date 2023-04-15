# web322-backend

## Planning

We need routes for:
1. service-worker requests (authenticated via shared constant token)
   1. This auth token needs to be stored in .env
2. storing (this would be static file serving) session histories, encrypted or not
   1. is will need some kind of static serving plugin to flask?
3. user settings page, where they setup api key to use, encryption settings, parameters for 
   prompt(?) and other settings
   1. Database schema will be using sqlalchemy to a postgres server on the gcp instance
4. user login and registration page
5. user status/history page, where they can see their invocation history

We will also need to be careful when doing the actual tcpdump/session capture of openai api calls

## TODO
