from typing import Dict, Optional, List
from Backend.App.Models.mock_request import MockDefinition, DEFAULT_SCENARIO_NAME

class InMemoryMockDatabase:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(InMemoryMockDatabase, cls).__new__(cls)
            cls._instance.mock_definitions: Dict[str, MockDefinition] = {}
        return cls._instance

    def _generate_key(self, method: str, path: str) -> str:
        return f"{method.upper()}:{path}"

    def add_or_update_mock(self, config: MockDefinition) -> None:
        key = self._generate_key(config.method, config.path)
        self.mock_definitions[key] = config
        print(f"INFO: Mock added/updated for key: {key}")

    def find_mock(self, method: str, path: str) -> Optional[MockDefinition]:
        key = self._generate_key(method, path)
        print(f"INFO: Searching for mock with key: {key}")
        return self.mock_definitions.get(key)

    def get_all_mocks(self) -> List[MockDefinition]:
        return list(self.mock_definitions.values())

    def delete_mock(self, method: str, path: str) -> bool:
        key = self._generate_key(method, path)
        if key in self.mock_definitions:
            del self.mock_definitions[key]
            print(f"INFO: Mock deleted for key: {key}")
            return True
        return False

mock_db = InMemoryMockDatabase()
