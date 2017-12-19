# hyper-validator
XML validator lib for Python

## How to use
Example:
```python
import XMLValidator

v = XMLValidator("/path/to/file/xml")
print v.validate_xml()
```
Output:
```python
return (validation_status, lxml_message)
```
