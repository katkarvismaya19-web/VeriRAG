# VeriRAG

### Evidence-Grounded Enterprise Knowledge & Decision Intelligence Platform

> **VeriRAG is a production-oriented Retrieval-Augmented Generation (RAG) platform designed to turn enterprise documents into trustworthy, citation-backed answers and measurable knowledge intelligence.**

VeriRAG is being built with a **SaaS-first architecture** for organizations that need to securely ingest internal knowledge, retrieve relevant evidence, generate grounded answers, and measure the quality and reliability of their AI knowledge systems.

The core principle is simple:

> **An AI answer should be traceable to evidence, not just plausible.**

---

# Why VeriRAG?

Enterprise RAG systems have a fundamental problem:

> **Generating an answer is easy. Generating an answer that can be trusted is much harder.**

VeriRAG focuses on the trust layer around RAG:

* Evidence-backed answers
* Source citations
* Insufficient-evidence detection
* Citation validation
* Retrieval quality measurement
* Document-aware retrieval
* Evaluation-driven improvements
* Provider-independent LLM architecture
* Production-oriented separation of concerns
* Future multi-tenant SaaS isolation

The goal is not to build another chatbot.

The goal is to build a **measurable enterprise knowledge infrastructure layer**.

---

# Product Vision

VeriRAG is being designed as a SaaS platform where organizations can create isolated knowledge environments for their teams.

### Target Workflow

```text
Organization
      │
      ├── Users
      │
      ├── Knowledge Bases
      │       │
      │       ├── Documents
      │       │      ├── Versions
      │       │      └── Metadata
      │       │
      │       └── Permissions
      │
      └── Queries
              │
              ▼
        Query Understanding
              │
              ▼
        Hybrid Retrieval
              │
              ▼
           Reranking
              │
              ▼
        Evidence Selection
              │
              ▼
        Grounded Generation
              │
              ▼
      Citation Validation
              │
              ▼
        Trusted Response
              │
              ├── Citations
              ├── Evidence
              └── Quality Signals
```

Future platform capabilities will include:

* Multi-tenant organizations
* Knowledge bases
* Role-based access control
* Document versioning
* Usage analytics
* Evaluation dashboards
* Audit logs
* Retrieval observability
* Feedback loops
* Usage metering
* Subscription and billing infrastructure

---

# Current Engineering Status

| Area                             | Status         |
| -------------------------------- | -------------- |
| Document ingestion               | 🟢 Working     |
| PDF/DOCX parsing                 | 🟢 Working     |
| OCR fallback                     | 🟢 Working     |
| Page-aware parsing               | 🟢 Working     |
| Document chunking                | 🟢 Working     |
| Embeddings                       | 🟢 Working     |
| PostgreSQL + pgvector            | 🟢 Working     |
| Vector retrieval                 | 🟢 Working     |
| Retrieval thresholding           | 🟢 Working     |
| Evidence layer                   | 🟢 Working     |
| Grounded generation architecture | 🟢 Working     |
| LLM provider abstraction         | 🟢 Working     |
| OpenAI provider                  | 🟢 Implemented |
| Citation extraction              | 🟢 Working     |
| Citation validation              | 🟢 Working     |
| Query orchestration              | 🟢 Working     |
| Query API                        | 🟢 Working     |
| Retrieval evaluation             | 🟡 Foundation  |
| Hybrid retrieval                 | 🔵 Planned     |
| Reranking                        | 🔵 Planned     |
| Query rewriting                  | 🔵 Planned     |
| Multi-hop retrieval              | 🔵 Planned     |
| Multi-tenancy                    | 🔵 Planned     |
| Authentication/RBAC              | 🔵 Planned     |
| SaaS dashboard                   | 🔵 Planned     |
| Billing/usage metering           | 🔵 Planned     |
| Production observability         | 🔵 Planned     |

---

# Development Phases

## Phase 1 — RAG Foundation

**Status: 🟢 Complete**

Implemented:

* Python project structure
* FastAPI backend
* PostgreSQL integration
* SQLAlchemy ORM
* Alembic migration foundation
* pgvector integration
* Document upload API
* PDF ingestion
* DOCX ingestion
* OCR fallback for scanned PDFs
* Page-aware document parsing
* Document chunking
* Chunk persistence
* Semantic embeddings
* Vector similarity search
* Retrieval ranking
* Retrieval relevance threshold
* Evidence construction
* Citation-ready evidence context

---

## Phase 2 — Grounded Generation

**Status: 🟢 Complete**

Implemented and tested:

* LLM provider abstraction
* OpenAI provider
* Prompt construction
* Evidence-constrained generation
* Insufficient-evidence handling
* Citation extraction
* Citation → page/section mapping
* Citation validation
* Unsupported citation detection
* Query orchestration
* Structured query responses
* `/api/v1/query` endpoint
* Provider-independent automated tests

Current generation test status:

```text
13 passed
```

### Generation Pipeline

```text
Query
  ↓
Retrieval
  ↓
Evidence Context
  ↓
Prompt Builder
  ↓
LLM Provider
  ↓
Citation Extraction
  ↓
Citation Validation
  ↓
Structured Query Result
```

---

## Phase 3 — Advanced Retrieval

**Status: 🔵 Next**

Planned:

* Hybrid vector + lexical retrieval
* Reciprocal Rank Fusion
* Candidate expansion
* Cross-encoder reranking
* Query rewriting
* Query expansion
* Multi-document retrieval
* Multi-hop retrieval
* Comparative questions
* Retrieval strategy configuration

The important design principle:

> **Every retrieval improvement will be evaluated against a baseline.**

Instead of adding retrieval techniques because they are popular, VeriRAG will measure whether they actually improve retrieval quality.

---

## Phase 4 — Trust & Evaluation

**Status: 🟡 Foundation**

Implemented:

* Retrieval evaluation model
* Recall@K metric
* Retrieval evaluator
* Labeled retrieval cases
* Real-document evaluation
* Evaluation tests

Current evaluation results:

```text
Retrieval metric tests:       4 passed
Evaluator tests:              1 passed
Real report benchmark:        Recall@5 = 1.00
```

The first real benchmark evaluates retrieval against an actual processed internship report.

### Planned Evaluation Capabilities

* Precision@K
* Recall@K
* MRR
* nDCG
* Retrieval threshold analysis
* Retrieval benchmark datasets
* Groundedness evaluation
* Citation correctness
* Citation completeness
* Answer relevance
* Insufficient-evidence evaluation
* Contradiction detection
* Document-version evaluation
* Regression evaluation
* Automated evaluation reports

---

## Phase 5 — SaaS & Production Platform

**Status: 🔵 Planned**

VeriRAG will evolve from a RAG engine into a **multi-tenant enterprise SaaS platform**.

### Multi-Tenancy

```text
Platform
   │
   ├── Organization A
   │     ├── Users
   │     ├── Knowledge Bases
   │     └── Documents
   │
   ├── Organization B
   │     ├── Users
   │     ├── Knowledge Bases
   │     └── Documents
   │
   └── Organization C
         ├── Users
         ├── Knowledge Bases
         └── Documents
```

Planned:

* Organization/tenant isolation
* User authentication
* Role-based access control
* Knowledge-base permissions
* Document-level permissions
* API authentication
* Audit logging
* Document versioning
* Background ingestion workers
* Redis
* Task queues
* Rate limiting
* Usage metering
* Subscription/billing architecture
* Production logging
* Metrics
* Distributed tracing
* Error monitoring
* CI/CD
* Containerized deployment
* Cloud deployment

---

# Core Architecture

VeriRAG deliberately separates the RAG pipeline into independently testable layers.

