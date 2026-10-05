---
name: mckinsey-storytelling
description: >
  Elite corporate storytelling architect using McKinsey Pyramid Principle, Aristotelian rhetoric, and classical logic to build narratives that guide audiences to predetermined conclusions. Trigger this skill whenever the user asks to structure a presentation, pitch, board deck, investor narrative, executive briefing, sales deck, or any persuasive corporate communication. Also trigger for "structure my story", "build the narrative for", "how do I present X to leadership", "make this more persuasive", "create the storyline for", "how do I convince the board", "pyramid my deck", "build the argument for", "rewrite this deck structure", or any request where the goal is to persuade, convince, align, or guide an audience through a structured argument toward a specific conclusion. Use even if the user only mentions "narrative", "story", "flow", or "structure" in a corporate context.
---

# McKinsey Storytelling Skill

## Philosophy

Corporate storytelling is **not** about being creative — it's about **engineering consent**. The audience must arrive at your conclusion feeling they derived it themselves. This skill builds that machinery.

Three interlocking systems:

1. **Structure** — Pyramid Principle (where to put the message)
2. **Logic** — Deduction / Induction / Abduction (how to prove it)
3. **Rhetoric** — Aristotle's Logos / Ethos / Pathos (why they believe it)

---

## PHASE 1 — Situation Intake

Before building anything, extract:

```
GOVERNING THOUGHT: What is the ONE conclusion the audience must leave with?
AUDIENCE: Who are they? What do they already believe? What do they fear?
CONTEXT: What triggered this communication? (problem, decision, update, pitch)
RESISTANCE: What is the main objection or inertia to overcome?
CALL TO ACTION: What do you want them to DO after?
```

**Intake protocol:**
1. Extract what's already in the user's message (explicit or inferable).
2. For what's missing, ask — but group into ONE single question, not five separate ones.
3. If the user can't answer, doesn't know, or says "you decide" — Claude infers from context and states assumptions explicitly before proceeding.
4. Never block execution waiting for perfect intake. A reasonable assumption + transparency beats paralysis.

---

## PHASE 2 — Logic Mode Mapping (per argument)

A presentation is not a single argument — it's a **chain of arguments**, each with its own evidentiary situation. Assign the optimal logic mode to each key point independently.

### Mode Selection Matrix

| Mode | Assign when the argument... | Slide-level pattern |
|---|---|---|
| **Deductive** | ...derives from a rule the audience already accepts | Rule → Case → Conclusion |
| **Inductive** | ...is proven by accumulating data points into a pattern | Data × N → Pattern → Implication |
| **Abductive** | ...explains an anomaly by eliminating competing hypotheses | Observation → Alternatives → Best fit |
| **Dialectical** | ...must defeat an entrenched opposing belief | Their view → Its limits → New frame |
| **Analogical** | ...is unfamiliar but maps cleanly to a domain they trust | Known domain → Structural parallel → Transfer |
| **Causal** | ...establishes a mechanism (not just correlation) | Mechanism → Evidence of causality → Projection |

### Assignment protocol

**Claude assigns logic modes autonomously — never asks the user to choose.**

For each Key Point, Claude selects the best-fit mode based on:
1. **Evidence available** — data points → Inductive; accepted rules → Deductive; anomaly to explain → Abductive
2. **Audience belief state** — entrenched opposition → Dialectical; unfamiliar concept → Analogical
3. **Argument type** — mechanism/urgency → Causal

If the user explicitly proposes a mode for a specific argument — accept it. Otherwise, assign and show rationale in the Logic Fingerprint output.

Example mapping:
```
KEY POINT                              → LOGIC MODE   → RATIONALE
──────────────────────────────────────────────────────────────────
KP1: Market is structurally broken     → Inductive    (3 data signals converge)
KP2: Root cause is X, not Y           → Abductive    (anomaly needs diagnosis)
KP3: Our solution works               → Deductive    (category rule + our proof)
KP4: Now is the right time            → Causal       (mechanism + trigger event)
KP5: Risk is manageable               → Dialectical  (audience believes it's high)
```

**Macro structure stays Pyramid (deductive top-down). Logic modes vary at Key Point level and below.**

The combination of modes is the Logic Fingerprint of the presentation — always include it in output.

Read `references/logic-modes.md` for deep examples and transition language between modes.

---

## PHASE 3 — Build the Pyramid

### The Minto Pyramid (canonical)

```
        ┌─────────────────────┐
        │   GOVERNING THOUGHT │  ← Answer first. Always.
        │  (Executive Summary)│
        └──────────┬──────────┘
          ┌────────┴────────┐
     KEY POINT 1      KEY POINT 2      KEY POINT 3
     (Argument)       (Argument)       (Argument)
          │                │                │
    Support 1.1      Support 2.1      Support 3.1
    Support 1.2      Support 2.2      Support 3.2
    Support 1.3      Support 2.3      Support 3.3
```

### The SCQA Frame (situate before the pyramid)

Wrap the Governing Thought in narrative context:

```
S — SITUATION   → What everyone agrees is true (neutral ground)
C — COMPLICATION → What disrupted the situation (the problem/tension)
Q — QUESTION    → The implicit question this creates in the audience's mind
A — ANSWER      → Your Governing Thought (the pyramid top)
```

**Key rule:** The Answer must be the ONLY logical response to the Question. If there are other plausible answers — your SCQA is broken.

### Groupings Rule (MECE)

Every level of the pyramid must be:
- **Mutually Exclusive** — no overlap between siblings
- **Collectively Exhaustive** — siblings together fully cover the parent

Test: Can you remove one branch and still have a complete argument? If yes — it's redundant.

---

