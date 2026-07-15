# Smart Prompt Optimizer

Analyzes any rough prompt and rewrites it using the most 
effective prompting technique — zero-shot, few-shot, 
chain-of-thought, or structured output.

## What it does

- Analyzes prompt intent, complexity, and missing elements
- Recommends the right prompting technique
- Rewrites the prompt with a clear explanation
- Two-stage LLM pipeline — analysis then rewriting

## Why it matters

Bad prompts cost companies money in wasted tokens and 
poor outputs. This tool generates an optimized first draft 
automatically — saving time and reducing prompt iteration cycles.

## Run it

```bash
pip install groq gradio python-dotenv
```

Add your Groq API key to a `.env` file:
