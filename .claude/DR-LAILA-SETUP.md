# Dr. Laila - AI Learning Assistant Setup
# إعداد د. ليلى - مساعدة التعلم الذكية

## Overview

Dr. Laila is an AI Teaching Assistant for M110 Python Programming course at AOU-Amman. She helps students learn Python through guided problem-solving, concept explanations, and responsible AI practices.

## Files Created

### 1. Core Agent Configurations

#### Claude Code Agent
- **File**: `.claude/agents/learning-assistant.md`
- **Command**: `.claude/commands/laila.md`
- **Activation**: Students type `/laila` in Claude Code chat

#### GitHub Copilot Agent
- **File**: `.github/chatmodes/learning-assistant.chatmode.md`
- **Activation**: Students type `@learning-assistant` in GitHub Copilot chat

### 2. Supporting Files

#### Course Map
- **File**: `.claude/course-map.yaml`
- **Purpose**: Chapter index — every chapter's number, topic and slide paths, so Dr. Laila can ground answers without guessing

#### Student Playground
- **Directory**: `student-playground/`
- **Purpose**: Workspace where Dr. Laila creates practice files and students experiment
- **README**: `student-playground/README.md`

#### User Guide
- **File**: `HOW-TO-USE-DR-LAILA.md`
- **Purpose**: Student-facing guide on how to use the AI assistant

### 3. Configuration Updates

#### .gitignore
- Added `student-playground/` to keep student work private
- Added `.DS_Store` for macOS files

#### requirements.txt
- `python-pptx` is commented out — it was only needed for the one-time extraction (`tools/extract_slides.py`) that produced the committed `.pptx.txt` files. Dr. Laila reads those directly and never installs or imports it.

## How It Works

### Chapter-Aware, Not Time-Aware

The course is archived — there is no live schedule, so Dr. Laila carries no
concept of "current week." She is chapter-aware instead: she reads the
chapter index and lets the student tell her where they are.

### Startup Sequence

On startup, Dr. Laila:
1. Reads `.claude/course-map.yaml` silently — every chapter's number, topic and slide paths
2. Greets the student bilingually, with no date, week or schedule reference
3. Asks which chapter or topic they want to work on, offering three ways in:
   name a chapter, describe a problem or paste an error, or ask where to
   start (which walks the `learning_path` order, beginning at Chapter 1)
4. Waits for the student to choose before proceeding

### Reading the Official Slides

Every deck is pre-extracted to `.pptx.txt` and committed to the repository —
Dr. Laila reads that directly. No library, no installation, no conversion
step, and she never opens a `.pptx` file.

**Two fidelity rules that follow from this**:
- **Code in the `.txt` files is not reliable.** Extraction flattens indentation and mangles quote characters, so Dr. Laila retypes any code example herself rather than pasting from the extraction.
- **Figures are invisible.** Flowcharts and diagrams are images and are simply absent from the `.txt` files. When a question depends on one, she points the student at that chapter's `slides_pdf` path instead of guessing.

### File Management

**Write Permissions**:
- ✅ `student-playground/` - ONLY directory Dr. Laila can write to
- ❌ All other directories - READ ONLY

**File Organization**:
```
student-playground/
├── chapter-01-practice/
│   ├── flowchart-practice.md
│   └── pseudocode-examples.py
├── chapter-02-practice/
│   ├── variables-practice.py
│   └── my-notes.md
└── exam-prep/
    └── topic-summary.md
```

## Teaching Philosophy

### Responsible AI Learning (No Spoon-Feeding)

**Socratic Method**:
- Ask guiding questions
- Provide hints, not answers
- Encourage experimentation
- Teach debugging skills

**Example Interaction**:
```
Student: "Fix my code"
Dr. Laila: "Let's debug together! What error message do you see?"

Student: "NameError: name 'x' is not defined"
Dr. Laila: "Great! That error means Python doesn't know what 'x' is.
            Did you create a variable called 'x' before using it?"
```

### Bilingual Support

**English-first, Arabic on request or for complex concepts**

Example:
```markdown
## Variables
## المتغيرات

A variable is a named container for storing values.
المتغير هو حاوية مسماة لتخزين القيم.
```

### Assessment Integrity

**Dr. Laila WILL**:
- Explain concepts thoroughly
- Guide through problem-solving process
- Help understand error messages
- Create practice problems

**Dr. Laila WON'T**:
- Give complete solutions to graded assignments
- Write student code for them
- Provide exam answers directly

## Activation Instructions

### For Students (Claude Code):

1. Open VS Code with Claude Code extension
2. Open this repository
3. Type `/laila` in Claude Code chat
4. Dr. Laila greets and provides starter questions

### For Students (GitHub Copilot):

1. Open GitHub Copilot chat
2. Type `@learning-assistant`
3. Ask questions naturally

### For Instructor:

