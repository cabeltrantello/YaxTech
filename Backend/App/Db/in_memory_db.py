from typing import Dict, Optional
from Backend.App.Models.mock_request import MockConfiguration

class InMemoryMockDatabase:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(InMemoryMockDatabase, cls).__new__(cls)
            # The main storage for our mocks.
            # Key format: "METHOD:/path/to/resource"
            # Value: MockConfiguration Object
            cls._instance.mock_configurations: Dict[str, MockConfiguration] = {}

        return cls._instance
    

    def _generate_key(self, method: str, path: str) -> str:
        """Generates a unique key for storing and retrieving mocks."""
        return f"{method.upper()}_{path}"
    
    def add_mock(self, config: MockConfiguration) -> None:
        key = self._generate_key(config.method, config.path)
        self.mock_configurations[key] = config
        print(f"INFO: Mock added/updated for key: {key}")

    def find_mock(self, method: str, path: str) -> Optional[MockConfiguration]:
        key = self._generate_key(method, path)
        print(f"INFO: Searching for mock with key: {key}")
        return self.mock_configurations.get(key)
    
mock_db = InMemoryMockDatabase()