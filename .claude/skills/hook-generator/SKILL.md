---
name: hook-generator
description: >
  Generate and score hook variants for ANY content surface — video, LinkedIn,
  carousels, X/Twitter, generic text posts, newsletter/article headlines, and
  email subject lines. Use whenever a hook, opening line, headline, subject line,
  or scroll-stopper is needed before writing the body. First step in any scripting
  or post pipeline; invoked internally by short-video-copywriting,
  longform-video-scripting, linkedin-post-generator, and threads-x-post-generator.
  Trigger directly on "hook options", "hook variants", "give me hooks for X",
  "write me a hook", "subject line for this email", "headline for this
  article/newsletter", or "opening line for this post". Produces N hooks (default 5),
  each scored against a unified 4-dimension rubric with per-surface weights.
---

# Hook Generator

## Purpose
Generate hook variants for a given topic and surface, then score each against a
single unified rubric (4 dimensions) whose weights shift per surface. The hook is
the single highest-leverage creative decision in any piece of content — it must be
locked before the body is written. One engine, every surface.

## Position in Pipeline
```
art-director brief / topic / transcript
                ↓
        hook-generator        ← THIS SKILL (surface-aware)
                ↓
   scripting OR post-writing skill for the chosen surface
```

---

## Step 1 — Resolve the Surface (do this first, always)

The surface determines the cut point, length limits, structure, and scoring
weights. Never generate hooks before the surface is known.

Detect from context. If ambiguous, ask ONE question:
> "Which surface? (video / LinkedIn / carousel / X-Twitter / text post / newsletter-article headline / email subject)"

Supported surfaces and their reference files (read the matching one before generating):

| Surface | Reference file |
|---|---|
| Video (short + long) | `references/video.md` |
| LinkedIn | `references/linkedin.md` |
| Carousel | `references/carousel.md` |
| X / Twitter | `references/x-twitter.md` |
| Text post (IG caption, Threads, FB, generic) | `references/text-post.md` |
| Newsletter / Article headline | `references/newsletter-article-headline.md` |
| Email subject line | `references/email-subject.md` |

For every non-video surface, ALSO read `references/text-style-rules.md` (shared
style + banned-words list). It is mandatory, not optional.

---

## Inputs
**Required**
- **Surface** (see Step 1)
- **Topic / message**: subject, working title, transcript, or core insight

**Optional**
- **Brand / art director brief**: tone + vocabulary constraints (apply as a filter)
- **N**: number of hooks (default 5)
- **Hook type constraint**: e.g. "only Contrarian hooks"

---

## Unified Hook Taxonomy

Every hook belongs to one of these master types. Generate variety across types by
default. Each reference file flags which types over- or under-index on that surface.

```
Contrarian / Myth-Bust        "Most people think X. They're wrong."
Exact Pain / Frustration      Names the precise wound the reader has right now
Arresting Claim / Bold        Extreme or counterintuitive statement demanding resolution
Identity Threat               Implicates the reader's self-image directly
Contrast / Before-After       Two opposing realities (or past vs present) in one line
Question                      Direct question the reader cannot answer without continuing
List Promise                  "N things that [outcome]" — withhold creates completion drive
Statistic / Number            Leads with a striking data point or result
Secret / Reveal               Implies insider knowledge ("What nobody tells you about X")
Personal Story (Failure/Win)  Vulnerability or milestone as the entry point
```

---

## Unified Scoring System (4 dimensions, per-surface weights)

Score every hook on the SAME four dimensions, 1–10 each. Only the **weights** change
by surface — that is the entire mechanism. This keeps scores comparable across surfaces
while respecting what each surface actually rewards.

### The 4 Dimensions

**D1 — Scroll-Stop / Fold Survival**
Does the hook survive this surface's cut point with zero context?
The "cut point" is surface-specific (defined in each reference): first ~1–3s for video,
first 180 chars for LinkedIn, the cover slide for carousel, ~280 chars / first tweet for X,
the visible subject line for email, the share-card/SEO truncation for headlines.
- 9–10: Stops a cold reader, no prior knowledge needed, lands fully before the cut
- 7–8: Strong but needs slight niche familiarity, or grazes the cut point
- 5–6: Works only on a warm audience
- 1–4: Dies at the fold / the scroll

