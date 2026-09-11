# VeriRAG

**Evidence-Grounded Enterprise Knowledge & Decision Intelligence Platform**

VeriRAG is a production-oriented Retrieval-Augmented Generation (RAG) platform designed to answer questions from enterprise knowledge while providing **verifiable evidence, citations, and transparent retrieval behavior**.

The goal is to build more than a basic document chatbot: VeriRAG is being engineered as a measurable, explainable, modular, and production-oriented knowledge intelligence system.

---

## Current Status

🚧 **Active development**

The core document-to-retrieval pipeline is currently implemented and tested.

### Implemented

* PDF and DOCX document upload
* Document metadata persistence
* PDF and DOCX parsing
* Document chunking
* Page-aware chunk metadata
* Semantic embeddings using `BAAI/bge-small-en-v1.5`
* PostgreSQL + pgvector vector storage
* Cosine-similarity vector retrieval
* Configurable retrieval relevance threshold
* Citation-ready evidence construction
* Evidence-aware generation contract
* Insufficient-evidence handling
* Generation provider abstraction
* Automated unit and integration tests

### In Progress

* Real LLM-backed answer generation
* Citation-aware answer formatting
* End-to-end RAG orchestration
* Query API
* Better retrieval evaluation and threshold calibration

### Planned

* Hybrid vector + keyword retrieval
* Reranking
* Query rewriting
* Multi-document reasoning
* Multi-hop reasoning
* Comparative and analytical queries
* Contradiction detection
* Document-version awareness
* Role-based access control
* RAG evaluation and benchmarking
* User feedback and analytics
* Observability and audit logging
* Production frontend and analytics dashboard
* Background processing with Redis/workers
* Docker-based deployment and CI/CD

---

## Architecture

```text
                         ┌─────────────────────┐
                         │      Documents      │
                         │    PDF / DOCX       │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │      Parsing        │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │     Chunking        │
                         │ page-aware metadata │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │     Embeddings      │
                         │ BGE-small-en-v1.5   │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │ PostgreSQL +        │
                         │     pgvector        │
                         └──────────┬──────────┘
                                    │
                                    │
                         ┌──────────▼──────────┐
                         │   Vector Retrieval  │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │  RetrievalService   │
                         │ relevance filtering │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   EvidenceService   │
                         │ citation-ready data │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │  GenerationService  │
                         │ evidence-grounded   │
                         │      answers        │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │  Answer + Citations │
                         └─────────────────────┘
```

---

## Technology Stack

### Backend

* **Python**
* **FastAPI**
* **SQLAlchemy**
* **Alembic**
* **Pydantic / Pydantic Settings**

### RAG Pipeline

* Custom ingestion pipeline
* PDF parsing with `pypdf`
* DOCX parsing with `python-docx`
* Custom text and paragraph chunking
* `sentence-transformers`
* `BAAI/bge-small-en-v1.5`
* Custom retrieval and evidence pipeline

### Database

* **PostgreSQL 16**
* **pgvector**
* SQLAlchemy ORM

### Testing

* **pytest**
* Unit tests
* Database integration tests
* Retrieval tests
* Embedding tests
* Evidence and generation contract tests

### Infrastructure

* **Docker**
* Docker Compose
* PostgreSQL container

### Frontend

Planned:

* **Next.js**
* **TypeScript**
* **Tailwind CSS**

---

## RAG Pipeline

The current RAG pipeline is deliberately modular:

```text
Document
   ↓
Parser
   ↓
Chunker
   ↓
EmbeddingService
   ↓
Vector Storage
   ↓
RetrievalService
   ↓
EvidenceService
   ↓
GenerationService
```

Each stage has a focused responsibility.

This makes it possible to test and improve individual components without coupling the entire system together.

---

## Evidence-Grounded Generation

A central design principle of VeriRAG is:

> **The system should not fabricate an answer when the available evidence is insufficient.**

The generation layer therefore receives a structured `EvidenceContext` rather than arbitrary document text.

Conceptually:

```text
EvidenceContext
      ↓
GenerationService
      ↓
GeneratedAnswer
      ├── answer
      ├── citations
      └── has_evidence
```

When no sufficiently relevant evidence is retrieved, the system can explicitly return an insufficient-evidence response instead of pretending to know the answer.

This design will later support:

* citation validation
* groundedness evaluation
* contradiction detection
* evidence coverage metrics
* answer-quality evaluation

---

## Retrieval

VeriRAG currently uses semantic vector retrieval.

Documents are converted into normalized embeddings using:

```text
BAAI/bge-small-en-v1.5
```

The model produces **384-dimensional embeddings**, which are stored in PostgreSQL using pgvector.

Retrieval uses cosine similarity to rank candidate document chunks.

A configurable relevance threshold is applied after retrieval so that weakly related chunks can be rejected as insufficient evidence.

The threshold will eventually be calibrated against a dedicated evaluation dataset rather than treated as a universal constant.

---

## Citation Architecture

Retrieved chunks are converted into citation-ready evidence before reaching the generation layer.

Each evidence item preserves:

* Citation ID
* Chunk ID
* Document ID
* Text
* Retrieval score
* Page number
* Section metadata

