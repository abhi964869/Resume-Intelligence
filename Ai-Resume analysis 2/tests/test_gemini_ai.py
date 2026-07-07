from utils import gemini_ai


def test_ask_gemini_without_client_returns_instruction_message():
    original_client = gemini_ai.client
    gemini_ai.client = None
    try:
        result = gemini_ai.ask_gemini("test")
    finally:
        gemini_ai.client = original_client

    assert "GEMINI_API_KEY" in result
