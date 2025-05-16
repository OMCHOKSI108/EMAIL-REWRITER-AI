import cohere
from typing import Dict, Any
from dataclasses import dataclass
import time

@dataclass
class EmailConfig:
    tone: str
    model: str = "command"  # Default model (Cohere's general-purpose model)
    temperature: float = 0.7
    max_tokens: int = 1000

class EmailRewriter:
    def __init__(self, api_key: str):
        """Initialize with Cohere API key"""
        self.api_key = api_key
        self.client = cohere.Client(api_key=api_key)

    def _construct_prompt(self, email: str, tone: str) -> str:
        return f"""Rewrite the following email in a {tone.lower()} tone. 
        Improve clarity, professionalism, and politeness while maintaining the original message.
        Make sure the rewritten version is well-structured and effectively communicates the message.

        Original email: {email}"""

    def rewrite_email(self, email: str, config: EmailConfig, max_retries: int = 3) -> Dict[str, Any]:
        for attempt in range(max_retries):
            try:
                print(f"[DEBUG] Using model: {config.model}, Attempt: {attempt + 1}/{max_retries}")
                prompt = self._construct_prompt(email, config.tone)
                response = self.client.chat(
                    model=config.model,
                    message=prompt,
                    temperature=config.temperature,
                    max_tokens=config.max_tokens
                )
                rewritten_email = response.text.strip()
                return {"status": "success", "rewritten_email": rewritten_email}
            except cohere.CohereAPIError as e:
                if "rate limit" in str(e).lower():  # Handle rate limiting
                    retry_delay = 21  # Default retry delay
                    print(f"[INFO] Rate limit exceeded. Retrying after {retry_delay} seconds...")
                    time.sleep(retry_delay)
                    continue
                return {"status": "error", "error": str(e)}
            except Exception as e:
                return {"status": "error", "error": str(e)}
        return {"status": "error", "error": "Max retries reached due to rate limits. Please try again later."}

    def validate_api_key(self) -> Dict[str, Any]:
        try:
            # Test the API key with a simple request
            self.client.chat(
                model="command",
                message="test",
                max_tokens=5
            )
            return {"status": "success", "message": "API key is valid."}
        except Exception as e:
            return {"status": "error", "error": f"API key validation failed: {str(e)}"}