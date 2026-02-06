# Git Commit Message Conventions

Please define your preferred git commit message format here.

## Format

`<github emoji> <type of commit>: <concise summary>`

## Types

List allowed types e.g., feat, fix, docs, style, refactor, test, chore

## Rules

Max 50 chars for subject, imperative mood, etc.
Before each commit, decide the proper prefix using GitHub-style emojis (see [GitHub Emoji Cheatsheet](https://github.com/jimit105/github-emoji-cheatsheet)):  
     - `:sparkles:` `feat:` for new feature
     - `:bug:` `fix:` for bug fix
     - `:memo:` `docs:` for documentation change
     - `:recycle:` `refactor:` for code cleanup
     - `:art:` `style:` for lint/format updates
     - `:white_check_mark:` `test:` for tests
     - `:wrench:` `chore:` for config/tooling  
Compose the commit title as `<github emoji> <type of commit>: <concise summary>` and include a
short body if context is useful.

**Always add a GitHub-style emoji at the beginning of the commit message.**

Always allow the user to review the commit message before it is committed.
