# DjangoAPI

# Personal Notes.. 
`Django `& `Django Rest Framework (DRF)`
The database was used: `PostgreSQL`
`Docker` & `Docker Compose`

### Communication with the application is via a simple API
  - There are two models .. Notes and Authors 
  - So that they are bound by a one-to-many relationship


First Step :  pre Run :
  ## you should init venv
- Create Virtualenv and Activate it
 <code> python -m venv env  </code> then  move to \env\Scripts\  <code> activate </code>

- Clone this Repo
- <code> git clone https://github.com/ammaralmansor/DjangpAPI2.git </code>
- install requirments library by this command 
  <code>  pip install -r requirments   </code>
    
  ### Good job getting here
  
Second Step : 
   - Start Postgres Server at port : 5432

   - <code> python manage.py runserver </code>

   - The project will work : 127.0.1:8000

Third Step :
- go to <code> 127.0.1:8000/LAA </code> to Add Authers in first 
- 127.0.1:8000/LAA : `It will return the list of authors by default`
- type in this sytax to add Auther by API :
        {
         "name" : "anyname"
        }
      
- You will get : 
      
      `HTTP 201 Created
      Allow: OPTIONS, GET, POST
      Content-Type: application/json
      Vary: Accept

      {
          "name": "Ammar"
      }`

If added successfully ... Otherwise `HTTP 400 Bad Request Error'

------------------------------------------------
## Adding a note.
## Listing all notes.

-  go to <code> 127.0.1:8000/LAN </code> to Add Notes in first 
- 127.0.1:8000/LAN : `It will return the list of Notes by default`
- type in this sytax to add Note by API :
    {
        "auther": 4,
        "note": "Note 2"
    }
    
- You will get : 
      
      `HTTP 201 Created
      Allow: OPTIONS, GET, POST
      Content-Type: application/json
      Vary: Accept

      {
        "auther": 4,
        "note": "Note 2"
      }`

If added successfully ... Otherwise `HTTP 400 Bad Request Error'

------------------------------------------------
## Deleting a note.
## Retrieving one note by id.

- go to <code> http://127.0.0.1:8000/DRPN/1 </code> to Retrieving Note with id = 1
- you can .. Delete or  Update it
- You will get : 
      
      `HTTP 200 OK
      Allow: OPTIONS, GET, DELETE, PUT
      Content-Type: application/json
      Vary: Accept

      {
          "auther": 4,
          "note": "Note"
      }`

If added successfully ... Otherwise `HTTP 404 Not Found'

-----------------------------------------------

Note :
We used PK because it is a trial version..
Better to use Slug or uuid to access object
