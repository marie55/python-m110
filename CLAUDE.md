
# M110 Python Programming — Repository Guide for AI Assistants

This file is loaded automatically by AI coding assistants working in this
repository. Read the routing section first: what you should do here depends
entirely on who you are working for.

---

## Who Are You Working For?

### If you are helping a student learn — this is almost everyone

**Use Dr. Laila.** She is the teaching assistant this repository was built
around, defined in `.claude/agents/learning-assistant.md` (and mirrored for
Copilot in `.github/chatmodes/learning-assistant.chatmode.md`). She carries
rules this file does not repeat — how to ground an answer in the official
slide text, why extracted code must be retyped rather than pasted, and when to
send a student to the PDF because a figure cannot be read out of text at all.

A student invokes her with `/laila` in Claude Code, or `@learning-assistant`
in Copilot chat.

Two rules bind you whether or not she is active:

- **Write only to `student-playground/`** (work you build with the student) and
  **`.assistant-memory/`** (notes on their learning, so the next session does
  not start from zero). Never modify course materials, guides, examples or
  exercises. A student's questions are not a mandate to edit the repository.
- **Never do graded work for a student.** Teach the concept, show a worked
  example of something adjacent, then let them write their own.

`.assistant-memory/README.md` explains the memory system, including how to
drive it from Copilot, Codex, Qwen or any other tool. Everything in that folder
except the README is gitignored — those notes describe what a student found
difficult and must never reach GitHub.

### If you are helping maintain or extend this repository

Everything below is for you — the conventions every piece of content here
already follows. Match them rather than inventing new ones.

### Either way

`slides-official/` is **read-only**. Those are the official Arab Open
University decks, the assessments were written from them, and the extracted
`.txt` files ship exactly as produced — including their broken quote
characters. Never "repair" them.

---

## Course Info
**Institution**: Arab Open University (AOU) - Amman Branch
**Course Name**: Python Programming
**Course Code**: M110
**Level**: First/Second Year Undergraduate
**Status**: Archived — self-study. No live semester, no schedule; students arrive at any chapter, in any order.

**Chapter Map** (source of truth: `.claude/course-map.yaml`):
- Chapter 1: Algorithms - Flowcharts & Pseudocodes
- Chapter 2: Fundamentals of Python Programming
- Chapter 3: Decision Structures and Boolean Logic
- Chapter 4: Repetition Structures
- Chapter 5: Functions
- Chapter 6: Files and Exceptions
- Chapter 7: Collection Data Types - Lists and Tuples
- Chapter 10: Classes and Object-Oriented Programming
- Chapter 13: GUI Programming
- Self-Study: SS1-Turtle Graphics, SS2-Recursion, SS3-Dictionaries and Sets

Chapter numbers are not contiguous (no 8, 9, 11 or 12 — those were lab/revision
weeks in the original live course), and the numeric order is not the suggested
teaching order. See `learning_path` in `.claude/course-map.yaml` for the
recommended sequence.

---

## Instructor Info
**Instructor Name**: Mohammad Al-Marie

### Education:
- Master's Degree in Artificial Intelligence, Yarmouk University, 2021
- High Diploma in Computer Science, Jordan University of Sciences and Technology, 2014
- B.Sc. in Computer Sciences, Zarka University, 2005

### Recent Work Experience:
- AI LEAD: BeSourceX, June 2025 - Present
- AI SOLUTIONS ENGINEER / FULL-STACK AI DEVELOPER: Mannai ICT, October 2024 - June 2025
- AI SOLUTIONS ARCHITECT: DRP Consulting Inc. USA, May 2023 - May 2024
- MACHINE LEARNING ENGINEER: ENTREVIABLE, June 2022 - May 2023
- TEACHING & RESEARCH ASSISTANT: Dept. of Computer Science, Yarmouk University, Jordan. Feb 2019 - June 2020

---

## Teaching Philosophy & Course Goals

### Core Objectives:
1. **Bridge Academia-Industry Gap**: Help students understand real-world programming practices early
2. **Practical Skills**: Beyond theory - teach tools, workflows, and professional development practices
3. **Git Literacy**: Use GitHub as learning platform to introduce version control
4. **Beginner-Friendly**: Students are first/second year with limited technical experience
5. **Professional Standards**: Introduce industry best practices (PEP 8, documentation, testing) gradually

### Course Constraints:
- **Official slides are fixed**: Provided by university global course supervisor, cannot be modified
- **Exam references official slides**: All assessments based on official course materials
- **Instructor adds practical layer**: Supplementary materials, code examples, exercises, real-world context

---

## Content Creation Guidelines for LLMs

### 1. Documentation Style

#### Length & Complexity:
- **Keep it concise**: Students are beginners - avoid overwhelming them with too much text
- **Direct to the point**: Each document should have ONE clear purpose
- **Progressive difficulty**: Start simple, build complexity gradually
- **Scannable format**: Use bullet points, short paragraphs, clear headings
- **Practical examples**: Show, don't just tell

**Bad Example**:
```markdown
# Functions in Python
Functions are reusable blocks of code that perform specific tasks. They help in code organization, reusability, and modularity. Functions can accept parameters and return values. In Python, functions are defined using the def keyword followed by the function name and parentheses. [continues for 3 more paragraphs...]
```

**Good Example**:
```markdown
# Functions in Python

## What is a Function?
A reusable piece of code that does a specific task.

## Basic Syntax:
def greet(name):
    return f"Hello, {name}!"

## Why Use Functions?
- Avoid repeating code
- Make code easier to read
- Fix bugs in one place

## Try It:
[Link to example code]
```

#### Technical Content:
- **Simplify technical jargon**: Explain terms in plain language first
- **Stay within scope**: Only teach what's needed for the course
- **Provide context**: Explain WHY something matters, not just HOW
- **Use analogies**: Relate concepts to real-world examples
- **Include visuals when possible**: Flowcharts, diagrams, screenshots

### 2. Bilingual Content (English & Arabic)

#### Main Documentation (README files, setup guides, important docs):
- **Write in BOTH English and Arabic**
- **Format**: English paragraph, followed immediately by Arabic translation
- **Consistency**: Maintain same structure in both languages

**Example**:
```markdown
# Getting Started with Python
# البدء مع بايثون

Python is a beginner-friendly programming language used for web development, data science, and automation.
بايثون هي لغة برمجة سهلة للمبتدئين تُستخدم في تطوير الويب وعلوم البيانات والأتمتة.

## Installation Steps
## خطوات التثبيت

1. Download Python from python.org
1. قم بتحميل بايثون من python.org
```

#### Code Comments:
- **Dual-language comments** for important explanations
- **English first**, then Arabic in parentheses or next line

**Example**:
```python
# Calculate the average of numbers
# حساب متوسط الأرقام
def calculate_average(numbers):
    """
    Returns the average of a list of numbers.
    يُرجع متوسط قائمة من الأرقام.
    """
    total = sum(numbers)  # Sum all numbers / جمع جميع الأرقام
    count = len(numbers)  # Count of numbers / عدد الأرقام
    return total / count  # Return average / إرجاع المتوسط
```