## PHASE 4 — Rhetorical Layering (Aristotle)

Logic alone doesn't persuade. Layer these three:

### Logos (Logic/Reason)
- Data, statistics, benchmarks, comparisons
- Causal chains ("because X, therefore Y")
- Analogies from domains the audience trusts

### Ethos (Credibility/Character)
- Establish authority early (track record, expertise, stakes)
- Cite sources the audience already respects
- Show you understand their world ("we know you face X")

### Pathos (Emotion/Stakes)
- Make the cost of inaction vivid and personal
- Use concrete future scenarios (not abstract projections)
- Create urgency via a "ticking clock" element

**Sequence rule:** Ethos first → Logos middle → Pathos close. Credibility opens the door; logic builds the case; emotion triggers the decision.

---

## PHASE 5 — Narrative Arc Selection

Choose based on audience psychology:

### Arc A — "Direct" (C-level, data-trusting audiences)
```
Answer → Why it's right (3 arguments) → Implications → Ask
```

### Arc B — "Situation-Problem-Solution" (operational audiences)
```
Current state → Gap/Pain → Root cause → Solution → ROI → Ask
```

### Arc C — "Visionary" (board, investor, change-resistant)
```
Status quo (safe but stagnating) → Disruption coming → 
Future with us → Future without us → Our path → Ask
```

### Arc D — "Refutation" (hostile audience)
```
Acknowledge their view → Show its limits → New frame → 
Evidence for new frame → Restate conclusion → Ask
```

Read `references/arc-templates.md` for slide-by-slide breakdown of each arc.

---

## PHASE 6 — Slide-Level Logic Annotation

Each slide = one assertion + one logic mode. Annotate explicitly.

| ❌ Weak title | ✅ Strong title | Logic mode |
|---|---|---|
| "Market Overview" | "Market is growing 3× but we're losing share" | Inductive |
| "Root Cause" | "Churn is an onboarding failure, not a product failure" | Abductive |
| "Our Solution" | "ISA reduces CAC by 40% vs. current SDR model" | Deductive |
| "Risk" | "Execution risk is real — here's exactly how we contain it" | Dialectical |
| "Why Now" | "Three market forces converge in Q3 — this window closes" | Causal |

**Slide anatomy:**
```
TITLE    → The assertion (what you want them to believe after this slide)
MODE TAG → [Inductive / Deductive / Abductive / Dialectical / Causal / Analogical]
BODY     → Evidence structured according to the mode's pattern
INSIGHT  → The "so what" — explicit, never assumed
```

**Mode-specific body patterns:**
- **Inductive:** 3+ data points → label the pattern → state implication
- **Deductive:** State the rule → apply to your case → conclusion is forced
- **Abductive:** Show the anomaly → list 2–3 competing explanations → eliminate → best fit
- **Dialectical:** "Some argue X" → "But this assumes Y" → "Evidence shows Z" → reframe
- **Causal:** Mechanism diagram → evidence of causality (not just correlation) → projection
- **Analogical:** Introduce the analogy domain → draw structural parallel → transfer the lesson

Never leave the "so what" implicit. Audiences will fill it in wrong.

---

## PHASE 7 — Objection Engineering

Map objections BEFORE building:

```
Objection → Type → Pre-emption technique
────────────────────────────────────────
"Too expensive"     → Value objection   → ROI slide before price
"We tried this"     → Experience bias   → Diagnostic: what failed and why ours differs
"Not the right time"→ Urgency objection → Cost of delay, competitive clock
"I need more data"  → Trust objection   → Pilot/POC as next step
```

Embed pre-emptions into the flow — don't address objections defensively at the end.

---

## OUTPUT FORMAT

When building a storytelling structure, deliver:

### 1. Governing Thought
One sentence. Present tense. Action-oriented.

### 2. SCQA Frame
Four sentences max per element.

### 3. Logic Fingerprint
Table mapping each Key Point to its logic mode + rationale. This is the mixed-logic blueprint for the whole deck.

```
| # | Key Point (assertion) | Logic Mode | Rationale |
|---|---|---|---|
| 1 | ... | Inductive | Multiple data signals available |
| 2 | ... | Abductive | Competing explanations to eliminate |
| 3 | ... | Deductive | Rule accepted; application is the argument |
```

### 4. Pyramid Structure (outline)
Hierarchical. Titles as assertions. Mode tag on each node.

### 5. Rhetorical Map
Per section: which Logos/Ethos/Pathos elements to include.

### 6. Narrative Arc
Named arc + rationale for the choice.

### 7. Slide Titles List
Ordered. Every title = assertion. Mode tag beside each. Ready to paste into deck.

### 8. Objection Map
Top 3 objections + pre-emption placement.

---

## QUALITY CHECKLIST

Before delivering, verify:

- [ ] Governing Thought is ONE sentence, not a topic
- [ ] SCQA Question has only ONE logical Answer
- [ ] Every pyramid level is MECE
- [ ] Logic Fingerprint is complete — every Key Point has a mode + rationale
- [ ] No two adjacent slides use the same logic mode without purpose (variety prevents cognitive fatigue)
- [ ] Mode-specific body pattern is followed per slide
- [ ] Every slide title is an assertion, not a label
- [ ] "So what" is explicit on every slide
- [ ] Ethos established before Logos
- [ ] Pathos deployed at close, not opening
- [ ] Top 3 objections are pre-empted in the flow
- [ ] Call to action is specific (verb + object + timeline)

---

## REFERENCE FILES

- `references/logic-modes.md` — Deep examples: deductive, inductive, abductive, dialectical chains with corporate examples
- `references/arc-templates.md` — Slide-by-slide breakdown for each of the 4 narrative arcs
