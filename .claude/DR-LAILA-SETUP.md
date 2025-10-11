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

#### Course Calendar
- **File**: `.claude/course-calendar.yaml`
- **Purpose**: Time-aware context - knows which week, topic, and materials to reference

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
- Already includes `python-pptx` for reading PowerPoint slides

## How It Works

### Time-Aware Intelligence

Dr. Laila calculates the current course week based on:
- **Course Start**: October 12, 2025 (Week 1)
- **Current Date**: Determines week number
- **Week's Topic**: Loads from `.claude/course-calendar.yaml`

### Context Loading

On startup, Dr. Laila:
1. Calculates current week
2. Identifies week's topic (e.g., "Fundamentals of Python Programming")
3. Checks for official slides in `slides-official/chapter-XX-*/`
4. Loads lecture notes from `lectures/week-XX-*/`
5. Accesses code examples from `code-examples/week-XX-*/`
6. Provides 3-5 contextual starter questions

### Reading Official Slides

**Preference Order**:
1. PDF files (Dr. Laila can read PDFs directly)
2. PPTX files (requires `python-pptx` library)

**Example**:
```python
from pptx import Presentation

prs = Presentation('slides-official/chapter-01-algorithms/Meeting1-Algorithms-s.pptx')
for slide in prs.slides:
    for shape in slide.shapes:
        if hasattr(shape, "text"):
            print(shape.text)
```

### File Management

**Write Permissions**:
- ✅ `student-playground/` - ONLY directory Dr. Laila can write to
- ❌ All other directories - READ ONLY

**File Organization**:
```
student-playground/
├── week-01-algorithms/
│   ├── flowchart-practice.md
│   └── pseudocode-examples.py
├── week-02-fundamentals/
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
- Update course calendar in `.claude/course-calendar.yaml`
- Add more starter questions based on student needs

## Customization Guide

### Adjusting Dr. Laila's Personality

Edit: `.claude/agents/learning-assistant.md` or `.github/chatmodes/learning-assistant.chatmode.md`

Change sections like:
- **Personality traits**: More strict, more friendly, etc.
- **Teaching style**: More hints, less hints, etc.
- **Language preference**: More Arabic, more English, etc.

### Updating Course Schedule

Edit: `.claude/course-calendar.yaml`

Modify:
- Week dates
- Topics
- Directory mappings
- Assessment information

### Adding New Capabilities

In the agent files, you can add:
- New question types to handle
- Different response formats
- Additional resources to reference
- Custom starter questions for specific scenarios

## Testing Dr. Laila

### Recommended Test Scenarios:

1. **Week Awareness**:
   - Test during different weeks
   - Verify correct materials are loaded
   - Check starter questions match the week

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
- Verify slides are in correct directory
- For PPTX: Install `python-pptx` (`pip install python-pptx`)
- For PDF: Should work automatically

### "Wrong week detected"
- Check system date/time is correct
- Verify dates in `.claude/course-calendar.yaml`
- Course starts October 12, 2025

### "@learning-assistant not working (Copilot)"
- Ensure GitHub Copilot subscription is active
- Check `.github/chatmodes/learning-assistant.chatmode.md` exists
- Restart VS Code

## Privacy & Data

### What's Shared with Students:
- ✅ Agent configuration files (`.claude/agents/`, `.github/chatmodes/`)
- ✅ Course calendar (`.claude/course-calendar.yaml`)
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
4. **Quiz Generator**: Create weekly quizzes automatically
5. **Exam Simulator**: Full practice exams with grading
6. **Video Recommendations**: Link to relevant tutorials
7. **Office Hours Integration**: Connect to instructor calendar

### Community Contributions:

Students could contribute:
- Example questions to starter questions database
- Common debugging scenarios
- Practice problems
- Translations improvements

## Credits

**Created by**: Mohammad Al-Marie
**For**: M110 Python Programming - AOU Amman
**Semester**: Spring 2024-2025
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
- Course calendar: `.claude/course-calendar.yaml`
- Student guide: `HOW-TO-USE-DR-LAILA.md`
- Playground: `student-playground/`

### Dr. Laila's Workspace:
- **Read from**: Anywhere in repository
- **Write to**: Only `student-playground/`

### Course Timeline:
- **Start**: October 12, 2025
- **Weeks**: 13 (plus self-study topics)
- **Schedule**: Sunday lectures (2-4pm), Tuseday labs (1hr online)

---

**Dr. Laila is ready to help students learn Python! 🐍✨**