This allows the eventual answer generator to reference the exact source evidence used to produce an answer.

---

## Engineering Principles

VeriRAG is being developed around several engineering principles:

### 1. Evidence before generation

Retrieval and evidence construction happen before answer generation.

### 2. No evidence, no confident answer

The system should explicitly acknowledge insufficient evidence rather than hallucinating.

### 3. Modular architecture

Parsing, chunking, embeddings, retrieval, evidence construction, and generation are separated into independent components.

### 4. Provider independence

The generation layer exposes an abstraction so that different LLM providers can be introduced without rewriting the retrieval pipeline.

### 5. Test-driven development

Important components are implemented together with automated tests before being integrated into larger workflows.

### 6. Measurable RAG

Future development will focus on evaluating retrieval quality, evidence coverage, groundedness, and answer quality rather than relying only on subjective chatbot responses.

---

## Project Structure

```text
VeriRAG/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── models/
│   │   ├── repositories/
│   │   ├── schemas/
│   │   ├── config.py
│   │   └── database.py
│   │
│   └── tests/
│
├── rag/
│   ├── ingestion/
│   │   ├── parsers/
│   │   └── chunking/
│   │
│   ├── embeddings/
│   ├── retrieval/
│   ├── generation/
│   ├── orchestration/
│   └── evaluation/
│
├── database/
│   └── migrations/
│
├── frontend/
│
├── workers/
│
├── infrastructure/
│
├── docs/
│   ├── architecture/
│   ├── api/
│   └── evaluation/
│
├── tests/
│
├── compose.yaml
├── pyproject.toml
├── .gitignore
└── README.md
```

---

## Development Environment

Current development environment:

```text
Python 3.12
FastAPI
PostgreSQL 16
pgvector
Docker
pytest
```

The project uses a dedicated Python virtual environment:

```text
.venv/
```

---

## Running the Project

### 1. Activate the virtual environment

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 2. Start PostgreSQL

```powershell
docker compose up -d
```

### 3. Run the test suite

```powershell
pytest
```

### 4. Start the FastAPI backend

```powershell
uvicorn backend.app.main:app --reload
```

The API and frontend are still under active development.

---

## Testing

The project currently contains tests covering:

* API health checks
* Document upload
* PDF parsing
* DOCX parsing
* Text chunking
* Paragraph chunking
* Document-level chunking
* Chunk repository operations
* Embedding generation
* Chunk embedding persistence
* Vector similarity search
* Retrieval relevance filtering
* Evidence context construction
* Evidence service
* Generated answer models
* Generation service
* Generator abstraction

The test suite is intended to grow alongside the RAG pipeline rather than being added only after implementation.

---

## Roadmap

### Phase 1 — RAG Foundation

* [x] Project structure
* [x] FastAPI backend
* [x] PostgreSQL
* [x] pgvector
* [x] Document upload
* [x] PDF/DOCX parsing
* [x] Chunking
* [x] Embeddings
* [x] Vector retrieval
* [x] Retrieval threshold
* [x] Evidence layer
* [x] Generation contract
* [x] Generator abstraction

### Phase 2 — Grounded Generation

* [ ] LLM provider integration
* [ ] Prompt construction
* [ ] Citation-aware generation
* [ ] Citation validation
* [ ] End-to-end query pipeline
* [ ] Query API

### Phase 3 — Advanced Retrieval

* [ ] Hybrid search
* [ ] Reranking
* [ ] Query rewriting
* [ ] Multi-document retrieval
* [ ] Multi-hop reasoning
* [ ] Comparative queries

### Phase 4 — Trust & Evaluation

* [ ] Insufficient-evidence benchmarking
* [ ] Retrieval evaluation dataset
* [ ] Retrieval metrics
* [ ] Groundedness evaluation
* [ ] Citation correctness
* [ ] Contradiction detection
* [ ] Document-version awareness

### Phase 5 — Production Platform

* [ ] Authentication
* [ ] Role-based access control
* [ ] Background workers
* [ ] Redis
* [ ] Observability
* [ ] Audit logging
* [ ] Feedback and analytics
* [ ] Production dashboard
* [ ] CI/CD
* [ ] Deployment

---

## Project Goal

The objective of VeriRAG is to demonstrate how a modern RAG system can be engineered as a **reliable knowledge platform rather than a simple chatbot**.

The final system should be:

* **Grounded** — answers are supported by retrieved evidence
* **Explainable** — users can inspect the sources behind answers
* **Measurable** — retrieval and generation quality can be evaluated
* **Modular** — individual components can evolve independently
* **Secure** — access and enterprise data boundaries are respected
* **Observable** — system behavior can be monitored and audited
* **Production-oriented** — architecture and deployment practices reflect real-world systems

---

## Repository

**GitHub:** `https://github.com/katkarvismaya19-web/VeriRAG`

---

## Development Philosophy

VeriRAG is being built incrementally.

Each major capability is:

1. Designed
2. Implemented
3. Tested
4. Committed
5. Integrated into the larger pipeline

This approach keeps the system maintainable while creating a clear engineering history of how the platform evolves from a basic RAG foundation into a production-oriented knowledge intelligence system.

