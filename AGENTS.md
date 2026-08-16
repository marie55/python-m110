# M110 Python Programming — Agent Instructions

This is the archived course repository for M110 Python Programming at Arab Open
University, Amman. It is no longer taught live. It stays public so that any
M110 student can learn from it alone, at any time, with an AI assistant.

What you should do here depends entirely on who you are working for. Read this
section before anything else.

---

## If you are helping a student learn

This is almost everyone who opens this repository.

**Spawn the `learning-assistant` subagent.** She is Dr. Laila, defined in
`.codex/agents/learning-assistant.toml` (and `.qoder/agents/learning-assistant.md`
for Qoder), and she carries the rules that make her answers trustworthy — how
to ground an explanation in the official slide text, why extracted code must be
retyped rather than pasted, and when to send a student to the PDF because a
figure cannot be read out of text at all.

Ask for her by name, for example: *"spawn the learning-assistant agent to help
me with Chapter 4."*

If you answer a student directly instead, these four rules still bind you:

1. **Ground it in the official slides.** Resolve the question to a chapter in
   `.claude/course-map.yaml`, read that chapter's `slides_text` file, and cite
   the chapter and slide heading. The assessments were written from those decks,
   not from general Python knowledge.
2. **Never paste code out of an extracted `.txt` file.** Extraction flattened
   the indentation and mangled the quote characters in all twelve decks — the
   code in them does not parse. Retype it, and run it before showing it.
3. **You cannot see the figures.** They are images and are absent from the text
   entirely, silently. If an answer needs a flowchart or diagram, send the
   student to that chapter's PDF. Never describe one you have not seen.
4. **Never do graded work.** Teach the concept, work an adjacent example, let
   them write their own.

**Write only to `student-playground/`** (work you build with the student) and
**`.assistant-memory/`** (notes on their learning, so the next session does not
start from zero). Nothing else. A student's question is not a mandate to edit
the repository.

---

## If you are helping maintain this repository

`CLAUDE.md` in the root holds the full authoring conventions — documentation
style, the bilingual English/Arabic requirement, code-example standards, and
where each kind of content belongs. Read it before creating or changing course
material. It applies to you regardless of which assistant you are.

Two things it will tell you that are worth knowing up front:

- Chapter numbers are **1, 2, 3, 4, 5, 6, 7, 10, 13**, plus self-study **ss1,
  ss2, ss3**. They are not contiguous. That matches the official course; it is
  not a gap to fill.
- Student-facing documents are bilingual: an English block immediately followed
  by its Arabic translation. Where two numbered lists sit adjacent, they need an
  `<!-- -->` separator between them or CommonMark merges them and the Arabic
  list renumbers.

---

## Either way

**`slides-official/` is read-only.** Those are the official Arab Open University
decks. The extracted `.txt` files ship exactly as produced, including their
broken quote characters — never "repair" them. Cite the PDFs; do not modify
anything in that directory.

**`.claude/course-map.yaml` is the single source of truth** for chapter
structure, slide paths, the suggested learning order, and assessment coverage.
Read it rather than assuming.

**Do not run `tools/extract_slides.py` without `--check`.** Without that flag it
overwrites the committed slide text, which must ship byte-for-byte as produced.

---

## Where things are

```
python-m110/
├── slides-official/        Official decks: PDF + PPTX + extracted .txt (READ-ONLY)
├── lectures/               Supplementary notes (Chapter 1 so far)
├── code-examples/          Runnable Python by chapter (Chapters 1-2 so far)
├── exercises/              Practice problems with solutions (Chapter 1 so far)
├── resources/              Setup guides, Git guides, cheatsheets, FAQ
├── student-playground/     Workspace for work built with a student
├── .assistant-memory/      Notes on one student's learning (private)
├── .codex/agents/          Dr. Laila for Codex
├── .claude/                Dr. Laila for Claude Code, and course-map.yaml
├── .qoder/agents/          Dr. Laila for Qoder
└── .github/chatmodes/      Dr. Laila for GitHub Copilot
```

Chapter 1 ships a finished walkthrough — notes, worked examples, exercises with
a solution. Chapter 2 has a starter example. Every other chapter has its
official slides, and the assistant builds the walkthrough from them on request.
That is the design, not a backlog.
