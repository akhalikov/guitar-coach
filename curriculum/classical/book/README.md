# The Book

This folder is reserved for a local copy of:

**Bradford Werner — *Classical Guitar Method Volume 1* (2020 edition)**

The PDF itself is **not committed** to this repository — it is intentionally listed in `.gitignore`.

## How to get the book

Download the free PDF directly from the author:

→ **<https://wernerguitareditions.com/products/classical-guitar-method-volume-1>**

Save it into this folder as `Classical-Guitar-Method-Vol1-Werner.pdf` so the classical coach (`../../../prompts/classical/SKILL.md`) can find it at the expected path:

```
curriculum/classical/book/Classical-Guitar-Method-Vol1-Werner.pdf
```

If you want a hardcopy, Werner sells print editions on Amazon:
- [Amazon.com](https://amzn.to/2RwxJ7b)
- [Amazon.ca](https://amzn.to/2C5wnGx)
- [Amazon.co.uk](https://www.amazon.co.uk/dp/1792936303/)

If the book has been useful, consider [supporting Werner directly](https://www.thisisclassicalguitar.com/donate-support/).

## License & attribution

The book is © Bradford C. Werner, 2020, and is licensed under the [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License (CC BY-NC-ND 4.0)](https://creativecommons.org/licenses/by-nc-nd/4.0/).

Under that license you may share the unmodified PDF for non-commercial purposes with attribution. **However, this repository does not redistribute the PDF** out of respect for the author — downloading from Werner's own site keeps the traffic with him.

## Why this folder exists at all

The classical coach (`../../../prompts/classical/SKILL.md`) occasionally needs to consult a specific page of the book — to verify a fingering, check a rhythm, or quote Werner's exact wording. The expected workflow is (run from the repo root):

```bash
pdftotext -f <page> -l <page> curriculum/classical/book/Classical-Guitar-Method-Vol1-Werner.pdf -
```

That only works if you've placed your local copy here. If you haven't, the coach will fall back to the online video lessons and the Werner plan / key-instructions files in `curriculum/classical/`.

## Don't commit the PDF

The `.gitignore` at the repo root has `book/*.pdf` to prevent accidental commits. Please don't override it.
