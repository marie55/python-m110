# Evergreen Slides-Grounded Repository — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Convert the M110 course repository from a semester-bound companion into an evergreen, chapter-based self-study resource where the official slide text grounds an AI assistant.

**Architecture:** Official slides (PDF + PPTX + extracted `.txt`) are the source of truth. `.claude/course-map.yaml` is the single data file mapping chapters to their slide assets. Dr. Laila reads that map, grounds answers in the extracted text, and generates content on demand into `student-playground/`. No pre-authored content for chapters 2-13; no calendar anywhere.

**Tech Stack:** Markdown, YAML, Python 3.9+ (standard library plus Pillow), `python-pptx` (optional dev tool only), git.

**Spec:** [docs/superpowers/specs/2026-08-16-evergreen-repo-design.md](../specs/2026-08-16-evergreen-repo-design.md)

## Global Constraints

- **Commit messages carry no AI attribution trailers.** No `Co-Authored-By: Claude`, no "Generated with Claude Code". Subject and body only.
- **Never modify anything under `slides-official/`** except adding `slides-official/README.md`. The decks and the extracted `.txt` files ship byte-for-byte unmodified (spec D4).
- **Chapter numbering only.** No directory, heading, or path may use `week-NN` or "Week N" after Task 9. Chapter numbers are 1, 2, 3, 4, 5, 6, 7, 10, 13 plus `ss1`, `ss2`, `ss3`.
- **Bilingual EN/AR** for every student-facing document: English block immediately followed by its Arabic translation, per `CLAUDE.md`.
- **Python code follows PEP 8** with bilingual comments and a trailing "Example Runs" docstring, matching the house style in `code-examples/chapter-01-algorithms/02_decision_even_odd.py`.
- **Preserve git history on moves** — always `git mv`, never delete-and-recreate.
- **Python floor is 3.9.** No dependency may be pinned with `==`; use `>=` lower bounds only.
- **No dates, no schedule, no instructor contact** in any tracked file. The one exception is the illustrative student email `ahmed.hassan@student.aou.edu.jo` in `resources/setup-guides/03-git-installation.md:291`, which is a `git config` example and must stay.

## Verification Toolkit

Four commands used repeatedly below. Run from the repository root.

**V1 — no week references in tracked files:**
```bash
git ls-files -z | grep -zv '^docs/superpowers/' | xargs -0 grep -n -E "week-[0-9]{2}|Week [0-9]+" 2>/dev/null
```
Expected after Task 9: no output.

**V2 — no date or schedule logic:**
```bash
git ls-files -z | grep -zv '^docs/superpowers/' | xargs -0 grep -n -E "course_start|current_week|October 12|Spring 202[0-9]|Tuseday|office hours|Office Hours|aou\.edu\.jo" 2>/dev/null
```
Expected after Task 9: only `resources/setup-guides/03-git-installation.md:291` (the illustrative student email).

**V3 — every relative markdown link resolves:**
```bash
git ls-files '*.md' | grep -v '^docs/' | while read -r f; do
  d=$(dirname "$f")
  grep -o '](\([^)#][^)]*\))' "$f" 2>/dev/null | sed 's/^](//;s/)$//' | while read -r l; do
    case "$l" in http*|mailto*|"#"*) continue;; esac
    [ -e "$d/$l" ] || [ -e "$l" ] || echo "BROKEN  $f -> $l"
  done
done
```
Expected after Task 9: no output.

**V4 — course map points only at files that exist:**
```bash
python3 -c "
import sys, pathlib, re
text = pathlib.Path('.claude/course-map.yaml').read_text(encoding='utf-8')
paths = re.findall(r'\"(slides-official/[^\"]+)\"', text)
missing = [p for p in paths if not pathlib.Path(p).exists()]
print('MISSING:', missing) if missing else print(f'OK - all {len(paths)} slide paths exist')
sys.exit(1 if missing else 0)
"
```
Expected after Task 3: `OK - all 36 slide paths exist`.

---

## File Structure

| File | Responsibility |
|---|---|
| `slides-official/*/*.pptx.txt` (12) | Extracted slide text — the assistant's grounding source. Never edited. |
| `slides-official/README.md` | Chapter index, which format to use when, fidelity caveats, AOU attribution. |
| `.claude/course-map.yaml` | The single source of chapter → directory → slide-asset mapping, learning path, assessment coverage. Everything else reads it. |
| `.claude/agents/learning-assistant.md` | Dr. Laila's behavior for Claude Code. |
| `.github/chatmodes/learning-assistant.chatmode.md` | Same behavior for GitHub Copilot. Must not diverge. |
| `README.md` | Student entry point. Archived banner, start-here, learning path, repo map, attribution. |
| `requirements.txt` | Minimal install that actually succeeds. |
| `tools/extract_slides.py` | Reproduces the `.txt` conversion. Provenance, not routine use. |
| `code-examples/chapter-NN-*/` | Runnable examples. Chapter 1 is the worked sample; Chapter 2 holds the moved files plus hello-world. |

**Deleted:** `labs/`, `projects/`, `assessments/`, `.claude/course-calendar.yaml`, all empty `week-NN-*` directories.

---

## Task 1: Track the extracted slide text

The enabling change, isolated so it is trivially reviewable and revertible.

**Files:**
- Add to git (12, unmodified): `slides-official/*/*.pptx.txt`

**Interfaces:**
- Produces: 12 tracked text files at the exact paths Task 3's `course-map.yaml` will reference.

- [ ] **Step 1: Confirm all 12 files are present and unignored**

```bash
ls slides-official/*/*.pptx.txt | wc -l          # expect: 12
git check-ignore -v slides-official/*/*.pptx.txt # expect: no output, exit 1
```

- [ ] **Step 2: Record checksums before staging**

```bash
shasum -a 256 slides-official/*/*.pptx.txt > /tmp/slides-before.sha
cat /tmp/slides-before.sha
```

- [ ] **Step 3: Stage and verify nothing was altered**

```bash
git add slides-official
git status --short slides-official     # expect: 12 lines, all "A "
shasum -a 256 -c /tmp/slides-before.sha  # expect: 12x OK
```

- [ ] **Step 4: Confirm the untracked xlsx stays out**

```bash
git status --short slides-official | grep -i xlsx   # expect: no output
```
`M110-Study Calendar-SP24-25.xlsx` is semester-specific and matched by the `*.xlsx` ignore rule. It must not be committed.

- [ ] **Step 5: Commit**

