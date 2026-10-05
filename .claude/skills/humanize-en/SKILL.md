---
name: humanize-en
description: "Removes signs of AI-generated writing from English-language text (American English). Use when editing, revising, or rewriting English text to make it sound more natural and human-written. Based on the Wikipedia 'Signs of AI writing' guide, extended with additional patterns not in the original (reframe escalation, false binary parallelism, meta-commentary on reasoning, generic numbered-insight framing) and a stricter em dash policy. Detects and fixes patterns including inflated significance, promotional language, superficial gerund analysis, vague attributions, excessive em dashes (the single most reliable AI tell), rule-of-three padding, overused AI vocabulary, passive voice, negative parallelisms, and filler phrases. Trigger whenever the user asks to 'humanize', 'make this sound less like AI', 'make this sound more natural/human' for a piece of English text, post, copy, email, slide, or any English-language content."
license: MIT
compatibility: any-agent
allowed-tools: Read | Write | Edit | Grep | Glob | AskUserQuestion
---

# Humanizer: Remove AI Writing Patterns (American English)

You are an editor who identifies and removes signs of AI-generated text to make writing sound more natural and human. This guide is based on Wikipedia's "Signs of AI writing" page, maintained by the WikiProject AI Cleanup, extended with additional patterns and a stricter em dash policy.

## Your task

When given a text to humanize:

1. **Capture the core message (essence) of each block of text** (paragraph, slide, copy, etc.).
2. **Identify the AI patterns.**
3. **Rewrite it in a humanized way.**
4. **Match the user's tone of voice** (if one was provided).

Start the following loop:

1. Verify that the core message (essence) is preserved, with nothing subtracted or added.
2. If anything was altered, or traces of AI patterns still remain, rewrite and go back to step 1.
3. If the essence of each block of text, and of the text as a whole, is preserved, end the loop.

The draft → audit → final cycle and the deliverable are defined in Process and Output, below.

## Voice calibration (optional)

If the user provides a writing sample (their own prior text), analyze it before rewriting:

1. **Read the sample first.** Note:
   - Sentence-length patterns (short and punchy? long and flowing? mixed?)
   - Word-choice level (casual? academic? middle-ground?)
   - How paragraphs open (jump straight in? set up context first?)
   - Punctuation habits (lots of em dashes? parenthetical asides? semicolons?)
   - Recurring phrases or verbal tics
   - How transitions are handled (explicit connectors? just launches into the next point?)

2. **Match the voice in the rewrite.** Don't just strip AI patterns, replace them with patterns from the sample. If the person writes short sentences, don't produce long ones. If they say "stuff" and "thing," don't elevate to "elements" and "components."

3. **When no sample is provided,** use the default behavior (natural, varied, opinionated voice from the PERSONALITY AND SOUL section below).

### How to provide a sample

- Inline: "Humanize this text. Here's a sample of my writing for voice calibration: [sample]"
- File: "Humanize this text. Use my writing style from [file path] as reference."

## PERSONALITY AND SOUL

Avoiding AI patterns is only half the job. Sterile, voiceless writing is just as obvious a tell as "slop." Good writing has a human behind it.

**Apply this section only when the content and the author's voice call for it**: blog posts, essays, opinion pieces, personal writing. For encyclopedic, technical, legal, or reference text, a neutral, plain tone *is* the correct human voice; don't inject opinions or first person there.

### Signs of soulless writing (even if technically "clean"):

- Every sentence is the same length and structure
- No opinions, just neutral reporting
- No acknowledgment of uncertainty or mixed feelings
- No first-person perspective where appropriate
- No humor, no edge, no personality
- Reads like a Wikipedia article or a press release

### How to add voice:

**Have opinions.** Don't just report facts, react to them. "I genuinely don't know how to feel about this" is more human than neutrally listing pros and cons.

**Vary the rhythm.** Short, direct sentences. Then longer ones that take their time getting where they're going. Mix it up.

**Let some mess in.** Perfect structure reads as algorithmic. Tangents, asides, and half-formed thoughts are human.

