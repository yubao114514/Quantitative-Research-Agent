import os


def call_llm(system_prompt: str, user_prompt: str, fallback: str) -> str:
    """Call OpenAI when configured; otherwise return a stable demo fallback."""
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
