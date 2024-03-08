"""initializes the models package, creating a global
FileStorage instance for managing data serialization
and deserialization, thereby enabling persistent
storage across the application.
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
