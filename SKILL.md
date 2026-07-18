---
name: kaoyan-english-mock
description: Create, revise, analyze, and quality-check printable 考研英语一 mock papers, answer keys, and PDF layouts. Use when the user asks to 出题, 命题, 仿真卷, 模拟卷, 英语一试卷, 阅读/完形/作文训练题, 试卷生态分析, 主题去重, 难度与区分度校准, 命题审核逻辑优化, or wants future exam papers in the style of recent 考研英语一真题.
---

# 考研英语一仿真出题

## Core Standard

Always produce a paper that feels like an exam paper, not a loose exercise handout.

Use the post-2010 English I structure unless the user asks for a partial drill:

| Section | Questions | Points | Requirement |
|---|---:|---:|---|
| Use of English | 1-20 | 10 | 20 numbered blanks in one cloze passage |
| Reading Part A | 21-40 | 40 | Four texts, five questions each |
| Reading Part B | 41-45 | 10 | Headings, matching, or ordering |
| Translation Part C | 46-50 | 10 | Five underlined long sentences |
| Writing Part A | 51 | 10 | Applied writing |
| Writing Part B | 52 | 20 | Picture/chart essay |

If the user has limited daily time, still make the full paper printable, then add a short split-use schedule in the answer key.

## Mandatory Cross-Paper Ecosystem Gate

Do not begin by drafting four individually good articles. First design the paper as an ecosystem.

Before selecting or writing sources, build a ledger for the recent papers and every proposed section with:

| Field | Record |
|---|---|
| Primary domain | technology, social governance, culture/history, health, education, economic institutions, environment, or other |
| Secondary topic | the concrete policy, event, practice, or controversy |
| Conflict fingerprint | who seeks what, by what mechanism, at whose cost, and what resolution the author supports |
| Author stance | supportive, critical, conditional, unresolved, or mixed |
| Argument structure | opening mode, paragraph roles, turn, and conclusion type |
| Discourse voice | news report, popular science, cultural commentary, criticism, narrative-led analysis, or other |

Run three levels of deduplication:

1. **Topic nouns:** detect repeated AI, medicine, urban policy, museums, data metrics, education, labor, and other visible topics.
2. **Conflict frames:** detect repeated efficiency vs accountability, universal rules vs individual difference, measurement vs value, access vs quality, innovation vs risk, preservation vs reinterpretation, or markets vs public value.
3. **Argument templates:** detect repeated `phenomenon -> supporters -> however -> equity problem -> balanced institutional solution` structures.

Treat a candidate as high-risk when any two levels repeat. When one level repeats in adjacent papers, record a concrete reason for keeping it and change the affected actors, mechanism, stakes, and author resolution.

Apply these full-paper constraints:

- Use four different primary domains in Reading Part A by default; never use fewer than three.
- Use each major conflict fingerprint at most once per paper.
- Let no more than two texts conclude with a routine `combine both sides / strengthen governance / involve stakeholders` compromise.
- Include at least one text with a clear directional stance and at least one text that preserves a genuine unresolved tension.
- Vary opening modes and paragraph rhythms. Do not let all four texts use five neat policy-essay paragraphs.
- Audit Cloze, Part B, Translation, and both Writing tasks against Reading Part A. A full paper can still be repetitive even when its four main readings are not.

For a new paper following Mock 04, read [references/mock-01-04-ecology.md](references/mock-01-04-ecology.md) before choosing topics. Use its cooling table and Mock 05 blueprint. After completing each later paper, update the historical ledger and replace the next-paper state.

## Content Rules

### Cloze

- Use visible blanks in the passage, e.g. `______1______`, not bare numbers.
- Keep 20 blanks.
- Target roughly 280-320 words. Do not let cloze become a second long reading passage.
- Test logic words, prepositions, collocations, context repetition, abstract nouns, and tone.
- Format answer options as a table-like list with `[A] [B] [C] [D]`, not crowded inline text.
- Across 20 items, aim for about 7 lexical distinctions, 4 collocations, 4 logical links, 3 syntax/grammar items, and 2 discourse-cohesion items.
- Require 5-6 items to use evidence beyond the sentence containing the blank.

