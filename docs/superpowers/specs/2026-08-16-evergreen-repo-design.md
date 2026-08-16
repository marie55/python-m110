# Design: Evergreen, Slides-Grounded M110 Repository

**Date**: 2026-08-16
**Status**: Approved design — implementation plan to follow
**Author**: Mohammad Al-Marie (with Claude)

---

## 1. Context

The repository was built to support a live M110 Python Programming course at Arab
Open University, Amman, during Spring 2024-2025. It assumes a semester in
progress: a start date, a weekly cadence, Sunday lectures, Tuesday labs, and an
instructor answering email.

None of that is true anymore. The course is no longer taught live. The repository
stays public to serve M110 students who find it.

Two things changed in the working tree and triggered this redesign:

1. All 12 official slide decks were converted from PPTX to plain text
   (`*.pptx.txt`, ~190 KB total). These are untracked.
2. The intent shifted from "companion to my live course" to "self-contained,
   evergreen study resource driven by an AI assistant."

### What the repository actually contains today

An audit found the published content far thinner than the README advertises:

| README claim ([README.md:518-524](../../../README.md)) | Reality in `HEAD` |
|---|---|
| 13 weeks of structured content | 1 chapter (Algorithms) |
| 50+ code examples | 10 `.py` files |
| 100+ exercises with solutions | 1 exercise, 1 solution |
| 3 lab sessions with starter code | 1 lab README — **0 bytes** |
| Project templates | 1 guidelines doc — **0 bytes** |
| Exam prep materials | 2 files — **both 0 bytes** |

`labs/`, `projects/` and `assessments/` contain nothing but empty files, in the
working tree and in `HEAD` alike. The `week-02` … `week-13` directories are empty
and therefore do not exist on GitHub at all — git does not track empty
directories. A student cloning today reads a promise of a full course and finds a
single chapter.

By contrast, `resources/` is genuinely complete: 26 substantive guides covering
setup, Git, VS Code, Python reference, cheatsheets and video curation. It is the
strongest asset in the repository and is not touched by this work.

### Latent structural problem

Directory names use week numbers that do not match the chapter numbers students
see on slides and exams:

| Directory | Actual chapter |
|---|---|
| `week-05-lists-tuples` | Chapter 7 |
| `week-07-functions` | Chapter 5 |
| `week-08-files-exceptions` | Chapter 6 |
| `week-11-gui` | Chapter 13 |

`slides-official/` already uses chapter naming, so the repository contradicts
itself. Removing the week cadence removes this mismatch at no extra cost.

---

## 2. Goals

1. Remove every dependency on a calendar, semester or current date.
2. Make the extracted slide text the assistant's primary grounding source.
3. Make the repository's claims true — advertise only what exists.
4. Reduce the repository to one numbering scheme: the official chapter numbers.
5. Ensure a student's first commands (`clone`, `pip install`, `/laila`) all work.

## 3. Non-goals

- Authoring lecture notes, examples or exercises for chapters 2-13. The assistant
  generates these on demand; the repository does not pre-ship them.
- Rewriting `resources/` content beyond fixing stale paths and schedule
  references.
- Modifying the official slide decks, or cleaning noise out of the extracted text.
- Any change to `student-playground/`'s gitignore behavior.

---

## 4. Decisions

These four were decided during design and are settled.

### D1 — Chapter-based structure

Content directories are renamed from `week-NN-topic` to `chapter-NN-topic`,
mirroring `slides-official/` exactly. Self-study directories keep `ssN-topic`.

*Why*: one numbering scheme repo-wide, matching how exams and slides refer to
material. The suggested learning order lives in the README and
`.claude/course-map.yaml` as data, not encoded in folder names — which is what
allows the order to differ from the numbering without confusing anyone.

### D2 — Assistant-generated content, not pre-authored

The repository ships: official slides (PDF + PPTX + text), the `resources/`
guides, Dr. Laila, and Chapter 1 as a worked sample of good output. Everything
else is generated on demand into `student-playground/`.