```bash
git commit -m "slides: track extracted text of all 12 official decks

Converted from the official PPTX decks and committed unmodified. These let
AI assistants and text search read the official slides directly.

Figures, flowcharts and diagrams are images and do not survive extraction --
the PDFs remain the visual source of truth."
```

---

## Task 2: Chapter-based structure

**Files:**
- Rename: `lectures/week-01-algorithms/` → `lectures/chapter-01-algorithms/`
- Rename: `code-examples/week-01-algorithms/` → `code-examples/chapter-01-algorithms/`
- Rename: `exercises/week-01/` → `exercises/chapter-01-algorithms/`
- Move: `lectures/week-02-fundamentals/*.py` → `code-examples/chapter-02-fundamentals/`
- Create: `code-examples/chapter-02-fundamentals/01_hello_world.py`
- Modify: `lectures/chapter-01-algorithms/lecture-notes.md` (broken slides path)
- Delete: `labs/`, `projects/`, `assessments/`

**Interfaces:**
- Produces: the chapter paths that Tasks 3, 6, 8 and 9 link to.

- [ ] **Step 1: Confirm the deleted directories hold nothing but empty files**

```bash
find labs projects assessments -type f -exec sh -c 'printf "%s %s\n" "$(wc -c < "$1")" "$1"' _ {} \;
```
Expected: four files, all `0` bytes. If any file is non-empty, **stop** — the spec's premise was that they are empty; report it instead of deleting.

- [ ] **Step 2: Rename the three chapter-1 directories**

```bash
git mv lectures/week-01-algorithms lectures/chapter-01-algorithms
git mv code-examples/week-01-algorithms code-examples/chapter-01-algorithms
git mv exercises/week-01 exercises/chapter-01-algorithms
```

- [ ] **Step 3: Move the misfiled Chapter 2 code examples**

The three `.py` files under `lectures/week-02-fundamentals/` are runnable examples, not lecture notes.

```bash
mkdir -p code-examples/chapter-02-fundamentals
git mv lectures/week-02-fundamentals/data_types.py        code-examples/chapter-02-fundamentals/
git mv lectures/week-02-fundamentals/simple_calculator.py code-examples/chapter-02-fundamentals/
git mv lectures/week-02-fundamentals/variables_demo.py    code-examples/chapter-02-fundamentals/
rmdir lectures/week-02-fundamentals
```

- [ ] **Step 4: Verify history survived the moves**

```bash
git log --follow --oneline -- code-examples/chapter-01-algorithms/02_decision_even_odd.py
```
Expected: at least one commit predating this branch. If empty, the move broke history — redo with `git mv`.

- [ ] **Step 5: Create the missing hello-world example**

`resources/setup-guides/07-running-first-program.md` — the primary onboarding guide — instructs students to open and run `01_hello_world.py` in ten places. The file has never existed. Create it, matching the house style exactly.

```python
"""
M110 - Python Programming
Chapter 2: Fundamentals of Python Programming
Topic: Your First Program
الفصل 2: أساسيات برمجة بايثون
الموضوع: برنامجك الأول

This is the traditional first program every programmer writes.
هذا هو البرنامج الأول التقليدي الذي يكتبه كل مبرمج.

It demonstrates the print() function, which displays text on the screen.
يوضح دالة print() التي تعرض النص على الشاشة.
"""

# Display a greeting / عرض تحية
print("Hello, World!")
print("مرحباً بالعالم!")

# Display a message about the course / عرض رسالة عن المقرر
print("Welcome to M110 - Python Programming")
print("أهلاً بك في M110 - برمجة بايثون")

"""
Example Run / مثال على التشغيل:

Hello, World!
مرحباً بالعالم!
Welcome to M110 - Python Programming
أهلاً بك في M110 - برمجة بايثون

Explanation / الشرح:
- print() displays whatever you put inside the parentheses
  دالة print() تعرض ما تضعه داخل الأقواس
- Text must be wrapped in quotes " " / النص يجب أن يكون داخل علامات اقتباس
- Each print() starts a new line / كل print() تبدأ سطراً جديداً

Try it yourself / جرّب بنفسك:
Change the text inside the quotes to your own name, then run the file again.
غيّر النص داخل علامات الاقتباس إلى اسمك، ثم شغّل الملف مرة أخرى.
"""
```

- [ ] **Step 6: Run it to confirm it works**

```bash
python3 code-examples/chapter-02-fundamentals/01_hello_world.py
```
Expected: four lines of output, no traceback.

- [ ] **Step 7: Fix the pre-existing broken slides link**

`lectures/chapter-01-algorithms/lecture-notes.md` links to `../../slides-official/week-01-algorithms/Meeting1-Algorithms-s.pdf`. That directory has never existed — `slides-official/` has always used chapter naming.

Replace `../../slides-official/week-01-algorithms/` with `../../slides-official/chapter-01-algorithms/` in that file.

- [ ] **Step 8: Delete the empty scaffolding**

```bash
git rm -r labs projects assessments
```

- [ ] **Step 9: Verify no week directories remain**

```bash
find . -type d -name 'week-*' -not -path './.git/*' -not -path './venv/*'   # expect: no output
git status --short
```

- [ ] **Step 10: Commit**

```bash
git add -A
git commit -m "refactor: rename content directories from weeks to chapters

Week numbers never matched chapter numbers -- week 5 was Chapter 7, week 7
was Chapter 5, week 11 was Chapter 13 -- while slides-official/ already used
chapter naming. The repository contradicted itself.

Also moves three misfiled code examples out of lectures/ into
code-examples/chapter-02-fundamentals/, adds the 01_hello_world.py that the
setup guide has always told students to run, fixes a slides link that pointed
at a directory which never existed, and deletes labs/, projects/ and
assessments/ -- which contained nothing but empty files."
```

---

## Task 3: Course map and slides index

**Files:**
- Create: `.claude/course-map.yaml`
- Create: `slides-official/README.md`
- Delete: `.claude/course-calendar.yaml`

**Interfaces:**
- Produces: `.claude/course-map.yaml` with top-level keys `course`, `chapters`, `self_study`, `assessments`, `learning_path`. Each `chapters` and `self_study` entry has: `number` (chapters only), `id`, `topic`, `slides_dir`, `slides_pdf`, `slides_text`, `figure_refs`. Tasks 4, 5, 6 read these key names.

- [ ] **Step 1: Create `.claude/course-map.yaml`**

Filenames below are copied verbatim from disk. Note `chapter-07`: the PDF has **no** space before its extension, the pptx/text files **do**. `figure_refs` is the measured count of figure/diagram mentions in the extracted text — a hint for how much a chapter depends on visuals that extraction dropped.