### Reading Part A

Target 380-430 words per text and about 1,520-1,720 words across the four texts. Once this range is met, invest effort in item discrimination rather than adding length.

Choose public-issue articles with:

- specific event or policy
- controversy or multi-party views
- subtle author attitude
- social relevance: education, culture, technology, environment, labor, academic publishing, museums, AI, urban policy

Avoid making all four texts follow the same five-paragraph compromise pattern. Vary openings, paragraph functions, argument direction, and voice. Use concrete cases, research findings, stakeholders, quotations or policy details when useful so the prose resembles edited public-affairs writing rather than a generic essay.

Select a credible real-world source or source family before designing questions. Write an original, copyright-safe adaptation rather than copying extended passages, while preserving concrete facts, individual voice, irregular argument rhythm, and a meaningful stance. Make the four texts feel as if they came from four different authors or publications.

Build a deliberate difficulty curve:

- Text 1: accessible entry, often life or social psychology, with some narrative movement.
- Text 2: medium difficulty, often science or technology, requiring information integration.
- Text 3: medium-hard, often culture, history, art or education, with contextual or attitudinal nuance.
- Text 4: hardest, often economics, media, ideas or institutional criticism, separating high scorers.

For a normal full paper, target exactly 5 easy, 10 medium, and 5 hard Reading Part A items unless real student calibration justifies a change. Treat this as an author-side prediction until timing and accuracy data are available.

- Easy: single-paragraph location with a restrained paraphrase, not a copied phrase.
- Medium: whole-paragraph integration, contextual sentence meaning, or a qualified viewpoint boundary.
- Hard: cross-paragraph comparison, argumentative function, applied scenario, or synthesis across competing views.

Distribute difficulty across all four texts. Do not make Texts 1-2 trivial and then place nearly all abstract reasoning in Texts 3-4. Difficulty must come from evidence span, viewpoint boundaries, author attitude, and distractor design—not rare vocabulary, excessive length, or abstract-noun density.

Cover at least three distinct subject domains and four distinct discourse modes where possible: news-like reporting, popular science, cultural commentary, and argument/criticism. At least one text should take a relatively clear position rather than ending with a routine “both sides need balance” conclusion.

Question mix per full paper:

- 5-6 detail/location questions
- 5-6 inference questions
- 3-4 example or paragraph-function questions
- 2-3 phrase/sentence-meaning questions
- 2-3 main-idea or author-attitude questions

Use this default audit matrix when the user has not requested a special drill:

| Category | Count | Operational definition |
|---|---:|---|
| Detail/location | 5 | bounded evidence from a sentence or paragraph |
| Inference | 7 | includes sentence meaning, viewpoint boundary, mechanism, and applied inference |
| Author attitude | 2 | direction plus degree of support, criticism, or reservation |
| Main idea | 2 | whole-text purpose, thesis, or title |
| Example/paragraph function | 4 | why a case, contrast, or paragraph exists in the argument |

Do not improve one category by starving another. A paper like Mock 01 with 10 direct-location items is too easy; a paper like Mock 04 with only 2 direct-location items and 11 inference items is too continuously abstract.

Correct answers should be restrained paraphrases of the text. Distractors should use common traps: swapped subject, exaggerated degree, reversed attitude, false causality, true-but-irrelevant detail, or common-sense bait not supported by the text.