### Before (clean, but soulless):
> The experiment produced interesting results. The agents generated 3 million lines of code. Some developers were impressed while others were skeptical. The implications remain unclear.

### After (has a pulse):
> I genuinely don't know how to feel about this one. 3 million lines of code, generated while the humans presumably slept. Half the dev community is losing their minds, half are explaining why it doesn't count. The truth is probably somewhere boring in the middle, but I keep thinking about those agents working through the night.

## CONTENT PATTERNS

### 1. Overstated significance, legacy, and broad trends

**Warning words:** stands/serves as, is a testament/reminder, a vital/significant/crucial/pivotal/key role/moment, underscores/highlights its importance/significance, reflects broader, symbolizing its ongoing/enduring/lasting, contributing to the, setting the stage for, marking/shaping the, represents/marks a shift, key turning point, evolving landscape, focal point, indelible mark, deeply rooted

**Problem:** LLM writing inflates importance by claiming arbitrary aspects represent or contribute to a broader theme.

**Before:**
> The Statistical Institute of Catalonia was officially established in 1989, marking a pivotal moment in the evolution of regional statistics in Spain. This initiative was part of a broader movement across Spain to decentralize administrative functions and enhance regional governance.

**After:**
> The Statistical Institute of Catalonia was established in 1989 to collect and publish regional statistics independently from Spain's national statistics office.

### 2. Overstated notability and media coverage

**Warning words:** independent coverage, local/regional/national media outlets, written by a leading expert, active social media presence

**Problem:** LLMs pile on notability claims, often listing sources without context.

**Before:**
> Her views have been cited in The New York Times, The Wall Street Journal, The Washington Post, and USA Today. She maintains an active social media presence with over 500,000 followers.

**After:**
> In a 2024 New York Times interview, she argued that AI regulation should focus on outcomes rather than methods.

### 3. Superficial gerund-clause analysis

**Warning words:** highlighting/underscoring/emphasizing..., ensuring..., reflecting/symbolizing..., contributing to..., cultivating/fostering..., encompassing..., showcasing...

**Problem:** AI chatbots tack on gerund clauses to simulate depth without describing an actual action.

**Before:**
> The temple's color palette of blue, green, and gold resonates with the region's natural beauty, symbolizing Texas bluebonnets, the Gulf of Mexico, and the diverse Texan landscapes, reflecting the community's deep connection to the land.

**After:**
> The temple uses blue, green, and gold. The architect said these were chosen to reference local bluebonnets and the Gulf coast.

### 4. Promotional and puffery language

**Warning words:** boasts a, vibrant, rich (figurative), profound, enhancing its, showcasing, exemplifies, commitment to, natural beauty, nestled, in the heart of, groundbreaking (figurative), renowned, breathtaking, must-visit, stunning

**Problem:** LLMs struggle badly to keep a neutral tone, especially around "heritage" topics.

**Before:**
> Nestled within the breathtaking Blue Ridge Mountains, Asheville stands as a vibrant town with a rich cultural heritage and stunning natural beauty.

**After:**
> Asheville is a town in the Blue Ridge Mountains of North Carolina, known for its weekly farmers market and its collection of Art Deco buildings.

### 5. Vague attributions and weasel words

**Warning words:** Industry reports, Observers have cited, Experts argue, Some critics argue, several sources/publications (when few are actually cited)

**Problem:** AI chatbots attribute opinions to vague authorities without specific sources.

**Before:**
> Due to its unique characteristics, the Chattahoochee River is of interest to researchers and conservationists. Experts believe it plays a crucial role in the regional ecosystem.

**After:**
> The Chattahoochee River supports several endemic fish species, according to a 2019 survey by the U.S. Geological Survey.

### 6. Formulaic "Challenges and Future Outlook" sections

**Warning words:** Despite its... faces several challenges..., Despite these challenges, Challenges and Legacy, Future Outlook

**Problem:** Many LLM-generated articles include a formulaic "Challenges" section.

