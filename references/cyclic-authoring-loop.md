# Stable Cross-Paper Authoring Loop

Read this reference before starting a new full paper, resuming a series, or deciding how external feedback should affect later papers.

## Purpose

The skill should behave as a maintained assessment system, not a prompt that independently generates unrelated papers. Each paper must inherit explicit state, pass the same class of gates, produce a frozen release candidate, and leave a verified handoff for the next paper.

This loop serves two related but separate outcomes:

- **Assessment:** the clean paper measures a candidate's current exam performance under timed, first-attempt conditions.
- **Learning transfer:** material revealed after completion helps the candidate improve sentence parsing, contextual vocabulary, argument mapping and sensitivity to qualification.

Do not use evidence from the learning layer to claim that the assessment layer is equivalent to a true paper. Do not expose the learning layer before the first attempt.

## State Packet

At the beginning of each paper, load or construct one state packet containing:

| Field | Required content |
|---|---|
| Series identity | New Version number and relationship to earlier papers |
| Completed record | final topics, sources, mechanisms, Part B form, writing tasks, lengths and released filenames |
| Cooling state | topics, conflict frames, argument templates, visuals and Part B forms that should not recur yet |
| Quality debt | demonstrated weaknesses that the next paper should target, without pretending they are already fixed |
| Empirical state | available timing, item accuracy, confidence, second choices and disputes; state `none` when absent |
| Calibration boundary | what is setter prediction, what is internally verified, and what remains unvalidated |
| Release identity | final hashes/page counts when a paper has been released |

Use the selected workspace `CURRENT_STATE.json` as the maintained series ledger. User-supplied historical ecology is read-only optional evidence; this public package contains no owner's history. Paper-specific facts belong in the workspace ledger. General decision rules belong in `CORE_SPEC.md` or this reference, with proposed changes versioned by the maintainer. Do not turn one reviewer's preference into a universal rule unless the same failure class is verified or the user explicitly adopts it as a series standard.

## The Cycle

### 1. Intake and two-way steelman gate

- Restate the real completion condition for the current paper.
- Give the strongest case that the proposed design can advance partial true-paper replacement.
- Give the strongest case that it cannot, including source, voice, item discrimination and missing candidate data.
- Identify the variables that could change the conclusion.
- Reuse a previously settled user decision unless new evidence materially changes it; do not ask the same question every paper.

### 2. Ecosystem and source design

- Apply the current cooling state before selecting passages.
- Build the full-paper ecosystem ledger before drafting individual texts.
- Ground every major passage in one concrete, auditable source.
- Preserve source-specific voice, irregularity, qualification and unresolved tension.
- Choose the Part B form and writing mechanism with cross-paper rotation in mind.

### 3. Authoring

- Build the Cloze construct map before final options.
- Design Reading questions from natural evidence spans, not from a preset answer matrix.
- Record canonical answer letter, exact option text, evidence chain, strongest distractor and failure boundary.
- Keep the paper clean: no hints, difficulty labels, training prompts or explanations in the candidate version.

### 4. Adversarial QA

- Run all-option substitution for Cloze.
- Audit duplicate evidence chains, direct-compression answers, uniquely cautious correct options and unsupported sophisticated-sounding distractors.
- Require a fresh blind pass after material revisions.
- Derive type and difficulty distributions after authoring; keep difficulty setter-predicted until candidate evidence exists.
- Render the final PDFs and inspect every page after the final pagination change.

### 5. Release freeze

Before distribution, freeze one release candidate and record:

- final test and answer filenames;
- page counts and SHA-256 hashes;
- canonical key and explanation coverage;
- known limitations and setter-side difficulty judgment;
- upload/file IDs and sharing state when delivered externally.

Do not silently replace a released file. A content change after release creates a new revision identity and requires fresh semantic and rendered-page verification.

### 6. Candidate use and empirical collection

The first attempt must remain uncontaminated. Ask for, when feasible:

- total and section timing;
- selected answer for each objective item;
- confidence or second choice for uncertain items;
- questions the candidate believes have two defensible answers;
- short reasons for high-confidence disagreements;
- writing completion and perceived time pressure.

Small samples are diagnostic, not psychometric proof. Preserve raw disagreements before interpreting them.

### 7. Post-test learning-transfer layer

Only after the timed attempt, provide a compact deep-review layer in or alongside the answer book. It should reuse real features of the current paper rather than attach generic study advice.

Include, where the material genuinely supports them:

1. **Sentence surgery:** select representative long sentences; mark finite verbs, clause boundaries and the minimal main clause, then require a natural Chinese restructuring rather than word-for-word translation.
2. **Argument reverse-engineering:** map claim, evidence, concession, qualification, mechanism and unresolved boundary for the hardest or most disputed passage.
3. **Contextual vocabulary network:** show how a key word's local disciplinary meaning differs from its common dictionary meaning.
4. **Tone transfer:** identify restrained academic moves such as concession, scope limitation and non-causal association; ask for a short paraphrase or imitation without claiming that imitation alone improves scores.
5. **Distractor autopsy:** compare the selected answer and second choice at the exact boundary where one fails.

This layer must not make promotional claims such as `read top journals effortlessly`, `improve intelligence`, or `automatically recognize wrong answers`. Describe the trained operation and leave transfer as a hypothesis until performance data supports it.

### 8. Feedback adjudication

For every external AI or human suggestion, record:

| Decision field | Question |
|---|---|
| Valid diagnosis | What observable failure did the reviewer correctly identify? |
| Reviewer error | Did the reviewer misread the passage, key, rendered visual or task boundary? |
| Patch risk | Would the proposed wording introduce ambiguity, unsupported content or style drift? |
| Decision | Accept, modify, reject, or defer to candidate data? |
| Scope | Revise the current release, apply only to the next paper, or generalize into the skill? |

Positive comments about educational value are not item-quality validation. A useful training idea may be accepted for the post-test layer while providing no evidence about answer uniqueness or true-paper equivalence.

### 9. Closeout and handoff

After a paper is completed or revised:

1. append its completed record to the ecology ledger;
2. replace the next-paper cooling state;
3. list unresolved quality debt honestly;
4. add empirical results or explicitly record that none exist;
5. propose maintainer-reviewed changes to general rules only for reusable, evidence-supported failure classes;
6. validate the workspace state and paper, retaining uncompleted semantic and visual checks as pending;
7. begin the next paper from this handoff rather than reconstructing history from memory.

## Stability Tests

The series is operating stably only when all of these remain true across papers:

- no cooled topic, conflict fingerprint or argument template recurs without a recorded reason;
- every major passage has auditable provenance and adaptation boundaries;
- canonical answer text agrees with the key and explanation;
- blind disagreements are investigated rather than outvoted;
- released PDFs pass complete text and rendered-page checks;
- difficulty claims remain separated into setter prediction, internal evidence and candidate evidence;
- learning tasks appear after, never before, the clean first attempt;
- every completed paper leaves an explicit next-state packet.

Stable does not mean identical. Topic domains, discourse voices, item mix, difficulty distribution, Part B form, writing visual and learning-transfer exercises should vary when the evidence and cooling state call for variation.