```yaml
# M110 Python Programming - Course Map
# خريطة مقرر M110 برمجة بايثون
#
# The single source of truth for chapter structure. Contains no dates:
# the course is archived and no longer taught on a schedule.
#
# figure_refs counts mentions of figures/diagrams in the extracted slide text.
# ALL figures are images and are absent from the .txt files. A high count means
# answers about that chapter should send students to the PDF.

course:
  code: M110
  name: Python Programming
  institution: Arab Open University (AOU) - Amman
  status: archived

chapters:
  - number: 1
    id: chapter-01-algorithms
    topic: "Algorithms: Flowcharts & Pseudocodes"
    slides_dir: "slides-official/chapter-01-algorithms"
    slides_pdf: "slides-official/chapter-01-algorithms/Meeting1-Algorithms-s.pdf"
    slides_text: "slides-official/chapter-01-algorithms/Meeting1-Algorithms-s.pptx.txt"
    figure_refs: 27

  - number: 2
    id: chapter-02-fundamentals
    topic: "Fundamentals of Python Programming"
    slides_dir: "slides-official/chapter-02-fundamentals"
    slides_pdf: "slides-official/chapter-02-fundamentals/Meeting2-Fundamentals of Python Programming-s.pdf"
    slides_text: "slides-official/chapter-02-fundamentals/Meeting2-Fundamentals of Python Programming-s.pptx.txt"
    figure_refs: 4

  - number: 3
    id: chapter-03-decision-structures
    topic: "Decision Structures and Boolean Logic"
    slides_dir: "slides-official/chapter-03-decision-structures"
    slides_pdf: "slides-official/chapter-03-decision-structures/Meeting3-Decision Structures and Boolean Logic-s.pdf"
    slides_text: "slides-official/chapter-03-decision-structures/Meeting3-Decision Structures and Boolean Logic-s.pptx.txt"
    figure_refs: 2

  - number: 4
    id: chapter-04-repetition
    topic: "Repetition Structures"
    slides_dir: "slides-official/chapter-04-repetition"
    slides_pdf: "slides-official/chapter-04-repetition/Meeting4-Repetition Structures-s.pdf"
    slides_text: "slides-official/chapter-04-repetition/Meeting4-Repetition Structures-s.pptx.txt"
    figure_refs: 1

  - number: 5
    id: chapter-05-functions
    topic: "Functions"
    slides_dir: "slides-official/chapter-05-functions"
    slides_pdf: "slides-official/chapter-05-functions/Meeting7-Functions-s.pdf"
    slides_text: "slides-official/chapter-05-functions/Meeting7-Functions-s.pptx.txt"
    figure_refs: 0

  - number: 6
    id: chapter-06-files-exceptions
    topic: "Files and Exceptions"
    slides_dir: "slides-official/chapter-06-files-exceptions"
    slides_pdf: "slides-official/chapter-06-files-exceptions/Meeting8-Files and Exceptions-s.pdf"
    slides_text: "slides-official/chapter-06-files-exceptions/Meeting8-Files and Exceptions-s.pptx.txt"
    figure_refs: 2

  - number: 7
    id: chapter-07-lists-tuples
    topic: "Collection Data Types: Lists and Tuples"
    slides_dir: "slides-official/chapter-07-lists-tuples"
    slides_pdf: "slides-official/chapter-07-lists-tuples/Meeting5 Collection Data Types-s.pdf"
    slides_text: "slides-official/chapter-07-lists-tuples/Meeting5 Collection Data Types-s .pptx.txt"
    figure_refs: 1

  - number: 10
    id: chapter-10-oop
    topic: "Classes and Object-Oriented Programming"
    slides_dir: "slides-official/chapter-10-oop"
    slides_pdf: "slides-official/chapter-10-oop/Meeting10-Classes and Object-Oriented Programming-s.pdf"
    slides_text: "slides-official/chapter-10-oop/Meeting10-Classes and Object-Oriented Programming-s.pptx.txt"
    figure_refs: 4

  - number: 13
    id: chapter-13-gui
    topic: "GUI Programming"
    slides_dir: "slides-official/chapter-13-gui"
    slides_pdf: "slides-official/chapter-13-gui/Meeting11-GUI Programming-s.pdf"
    slides_text: "slides-official/chapter-13-gui/Meeting11-GUI Programming-s.pptx.txt"
    figure_refs: 2

self_study:
  - id: ss1-turtle-graphics
    topic: "Turtle Graphics"
    slides_dir: "slides-official/ss1-turtle-graphics"
    slides_pdf: "slides-official/ss1-turtle-graphics/SS1-Turtle Graphics.pdf"
    slides_text: "slides-official/ss1-turtle-graphics/SS1-Turtle Graphics.pptx.txt"
    figure_refs: 5

  - id: ss2-recursion
    topic: "Recursion"
    slides_dir: "slides-official/ss2-recursion"
    slides_pdf: "slides-official/ss2-recursion/SS2-Recursion.pdf"
    slides_text: "slides-official/ss2-recursion/SS2-Recursion.pptx.txt"
    figure_refs: 6

  - id: ss3-dictionaries-sets
    topic: "Dictionaries and Sets"
    slides_dir: "slides-official/ss3-dictionaries-sets"
    slides_pdf: "slides-official/ss3-dictionaries-sets/SS3-Dictionaries and Sets.pdf"
    slides_text: "slides-official/ss3-dictionaries-sets/SS3-Dictionaries and Sets.pptx.txt"
    figure_refs: 0

assessments:
  # Coverage only. Grade weightings and dates applied to one specific
  # offering of the course and are deliberately omitted.
  - id: mta
    name: "Mid-Term Assessment"
    covers: "Through Collection Data Types (Chapters 1-4 and 7)"
  - id: tma
    name: "Tutor-Marked Assignment (Lab Test)"
    covers: "MTA material plus SS1, SS2 and SS3"
  - id: final
    name: "Final Exam"
    covers: "All regular chapters; excludes the self-study topics"

learning_path:
  # Suggested order. Deliberately differs from chapter numbering -- this was
  # the original teaching sequence, with self-study topics slotted where they
  # reinforce what precedes them.
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

- [ ] **Step 2: Verify the YAML parses and every path exists**

```bash
python3 -c "
import sys, pathlib, re
text = pathlib.Path('.claude/course-map.yaml').read_text(encoding='utf-8')
paths = re.findall(r'\"(slides-official/[^\"]+)\"', text)
missing = [p for p in paths if not pathlib.Path(p).exists()]
print('MISSING:', missing) if missing else print(f'OK - all {len(paths)} slide paths exist')
sys.exit(1 if missing else 0)
"
```
Expected: `OK - all 36 slide paths exist`. Any MISSING entry is a typo in a filename — fix it against `ls slides-official/*/`.

- [ ] **Step 3: Create `slides-official/README.md`**

Bilingual EN/AR throughout. Required sections:

1. **Title + purpose** — these are the official AOU slide decks, the source of truth for every answer in this repository.
2. **Chapter table** — columns: Chapter | Topic | Folder. All 12 rows (9 chapters + 3 self-study), matching `course-map.yaml`.
3. **Which file to use** — a three-row table:
   - `.pdf` — reading and studying. **Contains the figures and flowcharts.**
   - `.pptx` — the original PowerPoint.
   - `.pptx.txt` — plain text for AI assistants and text search.
4. **What the text files lose** — state all three verbatim from the spec §5, with the concrete examples:
   - Code indentation is partly flattened (`print(num)` appears unindented under its `for` loop in Chapter 4).
   - Smart quotes are mangled (`print('Hello’, i)` will not parse).
   - **Figures are absent entirely** — Chapter 1 is almost entirely flowcharts, and none of them are in the text.
   Follow with the rule for students: use the text to search and read, use the PDF whenever a diagram matters, and never copy code from the `.txt` without checking it runs.
5. **Attribution** — the slides are the copyright of Arab Open University and are redistributed here for student study. This repository is not affiliated with, nor endorsed by, AOU.

- [ ] **Step 4: Delete the calendar**

```bash
git rm .claude/course-calendar.yaml
```

- [ ] **Step 5: Commit**

```bash
git add -A
git commit -m "feat: replace course calendar with a dateless chapter map

course-map.yaml gives the assistant one place to learn chapter structure,
slide asset paths, the suggested learning path and assessment coverage --
with no start date, no week numbers and no schedule.

figure_refs records how often each deck's text mentions a figure, so the
assistant knows which chapters depend on visuals that extraction dropped.

Adds slides-official/README.md documenting which format to use when, what
the text extraction loses, and AOU attribution."
```

---

## Task 4: Rewrite Dr. Laila (Claude Code agent)

The substantive task. Behavior changes, not cosmetics.

**Files:**
- Modify: `.claude/agents/learning-assistant.md`

**Interfaces:**
- Consumes: `.claude/course-map.yaml` keys from Task 3 — `chapters[].id`, `.topic`, `.slides_text`, `.slides_pdf`, `.figure_refs`, plus `learning_path` and `assessments`.
- Produces: the behavior contract Task 5 mirrors into the Copilot chatmode.

- [ ] **Step 1: Remove all time-awareness**

Delete these sections outright:
- The entire `## Time-Aware Behavior` section, including the `current_week = floor((today - course_start) / 7) + 1` algorithm and the "If before Oct 12, 2025 / If week 1-13 / If after week 13" branches.
- In `## Startup Sequence`, Step 1's week calculation and the `📅 Current Week: Week X (Date Range)` greeting template.
- All day-of-week starter question groups: "After Sunday Lecture", "Tuseday Lab Day", "Mid-Week", "Lab Weeks (6, 9, 12)", "Week 13 (Revision)".
- From `## Course Context`: the `Semester`, `Course Start`, and `Class Schedule` lines.
- From `## Final Reminders`: "Always be time-aware: know what week it is".

- [ ] **Step 2: Replace slide access with the grounding protocol**

Delete the existing `### Reading Official Slides` block — the `PDF → PPTX → check python-pptx → guide student to install it` cascade — along with the `### If python-pptx Is Not Installed` error-handling block. Both are obsolete: the text is already extracted and committed.

Replace with a section stating:

- Read `.claude/course-map.yaml` first to resolve a chapter id to its `slides_text` path.
- Read that `.txt` file to ground the answer. Cite the chapter number and the slide's topic heading.
- When the slides genuinely do not cover something, say so plainly rather than implying they do.
- **Fidelity rules**, stated as hard constraints:
  - Extracted code has flattened indentation and mangled quote characters. Never paste it as if it were correct. Re-derive any code example and confirm it runs before showing it.
  - Figures, flowcharts and diagrams are **not** in the text. When an answer depends on one, point the student at the chapter's `slides_pdf`. Chapters with a high `figure_refs` — Chapter 1 above all — need this constantly.
  - Never modify anything under `slides-official/`.

- [ ] **Step 3: Replace the startup sequence with chapter-aware onboarding**

New Step 1: read `.claude/course-map.yaml`. New Step 2: greet bilingually **without** any date or week. New Step 3: ask which chapter or topic the student is working on, offering three ways in:
- name a chapter,
- describe a problem or paste an error,
- or "I don't know where to start" → offer the `learning_path` order, beginning at Chapter 1.

New Step 4: wait for the student to choose. Keep the existing rule that she does not proceed until they do.

- [ ] **Step 4: Change her role from co-teacher to primary guide**

Find every fallback that defers to a live instructor or class and replace it with something she can do:
- "ask Mohammad in the lecture" / "your instructor will cover this" → she explains it now.
- The `### If You Can't Find Course Materials` block's "We haven't reached that week yet / Materials are still being prepared by your instructor" → replace with: this repository ships the official slides for every chapter plus worked examples for Chapter 1; for other chapters she builds the walkthrough from the slides on request.
- Update the `### Repository Structure` block to the Task 2 layout (chapter directories; no `labs/`, `projects/`, `assessments/`).
- Fix the three broken example links in the "Example Response" block — `resources/git-guides/01-git-basics.md`, `02-cloning-repo.md`, `03-pull-updates.md` do not exist. The real filenames are `01-what-is-git.md`, `02-basic-git-commands.md`, `03-cloning-course-repo.md`, `04-staying-updated.md`, `05-git-workflow-for-students.md`.
- In `### Working in student-playground/`, change the `week-XX-practice/` example directory to `chapter-XX-practice/`, and drop the `Created: October 19, 2025` line from the file-header template.

- [ ] **Step 5: Confirm what must NOT change**

Verify these survive the rewrite intact — they are the reason the assistant works:
- Socratic style and the no-spoon-feeding rules (`### 1. Responsible AI Learning`).
- Bilingual EN/AR support and formats.
- Assessment integrity: no direct answers to graded work.
- Writes only to `student-playground/`; reads everything else.
- End-of-response follow-up questions.
- "Official slides are sacred" read-only constraint.

- [ ] **Step 6: Verify no time logic remains**

```bash
grep -n -E "week|Week|October|Sunday|Tuseday|Spring 202|semester|current_week|course_start" .claude/agents/learning-assistant.md
```
Expected: no output. Any hit is a missed edit.

- [ ] **Step 7: Behavioral test — cold start**

In a fresh Claude Code session in this repository, run `/laila`. Confirm all four:
1. The greeting contains no week number, no date, no day of the week.
2. She asks which chapter or topic you're working on.
3. Answering "Chapter 4, I don't understand while loops" makes her read `slides-official/chapter-04-repetition/Meeting4-Repetition Structures-s.pptx.txt`.
4. Asking "show me the flowchart for a while loop" makes her point at the **PDF**, not invent a description from the text.

Record the actual responses in the commit body if any of the four needed a follow-up fix.

- [ ] **Step 8: Commit**

```bash
git add .claude/agents/learning-assistant.md
git commit -m "feat: make Dr. Laila chapter-aware and slides-grounded

Removes the date arithmetic that computed a course week from October 12,
2025, along with every day-of-week and lab-week branch. She now asks what
you are working on instead of inferring it from a calendar.

Replaces the PDF-then-PPTX-then-install-python-pptx cascade with reading the
committed slide text directly, and adds the fidelity rules that follow from
it: extracted code has broken indentation and quote characters and must be
re-derived, and figures are absent from the text entirely, so diagram
questions go to the PDF.

Also reframes her from co-teacher to primary guide -- there is no live
lecture to defer to anymore."
```

---

## Task 5: Copilot chatmode parity

**Files:**
- Modify: `.github/chatmodes/learning-assistant.chatmode.md`

**Interfaces:**
- Consumes: the finished behavior contract from Task 4. The two files must not diverge.

- [ ] **Step 1: Apply every Task 4 change in the chatmode's format**

Specifically, in this file: delete the `semester: Spring 2024-2025`, `start_date: October 12, 2025` and `Tuseday_lab` lines from the embedded course data; delete `STEP 2: Determine current week by calculating days since October 12, 2025` and `STEP 3` from the startup steps; delete the `📅 Current Week: Week [X] ([Date Range])` greeting lines; delete the `Tuseday_lab`, `mid_week`, `lab_weeks` and `revision_week` starter-question groups; replace the embedded `weeks:` list with the chapter list from `course-map.yaml`; change `week-XX-practice/` to `chapter-XX-practice/`; update "Time-Aware Context - Know current course week" and "Always be time-aware (know current week)" to chapter-awareness; replace `Week [X]: [Topic]` in the file-header template with `Chapter [N]: [Topic]`; and rewrite the "Hmm, I couldn't find materials for Week [X] ... We haven't reached that week yet" block the same way as Task 4 Step 4.

- [ ] **Step 2: Add the slide-grounding protocol**

Delete this file's PDF/PPTX access instructions and replace them with the same
protocol the Claude Code agent carries, stated in full so the two files match:

- Read `.claude/course-map.yaml` first to resolve a chapter id to its
  `slides_text` path.
- Read that `.txt` file to ground the answer. Cite the chapter number and the
  slide's topic heading.
- When the slides genuinely do not cover something, say so plainly rather than
  implying they do.
- **Fidelity rules**, as hard constraints:
  - Extracted code has flattened indentation and mangled quote characters.
    Never paste it as if it were correct. Re-derive any code example and
    confirm it runs before showing it.
  - Figures, flowcharts and diagrams are **not** in the text. When an answer
    depends on one, point the student at the chapter's `slides_pdf`. Chapters
    with a high `figure_refs` — Chapter 1 above all — need this constantly.
  - Never modify anything under `slides-official/`.

- [ ] **Step 3: Verify no time logic remains**

```bash
grep -n -E "week|Week|October|Sunday|Tuseday|Spring 202|semester" .github/chatmodes/learning-assistant.chatmode.md
```
Expected: no output.

- [ ] **Step 4: Verify behavioral parity against the agent**

Confirm this file and `.claude/agents/learning-assistant.md` agree on all six:
1. Socratic style and the no-spoon-feeding rules.
2. Bilingual EN/AR support and formats.
3. Assessment integrity: no direct answers to graded work.
4. Writes only to `student-playground/`; reads everything else.
5. End-of-response follow-up questions.
6. "Official slides are sacred" read-only constraint.

Note any intentional format-only difference in the commit body.

- [ ] **Step 5: Commit**

```bash
git add .github/chatmodes/learning-assistant.chatmode.md
git commit -m "feat: mirror the chapter-aware assistant into the Copilot chatmode

Same behavior contract as the Claude Code agent: no date arithmetic, chapter
map instead of a week list, slide text as the grounding source, and the
fidelity rules for extracted code and missing figures.

Copilot users get the identical Dr. Laila."
```

---

## Task 6: Rewrite the README

**Files:**
- Modify: `README.md` (currently 917 lines)

**Interfaces:**
- Consumes: chapter paths from Task 2, `learning_path` and `assessments` from Task 3.

- [ ] **Step 1: Remove everything semester-bound**

Delete these sections entirely:
- `## 📍 Current Week` (the highlighted Week 1 block).
- The dated 13-week syllabus table under `## 📚 Course Syllabus (13 Weeks)`.
- The `**Schedule:**` block (Sunday lectures, Tuesday labs, start date) under Course Information.
- `## 📅 How to Use This Repository` in full — the Sunday/Monday-Wednesday/Tuesday weekly flow.
- `## 🆘 Getting Help` — office hours, `m.almarie@aou.edu.jo`, the Teams/Discord placeholder.
- The "Mohammad Provides" list (live lectures, grading, assessment) and the "Best of Both Worlds" framing in `## 🤝 Human-AI Collaboration in Learning`.
- The `Semester-Spring%202025` badge in the header, and the `**M110 Python Programming - Spring 2024-2025**` line in the footer.
- The inflated counts under `## 📦 Available Resources`: "13 weeks", "50+ code examples", "100+ practice exercises", "3 lab sessions", "Project templates".
- "Let's make this semester amazing!" and "this semester" phrasing in the closing notes.

- [ ] **Step 2: Add the archived banner**

Directly beneath the title, before anything else, bilingual:

> **This course is no longer taught live.** These materials and Dr. Laila remain here, free, for any M110 student who finds them.
>
> **لم يعد هذا المقرر يُدرَّس بشكل مباشر.** هذه المواد ود. ليلى تبقى هنا، مجاناً، لأي طالب في مقرر M110.

- [ ] **Step 3: Rewrite the structure to these nine sections**

1. Title, badges (drop the semester badge), archived banner.
2. **What this is** — the official AOU slides plus an AI study guide that teaches from them.
3. **Start here** — three steps: clone; install Python and VS Code (link the existing setup guides); run `/laila`.
4. **The learning path** — a table in `learning_path` order from `course-map.yaml`: Order | Chapter | Topic | Slides. Twelve rows. No dates, no week numbers.
5. **How Dr. Laila works** — what she does, what she won't do (graded work), which extension to install, that she grounds answers in the slide text, and that she writes into `student-playground/`.
6. **What's in the repository** — accurate map matching Task 2's layout. State plainly: official slides for all 12 topics, 26 setup and reference guides, Chapter 1 as a worked sample, and everything else generated on demand. No counts that aren't true.
7. **Assessments** — the three `assessments` entries from `course-map.yaml`, coverage only.
8. **Built by** — Mohammad's bio, education, experience and teaching philosophy, retained. No email, no office hours, no schedule.
9. **License and attribution** — MIT for repository content; the official slides are the copyright of Arab Open University; this repository is unaffiliated with and not endorsed by AOU.

- [ ] **Step 4: Verify the README is clean**

```bash
grep -n -E "week|Week|Sunday|Tuseday|October|Spring 202|office hours|aou\.edu\.jo|50\+|100\+|13 [Ww]eeks" README.md
```
Expected: no output.

- [ ] **Step 5: Verify every README link resolves**

```bash
grep -o '](\([^)#][^)]*\))' README.md | sed 's/^](//;s/)$//' | while read -r l; do
  case "$l" in http*|mailto*|"#"*) continue;; esac
  [ -e "$l" ] || echo "BROKEN  $l"
done
```
Expected: no output.

- [ ] **Step 6: Commit**

```bash
git add README.md
git commit -m "docs: rewrite README for an archived, self-study course

Removes the current-week block, dated syllabus, weekly Sunday/Tuesday flow,
class schedule, office hours and contact details -- none of which describe
anything that still exists.

Replaces the inflated resource counts with what the repository actually
contains. The learning path is now an ordered chapter table rather than a
calendar, and Dr. Laila is presented as the guide rather than as the
instructor's counterpart.

Adds AOU attribution for the official slide decks."
```

---

## Task 7: Dependencies and the extraction tool

**Files:**
- Modify: `requirements.txt`
- Create: `tools/extract_slides.py`

- [ ] **Step 1: Confirm the current file is broken**

```bash
python3 -m venv /tmp/m110-before && /tmp/m110-before/bin/pip install -q -r requirements.txt
echo "exit: $?"
```
Expected: non-zero exit, with a build failure from `numpy==1.26.2` or `matplotlib==3.8.2`. This is what students hit at step 3 of the setup guide. Record the error in the commit body.

- [ ] **Step 2: Replace `requirements.txt`**

```
################################
# M110 Python Programming
# متطلبات مقرر M110
################################
#
#   pip install -r requirements.txt
#
# M110 is a standard-library course. Almost everything you need ships with
# Python itself -- including turtle graphics (SS1) and Tkinter GUIs
# (Chapter 13). There is very little to install.
#
# مقرر M110 يعتمد على مكتبة بايثون القياسية. كل ما تحتاجه تقريباً يأتي مع
# بايثون نفسه، بما في ذلك رسومات السلحفاة وواجهات Tkinter الرسومية.
#
# Requires Python 3.9 or newer / يتطلب بايثون 3.9 أو أحدث
################################

# Images inside Tkinter GUIs (Chapter 13)
# الصور داخل واجهات Tkinter الرسومية (الفصل 13)
Pillow>=10.0


################################
# Optional / اختياري
################################
#
# Only needed to re-run tools/extract_slides.py, which regenerates the
# slide text files. Students never need this.
# مطلوب فقط لإعادة تشغيل أداة استخراج نص الشرائح. الطلاب لا يحتاجونها.
#
# python-pptx>=1.0
```

- [ ] **Step 3: Verify a clean install now succeeds**

```bash
rm -rf /tmp/m110-after && python3 -m venv /tmp/m110-after && /tmp/m110-after/bin/pip install -r requirements.txt
echo "exit: $?"
```
Expected: exit 0, Pillow installed.

- [ ] **Step 4: Create `tools/extract_slides.py`**

```python
"""
Extract text from the official M110 slide decks.
استخراج النص من شرائح مقرر M110 الرسمية

Walks slides-official/, reads every .pptx, and writes a sibling .pptx.txt
holding the deck's text in slide order.
يمر على مجلد الشرائح ويكتب ملف نصي بجانب كل ملف عرض تقديمي.

These text files let AI assistants and text search read the official slides.
They do NOT replace the PDFs: figures, flowcharts and diagrams are images and
do not survive extraction.
هذه الملفات النصية لا تُغني عن ملفات PDF: الأشكال والمخططات صور ولا تُستخرج.

Usage / الاستخدام:
    pip install python-pptx
    python tools/extract_slides.py           # write the .txt files
    python tools/extract_slides.py --check   # compare only, write nothing
"""

import argparse
import sys
from pathlib import Path

from pptx import Presentation

# slides-official/ sits next to tools/ / مجلد الشرائح بجانب مجلد الأدوات
SLIDES_DIR = Path(__file__).resolve().parent.parent / "slides-official"


def extract_deck(pptx_path):
    """
    Return every slide's text, blank line between slides.
    يُرجع نص كل شريحة، مع سطر فارغ بين الشرائح.
    """
    presentation = Presentation(str(pptx_path))
    blocks = []

    for slide in presentation.slides:
        lines = []
        for shape in slide.shapes:
            if not shape.has_text_frame:
                continue
            for paragraph in shape.text_frame.paragraphs:
                text = "".join(run.text for run in paragraph.runs)
                if text.strip():
                    lines.append(text)
        blocks.append("\n".join(lines))

    return "\n\n".join(blocks) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="Compare against existing .txt files without writing",
    )
    args = parser.parse_args()

    decks = sorted(SLIDES_DIR.glob("*/*.pptx"))
    if not decks:
        print(f"No .pptx files found under {SLIDES_DIR}")
        return 1

    differences = 0
    for deck in decks:
        target = deck.with_suffix(".pptx.txt")
        extracted = extract_deck(deck)

        if args.check:
            existing = target.read_text(encoding="utf-8") if target.exists() else ""
            status = "same" if existing == extracted else "DIFFERS"
            differences += status == "DIFFERS"
            print(f"{status:8} {target.relative_to(SLIDES_DIR.parent)}")
        else:
            target.write_text(extracted, encoding="utf-8")
            print(f"wrote    {target.relative_to(SLIDES_DIR.parent)}")

    return 1 if differences else 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 5: Run `--check` against the committed text**

