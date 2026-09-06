# Search Agent

A simple AI-powered search agent built as a learning project to understand how modern LLM agents work.

The agent searches the web using **Tavily**, synthesizes the retrieved information using **LangChain**, and returns concise, context-aware answers—similar to tools like ChatGPT or Claude, but built from scratch to explore the underlying concepts.

## Tech Stack

- LangChain
- LangSmith (tracing & debugging)
- Tavily Search API
- NVIDIA Inference API
- `openai/gpt-oss-20b` as the LLM

## Purpose

This project is part of my journey to learn:

- Agentic AI with LangChain
- Tool calling
- Web search integration
- Prompt engineering
- LLM orchestration and observability

> **Note:** The goal isn't to build a ChatGPT replacement, but to understand how search agents are designed and implemented under the hood. NVIDIA's free inference endpoint is used to run `openai/gpt-oss-20b`.