*Why*: it is honest, it needs no maintenance, and it is exactly what the slide
text conversion makes possible. Pre-authoring 12 chapters would create ~200 files
requiring ongoing slide-alignment review, for a course the author no longer
teaches.

### D3 — Credited author, course archived

Mohammad Al-Marie's name, bio and teaching philosophy stay — they give the
material its authority. A banner states the course is no longer taught live. The
AOU email, office hours, Teams/Discord placeholder and lecture schedule are
removed. Dr. Laila is reframed from "the other teacher" to the primary guide.

*Why*: preserves credibility without setting an expectation of personal support.

### D4 — Slide text ships unmodified

The 12 `*.pptx.txt` files are committed exactly as converted, keeping their
`.pptx.txt` double extension.

*Why*: the double extension documents provenance. Cleaning the `AOU- M110` and
page-number noise would break the "unmodified official source" guarantee for a
problem the assistant can simply ignore.

---

## 5. Extraction fidelity — a constraint the design must respect

Verified against the converted files. The text is faithful for prose and
definitions, but three things are damaged, and the assistant's rules depend on
knowing this:

1. **Code indentation is partly flattened.** In
   `chapter-04-repetition/…pptx.txt`, `print(num)` appears at column 0 under
   `for num in [0, 1, 2, 3, 4]:` — syntactically wrong Python.
2. **Smart quotes are mangled.** `print('Hello’, i)` — mismatched quote
   characters that will not parse.
3. **Figures are absent entirely.** The text reads "The below Figure shows the
   logic of a while loop" with no figure. Chapter 1 is almost entirely
   flowcharts.

**Consequence, binding on the assistant spec**: extracted text grounds
definitions, explanations and prose. It must never be presented as
verbatim-correct code, and any answer depending on a diagram must direct the
student to the PDF.

---

## 6. Target structure

```
python-m110/
├── slides-official/                    # SOURCE OF TRUTH — location unchanged
│   ├── README.md                       # NEW: chapter index + fidelity caveats
│   ├── chapter-01-algorithms/
│   │   ├── Meeting1-Algorithms-s.pdf       # figures & flowcharts live here
│   │   ├── Meeting1-Algorithms-s.pptx
│   │   └── Meeting1-Algorithms-s.pptx.txt  # NEW — what Dr. Laila reads
│   ├── chapter-02-fundamentals/
│   ├── chapter-03-decision-structures/
│   ├── chapter-04-repetition/
│   ├── chapter-05-functions/
│   ├── chapter-06-files-exceptions/
│   ├── chapter-07-lists-tuples/
│   ├── chapter-10-oop/
│   ├── chapter-13-gui/
│   ├── ss1-turtle-graphics/
│   ├── ss2-recursion/
│   └── ss3-dictionaries-sets/
├── lectures/
│   └── chapter-01-algorithms/          # renamed; the one worked sample
├── code-examples/
│   ├── chapter-01-algorithms/          # renamed
│   └── chapter-02-fundamentals/        # NEW — 3 stray .py files moved here
├── exercises/
│   └── chapter-01-algorithms/          # renamed
├── resources/                          # untouched except stale-path sweep
├── student-contributions/              # kept, reframed as open contributions
├── student-playground/                 # gitignored workspace; unchanged
├── tools/
│   └── extract_slides.py               # NEW — reproduces the .txt conversion
├── docs/superpowers/specs/             # this document
├── .claude/
│   ├── agents/learning-assistant.md    # rewritten
│   ├── commands/laila.md               # unchanged
│   ├── course-map.yaml                 # NEW — replaces course-calendar.yaml
│   ├── README.md                       # updated
│   └── DR-LAILA-SETUP.md               # updated
├── .github/chatmodes/
│   └── learning-assistant.chatmode.md  # rewritten to match the agent
├── CLAUDE.md                           # gitignored; calendar section replaced
├── HOW-TO-USE-DR-LAILA.md              # updated
├── README.md                           # rewritten
├── requirements.txt                    # slimmed
└── LICENSE
```