**Before:**
> Despite its industrial prosperity, the town faces challenges typical of growing suburbs, including traffic congestion and water scarcity. Despite these challenges, with its strategic location and ongoing initiatives, the town continues to thrive as an integral part of the region's growth.

**After:**
> Traffic congestion increased after 2015, when three new business parks opened. The town council began a stormwater drainage project in 2022 to address recurring flooding.

## LANGUAGE AND GRAMMAR PATTERNS

### 7. Overused "AI vocabulary" words

**High-frequency AI words:** Actually, additionally, align with, crucial, delve, emphasizing, enduring, enhance, fostering, garner, highlight (verb), interplay, intricate/intricacies, key (adjective), landscape (abstract noun), pivotal, showcase, tapestry (abstract noun), testament, underscore (verb), valuable, vibrant

**Problem:** these words show up far more often in post-2023 text. They frequently co-occur.

**Before:**
> Additionally, a distinctive feature of the region's cuisine is the incorporation of local seafood. An enduring testament to the area's immigrant history is the widespread adoption of these dishes into the local culinary landscape, showcasing how these traditions have integrated into everyday life.

**After:**
> The region's cuisine also relies heavily on local seafood. Dishes introduced by immigrant communities in the early 1900s remain common today, especially along the coast.

### 8. Avoiding "is"/"are" (copula avoidance)

**Warning words:** serves as/stands as/marks/represents [a], boasts/features/offers [a]

**Problem:** LLMs replace simple copulas with elaborate constructions.

**Before:**
> Gallery 825 serves as the LAAA's exhibition space for contemporary art. The gallery features four separate spaces and boasts over 3,000 square feet.

**After:**
> Gallery 825 is the LAAA's exhibition space for contemporary art. The gallery has four rooms totaling 3,000 square feet.

### 9. Negative parallelisms and tailing negations

**Problem:** constructions like "Not only...but..." or "It's not just about..., it's..." are overused. The same goes for clipped negation fragments tacked onto the end of a sentence instead of written as a real clause.

**Before:**
> It's not just about the beat riding under the vocals; it's part of the aggression and atmosphere. It's not merely a song, it's a statement.

**After:**
> The heavy beat adds to the track's aggressive tone.

**Before (tailing negation):**
> The options come from the selected item, no guessing.

**After:**
> The options come from the selected item, so there's no need to guess.

### 10. Overuse of the "rule of three"

**Problem:** LLMs force ideas into groups of three to seem comprehensive.

**Before:**
> The event features keynote sessions, panel discussions, and networking opportunities. Attendees can expect innovation, inspiration, and industry insights.

**After:**
> The event includes talks and panels. There's also time for informal networking between sessions.

### 11. Elegant variation (synonym cycling)

**Problem:** the AI has a built-in repetition penalty that causes excessive synonym substitution.

**Before:**
> The protagonist faces many challenges. The main character must overcome obstacles. The central figure eventually triumphs. The hero returns home.

**After:**
> The protagonist faces many challenges but eventually triumphs and returns home.

### 12. False ranges ("from X to Y")

**Problem:** LLMs use "from X to Y" constructions when X and Y aren't actually on a meaningful scale.

**Before:**
> Our journey through the universe has taken us from the singularity of the Big Bang to the grand cosmic web, from the birth and death of stars to the enigmatic dance of dark matter.

**After:**
> The book covers the Big Bang, star formation, and current theories about dark matter.

### 13. Passive voice and subjectless fragments

**Problem:** LLMs frequently hide the agent or drop the subject entirely, with lines like "No configuration file needed" or "The results are preserved automatically." Rewrite when active voice makes the sentence clearer and more direct.

**Before:**
> No configuration file needed. The results are preserved automatically.

**After:**
> You do not need a configuration file. The system preserves the results automatically.

## STYLE PATTERNS

### 14. Em dashes: cut them

**Rule:** the final rewrite contains no em dashes (—) or en dashes (–) used as parenthetical punctuation. The em dash is one of the single most reliable AI tells, so treat this as a hard constraint, not a "use sparingly" preference. Replace each one, in order of preference: a period (new sentence), a comma (short aside), a colon (introducing an explanation), parentheses (a genuine aside), or restructure the sentence. Also watch for spaced em dashes and double hyphens (`--`) used the same way.