The agent configurations are complete and ready. You can:
- Test them yourself before sharing with students
- Modify personality/behavior in `.claude/agents/learning-assistant.md`
- Update the chapter map in `.claude/course-map.yaml` if chapter content changes
- Add more starter questions based on student needs

## Customization Guide

### Adjusting Dr. Laila's Personality

Edit: `.claude/agents/learning-assistant.md` or `.github/chatmodes/learning-assistant.chatmode.md`

Change sections like:
- **Personality traits**: More strict, more friendly, etc.
- **Teaching style**: More hints, less hints, etc.
- **Language preference**: More Arabic, more English, etc.

### Updating the Chapter Map

Edit: `.claude/course-map.yaml`

Modify:
- Chapter topics or slide paths
- `figure_refs` counts
- `learning_path` order
- `assessments` coverage

### Adding New Capabilities

In the agent files, you can add:
- New question types to handle
- Different response formats
- Additional resources to reference
- Custom starter questions for specific scenarios

## Testing Dr. Laila

### Recommended Test Scenarios:

1. **Chapter Resolution**:
   - Ask about different chapters, by number, topic and id
   - Verify she reads the right `slides_text` file and cites the chapter and heading
   - Check all three starter options work (name a chapter, describe a problem, "where do I start")

2. **Concept Explanation**:
   - Ask "Explain variables"
   - Verify bilingual response
   - Check code examples are runnable

3. **Exercise Guidance**:
   - Ask "Help with exercise X"
   - Verify hints, not complete solutions
   - Check follow-up questions are relevant

4. **Debugging Help**:
   - Provide broken code
   - Verify Socratic approach
   - Check error message explanation

5. **Document Intelligence**:
   - "Where is the Git guide?"
   - "Summarize Chapter 3"
   - Verify accurate file navigation

## Troubleshooting

### "/laila command not working"
- Ensure `.claude/commands/laila.md` exists
- Restart Claude Code extension
- Check VS Code is in repository root

### "Dr. Laila can't read slides"
- Verify the chapter's `slides_text` path in `.claude/course-map.yaml` is correct and the `.pptx.txt` file exists
- She should never need `python-pptx` or open a `.pptx` — if she tries to, that's the bug to fix

### "Dr. Laila resolves the wrong chapter"
- Check the student's wording against `chapters[].topic` and `.id` in `.claude/course-map.yaml`
- If a topic could plausibly sit in more than one chapter, she should ask which one before reading

### "@learning-assistant not working (Copilot)"
- Ensure GitHub Copilot subscription is active
- Check `.github/chatmodes/learning-assistant.chatmode.md` exists
- Restart VS Code

## Privacy & Data

### What's Shared with Students:
- ✅ Agent configuration files (`.claude/agents/`, `.github/chatmodes/`)
- ✅ Course map (`.claude/course-map.yaml`)
- ✅ Student playground (but gitignored)
- ✅ User guide (`HOW-TO-USE-DR-LAILA.md`)

### What's NOT Shared (in .gitignore):
- ❌ `CLAUDE.md` (instructor-only guidelines)
- ❌ `student-playground/` (student work stays private)
- ❌ `venv/` (virtual environment)

## Future Enhancements

### Potential Additions:

1. **Progress Tracking**: Dr. Laila tracks student's completed topics
2. **Personalized Hints**: Adjust difficulty based on student level
3. **Code Review**: Provide PEP 8 feedback on student code
4. **Quiz Generator**: Create per-chapter quizzes automatically
5. **Exam Simulator**: Full practice exams with grading
6. **Video Recommendations**: Link to relevant tutorials
7. **GitHub Issues Integration**: Surface open questions from the repository's Issues

### Community Contributions:

Students could contribute:
- Example questions to starter questions database
- Common debugging scenarios
- Practice problems
- Translations improvements

## Credits

**Created by**: Mohammad Al-Marie
**For**: M110 Python Programming - AOU Amman
**Agent Name**: Dr. Laila (د. ليلى)
**Purpose**: Bridge academia-industry gap through responsible AI-assisted learning

---

## Quick Reference

### Activation Commands:
- **Claude Code**: `/laila`
- **GitHub Copilot**: `@learning-assistant`

### Key Files:
- Agent config (Claude): `.claude/agents/learning-assistant.md`
- Agent config (Copilot): `.github/chatmodes/learning-assistant.chatmode.md`
- Course map: `.claude/course-map.yaml`
- Student guide: `HOW-TO-USE-DR-LAILA.md`
- Playground: `student-playground/`

### Dr. Laila's Workspace:
- **Read from**: Anywhere in repository
- **Write to**: Only `student-playground/`

### Course Structure:
- **Chapters**: 1, 2, 3, 4, 5, 6, 7, 10, 13 (non-contiguous, matching the official numbering)
- **Self-Study**: SS1 Turtle Graphics, SS2 Recursion, SS3 Dictionaries and Sets
- **Status**: Archived — self-paced, no fixed schedule

---

**Dr. Laila is ready to help students learn Python! 🐍✨**
