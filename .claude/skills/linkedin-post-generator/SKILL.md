---
name: linkedin-post-generator
description: "Generate high-performing LinkedIn posts from any input (idea, theme, message, transcript, or notes). Always follows a structured pipeline: 5 hook options first, user selects, full post generated. Use this skill whenever the user wants to write, draft, or create a LinkedIn post, wants hook options for LinkedIn, says 'write me a LinkedIn post', 'I need a post about X', 'give me hooks for LinkedIn', or provides a topic/idea and mentions LinkedIn content. Also trigger when the user provides a transcript or article and asks to turn it into a LinkedIn post. Invoke even for casual requests like 'quick LinkedIn post about X' or 'make a post from this'."
---

# LinkedIn Post Generator

Generate scroll-stopping LinkedIn posts. The pipeline always has two stages:

**Stage 1 → 5 Hook Options** (present first, wait for selection)
**Stage 2 → Full Post** (only after hook is chosen)

Never skip to the full post without hook selection.

---

## Input

Accept any of the following (alone or combined):
- Raw idea / theme / main message
- Article, notes, or meeting transcript
- Existing post draft to rewrite

If no persona/voice is specified, infer from context. If unclear, ask one quick question: "What's the tone? (e.g. personal story, thought leadership, contrarian take, practical tips)"

---

## Stage 1: Hook Generation

Generate exactly **5 hook options**. Each must use a different hook type (see list below). Label each with its type.

### Hook Structure

**Simple Hook** (2 lines):
Line 1 — assertive statement, max 7 words.
Line 2 — complement to line 1, max 7 words.

**Full Hook** (3 lines):
Line 1 — assertive statement, max 7 words.
Line 2 — complement to line 1, max 7 words.
Line 3 — reading CTA with strong curiosity pull, OR second complement following the hook's structural logic.

Rules:
- Line 1 is always a statement (never a question, never a subordinate clause).
- Language must be simple, conversational, minimally formal.
- Default to Simple Hook. Use Full Hook only when topic complexity warrants a reading CTA.

### Hook Type Menu (use variety across the 5 options)

- **Contrarian** — Challenge a common belief
- **Statistic/Number** — Lead with a striking data point or result
- **Personal failure/win** — Story-based, vulnerability or milestone
- **Question** — Direct question that triggers self-reflection
- **Bold statement** — Provocative claim or declaration
- **Secret/Reveal** — Imply insider knowledge ("Most people don't know...")
- **Before/After** — Contrast past vs. present state
- **Relatable frustration** — Name a pain the audience feels

After the 5 options, ask: *"Which hook do you prefer? (1–5) — or tell me what to adjust."*

---

## Stage 2: Full Post

Once the hook is selected, write the complete post using this structure:

```
[CHOSEN HOOK]

[BODY]

[CTA]
```

### Body Guidelines

- Max 3 lines per paragraph.
- Prioritize short sentences. Alternate them with 2–3 denser explanatory blocks per post.
- Use bullet lists with characters: "↳", "⤷", "→" — always varying. More than one list per post is allowed when content demands it. Randomly alternate between arrow-style lists and numbered lists.
- Vary post formats and lengths across generations to avoid repetitive patterns.
- Avoid walls of text; use line breaks for scannability (see Layout Pattern below).
- Length: 150–300 words for most posts. Long-form (300–600w) only if topic demands depth.

### Layout Pattern

Structure posts for fast scanning. Follow this rhythm as a reference — adapt with judgment for shorter or longer posts while preserving the rhythm logic:

```
Hook (2 lines)

3 short lines

List intro sentence
List (3 items)

2 short lines

Dense explanatory block (2 lines)

3 short lines

Dense explanatory block (3 lines)

2 lines

CTA
```

### Writing Style

**Voice and person:**
- Write in first person ("I") or address the reader directly ("you"). Never use indirect third-person framing.
- Use: "Have you ever gone through a transformation that changed everything?" NOT: "Transformations that change people's lives are constant."
- Emit personal opinions. The post should feel like a POV, not a report.

**Assertiveness:**
- Use assertive, direct sentences. No over-qualified, hedge-everything language.
- Use: "Companies that invest in AI will lead the next economic wave." NOT: "In the world of tech companies, the use of AI is becoming increasingly important."
- Avoid excess adjectives. Let facts and actions carry weight.