```bash
/tmp/m110-after/bin/pip install "python-pptx>=1.0"
/tmp/m110-after/bin/python tools/extract_slides.py --check
```

Two possible outcomes, and **the committed `.txt` files are never overwritten either way** (spec D4):
- All 12 report `same` → the script reproduces the committed text exactly. Say so in the commit body.
- Some report `DIFFERS` → the original conversion used different settings. Leave the committed files untouched and add a note to the module docstring recording that this script produces equivalent-but-not-identical output, and which decks differ.

- [ ] **Step 6: Confirm the script never writes during `--check`**

```bash
git status --short slides-official     # expect: no output
```

- [ ] **Step 7: Commit**

```bash
git add requirements.txt tools/extract_slides.py
git commit -m "fix: make pip install -r requirements.txt actually work

The old file pinned 40+ packages at 2023 versions. numpy==1.26.2 and
matplotlib==3.8.2 cannot build on current Python, so step 3 of the setup
guide failed outright for anyone starting today.

M110 is a standard-library course -- turtle and tkinter ship with Python --
so the only real dependency is Pillow, for images in Tkinter GUIs. Lower
bounds only, so it cannot rot the same way again.

Adds tools/extract_slides.py documenting how the slide text was produced and
allowing it to be regenerated if the decks are ever replaced."
```