**Removed**: `labs/`, `projects/`, `assessments/` (empty files only),
`.claude/course-calendar.yaml`, `lectures/week-02-fundamentals/` (contents
moved), and all empty `week-NN-*` directories.

---

## 7. Change inventory

### 7.1 Track the slide text (12 files)

Commit all `slides-official/*/*.pptx.txt` unmodified. Verified not matched by any
`.gitignore` rule. This is a standalone first commit — it is the enabling change.

The `slides-official/M110-Study Calendar-SP24-25.xlsx` stays untracked; it is
matched by the `*.xlsx` ignore rule and is semester-specific by nature.

### 7.2 Directory renames (`git mv`, preserving history)

| From | To |
|---|---|
| `lectures/week-01-algorithms/` | `lectures/chapter-01-algorithms/` |
| `code-examples/week-01-algorithms/` | `code-examples/chapter-01-algorithms/` |
| `exercises/week-01/` | `exercises/chapter-01-algorithms/` |
| `lectures/week-02-fundamentals/*.py` | `code-examples/chapter-02-fundamentals/` |

The three files moved out of `lectures/week-02-fundamentals/`
(`data_types.py`, `simple_calculator.py`, `variables_demo.py`) are runnable code
examples that were misfiled under `lectures/`. Moving them gives Chapter 2 real
content.

### 7.3 New file — `slides-official/README.md`

Bilingual (EN/AR). Contents:

- Table: chapter number → directory → topic → slide deck filename.
- Which file to use when: PDF for figures and reading, PPTX for the original,
  `.txt` for AI assistants and text search.
- The three fidelity caveats from §5, stated plainly for students.
- Attribution: slides are the copyright of Arab Open University; this repository
  is unaffiliated and redistributes them for student study.

### 7.4 New file — `.claude/course-map.yaml`

Replaces `course-calendar.yaml`. Contains no dates. Schema:

```yaml
course:
  code: M110
  name: Python Programming
  institution: Arab Open University (AOU) - Amman
  status: archived        # course no longer taught live

chapters:
  - number: 1
    id: chapter-01-algorithms
    topic: "Algorithms: Flowcharts & Pseudocodes"
    slides_dir: slides-official/chapter-01-algorithms
    slides_text: "slides-official/chapter-01-algorithms/Meeting1-Algorithms-s.pptx.txt"
    slides_pdf: "slides-official/chapter-01-algorithms/Meeting1-Algorithms-s.pdf"
    has_figures: true     # answers requiring diagrams must cite the PDF
    # ... one entry per chapter: 1,2,3,4,5,6,7,10,13

self_study:
  - id: ss1-turtle-graphics
    topic: "Turtle Graphics"
    # ... same fields

assessments:              # coverage only — no weightings, no dates
  - id: mta
    name: "Mid-Term Assessment"
    covers: "through Collection Data Types (Ch 1-4, 7)"
  - id: tma
    name: "Tutor-Marked Assignment (Lab Test)"
    covers: "MTA material plus SS1, SS2, SS3"
  - id: final
    name: "Final Exam"
    covers: "all regular chapters; excludes self-study topics"

learning_path:            # suggested order — deliberately differs from numbering
  - chapter-01-algorithms
  - chapter-02-fundamentals
  - chapter-03-decision-structures
  - chapter-04-repetition
  - ss1-turtle-graphics        # visual reinforcement of loops
  - chapter-07-lists-tuples
  - ss3-dictionaries-sets      # natural follow-on from collections
  - chapter-05-functions
  - ss2-recursion              # requires functions
  - chapter-06-files-exceptions
  - chapter-10-oop
  - chapter-13-gui
```

The learning path preserves the original teaching sequence (collections before
functions), which was a deliberate pedagogical choice, with the three self-study
topics slotted where they reinforce what precedes them.

Exact slide filenames must be copied verbatim from disk; several contain spaces
and one (`Meeting5 Collection Data Types-s .pptx.txt`) contains a space before
the extension.

