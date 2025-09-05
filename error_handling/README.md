
## **Common types of exceptions in Python**

Exceptions are **objects** derived from the base class `BaseException`.  
Python has **many built-in exceptions**, but here are the most frequently used:

| Exception Type                        | When It Happens                                                      |
| ------------------------------------- | -------------------------------------------------------------------- |
| `Exception`                           | Base class for most exceptions. Can catch many errors.               |
| `ValueError`                          | Invalid value, e.g., `int("abc")`.                                   |
| `TypeError`                           | Operation on an invalid type, e.g., `"2" + 3`.                       |
| `ZeroDivisionError`                   | Division by zero, e.g., `10 / 0`.                                    |
| `IndexError`                          | Accessing a list/tuple out of range, e.g., `lst[10]`.                |
| `KeyError`                            | Accessing a dictionary with a missing key, e.g., `d["missing"]`.     |
| `FileNotFoundError`                   | Trying to open a file that doesn’t exist.                            |
| `PermissionError`                     | No permission to access a file or resource.                          |
| `ImportError` / `ModuleNotFoundError` | Error importing a module.                                            |
| `AttributeError`                      | Accessing a missing attribute, e.g., `obj.missing_method()`.         |
| `OSError`                             | General system-related errors, e.g., disk errors or failed OS calls. |


