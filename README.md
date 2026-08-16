# M110 Python Programming
# M110 برمجة بايثون

<div align="center">

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Course](https://img.shields.io/badge/Course-M110-green.svg)
![University](https://img.shields.io/badge/University-AOU%20Amman-red.svg)
![Status](https://img.shields.io/badge/Status-Archived-lightgrey.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

**Arab Open University - Amman Branch**

**الجامعة العربية المفتوحة - فرع عمان**

</div>

> **This course is no longer taught live.** These materials and Dr. Laila remain here, free, for any M110 student who finds them.
>
> **لم يعد هذا المقرر يُدرَّس بشكل مباشر.** هذه المواد ود. ليلى تبقى هنا، مجاناً، لأي طالب في مقرر M110.

---

## What This Is
## ما هذا المستودع

Two things, and they work together:

شيئان اثنان، ويعملان معاً:

1. **The official AOU slides for all twelve M110 topics** — every deck as a PDF, as PowerPoint, and as extracted plain text. These are the source of truth. The assessments were written from them.
2. **Dr. Laila (د. ليلى)** — an AI study guide who teaches *from those slides*. She reads the extracted text before she answers, cites the chapter and slide heading she took it from, and builds the explanations, worked examples and practice problems you need, on request.

<!-- -->

1. **الشرائح الرسمية للجامعة العربية المفتوحة لجميع مواضيع M110 الاثني عشر** — كل ملف بصيغة PDF وPowerPoint ونص مُستخرَج. هذه هي المرجع الموثوق، ومنها كُتبت التقييمات.
2. **د. ليلى** — مساعدة تعلّم ذكية تُدرّس *انطلاقاً من تلك الشرائح*. تقرأ النص المستخرج قبل أن تجيب، وتذكر الفصل وعنوان الشريحة الذي أخذت منه، وتبني لك الشروحات والأمثلة والتمارين عند الطلب.

You do not need a class, a schedule or a teacher to use this. You need Python, a text editor, and a question.

لا تحتاج إلى صف دراسي ولا جدول ولا مدرّس لاستخدام هذا المستودع. تحتاج فقط إلى بايثون ومحرّر نصوص وسؤال.

<div align="center">

[![M110 Python Course Overview](https://img.youtube.com/vi/U5vfBpbVwsg/maxresdefault.jpg)](https://youtu.be/U5vfBpbVwsg?si=cM8AoHqlV0A1C1q5)

**[Watch: an overview of the course, with Arabic voiceover](https://youtu.be/U5vfBpbVwsg?si=cM8AoHqlV0A1C1q5)**

**[شاهد: نظرة عامة على المقرر، بتعليق صوتي بالعربية](https://youtu.be/U5vfBpbVwsg?si=cM8AoHqlV0A1C1q5)**

*This overview was recorded while the course was running live, so it may mention dates or a schedule that no longer apply. Everything it explains about the material itself is still accurate.*

*سُجّلت هذه النظرة العامة أثناء تدريس المقرر بشكل مباشر، لذا قد تذكر تواريخ أو جدولاً لم يعد قائماً. أما ما تشرحه عن المادة نفسها فما زال صحيحاً.*

*Generated using NotebookLM by Google | مُولّد باستخدام NotebookLM من Google*

</div>

---

## Start Here
## ابدأ من هنا

Three steps. Fifteen minutes if nothing is installed yet.

ثلاث خطوات. خمس عشرة دقيقة إذا لم يكن لديك شيء مثبّت بعد.

### 1. Get the repository
### 1. احصل على المستودع

```bash
git clone https://github.com/marie55/python-m110.git
cd python-m110
```

No Git yet? Install it first — [Git installation guide](resources/setup-guides/03-git-installation.md) — or download the repository as a ZIP from GitHub. There is also a walkthrough of cloning: [cloning the course repository](resources/setup-guides/06-github-repo-cloning.md).

لا يوجد لديك Git بعد؟ ثبّته أولاً — [دليل تثبيت Git](resources/setup-guides/03-git-installation.md) — أو نزّل المستودع كملف ZIP من GitHub. وهناك أيضاً شرح خطوة بخطوة لعملية الاستنساخ: [استنساخ مستودع المقرر](resources/setup-guides/06-github-repo-cloning.md).

### 2. Install Python and VS Code
### 2. ثبّت بايثون و VS Code

- [Install Python](resources/setup-guides/01-python-installation.md) (3.9 or newer)
- [Install VS Code](resources/setup-guides/02-vscode-installation.md)
- [Add the Python extension to VS Code](resources/setup-guides/05-python-extension-vscode.md)

<!-- -->

- [تثبيت بايثون](resources/setup-guides/01-python-installation.md) (الإصدار 3.9 أو أحدث)
- [تثبيت VS Code](resources/setup-guides/02-vscode-installation.md)
- [إضافة امتداد بايثون إلى VS Code](resources/setup-guides/05-python-extension-vscode.md)

M110 runs on Python's standard library. `turtle` and `tkinter` ship with Python itself, so there is nothing extra to install before you start.

يعتمد مقرر M110 على المكتبة القياسية لبايثون. وحدتا `turtle` و`tkinter` تأتيان مع بايثون نفسه، لذا لا يوجد ما يلزم تثبيته إضافياً قبل أن تبدأ.

**Check it works** — run the first program in the repository:

**تأكد أن كل شيء يعمل** — شغّل أول برنامج في المستودع:

```bash
python code-examples/chapter-01-algorithms/01_sequence_average.py
```

If it asks you for input, you are set. If it does not, the [troubleshooting guide](resources/setup-guides/10-troubleshooting-common-issues.md) and [running your first program](resources/setup-guides/07-running-first-program.md) cover the usual causes.

إذا طلب منك إدخال بيانات، فأنت جاهز. وإذا لم يعمل، فإن [دليل حل المشكلات الشائعة](resources/setup-guides/10-troubleshooting-common-issues.md) و[تشغيل أول برنامج لك](resources/setup-guides/07-running-first-program.md) يغطيان الأسباب المعتادة.

### 3. Meet Dr. Laila
### 3. تعرّف على د. ليلى

Install the [Claude Code extension](resources/setup-guides/08-claude-code-extension-setup.md) in VS Code, open this repository folder, then type into the chat:

ثبّت [امتداد Claude Code](resources/setup-guides/08-claude-code-extension-setup.md) في VS Code، وافتح مجلد هذا المستودع، ثم اكتب في المحادثة:

```
/laila
```

She will greet you and ask which chapter you want to work on. If you do not know, tell her that — she will start you at the beginning.

سترحّب بك وتسألك عن الفصل الذي تريد العمل عليه. وإذا كنت لا تعرف، فقل لها ذلك — ستبدأ بك من البداية.

Using GitHub Copilot instead? [Set it up](resources/setup-guides/09-github-copilot-setup.md), then call `@learning-assistant` in Copilot chat.

تستخدم GitHub Copilot بدلاً من ذلك؟ [اضبطه](resources/setup-guides/09-github-copilot-setup.md)، ثم استدعِ `@learning-assistant` في محادثة Copilot.

---

## The Learning Path
## مسار التعلّم

A suggested order through the material. It deliberately differs from the chapter numbering: the self-study topics are slotted where they reinforce whatever comes just before them.

ترتيب مقترح للسير في المادة. وهو يختلف عمداً عن ترقيم الفصول: فمواضيع الدراسة الذاتية موضوعة في الأماكن التي تُرسّخ ما قبلها.

| # | Chapter / الفصل | Topic | الموضوع | Slides / الشرائح |
|---|---|---|---|---|
| 1 | 1 | Algorithms: Flowcharts & Pseudocodes | خوارزميات: مخططات انسيابية وأكواد زائفة | [chapter-01-algorithms/](slides-official/chapter-01-algorithms/) |
| 2 | 2 | Fundamentals of Python Programming | أساسيات برمجة بايثون | [chapter-02-fundamentals/](slides-official/chapter-02-fundamentals/) |
| 3 | 3 | Decision Structures and Boolean Logic | هياكل اتخاذ القرار والمنطق البولياني | [chapter-03-decision-structures/](slides-official/chapter-03-decision-structures/) |
| 4 | 4 | Repetition Structures | هياكل التكرار | [chapter-04-repetition/](slides-official/chapter-04-repetition/) |
| 5 | SS1 | Turtle Graphics | رسومات السلحفاة | [ss1-turtle-graphics/](slides-official/ss1-turtle-graphics/) |
| 6 | 7 | Collection Data Types: Lists and Tuples | أنواع البيانات التجميعية: القوائم والصفوف | [chapter-07-lists-tuples/](slides-official/chapter-07-lists-tuples/) |
| 7 | SS3 | Dictionaries and Sets | القواميس والمجموعات | [ss3-dictionaries-sets/](slides-official/ss3-dictionaries-sets/) |
| 8 | 5 | Functions | الدوال | [chapter-05-functions/](slides-official/chapter-05-functions/) |
| 9 | SS2 | Recursion | العودية | [ss2-recursion/](slides-official/ss2-recursion/) |
| 10 | 6 | Files and Exceptions | الملفات والاستثناءات | [chapter-06-files-exceptions/](slides-official/chapter-06-files-exceptions/) |
| 11 | 10 | Classes and Object-Oriented Programming | الفئات والبرمجة الكائنية التوجه | [chapter-10-oop/](slides-official/chapter-10-oop/) |
| 12 | 13 | GUI Programming | برمجة الواجهات الرسومية | [chapter-13-gui/](slides-official/chapter-13-gui/) |

The chapter numbers are the official course's own, and they are not contiguous — M110 has no Chapter 8, 9, 11 or 12. That is correct, not a missing folder. `SS1`, `SS2` and `SS3` are the self-study topics.

أرقام الفصول هي أرقام المقرر الرسمية، وهي غير متسلسلة — فلا يوجد في M110 فصل 8 أو 9 أو 11 أو 12. هذا صحيح وليس مجلداً ناقصاً. أما `SS1` و`SS2` و`SS3` فهي مواضيع الدراسة الذاتية.

Nothing forces you to follow this order. Start wherever your question is.

لا شيء يُلزمك باتباع هذا الترتيب. ابدأ من حيث يكون سؤالك.

### Working Through a Chapter
### كيف تدرس فصلاً

1. **Open the PDF** for that chapter in [`slides-official/`](slides-official/) and read it. The PDF is the only version that contains the flowcharts and diagrams — see the [slides guide](slides-official/README.md) for why that matters.
2. **Run `/laila` and name the chapter.** She reads the official text for it and teaches from there, in English or Arabic, at whatever pace you need.
3. **Type the code yourself.** Do not copy and paste it. Typing is what builds the memory.
4. **Ask her for practice problems**, and try each one before you ask for the answer.
5. **When you are stuck**, read the error message — [this guide teaches you how](resources/python-guides/02-reading-error-messages.md) — then ask her about the specific line.

<!-- -->

1. **افتح ملف PDF** الخاص بالفصل في [`slides-official/`](slides-official/) واقرأه. نسخة PDF هي الوحيدة التي تحتوي على المخططات الانسيابية والأشكال — راجع [دليل الشرائح](slides-official/README.md) لمعرفة السبب.
2. **شغّل `/laila` واذكر اسم الفصل.** ستقرأ النص الرسمي الخاص به وتُدرّسه لك، بالإنجليزية أو بالعربية، وبالسرعة التي تناسبك.
3. **اكتب الكود بنفسك.** لا تنسخه وتلصقه. الكتابة هي ما يبني الذاكرة.
4. **اطلب منها تمارين**، وحاول حل كل تمرين قبل أن تسأل عن الإجابة.
5. **عندما تتعثّر**، اقرأ رسالة الخطأ — [هذا الدليل يعلّمك كيف](resources/python-guides/02-reading-error-messages.md) — ثم اسألها عن السطر تحديداً.

---

## How Dr. Laila Works
## كيف تعمل د. ليلى

She is the guide here. There is no lecture to defer to and no instructor on call, so she answers the question herself, now.

هي المرشدة هنا. لا توجد محاضرة تُحيلك إليها ولا مدرّس متاح، لذلك تجيب على سؤالك بنفسها، وفي حينه.

**What she does / ما تفعله:**

- Reads the official slide text for your chapter **before** answering, and tells you which chapter and which slide heading the answer came from
- Explains in English or Arabic, whichever you ask for
- Writes runnable code examples, retyped and tested — never pasted out of the extracted text, which has broken indentation and mangled quotes
- Sends you to the chapter PDF when the answer depends on a flowchart or diagram, because figures are images and she genuinely cannot see them
- Builds the notes, worked examples and practice problems for any chapter on request, and saves them into [`student-playground/`](student-playground/) so you keep them
- Guides you through debugging by teaching you to read the error, rather than silently fixing it

<!-- -->

- تقرأ النص الرسمي لشرائح فصلك **قبل** أن تجيب، وتخبرك بالفصل وعنوان الشريحة التي جاءت منها الإجابة
- تشرح بالإنجليزية أو بالعربية، أيّهما طلبت
- تكتب أمثلة برمجية قابلة للتشغيل، تعيد كتابتها وتختبرها — ولا تنسخها من النص المستخرج، لأن إزاحاته وعلامات اقتباسه مُعطوبة
- تُحيلك إلى ملف PDF الخاص بالفصل عندما تعتمد الإجابة على مخطط أو شكل، لأن الأشكال صور ولا تستطيع رؤيتها فعلاً
- تبني لك الملاحظات والأمثلة والتمارين لأي فصل عند الطلب، وتحفظها في [`student-playground/`](student-playground/) لتبقى معك
- ترشدك في تصحيح الأخطاء بتعليمك قراءة رسالة الخطأ، بدلاً من إصلاحها بصمت

**What she will not do / ما لن تفعله:**

- Hand you the answer to a TMA question or any other graded work
- Write a complete assignment solution for you
- Produce exam answers
- Change anything under `slides-official/` — the official record stays exactly as it is

<!-- -->

- تعطيك إجابة سؤال في الواجب المصحح (TMA) أو أي عمل يُرصد له علامة
- تكتب لك حلاً كاملاً لواجب
- تقدّم إجابات امتحانات
- تعدّل أي شيء داخل `slides-official/` — السجل الرسمي يبقى كما هو تماماً

This is not her being unhelpful. Work you did not do teaches you nothing, and the person it costs is you.

هذا ليس تقصيراً منها. فالعمل الذي لم تقم به أنت لا يعلّمك شيئاً، والخاسر الوحيد هو أنت.

📖 Full guide: [HOW-TO-USE-DR-LAILA.md](HOW-TO-USE-DR-LAILA.md) — how to phrase questions, what to expect, and worked example conversations.

📖 الدليل الكامل: [HOW-TO-USE-DR-LAILA.md](HOW-TO-USE-DR-LAILA.md) — كيف تصوغ أسئلتك، وماذا تتوقع، وأمثلة على محادثات كاملة.

---

## What's in the Repository
## محتويات المستودع

```
python-m110/
│
├── slides-official/              # SOURCE OF TRUTH — all 12 topics
│   ├── chapter-01-algorithms/    #   each folder: PDF + PPTX + extracted .pptx.txt
│   │   … chapter-13-gui/
│   └── ss1-turtle-graphics/, ss2-recursion/, ss3-dictionaries-sets/
│
├── lectures/
│   └── chapter-01-algorithms/    # notes, a written lecture, and further reading
│
├── code-examples/
│   ├── chapter-01-algorithms/    # 7 runnable programs
│   └── chapter-02-fundamentals/  # 1 starter program
│
├── exercises/
│   └── chapter-01-algorithms/    # 2 exercise files + 1 worked solution
│
├── resources/                    # setup, Git, Python and VS Code guides, cheatsheets, FAQ
│
├── student-playground/           # your workspace — where Dr. Laila writes
├── student-contributions/        # share your own work here
│
└── .claude/                      # Dr. Laila's definition and the course map
```

**Be clear about what is and is not here.** The official slides cover all twelve topics. The `resources/` guides are complete. **Chapter 1** is written up end to end — notes, worked code, exercises with a solution — as a sample of what good material for a chapter looks like, plus one starter program for Chapter 2. For every other chapter, the slides are present and **Dr. Laila builds the walkthrough from them when you ask**. Nothing is missing and nothing is being prepared.

**لنكن واضحين بشأن ما هو موجود وما هو غير موجود.** الشرائح الرسمية تغطي المواضيع الاثني عشر كلها. وأدلة `resources/` مكتملة. أما **الفصل الأول** فمكتوب بالكامل — ملاحظات وأكواد مشروحة وتمارين مع حل — بوصفه نموذجاً لما ينبغي أن تكون عليه مادة أي فصل، إضافة إلى برنامج تمهيدي واحد للفصل الثاني. وبالنسبة لبقية الفصول، فالشرائح موجودة و**د. ليلى تبني لك الشرح منها عندما تطلب**. لا ينقص شيء، ولا يوجد شيء قيد الإعداد.

### The `resources/` Folder
### مجلد `resources/`

| Folder | What's in it | ماذا يحتوي |
|---|---|---|
| [setup-guides/](resources/setup-guides/) | 10 guides — Python, VS Code, the Python extension, Git, virtual environments, cloning this repository, running your first program, the Claude Code and Copilot extensions, troubleshooting | 10 أدلة — بايثون، VS Code، امتداد بايثون، Git، البيئات الافتراضية، استنساخ هذا المستودع، تشغيل أول برنامج، امتدادا Claude Code وCopilot، حل المشكلات |
| [git-guides/](resources/git-guides/) | 5 guides — what Git is, the commands you actually use, cloning, staying updated, a workflow that fits studying | 5 أدلة — ما هو Git، الأوامر التي ستستخدمها فعلاً، الاستنساخ، متابعة التحديثات، سير عمل يناسب الدراسة |
| [python-guides/](resources/python-guides/) | 5 guides — quick reference, reading error messages, PEP 8 for beginners, how to learn effectively, where to read more | 5 أدلة — مرجع سريع، قراءة رسائل الخطأ، PEP 8 للمبتدئين، كيف تتعلم بفعالية، أين تقرأ المزيد |
| [vscode-guides/](resources/vscode-guides/) | 4 guides — the interface, essential shortcuts, Python development, the built-in terminal | 4 أدلة — الواجهة، الاختصارات الأساسية، تطوير بايثون، الطرفية المدمجة |
| [cheatsheets/](resources/cheatsheets/) | 5 one-page references — Python syntax, control structures, Git commands, VS Code shortcuts, terminal commands | 5 مراجع من صفحة واحدة — صياغة بايثون، هياكل التحكم، أوامر Git، اختصارات VS Code، أوامر الطرفية |
| [video-tutorials/](resources/video-tutorials/) | Curated YouTube channels and videos | قنوات ومقاطع يوتيوب مختارة |
| [faq.md](resources/faq.md) | Common questions, answered | الأسئلة الشائعة، مع إجاباتها |

The chapter index and file paths Dr. Laila reads live in [`.claude/course-map.yaml`](.claude/course-map.yaml). The slide folder has its own guide explaining which file format to use and what the text extraction loses: [`slides-official/README.md`](slides-official/README.md).

فهرس الفصول ومسارات الملفات التي تقرأها د. ليلى موجودة في [`.claude/course-map.yaml`](.claude/course-map.yaml). ولمجلد الشرائح دليله الخاص الذي يشرح أي صيغة تستخدم وما الذي يفقده استخراج النص: [`slides-official/README.md`](slides-official/README.md).

---

## Assessments
## التقييمات

What each assessment covered. Everything assessed came from the official slides, so revise from `slides-official/`.

ما الذي غطّاه كل تقييم. كل ما يُختبر مصدره الشرائح الرسمية، لذا راجع من `slides-official/`.

| Assessment | Covers | يغطي |
|---|---|---|
| **MTA** — Mid-Term Assessment | Through Collection Data Types (Chapters 1-4 and 7) | حتى أنواع البيانات التجميعية (الفصول 1-4 و7) |
| **TMA** — Tutor-Marked Assignment (Lab Test) | MTA material plus SS1, SS2 and SS3 | مادة الـ MTA إضافة إلى SS1 وSS2 وSS3 |
| **Final Exam** | All regular chapters; excludes the self-study topics | جميع الفصول النظامية؛ باستثناء مواضيع الدراسة الذاتية |

Coverage only. Grade weightings and dates applied to one specific offering of the course and are deliberately left out — if you are sitting M110 now, take those from your own tutor, not from here.

التغطية فقط. أما نسب العلامات والتواريخ فكانت تخص طرحاً بعينه من المقرر وقد حُذفت عمداً — إذا كنت تدرس M110 حالياً فخذها من مدرّسك أنت، لا من هنا.

Dr. Laila can build you a revision plan for any of the three, and practice problems to go with it. She will never present anything as an actual assessment question.

يمكن لـ د. ليلى أن تبني لك خطة مراجعة لأي من الثلاثة، مع تمارين تدريبية تناسبها. ولن تقدّم أبداً أي شيء على أنه سؤال امتحان حقيقي.

---

## Built By
## من بناه

### Mohammad Al-Marie
### محمد المرعي

Mohammad built this repository while teaching M110 at Arab Open University, Amman. He brings over 15 years of programming experience and a conviction that the gap between what universities teach and what the industry actually does is bridgeable — and that first-year is the right time to start bridging it.

بنى محمد هذا المستودع أثناء تدريسه مقرر M110 في الجامعة العربية المفتوحة بعمّان. يتمتع بخبرة تزيد على 15 عاماً في البرمجة، وبقناعة أن الفجوة بين ما تُدرّسه الجامعات وما يمارسه سوق العمل قابلة للردم — وأن السنة الأولى هي الوقت المناسب للبدء بردمها.

**Education / التعليم**

- M.Sc. in Artificial Intelligence, Yarmouk University (2021) — ماجستير في الذكاء الاصطناعي، جامعة اليرموك
- High Diploma in Computer Science, Jordan University of Science and Technology (2014) — دبلوم عالٍ في علوم الحاسوب، جامعة العلوم والتكنولوجيا الأردنية
- B.Sc. in Computer Science, Zarqa University (2005) — بكالوريوس في علوم الحاسوب، جامعة الزرقاء

**Professional experience / الخبرة المهنية**

- AI Lead, BeSourceX — قائد الذكاء الاصطناعي
- AI Solutions Engineer / Full-Stack AI Developer, Mannai ICT — مهندس حلول الذكاء الاصطناعي
- AI Solutions Architect, DRP Consulting Inc. (USA) — مهندس معماري لحلول الذكاء الاصطناعي
- Machine Learning Engineer, ENTREVIABLE — مهندس تعلّم آلي
- Teaching & Research Assistant, Computer Science Dept., Yarmouk University — مساعد تدريس وبحث، قسم علوم الحاسوب

### The Ideas Behind the Course
### الأفكار التي بُني عليها المقرر

**1. Bridge the academia-industry gap.** Not just Python syntax, but the practices around it: Git for version control, VS Code as a real editor, code that meets professional standards.

**1. اردم الفجوة بين الأكاديميا وسوق العمل.** ليست صياغة بايثون فحسب، بل الممارسات المحيطة بها: Git لإدارة الإصدارات، وVS Code كمحرّر حقيقي، وكود يلبي المعايير المهنية.

**2. Practical skills matter.** Every concept connects to something real. Algorithms solve actual problems, functions organise production code, OOP structures large systems.

**2. المهارات العملية مهمة.** كل مفهوم مرتبط بشيء واقعي. الخوارزميات تحل مشاكل فعلية، والدوال تنظّم كود الإنتاج، والبرمجة الكائنية تبني أنظمة كبيرة.

**3. Think first, code later.** Plan with a flowchart or pseudocode before writing a line. That habit is what separates a programmer from someone who types code.

**3. فكّر أولاً، ثم ابرمج.** خطّط بمخطط انسيابي أو كود زائف قبل كتابة أي سطر. هذه العادة هي ما يفصل المبرمج عمّن يكتب كوداً فحسب.

**4. Use AI responsibly.** Dr. Laila is a learning companion, not an answer machine. Used well, an AI assistant deepens understanding; used to skip the work, it quietly replaces it.

**4. استخدم الذكاء الاصطناعي بمسؤولية.** د. ليلى رفيقة تعلّم، لا آلة إجابات. فإذا أحسنت استخدامها عمّقت فهمك، وإذا استخدمتها لتتجاوز الجهد استبدلته بهدوء.

**5. No question is too basic.** The material starts from zero and builds. Everything is available in English and Arabic, because struggling with the language should never be the reason you struggle with the programming.

**5. لا يوجد سؤال بسيط أكثر من اللازم.** المادة تبدأ من الصفر وتتدرّج. وكل شيء متاح بالإنجليزية والعربية، لأن الصعوبة في اللغة يجب ألا تكون سبب صعوبتك في البرمجة.

### A Note to Whoever Is Reading This
### كلمة لمن يقرأ هذا

Programming is hard. It is supposed to be. The moment you are stuck and frustrated is not the moment you are failing — it is the moment you are actually learning. Everyone who writes code for a living has sat exactly where you are sitting.

البرمجة صعبة. ومن المفترض أن تكون كذلك. اللحظة التي تتعثّر فيها وتشعر بالإحباط ليست لحظة فشلك — بل هي اللحظة التي تتعلّم فيها فعلاً. كل من يكتب الكود مهنةً جلس يوماً في المكان الذي تجلس فيه الآن.

The course may be over, but the material is not. Take it, use it, and finish what you started.

قد يكون المقرر قد انتهى، لكن المادة لم تنتهِ. خذها، واستخدمها، وأكمل ما بدأته.

— **Mohammad Al-Marie**

---

## License and Attribution
## الترخيص وحقوق الملكية

**Repository content** — the guides, code examples, exercises, lecture notes and Dr. Laila's definition — is released under the [MIT License](LICENSE). Use it, copy it, adapt it.

**محتوى المستودع** — الأدلة والأمثلة البرمجية والتمارين وملاحظات المحاضرات وتعريف د. ليلى — منشور بموجب [رخصة MIT](LICENSE). استخدمه وانسخه وعدّل عليه.

**The official slide decks** under [`slides-official/`](slides-official/) are the copyright of Arab Open University (AOU) and are redistributed here for student study. They are not covered by the MIT License above.

**الشرائح الرسمية** الموجودة في [`slides-official/`](slides-official/) محفوظة الحقوق للجامعة العربية المفتوحة (AOU)، ويُعاد نشرها هنا لغرض دراسة الطلاب. وهي غير مشمولة برخصة MIT أعلاه.

**This repository is not affiliated with, nor endorsed by, Arab Open University.** It is a personal teaching archive kept public for students.

**هذا المستودع غير تابع للجامعة العربية المفتوحة وغير معتمد من قبلها.** وهو أرشيف تدريسي شخصي أُبقي متاحاً للعموم من أجل الطلاب.

**Contributions are welcome.** If you fix something, improve an explanation or add an example, open a pull request — see [`student-contributions/`](student-contributions/).

**المساهمات مرحّب بها.** إذا صحّحت شيئاً أو حسّنت شرحاً أو أضفت مثالاً، فافتح طلب سحب (pull request) — راجع [`student-contributions/`](student-contributions/).

---

<div align="center">

**M110 Python Programming**

**Arab Open University - Amman Branch**

**الجامعة العربية المفتوحة - فرع عمان**

Clone it, open it, type `/laila`, and start.

استنسخه، وافتحه، واكتب `/laila`، وابدأ.

</div>
