# Class Dojo
Tools to get points from the classdojo point system


# Install using:

```pip3 install classdojo```

# Example:

```
import classdojo.classdojo as classdojo

classId = "<CLASS ID (Found in URL)"
cookie = "<Cookie (Found in developer console)

_class = classdojo.classDojo(classId, cookie)

print(_class.getPointsByCombinedName("KnowlesB")
```