### 7.5 Rewrite — `.claude/agents/learning-assistant.md`

**Remove**:
- The entire "Time-Aware Behavior" section ([lines 68-99](../../../.claude/agents/learning-assistant.md)) including the
  `current_week = floor((today - course_start) / 7) + 1` algorithm.
- The "Startup Sequence" week calculation and week-range greeting template.
- Day-of-week starter questions (After Sunday Lecture / Tuesday Lab / Mid-Week).
- Lab-week and revision-week branches.
- The `PDF → PPTX → install python-pptx` cascade.
- Course dates, semester, and schedule from "Course Context".

**Add**:
- *Chapter-aware startup*: greet, then ask which chapter or topic the student is
  working on — or infer it from their question or open file. Offer the learning
  path from `course-map.yaml` for students who don't know where to start.
- *Slide grounding protocol*: read `slides_text` for the relevant chapter; cite
  chapter number and slide topic; state plainly when the slides do not cover
  something rather than inventing coverage.
- *Fidelity rules* (from §5): never reproduce extracted code as
  verbatim-official — re-derive and verify it runs; when an answer depends on a
  figure or flowchart, direct the student to `slides_pdf`.
- *Role change*: primary guide. Every fallback of the form "ask Mohammad in the
  lecture" or "your instructor will cover this" is replaced with something she
  can do herself.

**Keep unchanged**: Socratic teaching style, bilingual EN/AR support, the
no-spoon-feeding rules for graded work, writes-only-to-`student-playground/`,
end-of-response follow-up questions, and the "official slides are sacred"
read-only constraint.

### 7.6 Rewrite — `.github/chatmodes/learning-assistant.chatmode.md`

Same changes as §7.5, in the Copilot chatmode format. The two files must not
diverge in behavior; the embedded course data block is replaced with the same
chapter map.

### 7.7 Rewrite — `README.md`

Structure, bilingual throughout:

1. **Archived banner** — course no longer taught live; materials and Dr. Laila
   remain, free, for any M110 student.
2. **What this is** — official AOU slides plus an AI study guide that teaches
   from them.
3. **Start here** — three steps: clone, set up Python/VS Code, run `/laila`.
4. **The learning path** — chapter-order table, no dates, no week numbers.
5. **How Dr. Laila works** — what she does, what she won't do (graded work),
   which extension to install, and that she writes to `student-playground/`.
6. **What's in the repository** — accurate map, no inflated counts.
7. **Assessments** — which chapters MTA, TMA and the final exam each cover,
   sourced from `course-map.yaml`. Coverage only: the grade weightings and dates
   applied to one specific offering and are dropped.
8. **Built by** — bio and teaching philosophy retained; no email, no office
   hours, no Teams/Discord, no schedule.
9. **License and attribution** — MIT for repository content; official slides are
   AOU copyright; repository is unaffiliated with AOU.

**Removed**: "Current Week" block, dated 13-week syllabus, "Weekly Learning Flow"
(Sunday/Monday-Wednesday/Tuesday), Schedule section, "Mohammad
Provides: live lectures / grading / assessment", Getting Help contact block, the
Semester badge, and all inflated resource counts.

### 7.8 Rewrite — `requirements.txt`

From 40+ packages pinned to 2023 versions down to what M110 actually needs.
`numpy==1.26.2` and `matplotlib==3.8.2` cannot build on current Python, so
`pip install -r requirements.txt` — step 3 of the setup guide — fails outright
today.

M110 is a standard-library course: `turtle` and `tkinter` ship with Python. The
new file contains `Pillow` (images in Tkinter GUIs, Chapter 13) with a lower
bound and no upper pin, plus comments stating that everything else in the course
is standard library. `python-pptx` is listed separately as an optional
development dependency for `tools/extract_slides.py`.

### 7.9 New file — `tools/extract_slides.py`

~30 lines using `python-pptx`. Walks `slides-official/*/` , extracts text from
each `.pptx` and writes a sibling `.pptx.txt`. Bilingual docstring; PEP 8;
follows the repository's own code-example standards, since students may read it.

