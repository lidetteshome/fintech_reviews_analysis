# Task 3: Oracle DB Insertion

This task focuses on storing the processed data in an **Oracle XE database**, simulating a real-world enterprise data pipeline.

---

## Objectives

- Setup Oracle XE on Docker (macOS)
- Create two relational tables:
  - `Banks`
  - `Reviews`
- Insert cleaned reviews into Oracle using `oracledb`

---

## Tables

### Banks
| Column | Type |
|--------|------|
| id | INT, PK |
| name | VARCHAR |

### Reviews
| Column | Type |
|--------|------|
| id | INT, PK |
| bank_id | FK to Banks |
| review_text | CLOB |
| rating | INT |
| review_date | DATE |
| source | VARCHAR |
| sentiment_label | VARCHAR |
| sentiment_score | FLOAT |
| themes | VARCHAR |

---

## Requirements

- Docker + Oracle XE image
- `oracledb` (Python driver)

---

## Usage

See: `notebooks/task-3/task_3_runner.ipynb`
