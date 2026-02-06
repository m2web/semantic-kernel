# Markdown Conventions

This document defines the Markdown formatting rules for this repository based
on the `.markdownlint.json` configuration.

## Code Blocks

### Fenced Code Blocks

Use fenced code blocks with backticks (not indentation):

```python
def example():
    return "Hello"
```

### Language Specification Required

Always specify the language for code blocks. Allowed languages:

- `bash`
- `css`
- `html`
- `javascript`
- `json`
- `markdown`
- `python`
- `text`
- `typescript`
- `xml`
- `yaml`
- `yml`
- `csharp`
- `c#`

## Headings

### ATX Style Only

Use `#` symbols for headings (not underline style):

```markdown
# Heading 1
## Heading 2
### Heading 3
```

### Duplicate Headings

Duplicate heading text is allowed if headings are not siblings (different
hierarchy levels).

## Lists

### Unordered Lists

Use dashes (`-`) for unordered lists:

```markdown
- Item 1
- Item 2
  - Nested item
```

### Ordered Lists

Use sequential numbering (1, 2, 3):

```markdown
1. First item
2. Second item
3. Third item
```

## Emphasis and Strong

### Emphasis (Italic)

Use single asterisks for emphasis:

```markdown
*italic text*
```

### Strong (Bold)

Use double asterisks for strong emphasis:

```markdown
**bold text**
```

## Horizontal Rules

Use three dashes for horizontal rules:

```markdown
---
```

## Links and Images

### Reference Links

Shortcut syntax is allowed:

```markdown
[link text]

[link text]: https://example.com
```

### Inline Links

Standard inline links are preferred for simplicity:

```markdown
[link text](https://example.com)
```

## Line Length

- Line length is **not strictly enforced**
- Code blocks are exempt from line length rules
- Use reasonable line breaks for readability

## HTML Elements

The following HTML elements are allowed in Markdown:

- `<details>` and `<summary>` - For collapsible sections
- `<br>` - Line breaks
- `<img>` - Images with specific attributes
- `<kbd>` - Keyboard input
- `<sub>` - Subscript
- `<sup>` - Superscript

## Character Encoding

Use ASCII-only characters when possible. Avoid extended ASCII unless necessary.

## Proper Names

Use correct capitalization for these proper names:

- Cake.Markdownlint
- CommonMark
- JavaScript
- Markdown
- markdown-it
- markdownlint
- Node.js

## Quick Reference Checklist

When creating or editing Markdown files, ensure:

- [ ] Headings use `#` ATX style
- [ ] Code blocks are fenced with backticks
- [ ] Code blocks specify language
- [ ] Unordered lists use dashes (`-`)
- [ ] Ordered lists use sequential numbers
- [ ] Emphasis uses `*asterisks*`
- [ ] Strong uses `**double asterisks**`
- [ ] Horizontal rules use `---`
- [ ] Only allowed HTML elements are used
- [ ] Proper names are correctly capitalized
