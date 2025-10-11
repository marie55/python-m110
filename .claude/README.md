# .claude Directory - Claude Code Configuration

This directory contains configuration files for Claude Code extension features.

## Contents

### `/agents/`
Custom AI sub-agents that provide specialized assistance.

**learning-assistant.md** - Dr. Laila, the M110 Python Learning Assistant
- Time-aware teaching assistant for students
- Guides learning through Socratic method
- Bilingual support (English/Arabic)
- See [DR-LAILA-SETUP.md](DR-LAILA-SETUP.md) for details

### `/commands/`
Slash commands for quick access to features.

**laila.md** - `/laila` command
- Activates Dr. Laila learning assistant
- Students type `/laila` in Claude Code to get help

### Configuration Files

**course-calendar.yaml** - Course schedule and timeline
- Week-by-week topics and dates
- Used by Dr. Laila for time-aware context
- Update as course progresses

**DR-LAILA-SETUP.md** - Complete setup documentation
- How Dr. Laila works
- Customization guide
- Troubleshooting tips

## For Students

To get help from Dr. Laila:
1. Open Claude Code chat in VS Code
2. Type `/laila`
3. Ask your questions!

See [../HOW-TO-USE-DR-LAILA.md](../HOW-TO-USE-DR-LAILA.md) for full guide.

## For Instructors

This directory is **shared with students** (not in .gitignore).

To modify Dr. Laila's behavior:
- Edit `agents/learning-assistant.md`
- Update `course-calendar.yaml` as weeks progress
- See `DR-LAILA-SETUP.md` for customization options

**Note**: `CLAUDE.md` (instructor guidelines) is in root and gitignored - not shared with students.