- Do not make every question map neatly to one paragraph.
- Include cross-paragraph inference, example/function, semantic and attitude questions.
- Keep all four options in the same semantic field and similar in plausibility and length.
- Prefer distractors that are partly supported but fail at the boundary: `may` becomes `will`, a qualified claim becomes a general rule, a cause becomes an effect, or a balance between two values is recast as support for one side.
- In higher-discrimination papers, increase author-intention, paragraph-function, whole-text inference, and viewpoint-boundary questions. A correct answer should often require combining claims rather than finding one sentence-level synonym.
- For the designated hardest Reading Part A text, require at least three items to use cross-paragraph synthesis, applied scenarios, or comparison of argumentative boundaries. A conceptually difficult article is not a high-discrimination text if most questions can still be answered by direct sentence compression.
- Do not force an exactly balanced A/B/C/D distribution. Check only for suspicious concentration.
- Require at least 6 questions to integrate two sentences or a complete paragraph.
- Require at least 4 correct answers that are not direct sentence-level synonyms of the source.
- Give every question at least one plausible distractor and at least 8 questions a genuinely strong distractor.
- Record each wrong option's mechanism in the authoring key: scope expansion, degree shift, swapped subject, reversed causality, locally true but irrelevant, unsupported inference, or concept substitution.
- Avoid relying on obvious absolutes such as `always`, `only`, `completely`, or `impossible` to make distractors wrong.
- For each item, record the strongest distractor separately and state the single boundary that makes it wrong.
- Make wrong options as linguistically restrained as the correct option. `The most cautious option` must not become a reliable test-taking shortcut.
- Reject an option set when the correct answer is the only institutional, nuanced, or qualified statement in the group.
- Reject an item when two options can be defended by appealing to the author's presumed intention rather than explicit textual evidence.

### Part B

Do not always use the same new-question format. Rotate among the major English I Part B forms across papers:

- headings/subheading matching
- paragraph ordering
- sentence/paragraph insertion, often called 七选五 or 句段填空
- person/viewpoint matching
- information matching

When the user asks for multiple papers, track the most recent Part B format in the conversation and choose a different one next time unless the user specifies a type.

Make paragraph clues depend on:

- topic sentence
- pronoun reference
- lexical repetition and synonym chains
- contrast/causal/sequence logic

Target roughly 430-550 words. Do not make ordering or insertion solvable mainly through explicit labels such as `first`, `next`, or `final`; combine visible clues with subtler semantic links.

For insertion or ordering, make every correct placement depend on at least two clues, such as pronoun reference plus topic progression. Blind-test the item: reading only first sentences must not reveal most answers, while full reading must leave only one valid arrangement.

### Translation

Write five sentences with clear long-sentence features:

- subordinate clauses
- non-finite structures
- passive voice
- abstract nouns
- insertions

Provide accurate, natural Chinese translations in the answer key.

Use a complete source passage of roughly 350-450 words. Spread the five underlined portions through the passage instead of placing five nearly independent sentences together. Aim for about 25-35 words per underlined portion while varying syntax.

### Writing

Part A must specify identity, audience, purpose, and required points.

Part B must include a visual prompt. Do not replace it with pure text. Prefer black-and-white exam-style visuals:

- picture only, or picture + chart
- Chinese labels inside the image are acceptable and often better for print clarity
- keep the visual simple, legible, and monochrome

Rotate visual structures. Do not repeat a mechanically rising three-year chart across papers. When combining a picture and chart, make them carry different information rather than duplicate the same message.

For a single-picture task, prefer an interpretable contradiction: easy to describe, not exhausted by one slogan, open to analyses of different depth, and not dependent on specialist knowledge. Avoid repeatedly using direct themes such as recycling, self-discipline, or generic “technology has pros and cons.”

For Part B Writing, require all three layers:

1. an observable social phenomenon shown by the picture/chart;
2. a mechanism-level explanation of the deeper cause;
3. specific individual, institutional, or social action.

Reject generic inspirational conclusions that merely praise effort, persistence, planning, discipline, or technology. Before approval, compare the writing task with every reading on both primary domain and conflict fingerprint. Reject a writing prompt that matches a reading on both. Also reject repeated values across consecutive papers even when the surface topic differs.

For Part A, add one realistic constraint when appropriate, such as a schedule change, inability to attend, need to recommend a substitute, or request for revision, so memorized templates alone are insufficient.