#### When to use bilingual vs English-only:
- **Bilingual Required**:
  - Main README.md
  - Setup guides (resources/setup-guides/*)
  - Lab instructions
  - Project guidelines
  - FAQs

- **English-only acceptable**:
  - Code examples (with bilingual comments)
  - Technical documentation beyond scope
  - Advanced optional materials
  - Git commit messages (industry standard)

### 3. Code Examples

#### Quality Standards:
- **Follow PEP 8**: Python style guide
- **Meaningful names**: Variables and functions should be self-documenting
- **Comments in both languages**: Explain the WHY, not the WHAT
- **Complete, runnable code**: No pseudocode unless teaching algorithms
- **Error handling**: Show students proper exception handling
- **Print outputs**: Include example outputs as comments

**Example**:
```python
"""
Student Grade Calculator
حاسبة درجات الطلاب

This program calculates final grades based on assignments and exams.
يحسب هذا البرنامج الدرجات النهائية بناءً على الواجبات والامتحانات.
"""

def calculate_final_grade(assignments, midterm, final):
    """
    Calculate final grade based on course components.
    حساب الدرجة النهائية بناءً على مكونات المقرر.

    Args:
        assignments (list): List of assignment scores (0-100)
        midterm (float): Midterm exam score (0-100)
        final (float): Final exam score (0-100)

    Returns:
        float: Final grade (0-100)
    """
    # Assignments worth 30% / الواجبات تساوي 30%
    assignment_avg = sum(assignments) / len(assignments)
    assignment_score = assignment_avg * 0.30

    # Midterm worth 30% / الامتحان النصفي يساوي 30%
    midterm_score = midterm * 0.30

    # Final worth 40% / الامتحان النهائي يساوي 40%
    final_score = final * 0.40

    # Calculate total / حساب المجموع
    total = assignment_score + midterm_score + final_score

    return round(total, 2)


# Example usage / مثال على الاستخدام
if __name__ == "__main__":
    student_assignments = [85, 90, 88]
    student_midterm = 82
    student_final = 90

    final_grade = calculate_final_grade(
        student_assignments,
        student_midterm,
        student_final
    )

    print(f"Final Grade: {final_grade}%")
    # Output: Final Grade: 87.1%
```

### 4. Repository Structure Awareness

When creating content, understand the file organization:

```
python-m110/
├── slides-official/        # Official course slides (READ-ONLY, reference only)
├── lectures/                # Chapter-by-chapter lecture notes & resources (Chapter 1 so far)
├── code-examples/           # Runnable Python code organized by chapter (Chapters 1-2 so far)
├── exercises/                # Practice problems with solutions (Chapter 1 so far)
├── resources/                # Setup guides, cheatsheets, tutorials
├── student-playground/       # Dr. Laila's workspace (gitignored)
├── student-contributions/    # Open contributions by pull request
├── .assistant-memory/        # Dr. Laila's notes on one student (gitignored except README)
└── .claude/                  # Dr. Laila's definition and course-map.yaml
```

**When asked to create materials**:
- Identify correct directory based on content type
- Follow chapter naming (`chapter-01-algorithms`, `chapter-02-fundamentals`, etc. — see `.claude/course-map.yaml` for every chapter's exact id)
- Cross-reference related materials (link exercises to lectures)
- Maintain consistency across chapters

### 5. Progressive Learning Path

Build content that follows this progression:

**Chapters 1-4**: Foundations
- Basic syntax, variables, control flow
- Simple programs
- Focus on logic and problem-solving
- Minimal technical tooling complexity

**Chapters 5-7**: Intermediate Concepts
- Data structures, functions, file I/O
- Introduce debugging techniques
- More complex programs
- Start discussing code organization

**Chapters 10 & 13**: Advanced Topics
- OOP, GUI programming
- Professional practices
- Code quality and testing
- Introduction to software design patterns

**Self-Study**: Enrichment
- Turtle graphics (fun, visual)
- Recursion (challenging concept)
- Dictionaries and sets (practical data structures)

### 6. Assessment Alignment

**Remember**:
- All exams reference **official slides only**
- Supplementary materials should **enhance understanding**, not introduce contradictory information
- When creating exercises/examples, **align with official slide terminology**
- MTA (Mid-Term Assessment), TMA (Tutor-Marked Assignment), Final all test official content

**Do**:
- Provide additional practice problems that reinforce slide concepts
- Offer real-world examples that illustrate slide material
- Create exercises that deepen understanding of official content

**Don't**:
- Teach alternative approaches that conflict with slides
- Use different terminology than official materials
- Cover topics not in the official curriculum (except as clearly marked "bonus")

### 7. Beginner-Friendly Technical Setup

**Assume students have minimal experience with**:
- Command line / terminal
- Text editors / IDEs
- File system navigation
- Installing software
- Git / version control
- Package management

**When creating setup guides**:
- Include screenshots for every step
- Provide troubleshooting for common errors
- Explain technical terms when first used
- Offer both Mac and Windows instructions
- Test on fresh installations
- Include "What to expect" sections

### 8. Cultural & Language Considerations

**Context**:
- Students are Arab, likely Arabic native speakers
- English proficiency varies
- Some students may prefer Arabic-first explanations
- Technical terms often have English equivalents (even in Arabic tech discourse)

**Best Practices**:
- Use simple English (avoid idioms, complex sentences)
- Provide Arabic translations for complex concepts
- Use internationally recognized examples (avoid US/Western-centric references)
- Be mindful of reading direction in bilingual documents
- Technical terms: use English term + Arabic explanation initially

### 9. Git & GitHub Integration

**Teaching Strategy** (self-paced — frame around engagement, not a calendar):
- First session: Students clone the repository (read-only)
- As they progress: Pull updates occasionally — the repository still receives fixes and new chapter walkthroughs
- Once comfortable: Start creating branches, making changes locally
- When ready to share: Submit contributions via Pull Requests (see `student-contributions/README.md`)
- Throughout: Use Issues for Q&A

**When creating Git guides**:
- Assume zero Git knowledge
- Focus on essential commands only
- Provide copy-paste commands with explanations
- Visual diagrams of Git workflow
- Troubleshooting section for common errors

### 10. Tone & Style

**Do**:
- Encouraging and supportive tone
- Clear, direct language
- Active voice
- Specific, actionable instructions
- Celebrate small wins

**Don't**:
- Condescending language
- Assume prior knowledge
- Use sarcasm or humor that may not translate
- Overuse technical jargon
- Create anxiety about difficulty

**Example - Good**:
```markdown
Great! You've just run your first Python program.
رائع! لقد قمت بتشغيل أول برنامج بايثون لك.

Next, let's try changing the message.
الآن، لنجرب تغيير الرسالة.
```

**Example - Bad**:
```markdown
Obviously, this is trivial for anyone who's programmed before.
If you're still confused at this point, programming might not be for you.
```

---

## Chapter Content Creation Checklist

When asked to create materials for a specific chapter, ensure:

- [ ] Aligned with the chapter map and official slides topic
- [ ] Created in correct directory (lectures/chapter-XX-*/, code-examples/chapter-XX-*/, etc.)
- [ ] Main README.md is bilingual (EN/AR)
- [ ] Code examples include bilingual comments
- [ ] Appropriate difficulty level for the chapter's place in the learning path
- [ ] Cross-referenced with related materials
- [ ] Runnable code examples (tested)
- [ ] Follows PEP 8 style guide
- [ ] Includes example outputs
- [ ] Practice exercises with solutions (in separate directory)
- [ ] Connects theory (official slides) to practice (code examples)

