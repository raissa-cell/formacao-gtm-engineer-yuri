---
name: proposal-followup-email
description: >
  Use this skill whenever the user wants to write a commercial email that accompanies or follows up
  on a business proposal. Triggers include: "escreve o email da proposta", "email acompanhando a proposta",
  "email de follow-up da reunião", "draft the proposal email", "email para enviar com a proposta",
  or any combination of [proposal/deck/doc] + [email/follow-up/cover letter] + [lead/client/meeting].
  Also trigger when the user provides a meeting transcript or summary AND a proposal document and
  asks for a communication artifact. This skill is essential — use it even if the user just says
  "email para o [nome] sobre a proposta".
---

# Skill: Proposal Follow-Up Email

Writes a high-converting commercial email that accompanies a business proposal, synthesizing
the proposal content + meeting transcript to produce a personalized, structured, send-ready message.

---

## Inputs Expected

The user should provide **at least one** of:
1. **Proposal** — PDF, deck, doc, or pasted text (pricing, scope, solution overview)
2. **Meeting transcript/notes** — raw transcript, summary, or bullet-point notes from the discovery/demo call

If only one is provided, proceed with what's available and flag what's missing.

---

## Step-by-Step Execution

### 1. Extract Key Signal

From the **proposal**, extract:
- Solution offered + key differentiators
- Pricing / commercial conditions (tiers, volumes, payment terms)
- Proposed next steps or CTA

From the **transcript**, extract:
- Lead's **pain points** stated explicitly (direct quotes preferred)
- Lead's **goals / desired outcomes**
- **Objections or hesitations** raised
- **Agreements reached** during the call (what they liked, what they validated)
- Decision-maker dynamics (who was in the room, who decides)
- Any **specific context** (company name, team size, urgency signals, integrations mentioned)

> If transcript is absent: work only from proposal + any context provided. Note the gap.

---

### 2. Construct the Email

Use the structure below. Adapt formality to the context (B2B default = semi-formal, objective).

```
SUBJECT: {{personalized_subject}} — avoid generic "Proposta Nuvia" style

BODY:

[Opening — 1–2 lines]
Reference the meeting directly. Acknowledge what was discussed, the lead's challenge,
or a specific moment from the conversation. No "espero que esteja bem".

[Bridge — 2–3 lines]
Connect their stated pain → what the proposal addresses.
Use their language, not generic sales language.

[Proposal Summary — 3–5 lines or bullet list]
Synthesize the proposed solution in 3–5 key points.
Highlight the one or two items that directly address the lead's top concern.
Do NOT paste the full proposal — this is a curated highlight reel.

[Commercial Conditions — optional, 1–2 lines]
Only if pricing was disclosed in the proposal. Keep brief.
Example: "Conforme combinado, incluímos a opção [X] com condição especial de onboarding."

[Objection Handling — optional, 1 short paragraph]
If a key hesitation was raised in the meeting, address it lightly here.
Frame as reassurance, not defense.

[CTA — 1–2 lines, explicit]
One clear next step. Either:
- Schedule a follow-up call
- Request a decision by a specific date
- Ask for feedback on the proposal by [date]

[Sign-off]
Professional but warm. Match persona/company tone.
```

---

### 3. Tone and Language Rules

- **Language**: Match the language of the transcript/proposal (PT-BR default for Nuvia/Datasaga)
- **Formality**: B2B semi-formal. "Você" for PT-BR unless the call used "senhor/senhora"
- **Length**: 150–280 words ideal. Never exceed 350 unless requested
- **No filler**: eliminate "espero que esteja bem", "conforme conversamos anteriormente", generic openers
- **Subject line**: specific + intriguing. Include company name or pain point.
  - Good: `ISA + [Empresa]: automatizando qualificação inbound`
  - Bad: `Proposta Nuvia — Revenue OS`

---

### 4. Variations to Offer (auto-generate unless told otherwise)

Always produce **2 variants**:

| Variant | Style | When to Use |
|---------|-------|-------------|
| **A — Direto** | Concise, exec-to-exec tone, bullets | Decision-maker is C-level / time-constrained |
| **B — Relacional** | Warmer, more narrative, references meeting moments | Champion who needs to sell internally |

Label clearly. User picks or asks to blend.

---

### 5. Placeholders

Use `{{variable}}` for anything not determinable from inputs:

- `{{lead_name}}` — first name of primary contact
- `{{company_name}}` — lead's company
- `{{sender_name}}` — email sender
- `{{follow_up_date}}` — proposed date for next step
- `{{specific_pain}}` — if the transcript doesn't make it explicit
- `{{pricing_tier}}` — if multiple tiers exist and choice is unclear

---

### 6. Output Format

Deliver:
1. **Variant A** (full email, subject included)
2. **Variant B** (full email, subject included)
3. **1-line rationale** per variant (when to use which)
4. **Optional**: flag any missing info that would sharpen personalization

Do NOT add commentary before the emails. Lead with the subject line immediately.

---

## Reference: What Makes a Great Proposal Email

See `references/quality-criteria.md` for scoring rubric and anti-patterns.
Consult it when evaluating output quality or iterating.
