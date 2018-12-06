# Init Flask PoC
This is an initial project of building a RESTful web service in Flask. Ideally, we expect the project structure can be a standard for staring a new web service.

## requirements
- python 3.6 up

## Instructions

### Creating Virtual Environment

1. Create a project folder
    ```sh
    $ mkdir my-project
    ```

1.  run [venv](https://docs.python.org/3/library/venv.html#module-venv)

    ```sh
    $ cd my-project
    $ python3 -m venv ./venv
    ```
1. activate virtual environment
    - On Windows, run:
        ```sh
        $ .\venv\Scripts\activate.bat
        ```
    - On Unix or Mac, run:
        ```sh
        $ source ./venv/bin/activate 
        ```
1. Copy the all files from the initial project to /my-project.
1. Install modules:
    ```sh
    $ pip install -r requirements.txt 
    ``` 