---

## Task 8: Sweep the resources guides

Twenty files under `resources/`. Mechanical but high-volume; the deliverable is that a student following any guide lands on a path that exists.

**Files (with hit counts):**
- `resources/git-guides/04-staying-updated.md` (21), `05-git-workflow-for-students.md` (14), `02-basic-git-commands.md` (12), `03-cloning-course-repo.md` (9)
- `resources/setup-guides/07-running-first-program.md` (20), `09-github-copilot-setup.md` (3), `06-github-repo-cloning.md` (3), `08-claude-code-extension-setup.md` (2), `01-python-installation.md` (1), `03-git-installation.md` (1), `10-troubleshooting-common-issues.md` (1)
- `resources/video-tutorials/video-tutorials-guide.md` (10), `README.md` (1)
- `resources/python-guides/04-how-to-learn-python-effectively.md` (7), `05-python-resources-and-documentation.md` (4), `03-pep8-style-guide-for-beginners.md` (1)
- `resources/faq.md` (7)
- `resources/cheatsheets/git-commands-cheatsheet.md` (3), `terminal-commands-cheatsheet.md` (1)
- `resources/vscode-guides/03-python-development-in-vscode.md` (2), `02-essential-vscode-shortcuts.md` (2), `01-vscode-interface-overview.md` (2)