Its purpose is provenance and reproducibility if the slides are ever replaced —
not routine use.

### 7.10 Documentation sweep

Roughly 20 files under `resources/`, plus `HOW-TO-USE-DR-LAILA.md`,
`.claude/README.md`, `.claude/DR-LAILA-SETUP.md`, `student-playground/README.md`
and `student-contributions/README.md`, contain stale `week-XX` paths, week
numbers, or references to lectures, labs and office hours.

Rules for the sweep:

- Path references (`code-examples/week-01-algorithms`) → new chapter paths.
- Week numbers used as topic labels ("Week 5: Collection Data Types") → chapter
  numbers.
- References to attending lectures/labs, submitting to LMS, or contacting the
  instructor → removed or redirected to Dr. Laila.
- `resources/video-tutorials/video-tutorials-guide.md` has per-week sections —
  relabel to chapters; the curated video links themselves are unaffected.
- `student-contributions/README.md` — reframe from "showcase for my class" to
  open contributions via pull request. Remove deadlines and grading references.

### 7.11 Update — `CLAUDE.md` (gitignored, instructor-private)

Replace the "Course Calendar" week list with the chapter map, drop the semester
line, and update the repository-structure section and directory-naming guidance
to match §6. Keeps the private authoring guide from contradicting the repository.

---

## 8. Execution order

Each step is a separate commit, in this order:

1. Track the 12 slide text files, unmodified (§7.1).
2. `git mv` directory renames and the Chapter 2 file moves (§7.2).
3. Delete `labs/`, `projects/`, `assessments/`, `.claude/course-calendar.yaml`.
4. Add `.claude/course-map.yaml` and `slides-official/README.md` (§7.3, §7.4).
5. Rewrite the assistant: agent + chatmode (§7.5, §7.6).
6. Rewrite `README.md` (§7.7).
7. Slim `requirements.txt`; add `tools/extract_slides.py` (§7.8, §7.9).
8. Documentation sweep (§7.10) and `CLAUDE.md` update (§7.11).

Steps 1-3 are mechanical and independently verifiable. Steps 5-6 carry the
substance. Step 8 is cleanup that depends on every path decision above being
final.

---

## 9. Verification

Work is not complete until all five pass, with output shown:

1. **No stale paths** — `grep -rn "week-[0-9]" --include='*.md' --include='*.yaml'`
   over tracked files returns nothing outside `docs/superpowers/specs/`.
2. **No date logic** — no occurrence of `course_start`, `current_week`,
   `October 12`, or `Spring 2024` in `.claude/` or `.github/`.
3. **Links resolve** — every relative markdown link in tracked `.md` files points
   at a path that exists.
4. **Setup works** — `python3 -m venv` a clean environment and
   `pip install -r requirements.txt` succeeds.
5. **Assistant cold-start** — invoking `/laila` produces a chapter-aware greeting
   with no date arithmetic, and correctly reads a chapter's `.txt` when asked
   about it.

---

## 10. Risks

**Slide redistribution.** The repository publishes AOU's copyrighted decks, and
the text conversion makes that content machine-readable and search-indexable in a
way the PDFs were not. This is new in reach, not in kind — the PDFs and PPTXs
were already published. Mitigation: explicit attribution and an unaffiliated
notice in both `README.md` and `slides-official/README.md`. Reversible: if the
reach is unwanted, the `.txt` files can be gitignored and kept local, at the cost
of the assistant's grounding.

**Assistant quality is now the product.** With no pre-authored content for
chapters 2-13, a weak Dr. Laila means a weak repository. Chapter 1 remains as a
worked sample precisely so her output has a standard to match. Mitigated by
verification step 5.

**Fidelity errors reaching students.** If the assistant reproduces damaged code
from the extracted text, students get code that does not run. Addressed directly
by the §7.5 fidelity rules, and this is the single most important behavior to
test in verification step 5.
