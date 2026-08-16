# ChatGPT Archive → Global Knowledge Pipeline

## What this does

The repository now contains `tools/import_chatgpt_export.py`, a local importer for a user-owned ChatGPT data export.

Pipeline:

`ChatGPT data export → local archive → manifest → thematic analysis → curated knowledge graph → GitHub`

## Important limitation

The OpenAI API cannot be used as a magic endpoint for retrieving a user's entire ChatGPT account history. The user must first obtain their own data export or otherwise provide the conversation files. The importer then processes those files.

## Optional OpenAI analysis

The importer can optionally call the OpenAI API to enrich the archive. It reads `OPENAI_API_KEY` from the environment; never commit an API key to GitHub.

Example:

```bash
python -m pip install openai
export OPENAI_API_KEY="YOUR_KEY"
python tools/import_chatgpt_export.py conversations.json --out archive --summarize
```

For an archive containing sensitive personal conversations, prefer processing locally and publish only a curated/redacted knowledge layer.

## Recommended repository layers

### Raw archive
Private/local only unless explicitly reviewed.

### Curated archive
Redacted conversations and research notes that are intentionally publishable.

### Knowledge layer
Machine-readable concepts, entities, relationships, timelines and evidence.

### Global World Knowledge layer
Public research standards and non-sensitive datasets derived from the archive.

## Suggested future graph

```text
Conversation
  ↓
Idea
  ↓
Topic
  ↓
Project
  ↓
Entity
  ↓
Evidence
  ↓
Decision
  ↓
Implementation
  ↓
Result
  ↓
Revision
```

This allows the history of an idea to be followed from its earliest appearance through later versions and implementation.

## Privacy rule

Do not publish passwords, API keys, private addresses, financial identifiers, health information, private correspondence, or other sensitive personal data. Review generated files before committing them to a public repository.
