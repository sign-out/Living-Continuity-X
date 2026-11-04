# Living Continuity X (LCX)

Monolithic clean-room continuity infrastructure for Latitude Voyage, distinct from modular LC.

Install **[LCX.json](LCX.json)** as the host-safe LCX core (86 trigger definitions, 15 AI hook groups). A host does not have to enable every LCX module.

The [November 3 Voyage export](exports/LCX_Voyage_2026-11-03.json) is a **full source snapshot**, not the recommended mod-only file. It includes native world defaults such as Story Starts, skills, health, author seeds, and archetypes that should not be imposed on other worlds.

See the [release notes](docs/releases/2026-11-03.md) or [GitHub releases](https://github.com/sign-out/Living-Continuity-X/releases).

Static verification: `python -m unittest discover -s tests -p 'test_*.py' -v`. Test actual runtime behavior separately in Voyage Studio.