- [ ] **Step 1: Apply these four substitution rules**

1. **Paths** — `week-01-algorithms` → `chapter-01-algorithms`; `exercises/week-01` → `exercises/chapter-01-algorithms`; `week-02-fundamentals` → `chapter-02-fundamentals`; `exercises/week-03` (in `terminal-commands-cheatsheet.md:150`) → `exercises/chapter-03-decision-structures`.
2. **Labels** — "Week N: Topic" → "Chapter M: Topic" using the mapping: W1→Ch1, W2→Ch2, W3→Ch3, W4→Ch4, W5→Ch7, W7→Ch5, W8→Ch6, W10→Ch10, W11→Ch13. `video-tutorials-guide.md` has nine such section headings; `03-pep8-style-guide-for-beginners.md:90` says "(Week 10)" → "(Chapter 10)"; `10-troubleshooting-common-issues.md:1148` says "my Week 1 exercise" → "my Chapter 1 exercise"; `video-tutorials/README.md:57` says "Course weeks (Week 1-13)" → "Course chapters".
3. **Live-course references** — remove or redirect to Dr. Laila: `01-python-installation.md:450` "Ask your instructor during office hours" → ask Dr. Laila or open a GitHub issue. Same treatment for weekly-pull framing in the git guides ("pull every Sunday before the lecture" → "pull whenever you want the latest").
4. **Leave alone** — `03-git-installation.md:291`, the `git config` example using `ahmed.hassan@student.aou.edu.jo`. It is an illustrative student address, not contact information.

