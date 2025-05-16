import cohere
from typing import Optional, List

class APIModelChecker:
    def __init__(self, cohere_key: str = None):
        self.cohere_key = cohere_key
        if cohere_key:
            self.client = cohere.Client(api_key=cohere_key)
        else:
            self.client = None

    def check_cohere_models(self) -> Optional[List[str]]:
        if not self.cohere_key or not self.client:
            return None
        try:
            # Since Cohere doesn't provide a /models endpoint, hardcode likely available models
            # Check https://docs.cohere.ai for the latest model names if needed
            models = ["command", "command-light"]
            print(f"[DEBUG] Available Cohere models: {models}")
            return models
        except Exception as e:
            print(f"[Cohere Error] {e}")
            return None