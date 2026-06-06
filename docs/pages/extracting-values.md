# Extracting values

Once you have a Result object, you need to safely extract the contained value or handle the potential error. This page covers the standard ways to unwrap your data.

## Pattern matching

The most explicit and Pythonic way to extract values is using the match statement (Python 3.10+). It forces you to handle both success and failure cases structurally.

```python
from result import Result, Ok, Err

def handle_response(result: Result[str, ValueError]) -> str:
    match result:
        case Ok(value):
            return f"Success: {value}"
        case Err(error):
            return f"Error occurred: {error}"
```

## Methods

### unwrap

Returns the contained Ok value if the result is a success. If the result is an Err, it raises an exception. Use this only when you are absolutely certain the operation succeeded.

```python
result: Result[int, str] = Ok(42)value = result.unwrap()  # Returns 42
failed_result: Result[int, str] = Err("Something went wrong")
failed_result.unwrap()  # Raises UnwrapError
```

### expect

Similar to unwrap, but allows you to provide a custom error message. The custom message will be included in the raised exception if the result is an Err.

```python
result: Result[dict, str] = Err("Connection timeout")
# Raises UnwrapError: "Database configuration failed: Connection timeout"
config = result.expect("Database configuration failed")
```

### unwrap_or

Returns the contained Ok value if it exists. If the result is an Err, it returns a default value that you provide instead of raising an exception.

```python
success: Result[int, str] = Ok(10)
print(success.unwrap_or(0))  # Outputs: 10
failure: Result[int, str] = Err("File not found")
print(failure.unwrap_or(0))  # Outputs: 0
```

### unwrap_err

The exact opposite of unwrap. Returns the contained Err value if the result failed. If the result is an Ok, it raises an exception.

```python
failure: Result[int, str] = Err("Access denied")
error_msg = failure.unwrap_err()  # Returns "Access denied"
success: Result[int, str] = Ok(200)
success.unwrap_err()  # Raises UnwrapError
```

### resolve

Acts as a lazy version of unwrap_or. Returns the contained Ok value if the result is a success. If it is an Err, it calls the provided fallback function (passing the error into it) and returns its result.This is useful when computing a default value is expensive and should only happen on failure.

```python
def get_backup_value(error: str) -> int:
    # This expensive fallback runs only if needed
    return 999

success: Result[int, str] = Ok(5)
# Returns 5 (get_backup_value is never called)
print(success.resolve(get_backup_value))  

failure: Result[int, str] = Err("Main system failure")
# Calls get_backup_value("Main system failure") and returns 999
print(failure.resolve(get_backup_value))  
```
