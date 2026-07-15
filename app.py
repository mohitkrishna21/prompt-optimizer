import os
from dotenv import load_dotenv
from groq import Groq
import gradio as gr

load_dotenv()
client=Groq(api_key=os.getenv("GROQ_API_KEY"))

def analyze_prompt(rough_prompt):
    response=client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role":"system", "content":"""You are an expert prompt engineer. Analyze the given prompt and return a JSON object with exactly these fields:
        - task_type: one of [creative, analytical, coding, factual, conversational]
        - complexity: one of [simple, moderate, complex]
        - missing_elements: a list of what the prompt is missing (examples, context, output format, constraints, audience)
        - recommended_technique: one of [zero-shot, few-shot, chain-of-thought, structured-output, meta-prompt]
        - reason: one sentence explaining why you chose that technique

         Return ONLY the JSON object, no other text."""},
         {"role":"user", "content":rough_prompt}
        ],
        temperature=0.3)

    result = response.choices[0].message.content
    result = result.replace("```json", "").replace("```", "").strip()
    return result
    

def rewrite_prompt(rough_prompt,analysis):
    response=client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role":"system", "content":"""You are an expert prompt engineer. You will receive a rough prompt and its analysis.
        Rewrite the prompt using the recommended technique from the analysis.

        Return your response in this exact format:
        TECHNIQUE USED: [technique name]
        REWRITTEN PROMPT:
        [the rewritten prompt]
        EXPLANATION:
        [2-3 sentences explaining what you changed and why]"""},
         {"role":"user", "content":f"Rough Prompt: {rough_prompt}\n\nAnalysis: {analysis}"}
        ],
        temperature=0.5)
    return response.choices[0].message.content

def optimize_prompt(rough_prompt):

    analysis=analyze_prompt(rough_prompt)
    optimized=rewrite_prompt(rough_prompt,analysis)

    return analysis, optimized

demo=gr.Interface(
        fn=optimize_prompt,
        inputs=gr.Textbox(lines=5, label="Paste Your Prompt Here"),
        outputs=([gr.Textbox(label="Prompt Analysis"),gr.Textbox(label="Optimized Prompt")]),
        title="Prompt Optimizer",
        description="Paste any rough prompt and get an optimized version with explanation"
    )

demo.launch(share=True)