**Scenarios and analogies:**
- When drawing scenarios, be direct. No "imagine", "suppose", "picture this."
- Use: "A company that ignores AI in 2025 is already losing ground." NOT: "Imagine a company that doesn't invest in AI. What will happen to it?"

**Structure:**
- Don't repeat yourself. Say it once, say it well.
- Use bullet points and short sentences to support arguments, not to pad length.
- Real examples and tangible results beat vague metaphors every time.
- When referencing a method, tool, or result: back it with a concrete case or number.

**Tone:**
- Thought leadership with personality. Confident, direct, occasionally humorous.
- Light humor and authentic voice keep the content accessible without losing authority.
- The goal: demystify complex concepts, offer practical insight, inspire action.

### CTA Guidelines

Default CTA: ask for the audience's opinion on the topic.
> Example: *"What's your take? Drop it in the comments."*

Vary by context:
- If promoting something — drive to link or DM
- If sharing a lesson — invite stories ("Has this happened to you?")
- If asking a question — encourage direct answers
- If controversial — invite debate ("Agree or disagree?")

Never use generic CTAs like "Like and share if you agree."

---

## Language

Default to the user's language. Produce the full post in that language — hooks, body, CTA all localized. Do not mix languages unless asked.

---

## Reference Library

The file `references/140_templates.txt` contains 140 LinkedIn post templates with real examples, breakdowns, and copywriting formulas (AIDA, PAS, Slippery Slide, etc.).

**Always open this file before writing the full post (Stage 2).** It is a mandatory step, not optional.

Process:
1. Open `references/140_templates.txt`
2. Identify the 2-3 templates most relevant to the chosen hook type and topic
3. Extract only the structural pattern (labels, sequence, format) — not the full text
4. Use that structure to inform the body of the post

Read selectively: scan for the relevant template type by number or keyword. Do not process all 140 templates — just find the match and move on.

---

## Output Format

**Stage 1 output:**
```
Here are 5 hook options for your post about [TOPIC]:

1. [Hook Type]
[Hook line]

[Rehook]

---
2. [Hook Type]
...

Which do you prefer? (1–5) Or let me know what to adjust.
```

**Stage 2 output:**
Deliver the full post as clean copy — no labels, no scaffolding — ready to paste into LinkedIn. Then add below:

```
---
Post stats: ~[X] words | Format: [format used] | CTA: [cta type]
```

---

## Rules

- Never generate the full post before the user selects a hook
- Never use hashtags unless the user asks (they rarely add value)
- Never use emojis — absolute rule, no exceptions
- Never use bold text anywhere in the post body
- First 180 characters = the preview text on LinkedIn; make them count, the hook must land there
- NEVER use em-dashes (—). Use a comma, period, colon, or line break instead
- Line breaks are rhythm tools; use them intentionally, not just for readability
- Parenthetical asides are allowed for humor or self-awareness (sparingly)
- State stakes, numbers, and targets bluntly, no softening language
- If the user provides a transcript or article, extract the core insight first, then treat it as the main message input
- The output must always be a ready-to-paste LinkedIn post. Never deliver analysis, explanations, or scaffolding as the final output
- Never write in gerund form as a main verb construction (PT/ES: avoid "explorando", "aproveitando", etc.)
- Never use reflexive formal constructions in Portuguese/Spanish (e.g. "explorar-se", "observar-se") — write as people actually speak

### Banned Words and Terms

Never use the following — replace with direct, concrete alternatives:

**English:**
crucial, essential, fundamental, key (as adjective), vital, journey, in summary, in short, to summarize, basically, needless to say, it goes without saying, synergy, leverage (as verb), unlock, game-changer, seamless, robust, holistic, cutting-edge, empower, disrupt

**Spanish:**
crucial, esencial, fundamental, clave (como adjetivo), vital, viaje / trayectoria (en sentido metafórico), en resumen, en definitiva, básicamente, huelga decir, no hace falta decir, sinergia, aprovechar (en sentido corporativo), potenciar, transformador, disruptivo, fluido, robusto, empoderar, desbloquear

**Portuguese (Brazil):**
crucial, essencial, fundamental, chave (como adjetivo), vital, jornada, em resumo, em suma, basicamente, desnecessário dizer, sinergia, alavancar, desbloquear, transformador, disruptivo, fluido, robusto, empoderar, potencializar
