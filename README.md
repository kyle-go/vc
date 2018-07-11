# vc
a python library for create image verification-code 

https://pypi.org/project/vc/

### How to use?

#### 0x01
```
pip install vc -i https://pypi.org/simple
```

#### 0x02
```
import os
from vc import create_image_base64, create_image_file

ret, result = create_image_base64()
print("Test create image base64.")
if ret is True:
    print(result['code'])
    print(result['base64'])

ret, result = create_image_file()
print("Test create image base64.")
if ret is True:
    print(result['code'])
    print(result['file'])
    # remove tmp file
    os.remove(result['file'])
```
