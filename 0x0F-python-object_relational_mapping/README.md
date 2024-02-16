ORMS - Object-relational Mappers(ORMs)
Is a code library that automates the transfer of data stored in relational database tables into objects that are more commonly used in application code.

ORMs provide a high-level abstraction upon a relational database that alows a developer to write Python code insted of SQL to perform the CRUD operations.

Example of query that does not use ORM ->
	SELECT * FROM USERS WHERE zip_code = 9410;
Example of query using ORM ->
	engine = Users.objects.filter(zip_code = 9410)

Thats it. Yeah
