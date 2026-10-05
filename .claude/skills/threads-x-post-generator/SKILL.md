---
name: threads-x-post-generator
description: "Generate high-performing Threads and X (Twitter) posts from any input (idea, theme, message, transcript, or notes). Handles both single posts and threads/tweet chains. Always follows a structured pipeline: platform selection first, then 5 hook options, then full post. Use this skill whenever the user wants to write, draft, or create a post for X, Twitter, or Threads, wants hook options for X or Threads, says 'write me a tweet', 'write me a thread', 'make a Threads post', 'I need a post for X about X', or provides a topic/idea and mentions X or Threads. Also trigger when the user provides a transcript or article and asks to turn it into a tweet, thread, or Threads post."
---

# Threads / X Post Generator

Generate sharp, high-impact posts for X (Twitter) and Threads. Same pipeline as LinkedIn, adapted for shorter formats and faster feeds.

Three stages:

**Stage 0: Platform + Format** (confirm before hooks)
**Stage 1: 5 Hook Options** (present first, wait for selection)
**Stage 2: Full Post or Thread** (only after hook is chosen)

Never skip to the full post without hook selection.

---

## Stage 0: Platform and Format

If not specified, ask one question:

> "Platform: X, Threads, or both? And format: single post or thread?"

**Platform differences:**
- **X:** 280 characters per post. Punchier, faster, more aggressive tone acceptable.
- **Threads:** 500 characters recommended per post. More conversational, closer to LinkedIn in register.
- **Both:** Write X first (tighter constraint), then adapt for Threads.

**Format options:**
- **Single post:** One standalone post. Maximum impact in minimum space.
- **Thread/chain:** Multi-post sequence. Numbered (1/N) for X, line-break separated for Threads.

---

## Stage 1: Hook Generation

Generate exactly **5 hook options**. Each must use a different hook type. Label each.

The hook is always post 1 in a thread, or the entire post in single format. It must work as a standalone sentence.

### Hook Structure

**Simple Hook** (default):
```
[Hook line]

[Rehook — optional for very punchy hooks]
```

For X: hook + rehook must fit 280 chars. If not, drop the rehook.
For Threads: Simple Hook default. Full Hook (3 lines) allowed if topic warrants it.

### Hook Type Menu

- **Contrarian** — Challenge a common belief
- **Statistic/Number** — Lead with a striking data point or result
- **Personal failure/win** — Story-based, vulnerability or milestone
- **Question** — Direct question that triggers self-reflection
- **Bold statement** — Provocative claim or declaration
- **Secret/Reveal** — Imply insider knowledge
- **Before/After** — Contrast past vs. present state
- **Relatable frustration** — Name a pain the audience feels

After the 5 options, ask: *"Which hook do you prefer? (1-5) Or tell me what to adjust."*

---

## Stage 2: Full Post or Thread

### Single Post Guidelines

- **X:** Max 280 characters. Every word earns its place.
- **Threads:** Up to 500 characters. More breathing room, still tight.
- One idea per post. End with a punchy final line or CTA. Not both.

### Thread Guidelines

**Structure:**
```
Post 1: Hook (must work standalone)
Post 2-N: Body (one idea per post)
Last post: CTA or takeaway
```

**Rules per post in thread:**
- One idea per post. No exceptions.
- Each post readable standalone. No "as I said above."
- X: numbered (1/7, 2/7...). Threads: line breaks + separators.
- Create pull to the next post. Never end mid-thread with dead silence.

**Thread length:**
- Short: 3-5 posts (default)
- Medium: 6-10 posts
- Long: 10+ (ask first)

### Writing Style

**Voice:**
- First person ("I") or direct "you." No indirect third-person.
- Personal opinions. POV, not a report.
- Rawer than LinkedIn. More edge, less polish. Same confidence.

**Assertiveness:**
- Direct, no hedging. Facts and actions carry weight.
- Use: "Companies that ignore AI in 2025 are already behind."
- NOT: "It is becoming increasingly important for companies to consider AI."

**Scenarios:**
- No "imagine", "suppose", "picture this." Direct framing only.
- Use: "A founder without a GTM system is just a builder with no customers."

**Tone:**
- Confident, direct, occasionally humorous. Faster delivery than LinkedIn.
- More casual contractions allowed. Wit sharpens the point.
- Short sentences dominate. Longer ones for setup only.

### CTA Guidelines

Default: ask for opinion or reaction.
> "What's your take?" / "Agree?" / "Seen this in your market?"

Vary by context:
- Promoting something: drive to link or DM
- Sharing a lesson: invite stories
- Controversial: one word works best ("Disagree?")
- Threads: CTA goes in the last post only

Never use engagement-bait phrasing ("Like and RT if you agree").

---

## Language

Default to the user's language. Full post/thread localized. Do not mix languages unless asked.

---

## Reference Library

The file `references/140_templates.txt` contains 140 LinkedIn post templates with real examples, breakdowns, and copywriting formulas (AIDA, PAS, Slippery Slide, etc.).

**Always open this file before writing the full post (Stage 2).** Mandatory step.

Process:
1. Open `references/140_templates.txt`
2. Identify 2-3 templates most relevant to the chosen hook type and topic
3. Extract the structural pattern only (labels, sequence, format)
4. Adapt to platform format: compress for X, adapt for Threads

Read selectively: scan by number or keyword. Do not process all 140 templates.

---

## Output Format

**Stage 0:** State platform + format. Skip question if already clear from context.

**Stage 1:**
```
5 hook options for your [X/Threads] post about [TOPIC]:

**1. [Hook Type]**
[Hook]
[Rehook]

---
**2. [Hook Type]**
...

Which do you prefer? (1-5) Or tell me what to adjust.
```

**Stage 2 — Single post:**
Clean copy, ready to paste.
```
---
Post stats: ~[X] chars | Platform: [X/Threads] | Single | CTA: [type]
```

**Stage 2 — Thread:**
```
-- 1/N --
[Hook]

-- 2/N --
[Body]

...

-- N/N --
[CTA]
---
Thread stats: [N] posts | Platform: [X/Threads] | ~[X] chars avg
```

---

## Rules

- Never generate the full post before hook selection
- Never use hashtags unless explicitly asked
- Never add emojis unless the user's tone is casual and they use them naturally
- NEVER use em-dashes (--). Use comma, period, colon, or line break instead
- X: respect 280-char limit per post
- Threads: each post standalone, no "as mentioned above"
- Line breaks are rhythm tools, use intentionally
- State stakes and numbers bluntly, no softening
- Bold coined terms when introduced
- If input is a transcript or article, extract core insight first
- If writing for both platforms, write X first, then adapt for Threads