---

## Common LLM Tasks for This Course

### Task 1: Create Chapter Lecture Notes
- Review official slides topic
- Create supplementary notes in `lectures/chapter-XX-*/README.md`
- Bilingual format
- Link to code examples
- Include practice problems
- Add additional resources (videos, articles)

### Task 2: Write Code Examples
- Create runnable Python files in `code-examples/chapter-XX-*/`
- Demonstrate concepts from official slides
- Bilingual comments
- Include example outputs
- Follow PEP 8
- Appropriate difficulty for the chapter

### Task 3: Generate Exercises
- Create practice problems in `exercises/chapter-XX-*/`
- Range of difficulty (easy, medium, hard)
- Solutions in `exercises/chapter-XX-*/solutions/`
- Align with the chapter's topics
- Include hints for difficult problems

### Task 4: Develop Setup Guides
- Step-by-step instructions in `resources/setup-guides/`
- Screenshots and visuals
- Troubleshooting section
- Platform-specific (Windows/Mac/Linux)
- Bilingual (EN/AR)

### Task 5: Create Cheatsheets
- One-page reference in `resources/cheatsheets/`
- Visual and concise
- Most common commands/patterns
- Examples for each item
- Can be English-only with Arabic annotations

### Task 6: Design Lab Sessions
- Lab instructions in `labs/lab-XX/README.md`
- Starter code provided
- Clear objectives and deliverables
- Solution code in separate directory
- Rubric for assessment

---

## Example Prompt Responses

### User: "Create code examples for Chapter 2 - Fundamentals"

**LLM Should**:
1. Check the chapter map (Chapter 2 = Fundamentals of Python Programming)
2. Create files in `code-examples/chapter-02-fundamentals/`
3. Cover: variables, data types, input/output, basic operators
4. Create 5-7 small, focused examples
5. Each file demonstrates ONE concept clearly
6. Bilingual comments
7. Include example outputs
8. Name files descriptively (e.g., `01_variables_and_datatypes.py`, `02_user_input.py`)

### User: "Write a setup guide for VS Code"

**LLM Should**:
1. Create file: `resources/setup-guides/02-vscode-installation.md`
2. Bilingual content (EN/AR)
3. Step-by-step with screenshots (describe where they should go)
4. Sections: Download, Install, First Launch, Basic Configuration
5. Troubleshooting section
6. Platform-specific instructions (Windows/Mac)
7. Next steps (link to next guide: Python extension)

### User: "Help me create README for the repository"

**LLM Should**:
1. Create bilingual `README.md` at root
2. Sections: Course Info, How to Use This Repo, Chapter Map, Setup Instructions, Contributing, Contact
3. Link to setup guides
4. Explain repository structure
5. Instructions for cloning and pulling updates
6. Support information (Dr. Laila, GitHub Issues) — there are no office hours, the course is archived
7. Clear, welcoming tone

---

## Final Notes for LLMs

- **Ask clarifying questions** if task is ambiguous
- **Suggest improvements** to course structure when appropriate
- **Maintain consistency** across all materials
- **Think from student perspective**: first-year, beginner level, learning programming AND tools
- **Reference official slides** when available (treat as source of truth)
- **Be helpful but not overwhelming**: students can be easily discouraged
- **Celebrate progress**: learning to code is hard, acknowledge achievements

---

**Version**: 2.0 — archived, self-study, chapter-based
**Last Updated**: 2026-08-16
**Maintained By**: Mohammad Al-Marie