## PDF Layout Rules

Before finalizing, make the PDF look like a real printed paper:

- cover page with exam title, subject, candidate info table
- centered `Section I Use of English`
- `Part A`, `Part B`, `Part C` labels
- `Directions:` labels before writing tasks
- page numbers
- enough margins
- no loose Markdown artifacts
- no question mark mojibake on Chinese cover text
- no bare cloze numbers without blanks
- no cramped inline option strings
- first-line indent every English body paragraph by about 2 characters; do not indent directions, questions, options, headings, or tables
- avoid orphan answer keys, split answer/explanation pairs, half-empty pages caused by forced page breaks, and clipped chart elements
- use a real table for study schedules; never expose Markdown pipes or separators in the PDF

If WPS or another app locks an old PDF, save the corrected paper under a new final filename and tell the user which old file could not be deleted.

## Verification Checklist

Always run a final check before answering:

1. Confirm only final files remain if the user asked to clean up.
2. Extract PDF text and verify question numbering:
   - Questions 1-52 appear in the test.
   - Answers/analysis cover 1-50 and include writing samples for 51-52.
3. Render screenshots of at least:
   - cover page
   - cloze/options page
   - writing page
4. Visually inspect screenshots:
   - Chinese cover text is readable.
   - Cloze blanks are visible as horizontal lines.
   - Options align clearly.
   - Writing prompt image is present and legible.
5. In the final response, link only the final test PDF and final answer PDF.

Also run content-level assertions before delivery:

- Build a canonical table for every objective item: question number, answer letter, exact option text, and explanation evidence.
- Verify that the answer letter selects the exact option supported by the explanation. Checking numbering or answer distribution alone is insufficient.
- For Reading Part A, store an expected keyword or paraphrase for each correct option and assert that it occurs in the selected option.
- Extract final PDFs and confirm 1-52 in the test, 1-50 plus writing samples in the answer book, 20 visible cloze blanks, five Part B positions, and five underlined translation portions.
- Render again after every pagination or chart-coordinate change.
- Randomize option positions only after content and distractors are final. Then recheck grammar, references and explanations.
- Reject answer patterns with four or more identical letters in succession, repeated first/last-answer patterns across texts, or a text using only two answer letters. Do not pursue exact mathematical balance.
- Re-run the ecosystem ledger after all sections are final. Reject last-minute topic clustering introduced by Translation, Part B, or Writing.
- Confirm the Reading Part A audit totals 5 easy, 10 medium, and 5 hard, or document the real calibration evidence supporting another distribution.
- Confirm the default question matrix totals 5 detail, 7 inference, 2 attitude, 2 main-idea, and 4 function items.
- Confirm the four texts do not share one recognizable moral answer pattern such as `formal compliance is insufficient; layered governance is needed`.

## Answer Analysis Standard

For every Reading Part A question, explain:

1. question type;
2. locating sentence or paragraph;
3. the paraphrase chain supporting the correct option;
4. the trap in each wrong option.

Do not stop at repeating the correct sentence. Keep the explanation concise but useful for error review.

## Continuous Improvement Loop

After completing every mock paper:

1. Review the finished paper for factual, answer-key, difficulty, length, typography, and pagination problems.
2. Incorporate the user's actual timing, accuracy and disputed questions when available.
3. Identify reusable lessons rather than paper-specific anecdotes.
4. Update this skill immediately with the reusable rules before starting the next paper.
5. Validate the updated skill folder.

Do not overwrite a useful general rule merely to fit one paper. Tighten standards when the same failure class recurs, especially answer-letter/option-text mismatches, formulaic reading structures, weak distractors, missing indentation, short translation context, or raw layout artifacts.

## Blind Review and Calibration

Do not finalize immediately after generation.

