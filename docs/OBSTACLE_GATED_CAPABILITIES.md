# Obstacle-gated player competence and positive capability continuity

## Tournament and LC lessons

The four approaches evaluated were (1) prompt-only policy, (2) automatic narration mining, (3) confirmed-event registry plus prompt policy, and (4) independent dice/difficulty engine. **Selected (3)**: (1) cannot persist evidence, (2) canonizes narrator mistakes, and (4) duplicates native mechanics.

Lessons from LC implementation:
- Separate **action proportionality** from **capability memory**. An ordinary bridge crossing should not need a remembered walking skill.
- Require confirmed structured evidence; do not infer success from an attempt or from prose alone.
- Store generalized positive competence, not the exact original feat or inferred maximum limits.
- Never turn a capability record into a native skill unlock, authorization, or guaranteed result.
- Preserve owner attribution and protect private player information in shared multiplayer context.
- Keep retrieval compact and action-relevant, rather than dumping the registry every turn.

## LCX integration

- `generateActionInfo`: obstacle-gated interpretation before narrator-created difficulty.
- `generateStory`: do not manufacture hazards or punitive complications from evocative descriptions.
- `summarization`: preserve actor-specific generalized capability with provenance.
- `lcx_positive_capability_ingest` (state): consumes `storage.LCX.capabilityEvidence` array entries `{id?,entityId,capability,sourceEventId,confirmed:true,visibility?}`. Only confirmed records admitted. Input producer must generalize positively. Unspecified visibility defaults to private.
- `lcx_positive_capability_context` (planning): emits up to three lexical action matches. In multiplayer, only explicitly public entries are eligible for shared story injection.
- `storage.LCX.positiveCapabilities`: persistent registry, independent of LCX specialist/micro/broad competency ratings and NPC bounded checks.
- Optional config: `storage.LCX.config.positiveCapabilities = {enabled:true,maxRecords:96,maxRelevant:3}`.

## Limitations and follow-up

The existing runtime does not provide a trustworthy general-purpose structured semantic extraction of capabilities from arbitrary narration. This PR provides the **confirmed-evidence consumer**, not a fully automatic event producer. Existing event sources need to populate `capabilityEvidence` with confirmed, positively generalized facts. Lexical retrieval can miss synonyms. Shared multiplayer projection intentionally withholds private evidence; future player-scoped projection can improve this.

## Regression matrix

1. Cross a described 'thin' one-meter bridge without an established hazard: no invented difficult check.
2. Cross a bridge with confirmed broken planks and wind: legitimate hazard remains relevant, severity proportional.
3. Catch a thrown ball: no invented check solely from the adjective 'red'.
4. Confirmed cargo gravity-field use persists as 'can manipulate external objects using gravitational fields'; original mass is not a ceiling.
5. Unconfirmed/failed attempt must not enter registry.
6. Host-native failed check remains failed; no re-roll.
7. Two actor IDs cannot overwrite each other's record with same stable ID.
8. Multiplayer private capability cannot be emitted into shared story; public capability can.
9. Disabled config or no relevant action yields no context.

Static script syntax and simulated evidence-to-context smoke checks were performed. Full Voyage Studio integration and native mechanical regression testing remain pending.

## Native Voyage multiplayer attribution discovery (2026-11-21)

The current community-maintained Voyage trigger documentation confirms that `scope: "player"` evaluates conditions against satisfying players and routes applicable effects to those players. A player-scoped `story` effect receives a host-generated attribution parenthetical identifying the affected player(s). `target: "satisfyingPlayers"` likewise directs individual player effects. Source: https://wiki.unofficial.voyage/mechanics/triggerDefinitions#targeting-a-specific-player

This is **native attribution for player-scoped trigger matching/effects**, not proof that scripts receive a per-action actor ID. The documented `check({type:'action-text'})` return is a raw array of player action strings, without a documented player-ID association. Therefore do not assume the array position maps to a player or parse the host's narrator parenthetical as a stable machine-readable ID.

Integration decision: use native player-scoped matching and player-specific effects for future capability evidence producers when appropriate; require explicit verified actor IDs for storage writes until a documented native actor-attribution script API is identified. Never assign a capability to the first/only guessed player in a multiplayer turn. Existing registry and narration policy remain usable. Do not claim complete automatic multiplayer evidence ingestion until this is verified in Voyage Studio.
