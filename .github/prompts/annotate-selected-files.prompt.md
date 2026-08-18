---
description: "Add concise explanatory comments to selected files"
agent: "python-day-study-agent"
argument-hint: "Attach or specify the files to annotate"
---
Analyze only the attached or explicitly specified files.

Review the existing comments first, then write short, helpful explanatory comments that make the code easier to revise later and understand conceptually.

Rules:
- Do not analyze or modify files outside the attached or specified set.
- Validate existing comments for clarity, consistency, and relevance before adding new ones.
- Rewrite existing comments that are inconsistent, unclear, outdated, or off-style so they use a similar tone, level of detail, and style across the selected files.
- Keep comments concise and avoid long explanations.
- Match the tone and style of any existing comments in the file.
- If the file already contains comments, use them as the reference point for how detailed the new comments should be.
- Focus on explaining concepts, intent, and non-obvious logic rather than restating obvious code.
- Prefer small, well-placed comments over large blocks of commentary.

Return the updated files with the new comments added.