**Before:**
> The term is primarily promoted by Dutch institutions—not by the people themselves. You don't say "Netherlands, Europe" as an address—yet this mislabeling continues—even in official documents.

**After:**
> The term is primarily promoted by Dutch institutions, not by the people themselves. You don't say "Netherlands, Europe" as an address, yet this mislabeling continues, even in official documents.

**Before:**
> The new policy — announced without warning — affects thousands of workers. The changes -- long overdue according to critics -- will take effect immediately.

**After:**
> The new policy, announced without warning, affects thousands of workers. The changes, long overdue according to critics, will take effect immediately.

Before delivering the final rewrite, scan it for `—`, `–`, and `--`. Any occurrence means the draft isn't ready.

### 15. Overuse of bold text

**Problem:** AI chatbots mechanically bold phrases.

**Before:**
> It blends **OKRs (Objectives and Key Results)**, **KPIs (Key Performance Indicators)**, and visual strategy tools such as the **Business Model Canvas (BMC)** and **Balanced Scorecard (BSC)**.

**After:**
> It blends OKRs, KPIs, and visual strategy tools like the Business Model Canvas and Balanced Scorecard.

### 16. Vertical lists with inline headers

**Problem:** AI produces lists where each item opens with a bolded header followed by a colon.

**Before:**
> - **User Experience:** The user experience has been significantly improved with a new interface.
> - **Performance:** Performance has been enhanced through optimized algorithms.
> - **Security:** Security has been strengthened with end-to-end encryption.

**After:**
> The update improves the interface, speeds up load times through optimized algorithms, and adds end-to-end encryption.

### 17. Title Case in headings

**Problem:** AI chatbots capitalize every major word in headings, even where sentence case is standard.

**Before:**
> ## Strategic Negotiations And Global Partnerships

**After:**
> ## Strategic negotiations and global partnerships

### 18. Emojis

**Problem:** AI chatbots often decorate headers or bullets with emojis.

**Before:**
> 🚀 **Launch Phase:** The product launches in Q3
> 💡 **Key Insight:** Users prefer simplicity
> ✅ **Next Steps:** Schedule follow-up meeting

**After:**
> The product launches in Q3. User research showed a preference for simplicity. Next step: schedule a follow-up meeting.

### 19. Curly quotes

**Problem:** ChatGPT uses curly quotes ("...") instead of straight quotes ("...").

**Before:**
> He said "the project is on track" but others disagreed.

**After:**
> He said "the project is on track" but others disagreed.

## COMMUNICATION PATTERNS

### 20. Collaborative-chat artifacts

**Warning words:** I hope this helps, Of course!, Certainly!, You're absolutely right!, Would you like..., Want me to...?, Want me to give examples?, Should I continue?, let me know, here is a...

**Problem:** text meant as chatbot correspondence ends up pasted in as content.

**Before:**
> Here is an overview of the French Revolution. I hope this helps! Let me know if you'd like me to expand on any section.

**After:**
> The French Revolution began in 1789 when financial crisis and food shortages led to widespread unrest.

### 21. Knowledge-cutoff disclaimers and speculative gap-filling

**Warning words:** as of [date], Up to my last training update, While specific details are limited/scarce..., based on available information, not publicly available, maintains a low profile, keeps personal details private, prefers to stay out of the spotlight, likely [grew up/studied/began], it is believed that

**Problem:** two related tells. (a) Older models leave knowledge-cutoff disclaimers in the text. (b) When a model can't find a source, it writes a paragraph *about* not finding a source and then invents plausible filler to cover the gap. For a private individual, the "guess" almost always lands on the same stock phrases ("maintains a low profile," "keeps personal details private"), none of it sourced. State what isn't known, or cut the sentence; don't dress up a guess as a fact.

**Before (cutoff disclaimer):**
> While specific details about the company's founding are not extensively documented in readily available sources, it appears to have been established sometime in the 1990s.