```text
                    ┌──────────────────┐
                    │    FastAPI API   │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Query Service    │
                    └────────┬─────────┘
                             │
              ┌──────────────┴──────────────┐
              ▼                             ▼
      ┌────────────────┐            ┌────────────────┐
      │ Retrieval      │            │ Generation     │
      │ Service        │            │ Service        │
      └───────┬────────┘            └───────┬────────┘
              │                             │
              ▼                             ▼
      ┌────────────────┐            ┌────────────────┐
      │ PostgreSQL     │            │ LLM Provider   │
      │ + pgvector     │            │ Abstraction    │
      └────────────────┘            └────────────────┘
              │                             │
              └──────────────┬──────────────┘
                             ▼
                    ┌──────────────────┐
                    │ Evidence &       │
                    │ Citation Layer   │
                    └──────────────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Evaluation       │
                    │ Infrastructure   │
                    └──────────────────┘
```

---

# Document Ingestion Pipeline

VeriRAG supports both normal text PDFs and scanned documents.

```text
Upload
  ↓
File Validation
  ↓
Document Persistence
  ↓
PDF / DOCX Parser
  ↓
Native Text Extraction
  │
  └── if insufficient text
          ↓
        OCR
  ↓
Page-Aware Parsed Content
  ↓
Semantic Chunking
  ↓
Chunk Persistence
  ↓
Embedding Generation
  ↓
pgvector
```

## Supported Formats

* PDF
* DOCX

## PDF Processing

Native PDF text extraction is attempted first.

For scanned/image-based pages, VeriRAG automatically falls back to OCR.

This allows the same ingestion pipeline to process both:

* digitally generated PDFs
* scanned documents

---

# Retrieval Pipeline

Current retrieval uses semantic vector search with PostgreSQL + pgvector.

```text
User Query
    ↓
Query Embedding
    ↓
Vector Similarity Search
    ↓
Ranked Candidates
    ↓
Relevance Threshold
    ↓
Evidence Context
```

Each retrieval result contains information such as:

* document ID
* chunk ID
* similarity score
* text
* page number
* section

This metadata becomes the foundation for citation-aware generation.

---

# Evidence-Grounded Generation

VeriRAG does not simply send a user question to an LLM.

The model receives:

```text
USER QUESTION

+

RETRIEVED EVIDENCE

+

GROUNDING INSTRUCTIONS
```

The generation contract instructs the model to:

1. Use only supplied evidence.
2. Avoid unsupported claims.
3. Cite claims using available citation IDs.
4. Never invent citation IDs.
5. Clearly report insufficient evidence.
6. Prefer concise answers.

---

# Citation Integrity

Citation validation is treated as a first-class component.

For example, if retrieved evidence contains:

```text
[1] Employee handbook — page 4
[2] Leave policy — page 5
```

and the model produces:

```text
Employees receive 20 days of annual leave [1].
```

the citation is valid.

If the model produces:

```text
Employees receive 20 days of annual leave [99].
```

VeriRAG detects:

```text
invalid_citation_ids = [99]
is_valid = false
```

Unsupported citations are deliberately **not silently discarded**.

This creates an explicit trust boundary between:

```text
LLM output
      ↓
Citation extraction
      ↓
Citation validation
      ↓
Trust signal
```

---

# Insufficient Evidence

A core VeriRAG principle is:

> **Not knowing is better than confidently hallucinating.**

When retrieval does not provide sufficient evidence, the generation layer can return an explicit insufficient-evidence response rather than inventing an answer.

This behavior will eventually become part of the evaluation framework and SaaS quality metrics.

---

# Evaluation Philosophy

RAG quality is not measured by whether the system "sounds good."

VeriRAG is being built around measurable evaluation.

Example:

```text
                 Baseline
                    │
                    ▼
             Vector Retrieval
                    │
              Recall@5 = X
                    │
                    ▼
             Hybrid Retrieval
                    │
              Recall@5 = Y
                    │
                    ▼
         Hybrid + Reranking
                    │
              Recall@5 = Z
```

This allows architectural decisions to be backed by evidence.

### Evaluation Principle