- [ ] **Step 2: Fix the anchor broken by the relabeling above**

`lectures/chapter-01-algorithms/README.md` links to `../../resources/video-tutorials/video-tutorials-guide.md#week-1`. Once that guide's headings become "Chapter 1", the anchor must become `#chapter-1`.

- [ ] **Step 3: Verify the resources tree is clean**

```bash
grep -rn -E "week-[0-9]{2}|Week [0-9]+|Tuseday|office hours|Office Hours" resources/
```
Expected: no output.

- [ ] **Step 4: Verify links inside resources resolve**

```bash
git ls-files 'resources/*.md' | while read -r f; do
  d=$(dirname "$f")
  grep -o '](\([^)#][^)]*\))' "$f" 2>/dev/null | sed 's/^](//;s/)$//' | while read -r l; do
    case "$l" in http*|mailto*|"#"*) continue;; esac
    [ -e "$d/$l" ] || [ -e "$l" ] || echo "BROKEN  $f -> $l"
  done
done
```
Expected: no output.

- [ ] **Step 5: Commit**

```bash
git add resources lectures
git commit -m "docs: update resource guides to chapter structure

Rewrites week-based paths and labels across 20 guides so every path a student
follows actually exists, and removes the weekly-pull and office-hours framing
that assumed a live course.

The git config example using a student address is deliberately kept -- it is
an illustration, not contact information."
```

---

## Task 9: Sweep the remaining documents

**Files:**
- `HOW-TO-USE-DR-LAILA.md` (3), `.claude/DR-LAILA-SETUP.md` (8), `.claude/README.md`
- `student-playground/README.md` (2), `student-contributions/README.md` (2)
- `lectures/chapter-01-algorithms/README.md` (9), `lecture-notes.md` (11), `additional-resources.md` (1)
- `exercises/chapter-01-algorithms/README.md` (1), `exercise-01.md`, `solutions/exercise_01_rectangle_area.py`
- `code-examples/chapter-01-algorithms/*.py` (7 files), `code-examples/chapter-02-fundamentals/*.py` (3 moved files)
- `CLAUDE.md` (gitignored, instructor-private)

- [ ] **Step 1: Update the Dr. Laila documentation**