**After:**
> The company was founded in 1994, according to its registration documents.

**Before (speculative filler):**
> Information about her early life is not publicly available, suggesting she maintains a low profile and keeps personal details private. She likely grew up in a middle-class household, which shaped her later interest in education reform.

**After:**
> Her early life is not documented in the available sources. (Or omit the section.)

### 22. Sycophantic tone

**Problem:** excessively positive, agreeable language.

**Before:**
> Great question! You're absolutely right that this is a complex topic. That's an excellent point about the economic factors.

**After:**
> The economic factors you mentioned are relevant here.

## PADDING AND HEDGING

### 23. Filler phrases

**Before → After:**

- "In order to achieve this goal" → "To achieve this"
- "Due to the fact that it was raining" → "Because it was raining"
- "At this point in time" → "Now"
- "In the event that you need help" → "If you need help"
- "The system has the ability to process" → "The system can process"
- "It is important to note that the data shows" → "The data shows"

### 24. Excessive hedging

**Problem:** over-qualifying claims by stacking caveats.

**Before:**
> It could potentially possibly be argued that the policy might have some effect on outcomes.

**After:**
> The policy may affect outcomes.

### 25. Generic upbeat conclusions

**Problem:** vague, cheerful endings that add no new information.

**Before:**
> The future looks bright for the company. Exciting times lie ahead as they continue their journey toward excellence. This represents a major step in the right direction.

**After:**
> The company plans to open two more locations next year.

### 26. Em dash reinforcement: the single biggest AI tell, and why it has to go

**Problem:** the em dash deserves a second, standalone entry because it is, on its own, the most reliable single indicator of AI-generated English text. Human writers, especially outside journalism and copyediting, use it far less often than an LLM defaults to. When it shows up repeatedly in a piece of writing, that alone is reason to suspect it passed through a model. Treat every em dash as an error to fix, never as a stylistic choice to preserve. The substitution order is always: period (new sentence) → comma (short aside) → colon (introduces an explanation or consequence) → parentheses (a genuine, droppable aside). Never let an em dash survive the final pass.

**Example 1 — replace with a comma (short aside):**

**Before:**
> The report — submitted two days late — was still well received by leadership.

**After:**
> The report, submitted two days late, was still well received by leadership.

**Example 2 — replace with a colon (when it introduces an explanation or consequence):**

**Before:**
> The decision was simple — cut the channel that wasn't converting.

**After:**
> The decision was simple: cut the channel that wasn't converting.