Every major retrieval or generation improvement should answer:

> **Did the change measurably improve the system?**

---

# Technology Stack

## Backend

* Python
* FastAPI
* Pydantic
* SQLAlchemy
* Alembic

## Data Layer

* PostgreSQL 16
* pgvector
* psycopg

## Document Processing

* pypdf
* python-docx
* Tesseract OCR
* pdf2image
* Pillow

## Embeddings

* Sentence Transformers
* `BAAI/bge-small-en-v1.5`

## Generation

* Provider abstraction
* OpenAI API

## Testing

* pytest
* HTTPX

## Infrastructure

* Docker
* Docker Compose

## Planned Frontend

* Next.js
* TypeScript
* Tailwind CSS

## Planned SaaS Infrastructure

* Redis
* Background workers
* Task queues
* Authentication
* RBAC
* Usage metering
* Observability
* CI/CD
* Cloud deployment

---

# Project Structure

```text
VeriRAG/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── models/
│   │   ├── repositories/
│   │   ├── routes/
│   │   ├── schemas/
│   │   ├── config.py
│   │   ├── database.py
│   │   └── main.py
│   │
│   └── tests/
│
├── rag/
│   ├── ingestion/
│   │   ├── parser/
│   │   └── chunking/
│   │
│   ├── embeddings/
│   ├── retrieval/
│   ├── generation/
│   │   └── llm/
│   │
│   ├── orchestration/
│   └── evaluation/
│
├── database/
│   └── migrations/
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
├── docker-compose.yml
├── pyproject.toml
├── .gitignore
└── README.md
```

---

# Local Development

## 1. Clone

```bash
git clone https://github.com/katkarvismaya19-web/VeriRAG.git
cd VeriRAG
```

## 2. Create the Virtual Environment

