# FastAPI Todo Application

This repository contains a simple Todo application built with FastAPI and SQLite. The aim is to help beginners get started with FastAPI by creating a basic CRUD (Create, Read, Update, Delete) application.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.6 or higher
- [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html) (Optional, but recommended)

### Setting Up a Virtual Environment (Optional)

It's recommended to create a virtual environment to manage dependencies for this project. This can help ensure that the project and its dependencies do not affect your system Python installation.

1. Install `virtualenv` if you haven't already:
    ```bash
    pip install virtualenv
    ```

2. Create a new virtual environment in the project directory:
    ```bash
    virtualenv venv
    ```

3. Activate the virtual environment:
    - On Windows:
        ```bash
        .\venv\Scripts\activate
        ```
    - On macOS and Linux:
        ```bash
        source venv/bin/activate
        ```

### Installing Dependencies

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/ronaldojr/blog_first_fastapi.git
    cd blog_first_fastapi
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

1. With your virtual environment activated, run the following command:
    ```bash
    uvicorn main:app --reload
    ```

2. The FastAPI application will start running on `http://127.0.0.1:8000`. You can access the interactive API docs at `http://127.0.0.1:8000/docs` to try out the API endpoints.

## Running Tests

This project includes a basic test suite. To run the tests, use the following command:
    ```bash
    pytest
    ```

## Further Reading

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLite Documentation](https://www.sqlite.org/docs.html)
- [Virtual Environments in Python](https://docs.python.org/3/tutorial/venv.html)

## Contributing

Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
