# Official Course Slides
# الشرائح الرسمية للمقرر

This folder holds the official AOU slide decks for M110 - Python Programming. They are the source of truth for every answer in this repository, including everything Dr. Laila (the course's AI assistant) tells you.

هذا المجلد يحتوي على شرائح الجامعة العربية المفتوحة (AOU) الرسمية لمقرر M110 - برمجة بايثون. وهي المرجع الموثوق لكل إجابة في هذا المستودع، بما في ذلك كل ما تخبرك به د. ليلى (المساعدة الذكية للمقرر).

If anything else in this repository ever seems to disagree with these slides, the slides are correct.

إذا بدا أن أي محتوى آخر في هذا المستودع يتعارض مع هذه الشرائح، فالعبرة بما ورد في الشرائح.

---

## Chapters
## الفصول

All chapters and self-study topics, matching [`.claude/course-map.yaml`](../.claude/course-map.yaml). English titles are the official slide titles, kept exact; the Arabic column is a translation, not a replacement.

جميع الفصول ومواضيع الدراسة الذاتية، بما يطابق [`.claude/course-map.yaml`](../.claude/course-map.yaml). العناوين الإنجليزية هي عناوين الشرائح الرسمية كما هي؛ أما العمود العربي فهو ترجمة له وليس بديلاً عنه.

| Chapter / الفصل | Topic | الموضوع | Folder / المجلد |
|---|---|---|---|
| 1 | Algorithms: Flowcharts & Pseudocodes | خوارزميات: مخططات انسيابية وأكواد زائفة | [chapter-01-algorithms/](chapter-01-algorithms/) |
| 2 | Fundamentals of Python Programming | أساسيات برمجة بايثون | [chapter-02-fundamentals/](chapter-02-fundamentals/) |
| 3 | Decision Structures and Boolean Logic | هياكل اتخاذ القرار والمنطق البولياني | [chapter-03-decision-structures/](chapter-03-decision-structures/) |
| 4 | Repetition Structures | هياكل التكرار | [chapter-04-repetition/](chapter-04-repetition/) |
| 5 | Functions | الدوال | [chapter-05-functions/](chapter-05-functions/) |
| 6 | Files and Exceptions | الملفات والاستثناءات | [chapter-06-files-exceptions/](chapter-06-files-exceptions/) |
| 7 | Collection Data Types: Lists and Tuples | أنواع البيانات التجميعية: القوائم والصفوف | [chapter-07-lists-tuples/](chapter-07-lists-tuples/) |
| 10 | Classes and Object-Oriented Programming | الفئات والبرمجة الكائنية التوجه | [chapter-10-oop/](chapter-10-oop/) |
| 13 | GUI Programming | برمجة الواجهات الرسومية | [chapter-13-gui/](chapter-13-gui/) |
| SS1 | Turtle Graphics | رسومات السلحفاة | [ss1-turtle-graphics/](ss1-turtle-graphics/) |
| SS2 | Recursion | العودية | [ss2-recursion/](ss2-recursion/) |
| SS3 | Dictionaries and Sets | القواميس والمجموعات | [ss3-dictionaries-sets/](ss3-dictionaries-sets/) |

---

## Which File to Use
## أي ملف تستخدم

Every folder holds the same deck in three formats:

يحتوي كل مجلد على نفس الشرائح بثلاث صيغ:

| Format / الصيغة | Use it for | استخدمه من أجل |
|---|---|---|
| `.pdf` | Reading and studying. **Contains the figures and flowcharts.** | القراءة والدراسة. **يحتوي على الأشكال والمخططات الانسيابية.** |
| `.pptx` | The original PowerPoint file. | ملف PowerPoint الأصلي. |
| `.pptx.txt` | Plain text, for AI assistants and text search. | نص عادي، للمساعدات الذكية والبحث النصي. |

---

## What the Text Files Lose
## ما تفقده ملفات النص

The `.pptx.txt` files are extracted automatically and are faithful for prose, definitions and explanations. Three things do not survive extraction:

يتم استخراج ملفات `.pptx.txt` آليًا، وهي دقيقة بالنسبة للنصوص والتعريفات والشروحات. لكن ثلاثة أشياء لا تصمد أمام عملية الاستخراج:

1. **Code indentation is partly flattened.** In Chapter 4, `print(num)` appears unindented directly under its `for` loop — syntactically incorrect Python.
2. **Smart quotes are mangled.** `print('Hello’, i)` will not parse.
3. **Figures are absent entirely.** Chapter 1 is almost entirely flowcharts, and none of them are in the text.

<!-- -->

1. **مسافات إزاحة الأكواد (indentation) تُفقد جزئيًا.** ففي الفصل الرابع، يظهر السطر `print(num)` بلا إزاحة تحت حلقة `for` الخاصة به — وهذا كود بايثون غير صحيح نحويًا.
2. **علامات الاقتباس الذكية (smart quotes) تُشوَّه.** السطر `print('Hello’, i)` لن يعمل عند تشغيله.
3. **الأشكال (figures) غائبة تمامًا.** يتكون الفصل الأول بشكل شبه كامل من مخططات انسيابية، ولا يظهر أي منها في النص.

Rule of thumb: use the `.txt` files to search and read, use the PDF whenever a diagram matters, and never copy code from the `.txt` without checking it runs.

قاعدة عامة: استخدم ملفات `.txt` للبحث والقراءة، واستخدم ملف PDF كلما كان الأمر يتعلق بمخطط أو شكل، ولا تنسخ أي كود من ملف `.txt` دون التأكد من أنه يعمل فعليًا.

---

## Attribution
## حقوق الملكية

These slide decks are the copyright of Arab Open University (AOU) and are redistributed here for student study. This repository is not affiliated with, nor endorsed by, AOU.

هذه الشرائح محفوظة الحقوق للجامعة العربية المفتوحة (AOU)، ويُعاد نشرها هنا لغرض دراسة الطلاب. هذا المستودع غير تابع للجامعة العربية المفتوحة وغير معتمد من قبلها.
