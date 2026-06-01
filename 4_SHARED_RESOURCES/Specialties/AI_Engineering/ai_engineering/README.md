# AI Engineering Knowledge Asset — Graph Layer

**Generated:** 2026-03-18
**Standard:** WET-GOLD v1.0 (Component: Graph Layer)

This directory contains the structural graph layer for the AI Engineering knowledge base. It represents one critical layer of the **WET-GOLD Knowledge Standard**, which mandates a multi-dimensional approach to knowledge persistence.

## The WET-GOLD Standard

A complete knowledge asset encompasses five distinct layers to ensure high-fidelity agent experience and human interaction:

1. **Raw Layer:** Preserved source media (.pdf, .epub, .txt, etc.)
2. **Graph Layer (Current):** Algorithmic chunking, embedding, and density clustering to map conceptual topology without LLM bias
3. **Entity Layer:** Targeted LLM extraction of high-value relational entities and summaries
4. **Relational Layer:** Conversion into strict SQL tables for precise data manipulation
5. **Interface Layer:** Indexed markdown documents for human-centric interaction

**Status:** This directory holds the **Graph Layer** only. It provides the algorithmic structure and conceptual anchors required for semantic search and graph-based reasoning.

## The Master Knowledge Graph

**`ai_engineering_knowledge_graph.json`** — Contains **28,096 entities** and **20,769 relations** extracted and enriched from seven source documents. All data points carry metadata tags including `publication_year` and domain `tags` for contextual filtering.

> Note: The master knowledge graph and all compiled data directories (chunks, embeddings, kg_fragments, entities_relations, raw_text) are excluded from git by `.gitignore` due to size. The structure and index files ship with the repo. Regenerate data locally using the Sensory Ingestor pipeline.

## Source Documents (7 of 8 processed)

| File | Year | Tags |
|---|---|---|
| Bass — Engineering AI Systems | 2024 | `ai-engineering`, `devops`, `architecture` |
| Huyen — Building Applications with Foundation Models | 2025 | `ai-engineering`, `foundation-models` |
| Phoenix — Prompt Engineering for Generative AI | 2024 | `ai-engineering`, `prompt-engineering` |
| Li — From Boolean Matrix Theory to Logical Dynamical Systems | 2025 | `ai-engineering`, `theory` |
| Rodriguez — Generative AI Foundations in Python | 2024 | `ai-engineering`, `python` |
| Pretraining Context Compressor (paper) | 2024 | `ai-engineering`, `llm-memory` |
| Doing AI Differently (white paper) | 2024 | `ai-ethics`, `methodology` |

**Excluded:** `BOOK_JainY_TheArtfPromptEngineeringforDeepSeek AI...` — Provider-specific. Preserved in `raw_text/` for future standalone indexing.

## Directory Structure

```
ai_engineering/
├── ai_engineering_knowledge_graph.json   ← Master consolidated KG (gitignored)
├── raw_text/                             ← Extracted plain text (gitignored)
├── chunks/                               ← Text chunk metadata (gitignored)
├── embeddings/                           ← Vector embeddings (gitignored)
├── entities_relations/                   ← Per-chunk extraction data (gitignored)
├── kg_fragments/                         ← Per-book KG fragments (gitignored)
└── README.md                             ← This file
```

## Usage

`ai_engineering.index.json` (at the `AI_Engineering/` parent level) is the lightweight pointer — load this first to orient queries without reading the full graph. The master knowledge graph is the primary access point for structured queries. Use the `embeddings/` directory for semantic search when available.

---

*This asset conforms to the WET-GOLD documentation standard.*
