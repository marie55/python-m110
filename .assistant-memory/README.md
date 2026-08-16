# Assistant Memory
# ذاكرة المساعِدة

This folder is where Dr. Laila — or any AI assistant you use with this
repository — keeps notes about your learning, so that the next session does not
start from zero.

هذا المجلد هو المكان الذي تحتفظ فيه د. ليلى — أو أي مساعد ذكاء اصطناعي تستخدمه
مع هذا المستودع — بملاحظات عن تعلّمك، حتى لا تبدأ الجلسة التالية من الصفر.

Without it, every conversation begins as if you had never met. With it, the
assistant can pick up where you stopped, avoid re-explaining what already made
sense, and stop reaching for an analogy that did not work for you last time.

بدونه، تبدأ كل محادثة وكأنكما لم تلتقيا من قبل. ومعه، يستطيع المساعد أن يكمل من
حيث توقفت، وأن يتجنّب إعادة شرح ما فهمته أصلاً، وأن يتوقف عن استخدام تشبيه لم
ينفع معك في المرة السابقة.

---

## Your notes are private
## ملاحظاتك خاصة

**Everything in this folder except this README is ignored by Git.** It stays on
your computer. It is never pushed to GitHub, not even if you fork this
repository and push your fork.

**كل ما في هذا المجلد عدا هذا الملف يتجاهله Git.** يبقى على جهازك، ولا يُرفع إلى
GitHub أبداً، حتى لو نسخت هذا المستودع ورفعت نسختك.

That is deliberate. These notes describe what you found difficult, and that is
nobody's business but yours.

وهذا مقصود. فهذه الملاحظات تصف ما وجدته صعباً، وهذا شأنك وحدك لا شأن أحد آخر.

You can read them at any time, edit them, or delete the whole folder. Nothing
breaks if you do — the assistant simply starts fresh.

يمكنك قراءتها في أي وقت، أو تعديلها، أو حذف المجلد بالكامل. لن يتعطل شيء إذا
فعلت — سيبدأ المساعد من جديد ببساطة.

---

## What is in here
## ما الموجود هنا

| File | What it holds |
|------|---------------|
| `MEMORY.md` | A short index — one line per topic. Read this first. |
| `progress.md` | Which chapters you have started, and where each stands. |
| `chapter-NN-topic.md` | A running record for one topic, newest entry at the top. |

| الملف | ما يحتويه |
|------|-----------|
| `MEMORY.md` | فهرس قصير — سطر واحد لكل موضوع. اقرأه أولاً. |
| `progress.md` | الفصول التي بدأتها، وأين وصلت في كل منها. |
| `chapter-NN-topic.md` | سجل متصل لموضوع واحد، أحدث إدخال في الأعلى. |

There is one file per topic, not one per session. Working on loops three times
adds three dated entries to the same file, the way a teacher keeps adding to
your file rather than starting a new one each lesson.

هناك ملف واحد لكل موضوع، لا ملف لكل جلسة. فالعمل على الحلقات ثلاث مرات يضيف ثلاثة
إدخالات مؤرخة إلى الملف نفسه، تماماً كما يواصل المعلّم الكتابة في ملفك بدل أن يبدأ
ملفاً جديداً كل حصة.

---

## What an entry looks like
## كيف يبدو الإدخال

```markdown
---
chapter: 4
topic: Repetition Structures
slides: slides-official/chapter-04-repetition/Meeting4-Repetition Structures-s.pdf
started: 2026-08-16
updated: 2026-08-22
---

# Chapter 4 — Repetition Structures

## 2026-08-22

**Where it got tricky**
Expected the `while` condition to be checked after the body ran, so predicted
one extra pass.

**What made it click**
"Check the ticket before you board." The flowchart on the PDF sealed it.

**Can now do without help**
Traced a three-iteration loop correctly, start to finish.

**Next time**
Sentinel-controlled loops — not covered yet.
```

Older entries sit below, so the top of the file is always the current picture.

الإدخالات الأقدم تأتي بالأسفل، لذا فإن أعلى الملف يعكس دائماً الوضع الحالي.

---

## Using this with other AI tools
## استخدام هذا مع أدوات ذكاء اصطناعي أخرى

Dr. Laila maintains this folder automatically in **Claude Code**, **GitHub
Copilot** and **Codex** — she is configured for all three, and no setup is
needed beyond opening the repository.

تحافظ د. ليلى على هذا المجلد تلقائياً في **Claude Code** و**GitHub Copilot**
و**Codex** — فهي مُهيّأة للثلاثة، ولا يلزم أي إعداد سوى فتح المستودع.

If you use something else — Qwen, Gemini, a local model — the folder still
works. It is only Markdown. Paste this into your assistant at the start of a
session:

وإذا استخدمت أداة أخرى — Qwen أو Gemini أو نموذجاً محلياً — فالمجلد يعمل كذلك،
فهو مجرد Markdown. الصق ما يلي في مساعدك عند بداية الجلسة:

> Read `.assistant-memory/MEMORY.md` before answering me. If I name a topic you
> have notes on, read that topic's file too. At the end of our session, add a
> dated entry to the topic file, update `progress.md`, and rewrite `MEMORY.md`
> so it stays one line per topic.

---

## The rules the assistant follows
## القواعد التي يتبعها المساعد

These are worth knowing, because you can hold the assistant to them:

يستحق أن تعرفها، لأنك تستطيع محاسبة المساعد عليها:

1. **It asks before writing anything the first time.** If you would rather not
   be recorded, say so and it will not start.
2. **It records evidence, not labels.** "Predicted one extra pass" — never
   "weak at loops."
3. **It writes what you could read comfortably**, because you can, and one day
   you probably will.
4. **It records what worked**, so a explanation that failed is not repeated.
5. **It never stores answers to graded work.**
6. **It trusts what it sees now over what the file says.** Understanding
   changes; old notes get corrected, not defended.

<!-- -->

1. **يسأل قبل أن يكتب أي شيء لأول مرة.** إن كنت تفضّل ألا يُسجَّل عنك شيء، فقل
   ذلك ولن يبدأ.
2. **يسجّل الدليل لا التصنيف.** "توقّع دورة إضافية" — لا "ضعيف في الحلقات".
3. **يكتب ما يمكنك قراءته دون حرج**، لأنك تستطيع، وستفعل غالباً يوماً ما.
4. **يسجّل ما نجح**، حتى لا يُعاد شرحٌ لم ينفع.
5. **لا يخزّن أبداً إجابات الأعمال المقيَّمة.**
6. **يثق بما يراه الآن أكثر من الملف.** الفهم يتغير، والملاحظات القديمة تُصحَّح
   لا يُدافَع عنها.

---

## Turning it off
## إيقافه

Delete the folder, or tell the assistant to stop keeping notes. Neither breaks
anything.

احذف المجلد، أو اطلب من المساعد التوقف عن تدوين الملاحظات. لن يتعطل شيء في
الحالتين.

```bash
rm -rf .assistant-memory
```

The folder returns the next time an assistant needs it — with this README
restored from the repository, and no memory of what came before.

سيعود المجلد في المرة التالية التي يحتاجه فيها المساعد — مع استعادة هذا الملف من
المستودع، وبلا أي ذاكرة لما سبق.
