📘 Book CRUD APIs
Method	      Endpoint	            Description
GET	        /book_list/	            Retrieve list of all books
POST	    /create_book/	            Create a new book
PUT	    /update_book/<int:pk>/	    Update book by ID
DELETE	 /delete_book/<int:pk>/     Delete book by ID

📂 CSV APIs
Method	    Endpoint	                   Description
GET	     /export_books/	         Export all books as CSV file
POST	   /upload_books/	         Upload books using CSV file

Password for Admin:
username=admin
password=admin

Kindly also give Basic auth and send username and password while hitting endpoint with postman.
