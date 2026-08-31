# Grok Build Skills Available Today

Grok Build has two kinds of skills on this machine: **yours** in `~/.grok/skills/` and **bundled** ones from Grok. Type `/` to run the slash ones, or just describe the task — Grok will load the matching skill.

Recorded from a Grok Build session on 2026-08-31.

---

## Most Useful for This Course Today

| Skill | How to use it | What it does |
|---|---|---|
| **pptx** | Ask for a presentation | Create, edit, or inspect PowerPoint files. This is the one for lesson decks such as `unit_002_lesson_001_order_of_operations.pptx`. |
| **pdf** | Mention a `.pdf` | Read, create, merge, split, OCR, watermark, or fill forms. |
| **docx** | Mention a Word doc | Create or edit `.docx` / `.dotx` files. |
| **imagine** | Ask for an image | Generate or edit images (lesson art, diagrams, slides). |
| **review** / **check-work** | `/review` or `/check-work` | Review diffs, PRs, or verify that work is actually correct. |
| **create-skill** | `/create-skill` | Capture a repeatable course workflow (for example, “make a lesson PowerPoint”). |
| **help** | Ask about Grok | Config, MCP, auth, shortcuts, commands. |

---

## All Skills Available Now

### Your Skills (`~/.grok/skills/`)

- `/check-work` — verification subagent
- `/code-review` — strict maintainability review
- `/create-skill` — scaffold a new skill
- `/help` — Grok docs and setup
- `/imagine` — image generation workflow

### Bundled: Course and Documents

- **pptx**, **pdf**, **docx** — Office files
- `/design` then `/execute-plan` — write a design doc, then implement it
- `/create-workflow` — multi-agent pipelines
- `/build-with-ai` — add LLM features (SpaceXAI)
- `/implement` — implement–review–fix loop

### Bundled: Art

- **game-asset-core**
- **game-ui-icons**
- **game-tilesets**
- **game-character-consistency**
- **game-animation-frames**

### Bundled: Git and Handoff

- `/review`
- `/pr-babysit`
- `/resume-cursor` — pick up work from Cursor
- `/resume-claude` — pick up work from Claude
- `/resume-codex` — pick up work from Codex
- `/skill-design-principles` — how to write skills well

---

## How Skills Are Invoked

`pptx`, `pdf`, `docx`, and the game-art skills are **auto** skills: they are not `/commands`. Just ask, for example: “Create a PowerPoint for unit 2 lesson 1.”

Slash skills can be run by typing `/` and the skill name, such as `/review` or `/create-skill`.

---

## Connected Integrations

These MCP integrations are also available in this Grok Build session:

- GitHub
- Gmail
- Google Drive
- Google Calendar
- Outlook
- Outlook Calendar
- Tasks

---

## Skill Locations

Grok discovers skills from these directories, in priority order:

| Location | Scope | Notes |
|---|---|---|
| `./.grok/skills/` | Local (CWD) | Highest priority |
| `<repo_root>/.grok/skills/` | Repo | Shared across the repo |
| `~/.grok/skills/` | User | Personal skills for all projects |
| `~/.grok/bundled/skills/` | Bundled | Platform skills shipped with Grok |

A same-named local, repo, or user skill overrides the bundled copy.

To browse discovered skills from the command line:

```text
grok inspect
grok inspect --json
```