In `HOW-TO-USE-DR-LAILA.md`: replace the `📅 Current Week: Week 2 (Oct 19-23)` sample greeting with a chapter-aware one — a bilingual welcome carrying no date, week or day, followed by her asking which chapter or topic the student is working on and offering three ways in (name a chapter, describe a problem or paste an error, or ask where to start and get the learning-path order beginning at Chapter 1). Change `student-playground/week-04-practice/` to `chapter-04-practice`; delete "Attend Sunday lectures and Tuseday labs" (line 311).

In `.claude/DR-LAILA-SETUP.md` and `.claude/README.md`: replace every week reference and every `course-calendar.yaml` mention with `course-map.yaml`, and rewrite the described startup sequence to the same chapter-aware flow — read `course-map.yaml`, greet without a date, ask which chapter, wait for the student to choose.

- [ ] **Step 2: Update the two student-space READMEs**

`student-playground/README.md`: change `week-XX-practice/` examples to `chapter-XX-practice/`. `student-contributions/README.md`: reframe from a showcase for one live class to open contributions by pull request — remove deadlines, grading and "your classmates" framing; and change the example link `2025-S200123-snake-game/` to plain text, since it points at a directory that does not exist.

- [ ] **Step 3: Update Chapter 1 content headers**

In `lectures/chapter-01-algorithms/*.md` and `exercises/chapter-01-algorithms/*.md`: "Week 1" → "Chapter 1" in titles and body. In `exercises/chapter-01-algorithms/exercise-01.md`, remove the link to `exercise-02.md` — that file does not exist.

- [ ] **Step 4: Update the code example docstrings**

All seven files in `code-examples/chapter-01-algorithms/` open with `Week 1: Algorithms - ...` and `الأسبوع 1: الخوارزميات`. Change to `Chapter 1: Algorithms - ...` and `الفصل 1: الخوارزميات`, preserving each file's specific topic line. Do the same for the three moved files in `code-examples/chapter-02-fundamentals/` (→ `Chapter 2` / `الفصل 2`), and for `exercises/chapter-01-algorithms/solutions/exercise_01_rectangle_area.py`.

- [ ] **Step 5: Confirm every example still runs**

```bash
for f in code-examples/chapter-01-algorithms/*.py code-examples/chapter-02-fundamentals/*.py; do
  python3 -c "import ast,sys; ast.parse(open('$f',encoding='utf-8').read())" && echo "OK  $f" || echo "FAIL $f"
done
```
Expected: `OK` for all eleven. Docstring edits must not break syntax.

- [ ] **Step 6: Update the private instructor guide**

`CLAUDE.md` is gitignored and stays that way. Replace its "Course Calendar" week list with the chapter map, drop the `Semester: Spring 2024-2025` line, update the repository-structure block and the `week-XX` directory-naming guidance to chapter naming, and update the "Weekly Content Creation Checklist" and example prompts to speak in chapters.

- [ ] **Step 7: Run the full verification suite**

All four toolkit commands, in order:

```bash
echo "--- V1: no week references"
git ls-files -z | grep -zv '^docs/superpowers/' | xargs -0 grep -n -E "week-[0-9]{2}|Week [0-9]+" 2>/dev/null

echo "--- V2: no date or schedule logic"
git ls-files -z | grep -zv '^docs/superpowers/' | xargs -0 grep -n -E "course_start|current_week|October 12|Spring 202[0-9]|Tuseday|office hours|Office Hours|aou\.edu\.jo" 2>/dev/null

echo "--- V3: links resolve"
git ls-files '*.md' | grep -v '^docs/' | while read -r f; do
  d=$(dirname "$f")
  grep -o '](\([^)#][^)]*\))' "$f" 2>/dev/null | sed 's/^](//;s/)$//' | while read -r l; do
    case "$l" in http*|mailto*|"#"*) continue;; esac
    [ -e "$d/$l" ] || [ -e "$l" ] || echo "BROKEN  $f -> $l"
  done
done

echo "--- V4: course map paths exist"
python3 -c "
import sys, pathlib, re
text = pathlib.Path('.claude/course-map.yaml').read_text(encoding='utf-8')
paths = re.findall(r'\"(slides-official/[^\"]+)\"', text)
missing = [p for p in paths if not pathlib.Path(p).exists()]
print('MISSING:', missing) if missing else print(f'OK - all {len(paths)} slide paths exist')
sys.exit(1 if missing else 0)
"
```

Expected: V1 silent; V2 shows only the `03-git-installation.md:291` student-email example; V3 silent; V4 `OK - all 36 slide paths exist`. **Do not commit until all four pass** — fix and re-run.

- [ ] **Step 8: Commit**

```bash
git add -A
git commit -m "docs: complete the chapter migration across remaining documents

Updates the Dr. Laila guides, both student-space READMEs, all Chapter 1
lecture and exercise material, and the docstring headers of eleven code
examples.

Also drops two links to files that never existed (exercise-02.md and a sample
contribution directory), and reframes student-contributions from a showcase
for one live class into open contributions by pull request.

Verified: no week references or date logic remain in tracked files, every
relative link resolves, and every slide path in course-map.yaml exists."
```

---

## Task 10: Final review

- [ ] **Step 1: Read the diff as a student would**

```bash
git diff main...HEAD --stat
```
Confirm the shape matches the spec's §6: slides text added, chapter renames, three directories deleted, calendar replaced by map, assistant and README rewritten.

- [ ] **Step 2: Simulate a first-time student**

In a clean clone of the branch:
```bash
git clone -b evergreen-repo-redesign . /tmp/m110-student && cd /tmp/m110-student
python3 -m venv venv && ./venv/bin/pip install -r requirements.txt
./venv/bin/python code-examples/chapter-02-fundamentals/01_hello_world.py
```
Expected: install succeeds, hello-world prints. This is the exact path `resources/setup-guides/07-running-first-program.md` walks them down.

- [ ] **Step 3: Confirm the README makes only true claims**

Read the finished README top to bottom against the repository. Every count, every directory named, every link. The original failed precisely here — it promised 50+ examples and 100+ exercises that did not exist.

- [ ] **Step 4: Report and hand back**

Summarize: what changed, what the verification showed, and anything deferred. Do not merge to `main` or push — that is Mohammad's call.

---

## Notes for the executor

- **The slide text is never edited.** If something in a `.txt` looks wrong, that is expected — see spec §5. Fix how the assistant *handles* it, never the file.
- **Task 4 is the one that matters.** Tasks 1-3 and 6-9 are plumbing. If Dr. Laila does not actually read the slide text and does not actually send students to the PDF for diagrams, the redesign has failed regardless of how clean the greps are.
- **When a step's expectation does not match reality, stop and report.** Several steps encode findings from the design audit (files that are empty, links that were already broken). If one turns out differently, that is new information, not an obstacle to route around.
