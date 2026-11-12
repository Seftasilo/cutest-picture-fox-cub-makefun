# Fox Cub with a Flower — Make the cutest picture (variant)

## Concept
A baby fox cub with huge sparkling blue eyes, soft orange fur, white cheeks and big fluffy ears, lying down with a tiny yellow flower tucked behind one ear. Soft pastel lavender background with bokeh.

Original AI-generated artwork made for this entry (make.fun bounty
"Make the cutest picture", $250, ends Fri 13 Nov 2026 17:00 WIB). Not stock,
not anyone else's work, and a different subject/concept from the main entry
(baby sea otter hugging a pink heart) and from the other variants.

## How it was made
Generated with an image-generation pipeline from a text prompt, then resized
1600x1600 -> 896x896 with PIL Lanczos and saved as PNG. No text or watermark
in the image.

## Jury rubric mapping (RULES.txt)
1. **Cute at a glance** — one subject fills almost the whole frame.
2. **Cute subject** — round soft shape, huge sparkling eyes, small/chubby
   proportions, smiling expression.
3. **Charm** — one personality touch: the tiny yellow flower behind one ear.
4. **Craft** — clean render, correct eyes/ears/limbs, no artefacts, no text.
5. **Readable small** — the large single subject stays clear at ~300 px.

## Verification
- `entry.png`: PNG 896x896, 833981 bytes (<= 1,048,576), magic bytes
  `89 50 4E 47`, SHA-256 `53c91d010887a5283a4c43ddb9c3cd3c3820618a3056d9a62065f63a0a7163fd`.
- `main.py` (stdlib only) run 2x writes byte-identical output equal to
  `entry.png` (verified locally).

## Files
- `entry.png` — the entry image
- `main.py` — entrypoint: copies `entry.png` byte-for-byte to
  `/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR`)
- `LICENSE` — MIT
- `.makefun/owner.json` — wallet ownership proof