**D2 — Curiosity Gap**
Does it withhold something the reader genuinely needs to know?
- 9–10: Unbearable tension, answer is not guessable
- 7–8: Clear withhold, answer somewhat guessable
- 5–6: Mild intrigue, reader could skip and feel no loss
- 1–4: No withhold, everything is telegraphed

**D3 — Pacing / Zero Throat-Clear**
Economy of words. No warm-up, no hedging, immediate tension.
- 9–10: Every word earns its place. Could not be shorter.
- 7–8: One or two words could be cut
- 5–6: Noticeable filler or slow start
- 1–4: Warm-up present, takes too long to land

**D4 — Shareability / Stake**
Would someone share, quote, repost, save, or forward this? Does it stake a position
worth taking sides on, or hand the reader social currency?
- 9–10: Reader wants to repost/quote to signal identity or start a fight
- 7–8: Clearly shareable, mild social risk
- 5–6: Interesting but private, no impulse to broadcast
- 1–4: Nobody attaches their name to this

### Per-Surface Weight Table (each row sums to 1.00)

| Surface | D1 Scroll/Fold | D2 Curiosity | D3 Pacing | D4 Shareability |
|---|---|---|---|---|
| Video — Short | 0.40 | 0.30 | 0.20 | 0.10 |
| Video — Long | 0.35 | 0.35 | 0.15 | 0.15 |
| LinkedIn | 0.35 | 0.25 | 0.20 | 0.20 |
| Carousel | 0.35 | 0.30 | 0.10 | 0.25 |
| X / Twitter | 0.30 | 0.25 | 0.15 | 0.30 |
| Text post (generic) | 0.35 | 0.30 | 0.15 | 0.20 |
| Newsletter / Article headline | 0.35 | 0.40 | 0.10 | 0.15 |
| Email subject | 0.40 | 0.40 | 0.15 | 0.05 |

### Formula
```
Hook Score = (D1 × wD1) + (D2 × wD2) + (D3 × wD3) + (D4 × wD4)
expressed as X/10, using the active surface's weights
```
Each reference file restates its own weight row so the scorer never has to leave it.

---

## Generation Rules (shared across surfaces)

**Brand voice filter (if a brief is provided)**
- Apply brand tone and vocabulary constraints from the brief
- The hook must pass the brand's persona test before being included

**Diversity rule**
- Default 5 hooks must span at least 3 different master types
- Never generate 5 hooks of the same type
- At least one hook must score 8+ on D1 (Scroll-Stop / Fold Survival)

**Quality floor**
- Do not output any hook scoring below 6.0 overall
- If generation produces weak hooks, regenerate before outputting
- Better to output 3 strong hooks than 5 weak ones

**Length & structure**
- Governed by the active surface's reference file. Read it first.

---

## Output Format (surface-aware)

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
HOOK VARIANTS
Topic:    [topic]
Surface:  [surface]    Brand: [brand/channel or "—"]
Weights:  D1 [..] · D2 [..] · D3 [..] · D4 [..]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

HOOK 01 — [Type]
"[Hook text — formatted as it will appear on the surface]"
D1 Scroll/Fold: [X/10]   D2 Curiosity: [X/10]
D3 Pacing:      [X/10]   D4 Share:     [X/10]
Hook Score:     [X/10]
Why it works:   [One sentence — the specific mechanism]

[...repeat for all N hooks]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
RECOMMENDED: HOOK [number]
Reason: [One sentence — why it wins for this topic + surface]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

For multi-line surfaces (LinkedIn, carousel, text post), show the hook with its real
line breaks. For headline/subject surfaces, show character count next to the hook.

---

## Handoff to Writing Skills

When invoked internally by a scripting or post skill:
1. Generate and score hooks as above
2. Present to the user for selection (or auto-select the highest scorer in fully
   automated pipelines)
3. Pass to the downstream skill:
   - SELECTED_HOOK: "[hook text]"
   - SURFACE: [surface]
   - HOOK_TYPE: [type]
   - HOOK_SCORE: [X/10]
   - HOOK_MECHANISM: [why it works — informs body tone]

The hook is the contract with the reader. Everything in the body must deliver on it.
