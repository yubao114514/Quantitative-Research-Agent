import os


def call_llm(system_prompt: str, user_prompt: str, fallback: str) -> str:
    """Call Gemini or OpenAI when configured; otherwise return a stable fallback."""
    gemini_key = os.getenv("GEMINI_API_KEY")
    if gemini_key:
        try:
            from google import genai

            client = genai.Client(api_key=gemini_key)
            response = client.models.generate_content(
                model=os.getenv("GEMINI_MODEL", "gemini-2.5-flash"),
                contents=f"{system_prompt}\n\n{user_prompt}",
            )
            return response.text or fallback
        except Exception as exc:
            return f"{fallback}\n\n_Note: Gemini call failed, using fallback. Error: {exc}_"

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return fallback

    try:
        from openai import OpenAI

        client = OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.3,
        )
        return response.choices[0].message.content or fallback
    except Exception as exc:
        return f"{fallback}\n\n_Note: LLM call failed, using fallback. Error: {exc}_"