```powershell
py -3.12 -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

## 3. Install Dependencies

```powershell
python -m pip install -r requirements.txt
```

## 4. Start PostgreSQL

```powershell
docker compose up -d
```

Verify:

```powershell
docker ps
```

The PostgreSQL container should report a healthy status.

## 5. Run the API

```powershell
uvicorn backend.app.main:app --reload
```

API:

```text
http://127.0.0.1:8000
```

Swagger:

```text
http://127.0.0.1:8000/docs
```

---

# Testing

Run the complete test suite:

```powershell
pytest
```

Run generation tests:

```powershell
pytest rag\generation -q
```

Run evaluation tests:

```powershell
pytest rag\evaluation -q
```

Run the real retrieval benchmark:

```powershell
pytest rag\evaluation\test_real_report_evaluation.py -q -s
```

---

# API

## Health

```http
GET /health
```

Example:

```json
{
  "status": "healthy",
  "service": "verirag-api",
  "version": "0.1.0"
}
```

## Upload Document

```http
POST /api/v1/documents/
```

Supported:

```text
.pdf
.docx
```

## Query Documents

```http
POST /api/v1/query
```

Example request:

```json
{
  "query": "What is the internship project about?",
  "limit": 5
}
```

The response includes:

* generated answer
* citations
* evidence status
* citation validation status
* invalid citation IDs when applicable

---

# Security & SaaS Principles

Security is being treated as an architectural concern rather than a final feature.

Planned SaaS security boundaries include:

* Tenant isolation
* Authentication
* Authorization
* Role-based access control
* Knowledge-base permissions
* Document permissions
* API key management
* Secret management
* Audit logs
* Rate limiting
* Usage controls
* Secure document storage
* Data lifecycle management

A fundamental platform invariant will be:

> **No tenant should be able to retrieve another tenant's documents, chunks, embeddings, or evidence.**

---

# Engineering Principles

VeriRAG is being developed around several principles.

### 1. Evidence Over Confidence

A confident answer without evidence is not trustworthy.

### 2. Measure Before Optimizing

Retrieval changes should be evaluated against measurable baselines.

### 3. Separation of Concerns

Retrieval, generation, evaluation, storage, and API layers remain independently testable.

### 4. Provider Independence

LLM providers should be replaceable without rewriting the RAG pipeline.

### 5. Fail Explicitly

Unsupported citations and insufficient evidence should be surfaced rather than hidden.

### 6. SaaS-First Architecture

Tenant isolation, permissions, observability, and scalability are considered during architecture design—not bolted on at the end.

### 7. Production Over Demo

The objective is a system that can evolve from a development project into a deployable product.

### 8. Evaluation-Driven Development

Major changes should be accompanied by tests and measurable evaluation wherever possible.

---

# Roadmap

```text
Phase 1  ████████████████████  RAG Foundation             DONE
Phase 2  ████████████████████  Grounded Generation        DONE
Phase 3  ███░░░░░░░░░░░░░░░░  Advanced Retrieval         NEXT
Phase 4  ████░░░░░░░░░░░░░░░  Trust & Evaluation         FOUNDATION
Phase 5  ██░░░░░░░░░░░░░░░░░  SaaS Production Platform   PLANNED
```

## Near-Term Priorities

1. Build a larger retrieval benchmark
2. Measure the current vector-search baseline
3. Implement hybrid retrieval
4. Measure hybrid vs. vector baseline
5. Add reranking
6. Measure reranking impact
7. Add query rewriting
8. Build multi-document retrieval
9. Build multi-hop retrieval
10. Expand evaluation infrastructure
11. Introduce tenant-aware data architecture
12. Build authentication and RBAC
13. Build the SaaS API layer
14. Build the production dashboard
15. Add usage metering and billing infrastructure
16. Add production observability
17. Deploy the platform

---

# Long-Term Product

The long-term goal is for VeriRAG to become an **enterprise AI knowledge platform**, rather than simply a RAG API.

Potential use cases include:

* Internal company knowledge assistants
* HR policy assistants
* Technical documentation search
* SOP and operations assistants
* Compliance knowledge systems
* Product knowledge assistants
* Engineering documentation
* Financial/report analysis
* Research knowledge systems
* Customer-support knowledge systems

The platform should allow an organization to connect its knowledge and ask:

> **"What does our information actually say?"**

while providing enough evidence and evaluation signals to determine:

> **"Can we trust the answer?"**

---

# Product Quality Goals

As VeriRAG evolves into a SaaS product, the platform will be evaluated across multiple dimensions:

```text
                    VeriRAG Quality
                          │
        ┌─────────────────┼─────────────────┐
        ▼                 ▼                 ▼
    Retrieval         Generation         Trust
    Quality             Quality           Quality
        │                 │                 │
   Recall@K           Relevance        Citations
   MRR                Groundedness     Evidence
   nDCG               Completeness     Contradictions
   Latency            Consistency      Abstention
        │                 │                 │
        └─────────────────┼─────────────────┘
                          ▼
                  Product Reliability
```

Long-term SaaS metrics will also include:

* Query latency
* Retrieval latency
* Ingestion latency
* Token usage
* Cost per query
* Documents processed
* Queries per organization
* Error rate
* User feedback
* Retrieval quality
* Answer quality
* Citation validity

---

# Current Development Philosophy

VeriRAG is intentionally being built incrementally.

Each major capability should follow:

```text
Architecture
     ↓
Implementation
     ↓
Tests
     ↓
Evaluation
     ↓
Measurement
     ↓
Optimization
```

The objective is to build a system that can withstand both:

* **real-world product requirements**
* **deep technical engineering review**

---

# Project Status

VeriRAG is currently in the transition from a **RAG foundation** toward an **evaluation-driven advanced retrieval platform**.

The core ingestion, retrieval, evidence, generation, citation, and query orchestration foundations are implemented.

The next major engineering milestone is to establish a broader retrieval benchmark and use it to drive the design of hybrid retrieval and reranking.

---

## Author

**Vismaya Katkar**

Computer Engineering

GitHub:

`https://github.com/katkarvismaya19-web/VeriRAG`
