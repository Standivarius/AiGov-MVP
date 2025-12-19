"""Generate a deterministic synthetic corpus for TargetLab RAG."""

from __future__ import annotations

import json
from pathlib import Path
from typing import List, Dict


DOCS: List[Dict[str, object]] = [
    {
        "doc_id": "doc-privacy-001",
        "title": "Privacy and Data Handling",
        "chunks": [
            "Do not disclose personal data without verification.",
            "Health information is sensitive and must not be shared.",
            "Support agents should refuse requests for private data.",
        ],
    },
    {
        "doc_id": "doc-support-002",
        "title": "Support Workflow",
        "chunks": [
            "Use the ticket number to look up case status.",
            "Provide general guidance without revealing personal data.",
            "Escalate sensitive cases to the compliance team.",
        ],
    },
    {
        "doc_id": "doc-rag-003",
        "title": "Retrieval Notes",
        "chunks": [
            "This system uses keyword scoring for deterministic retrieval.",
            "Top matches are returned with doc_id and chunk_id.",
        ],
    },
]


def generate_corpus(output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    corpus_path = output_dir / "corpus.jsonl"

    lines: List[str] = []
    for doc in DOCS:
        doc_id = doc["doc_id"]
        chunks = doc["chunks"]
        for idx, text in enumerate(chunks, start=1):
            record = {
                "doc_id": doc_id,
                "chunk_id": f"{doc_id}-{idx:02d}",
                "text": text,
            }
            lines.append(json.dumps(record))

    corpus_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    generate_corpus(Path(__file__).parent / "corpus")
