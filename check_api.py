from typing import Optional, List

class APIModelChecker:
    def __init__(self, xai_key: str = None):
        self.xai_key = xai_key

    def check_xai_models(self) -> Optional[List[str]]:
        if not self.xai_key:
            return None
        try:
            # Since Grok 3 is the only publicly available model, return it as the only option
            # If xAI API provides a model listing endpoint, implement it here (check https://x.ai/api)
            return ["grok-3"]
        except Exception as e:
            print(f"[xAI Error] {e}")
            return None