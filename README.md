# JWT Manager

JWT Manager is a powerful and efficient library designed to manage JWT tokens in applications. It simplifies the process of retrieving access tokens and JWT tokens from external authentication services, caching them using Redis for improved performance, and handling token expiration and automatic refresh. This library is ideal for developers looking to integrate secure and efficient token management into their projects.

## Features

- **Token Retrieval**: Easily retrieve access tokens and JWT tokens from external authentication services.
- **Caching**: Utilize Redis for caching tokens to improve performance.
- **Token Expiration Handling**: Automatically handle token expiration and refresh tokens as needed.
- **Efficient**: Designed to be efficient and easy to integrate into your projects.
- **Readable Expiration Time**: Displays token expiration time in a human-readable format.

## Installation

You can install the package using pip:
```sh
pip install jwt_manager
```

## Usage

Here is an example of how to use the `jwt_manager` package:

### Basic Usage

```python
from jwt_manager.api.jwt_service import JWTService

# Initialize the JWTService
auth_service = JWTService()

# Retrieve the JWT token
jwt_result = auth_service.get_jwt()
print(jwt_result)
```

### Advanced Usage

You can also configure the service with custom settings, such as specifying a different Redis server for caching:

```python
from jwt_manager.api.jwt_service import JWTService

# Initialize the JWTService with custom settings
auth_service = JWTService(redis_host='your-redis-host', redis_port=6379)

# Retrieve the JWT token
jwt_result = auth_service.get_jwt()
print(jwt_result)
```

## Configuration

The `jwt_manager` library can be configured using environment variables. Here are the available configuration options:

- `USERNAME`: The username for the authentication service.
- `PASSWORD`: The password for the authentication service.
- `ACCESS_TOKEN_URL`: The URL for retrieving the access token.
- `JWT_TOKEN_URL`: The URL for retrieving the JWT token.
- `API_KEY`: The API key for the authentication service.
- `REDIS_HOST`: The hostname of the Redis server (default: `localhost`).
- `REDIS_PORT`: The port of the Redis server (default: `6379`).

You can set these environment variables in a `.env` file or directly in your environment.

## Running the Application

To run the FastAPI application, use the following command:

```sh
uvicorn jwt_manager.api.main:app --reload
```

## Testing

To run the tests, use the following command:

```sh
pytest
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For any questions or support, please contact [Vivien](mailto:bognetienoue@gmail.com).
```