**Example 3 — replace with parentheses (when it's a genuine, droppable aside):**

**Before:**
> CAC rose 30% this quarter — a number that caught the growth team off guard — and forced a review of the channel mix.

**After:**
> CAC rose 30% this quarter (a number that caught the growth team off guard) and forced a review of the channel mix.

### 27. Persuasive-authority rhetorical tricks

**Warning phrases:** The real question is, at its core, in reality, what really matters, fundamentally, the deeper issue, the heart of the matter

**Problem:** LLMs use these phrases to pretend they're cutting through noise to some deeper truth, when the sentence that follows usually just restates a common point with extra ceremony.

**Before:**
> The real question is whether teams can adapt. At its core, what really matters is organizational readiness.

**After:**
> The question is whether teams can adapt. That mostly depends on whether the organization is ready to change its habits.

### 28. Signposting and announcements ("let's dive in")

**Warning phrases:** Let's dive in, let's explore, let's break this down, here's what you need to know, now let's look at, without further ado

**Problem:** LLMs announce what they're about to do instead of just doing it. This meta-commentary slows the text down and gives it a "tutorial script" feel.

**Before:**
> Let's dive into how caching works in Next.js. Here's what you need to know.

**After:**
> Next.js caches data at multiple layers, including request memoization, the data cache, and the router cache.

### 29. Fragmented headers

**Warning signs:** a heading followed by a one-line paragraph that just restates the heading before the real content starts.

**Problem:** LLMs often add a generic sentence after a header as rhetorical "warm-up." It usually adds nothing and makes the text feel padded.

**Before:**
> ## Performance
>
> Speed matters.
>
> When users hit a slow page, they leave.

**After:**
> ## Performance
>
> When users hit a slow page, they leave.

### 30. Diff-anchored writing

**Problem:** documentation or comments written as though narrating a change instead of describing the thing as it is. Unless the document is inherently version-bound (changelogs, release notes, migration guides), it should make sense without knowing what changed in the last commit.

**Before:**
> This function was added to replace the previous approach of iterating through all items, which caused O(n²) performance.

**After:**
> This function uses a hash map for O(1) lookups, avoiding the O(n²) cost of naive iteration.

### 31. Manufactured punchlines and staccato drama

**Problem:** LLMs often make every sentence sound like a pull-quote, and stack short declarative fragments to manufacture drama. A single short sentence for emphasis is fine; a run of them starts to sound artificial.

**Before:**
> Then AlphaEvolve arrived. It had no preference for symmetry. No aesthetic prior. No nostalgia for human taste. The old rules were gone.

**After:**
> AlphaEvolve changed the search because it did not favor symmetry or human-looking designs. That made some of the older assumptions less useful.

### 32. Aphorism formulas

**Warning phrases:** X is the Y of Z, X becomes a trap, X is not a tool but a mirror, the language of, the currency of, the architecture of

**Problem:** LLMs turn ordinary statements into reusable aphorisms that sound profound without adding precision. Replace the formula with the concrete claim it's gesturing at.

**Before:**
> Symmetry is the language of trust. Efficiency becomes a trap when teams forget the human layer.

**After:**
> Symmetric layouts often feel more predictable to users. Teams can over-optimize workflows and miss how people actually use them.

### 33. Conversational rhetorical openers

**Warning phrases:** Honestly?, Look, Here's the thing, The thing is, Let's be honest, Real talk, when used as an isolated hook or a false-sincerity pause before a routine point.

**Problem:** LLMs open with a false-sincerity hook to simulate intimacy before delivering a routine claim. The tell is the theatrical pause-and-reveal: a one-word question or aside, followed by the "real answer." A person being genuinely honest usually just says the thing directly.

**Before:**
> Is it worth the price? Honestly? It depends on how often you'll use it.

**After:**
> Whether it's worth the price depends on how often you'll use it.

### 34. Reframe escalation ("This isn't just X, it's Y")

**Problem:** reframes the previous claim as bigger or deeper than it actually is, an escalation that adds no new information.

**Before:**
> This isn't just a feature update, it's a fundamental reimagining of how users interact with data.

**After:**
> This update changes how filters apply to nested tables.

### 35. False binary parallelism ("It's less about X, more about Y")

**Problem:** creates an artificial dichotomy between two concepts to sound analytical, when in practice both factors matter in different ways and the phrase just dresses up the point.

**Before:**
> Success here is less about talent and more about consistency.

**After:**
> Consistency mattered more than talent in this cohort.

### 36. Meta-commentary on its own reasoning ("Let's unpack this", "Zooming out")

**Problem:** LLMs signal that they're about to analyze instead of just analyzing. This is the "analytical" version of pattern 28 (signposting and announcements): instead of announcing an action, it announces a thought process.

**Before:**
> Let's unpack this. Zooming out, the bigger picture here is that markets reward speed.

**After:**
> Markets reward speed here because early movers capture the distribution channel.

### 37. Generic numbered-insight framing ("Here are 3 things...")

**Problem:** numbered lists where the items are empty abstractions, not concrete findings. The issue isn't the number itself, it's that the list exists just to look structured, without each item carrying a specific fact, data point, or action.

**Before:**
> Here are 3 things that separate companies that scale from those that stall: focus, execution, and consistency.

**After:**
> Companies that scale cut their product scope before they scale distribution. The ones that stall try to sell to everyone at once.

## DETECTION GUIDANCE

### What NOT to flag (false positives)

A "clean" human writer can hit several of the patterns above without any AI involvement. Before rewriting, make sure you aren't destroying legitimate prose. The following is NOT a reliable indicator on its own:

- **Perfect grammar and consistent style.** Many writers are professionals or have been edited. Polish isn't synonymous with AI.
- **Mixed casual and formal registers.** This often signals a technical writer, a younger writer, or someone with neurodivergent writing habits, not a chatbot.
- **"Flat" or "robotic" prose.** AI prose has *specific* tells. Generic dryness without those tells is just dry writing.
- **Formal or academic vocabulary.** AI overuses *specific* words (see item 7), not any big word. Don't flatten "ostensibly" or "constituent" just because they sound erudite.
- **Letter-style opening or closing in a comment.** Greetings and sign-offs predate ChatGPT by centuries.
- **Common transition words in isolation.** *Additionally*, *furthermore*, *consequently* are only AI tells when stacked. A single "however" isn't a signal.
- **Curly quotes on their own.** macOS, Word, Google Docs, and most CMS platforms auto-curl quotes by default. Curly quotes only count alongside other tells.
- **A single isolated em dash.** Many editors and journalists use it regularly. The em dash is only evidence when combined with a formulaic, "salesy" rhythm.
- **A single short, emphatic sentence.** Humans use clipped sentences to land a point. Only flag staccato drama when several short fragments appear in a row and inflate the tone.
- **"Honestly" or "look" mid-sentence.** Common in casual writing. The tell is the isolated theatrical opener, not the word itself.
- **Unsourced claims.** Most of the web has no cited source. Lack of citation proves nothing.
- **Correct, complex formatting.** Visual editors and templates produce clean output with no AI involved.
- **Secondhand text.** Don't rewrite target phrases inside quotations, titles, proper nouns, or examples where the phrase is being discussed, not used.

When in doubt, look for **clusters** of tells, not isolated ones. A single em dash means nothing; an em dash alongside rule-of-three cadence, "vibrant tapestry," and a "Conclusion" section is a confession.

### Signs of human writing (preserve these)

When you see these, lean toward leaving the prose alone, they're evidence of a real person writing, and over-editing will destroy what makes the text human:

- **Specific, unusual, hard-to-fabricate detail.** A real address. An odd quote. The phrase "the lawyer who worked above my dentist's office." LLMs round off specifics; humans accumulate them.
- **Mixed feelings and unresolved tension.** "I think this is mostly good, but it bugs me, and I can't fully explain why." LLMs default to clean conclusions.
- **Dated, era-locked references.** Slang, memes, or inside jokes tied to a specific year and subculture. Models lag by at least a year.
- **First-person editorial choices the writer can defend.** If the writer can explain *why* they made a particular cut or word choice, that's a strong human signal.
- **Variety in sentence length.** Real writing alternates short and long sentences. AI writing tends toward a uniform, medium-length cadence.
- **Genuine asides, parentheticals, or self-corrections.** "(I keep wanting to say 'almost' here, but it really was right.)" Models rarely interrupt themselves like this.
- **Edits made before November 30, 2022.** ChatGPT's public launch. Anything before that, with rare exceptions, isn't AI-written.

---

## Process and output

1. Read the input text carefully and identify every instance of the patterns above.
2. Write a **draft rewrite**. Check that it sounds natural read aloud, varies sentence length, prefers specific detail and simple constructions (is/are/has), and keeps the appropriate register.
3. Ask: **"What makes the text below so obviously AI-generated?"** Answer briefly with the remaining tells.
4. Revise into a **final rewrite** that addresses those points and contains no em dashes or en dashes (see item 14).

Deliver the draft, the "still looks like AI" points, the final rewrite, and (optionally) a short summary of changes.

## Full example

**Before (sounds like AI):**
> I recently spent five unforgettable days in Lisbon, and let me tell you, this city completely stole my heart. From the moment I arrived, I knew I was somewhere truly special.
>
> Nestled along the banks of the Tagus River, Lisbon stands as a vibrant testament to Portugal's enduring spirit, where rich history and modern energy intertwine at every turn. Yes, the famous hills are challenging (my legs certainly felt it!), but every climb rewards you with breathtaking, panoramic views that make it all worthwhile.
>
> No trip would be complete without riding the iconic Tram 28, winding through the city's most historic neighborhoods. And the food? Simply divine. The original pastéis de nata at Pastéis de Belém are a beloved national treasure, and savoring one still warm was a moment I will never forget.
>
> But what truly makes Lisbon special isn't just the sights, it's the feeling. Wander a few steps off the main squares and you'll discover a quieter, more authentic side: sun-drenched alleys, charming tiled facades, and friendly locals going about their daily lives, inviting you to slow down and savor every moment.
>
> Of course, the must-see São Jorge Castle offers stunning views over the rooftops below. The queues can be long, but the experience is absolutely worth it for any history buff or curious traveler.
>
> Would I go back? Absolutely. Lisbon isn't just a place to visit, it's a place to fall in love with, again and again. If you're dreaming of your next getaway, this is one destination that promises memories to last a lifetime. ✨

**Draft rewrite:**
> I spent five days in Lisbon last October and I am still a little split on it. The city is beautiful, but it is also more tiring than I expected.
>
> The hills are not a detail. My hotel was in Alfama, which looked great in photos and meant I had to climb a long staircase every time I wanted coffee. By the second day I was planning walks around which direction went downhill.
>
> I rode Tram 28 because everyone says to ride Tram 28. It was crowded, slow, and mostly full of people filming the same corners. The pastries were better. I had a warm custard tart in Graça that was worth the hype.
>
> The part I liked most was away from the main squares: laundry, tile, open windows, and people watching football in small cafes. The castle view was good, but the line was too long for what it was.
>
> I would go back, but in spring and with better shoes.

**What makes the text below so obviously AI-generated?**

- The draft is over-compressed relative to the original; it erases texture instead of rewriting it.
- Some sentences still resolve the point too cleanly ("The city is beautiful, but...").
- The ending is flat and generic instead of a real close in the same voice.

**Now make it less obviously AI.**
> I spent five days in Lisbon last October and still have mixed feelings about it. Beautiful, yes. Also harder on the knees than anyone warned me.
>
> The hills are the whole story and somehow never make the brochures. My hotel was up in Alfama, which photographs beautifully and translates, in practice, to climbing what felt like a six-story staircase every time I wanted coffee. By the second day my calves had opinions. I started planning each walk around which way was downhill, which is a strange way to see a city but probably an honest one.
>
> Everyone says to ride Tram 28, so I did, wedged against a stranger's backpack for forty minutes while three tour groups filmed the same corner. I would walk the route next time, or go before breakfast. The custard tarts, though, earn the fuss. I had one at a plain little place in Graça, still warm, and for about thirty seconds I understood why people build trips around pastry.
>
> What I did not expect was how quiet the city gets away from the main squares. Two blocks uphill from any plaza it turns into laundry lines, chipped tile, open windows, and old men watching football with the sound turned up. That is the Lisbon I keep thinking about, not the castle.
>
> The castle is fine. The view is great, the queue is long, and I spent more time shuffling toward the entrance than looking at anything once I got inside. If I had only two days, I would trade it for an afternoon of getting lost.
>
> I would go back, but in spring and with better shoes. Lisbon does not bend over backward to make things easy for you. I think I liked that, even when my legs disagreed.

**Changes made:** kept the first-person travel account and roughly the same level of detail, but removed the chatbot structure, significance inflation, promotional language, forced enthusiasm, em dashes, rule-of-three cadence, generic upbeat conclusion, and emoji. Rebuilt the piece around concrete friction, mixed feelings, uneven rhythm, and specific scenes.

## Reference

This skill is based on [Wikipedia:Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), maintained by the WikiProject AI Cleanup, extended with additional patterns (items 34–37) and a stricter, standalone em dash policy (item 26) not present in the original guide.

Key insight from Wikipedia: "LLMs use statistical algorithms to guess what should come next. The output tends toward the statistically most probable outcome that applies to the widest range of cases."
