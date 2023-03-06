# ALX-SE AirBnB Clone Project
This project creates a console to manage the objects of the larger project.
## How the console works
### Interactive mode
> $ ./console.py
> (hbnb) help

> Documented commands (type help <topic>):
> EOF  help  quit

> (hbnb) 
> (hbnb) 
> (hbnb) quit
> $
### Non-interactive mode
> $ echo "help" | ./console.py
> (hbnb)

> Documented commands (type help <topic>):
> EOF  help  quit
> (hbnb) 
> $
> $ cat test_help
> help
> $
> $ cat test_help | ./console.py
> (hbnb)

> Documented commands (type help <topic>):
> EOF  help  quit
> (hbnb) 
> $