1. Give the test without its answer key to an independent reviewer or fresh subagent when available.
2. Compare the independent answers with the intended key and investigate every disagreement.
3. Audit the source evidence and failure mechanism for every distractor.
4. Check the difficulty curve across Texts 1-4 and within cloze/Part B.
5. Incorporate real user timing, accuracy and disputed questions after use; adjust future items from observed results rather than intuition alone.
6. Render every PDF page and inspect fonts, spacing, page breaks, tables and visuals.

For blind review, record the reviewer's selected answer, confidence, and second choice. Rewrite any item that produces a high-confidence disagreement or two defensible answers. Resolve the dispute from source evidence and scope boundaries, never from `what the author meant to ask`.

The target is a medium-hard stage mock whose difficulty comes from evidence, inference and fine discrimination, not obscure knowledge, excessive length, rare vocabulary, or deliberately tangled prose.

## Next Paper State: Mock 05

Mock 04 completed person/viewpoint matching and used Text 2 as the designated hardest article. For the next full paper, apply these paper-specific choices, then replace this section after completion:

- Use this Reading Part A matrix:

| Text | Domain | Topic | Core conflict | Difficulty |
|---|---|---|---|---|
| Text 1 | social/consumer institutions | cashless venues and payment choice | transaction convenience vs choice and system resilience | 2 easy + 3 medium |
| Text 2 | environment/science | assisted migration under climate change | ecological caution vs the risk of inaction | 1 easy + 3 medium + 1 hard |
| Text 3 | culture/history | reconstructing historic buildings after disaster | material authenticity vs communal memory and cultural continuity | 1 easy + 3 medium + 1 hard |
| Text 4 | economic institutions/technology markets | interoperability rules for digital platforms | integrated experience and security vs exit freedom and competition | 1 easy + 1 medium + 3 hard |

- Use exactly 5 detail, 7 inference, 2 attitude, 2 main-idea, and 4 function items across these texts.
- Make Text 4 the main discriminator and require at least three applied, functional, or cross-paragraph boundary questions.
- Use information matching for Part B: five skilled-trade workers discussing apprenticeship mentoring, with seven candidate statements and two extras that are locally plausible but wrong in ownership, scope, or argumentative role.
- Use a Cloze passage about why maps require deliberate distortion. Avoid libraries, AI, and generic public-governance prose.
- Use a Translation passage about how standardized time changed railways, commerce, and daily life. Keep five demanding sentences in a complete 350-450-word passage.
- Use a Part A Writing task in which a campus film-screening venue is cancelled and the writer must explain the change, propose an alternative, and request confirmation.
- Use a Part B Writing picture-plus-chart about sports facilities that appear fully booked but remain physically empty, followed by improved use after wait-list and cancellation reminders. Require observable behavior, causes such as low-cost reservation and scarcity anxiety, and individual plus institutional remedies.
- Preserve the stronger boundary-based distractor rule from Mock 04, but avoid creating near-synonym cloze options that remain equally grammatical and contextually defensible.
- Apply a full cooling period to AI ethics, AI medicine, AI education, precision medicine, age-friendly design, urban lighting/tree/public-space design, data governance, average-metric bias, museum restitution, and museum labels as primary topics.
- Do not use AI, medicine, or `human responsibility remains central` as the main topic or conflict in Cloze, Reading, Translation, or Writing. If AI returns in a later paper, wait at least two full papers and change the actors, mechanism, stakes, and conclusion—not merely the application field.
- Keep Translation syntactically demanding, especially through abstract subjects, parenthetical insertions, and clauses that require Chinese reordering rather than rare vocabulary.
- Keep the Part B Writing visual on the same page as its directions. If vertical space is tight, redesign the visual's internal geometry instead of uniformly shrinking its labels below print-readable size.

## File Hygiene

For user workspaces, keep final artifacts clear and delete temporary files:

- Keep: `*_最终版.pdf`, `*_最终版_答案解析.pdf`
- Delete when no longer needed: old layout PDFs, temporary images, render-check folders, Markdown source files if the user asks for only final versions
- Never delete unrelated user materials.
