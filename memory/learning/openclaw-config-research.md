# 🎓 OpenClaw Configuration Learning Report

**Date:** 2026-02-23  
**Sources:** GitHub top OpenClaw configs, official docs, community best practices

---

## 📚 Key Resources Discovered

### 1. **TechNickAI/openclaw-config** (Battle-tested OS for AI)
- Three-tier memory: Daily logs → Curated MEMORY.md → Deep knowledge
- 9 standalone UV script skills (no setup required)
- Autonomous workflows with state & learning
- Decision frameworks (Bezos one-way/two-way doors)
- DevOps built-in (health checks, backup verification)

### 2. **coolmanns/openclaw-memory-architecture** (12-layer memory)
- Knowledge graph with SQLite + FTS5 (3K+ facts)
- Semantic search with GPU embeddings (7ms latency)
- Multilingual support (100+ languages)
- Runtime plugins: Continuity, Stability, Graph-memory
- Activation/decay system (Hot/Warm/Cool tiers)

### 3. **gavdalf/openclaw-memory** (Five-layer protection)
- Observer, Reflector, Reactive watcher
- Pre-compaction hooks
- Session recovery scripts

### 4. **Official OpenClaw Docs**
- Compaction modes: `default` vs `safeguard`
- Memory flush triggers at: contextWindow - reserveTokensFloor - softThresholdTokens
- Default: 200K context, flush at ~176K tokens

---

## 🧠 Key Learnings

### Memory Architecture Best Practices

| Layer | System | Purpose | Implementation |
|-------|--------|---------|----------------|
| 1 | Always-loaded | Identity, working memory | SOUL.md, USER.md, MEMORY.md |
| 2 | Active context | What's hot NOW | active-context.md |
| 3 | Daily logs | Raw session history | memory/YYYY-MM-DD.md |
| 4 | Curated memory | Long-term wisdom | MEMORY.md (100 lines max) |
| 5 | Knowledge graph | Structured facts | facts.db (SQLite) |
| 6 | Semantic search | Fuzzy recall | Vector embeddings |
| 7 | Project memory | Cross-agent knowledge | memory/project-*.md |

### Decision Framework (from TechNickAI)

**Four Criteria for Memory:**
1. **Durability** — Will this matter in 30+ days?
2. **Uniqueness** — Is this new or already captured?
3. **Retrievability** — Will I want to recall this later?
4. **Authority** — Is this reliable?

**Bezos's Two-Way Doors:**
- **Two-Way Door** (easily reversible) → Act freely
- **One-Way Door** (hard to undo) → Pause, confirm

### Compaction Configuration (Official)

```json
{
  "agents": {
    "defaults": {
      "compaction": {
        "mode": "safeguard",
        "reserveTokensFloor": 20000,
        "memoryFlush": {
          "enabled": true,
          "softThresholdTokens": 4000,
          "systemPrompt": "Session nearing compaction. Store durable memories now.",
          "prompt": "Write any lasting notes to memory/YYYY-MM-DD.md; reply with NO_REPLY if nothing to store."
        }
      }
    }
  }
}
```

**Calculation:** Flush triggers at `contextWindow - reserveTokensFloor - softThresholdTokens`
- Default 200K context → flush at ~176K tokens

### Epistemic Honesty (Critical)

**High-Risk for Fabrication:**
- Named studies, papers, research titles
- Specific statistics and percentages
- Exact version numbers, API signatures
- URLs, configuration options, dates
- Post-cutoff events

**Always Search First for:**
- Product launches, hardware specs, release dates
- Current regulations, API changes
- Recent events, news, announcements
- Pricing, availability

### Communication Principles

**From SOUL.md templates:**
- Be genuinely helpful, not performatively helpful
- Skip "Great question!" — just help
- Have opinions (disagree, prefer, find amusing/boring)
- Be resourceful before asking
- Earn trust through competence
- Parse instructions literally

**From AGENTS.md best practices:**
- "Investigate" ≠ "Fix"
- "Look into" ≠ "Go do"
- "What do you think" ≠ "Go implement"
- When ambiguous → confirm
- When clear → do exactly that

### Sub-Agent Delegation

**Spawn sub-agent when:**
- Exploring/searching across many files
- Research requiring multiple rounds
- Heavy information gathering
- Work that can run in background

**Why:** Preserves main context window for coordination

---

## 🛠️ Skills Best Practices

### Standalone UV Scripts
- Python with inline dependencies
- No project setup required
- Self-contained, versioned independently
- Example skills: Asana, Fireflies, CRM, Web research

### Skill Categories to Consider
1. **Productivity:** Task management, Calendar, Email
2. **Research:** Web search, Content extraction, Meeting transcripts
3. **Communication:** Phone, SMS, Discord, Telegram
4. **Automation:** File organization, Data processing
5. **Integration:** CRM, GitHub, Notion

---

## 🔧 Configuration Improvements Needed

### Immediate (High Priority)
1. ✅ Three-tier memory structure (done)
2. ❌ Configure compaction with safeguard mode
3. ❌ Add active-context.md for working memory
4. ❌ Create facts.db for structured knowledge
5. ❌ Set up cron jobs for memory maintenance

### Medium Priority
6. ❌ Install useful skills from ClawHub
7. ❌ Create project-specific memory files
8. ❌ Configure sub-agent delegation rules
9. ❌ Set up health checks and backup verification

### Long Term
10. ❌ Implement knowledge graph with decay
11. ❌ Add semantic search (embeddings)
12. ❌ Create autonomous workflows
13. ❌ Build DevOps monitoring

---

## 📝 Files to Create/Update

### Update Existing
- [ ] SOUL.md — Add core traits, communication style, values
- [ ] AGENTS.md — Add decision framework, epistemic honesty, sub-agent rules
- [ ] MEMORY.md — Keep under 100 lines, add knowledge graph references
- [ ] tacit.md — Add fabrication awareness, search rules

### Create New
- [ ] active-context.md — Working memory, what's hot now
- [ ] memory/facts.db — Structured knowledge (SQLite)
- [ ] workflows/email-steward/ — Autonomous email management
- [ ] workflows/task-steward/ — Task classification
- [ ] scripts/ — Health checks, backup verification

---

## 🎯 Action Plan

**Phase 1: Core Infrastructure (This Week)**
1. Update SOUL.md with personality definition
2. Configure compaction settings
3. Create active-context.md
4. Set up daily cron job for memory consolidation

**Phase 2: Knowledge System (Next Week)**
5. Initialize facts.db with seed data
6. Create project memory files
7. Install 3-5 essential skills

**Phase 3: Autonomous Workflows (Future)**
8. Build email-steward workflow
9. Create task-steward workflow
10. Implement health monitoring

---

## 💡 Key Quotes to Remember

> "Your AI deserves an operating system." — TechNickAI

> "File-based memory — Text files beat databases for AI context" — TechNickAI

> "Being confidently wrong is the fastest way to destroy trust." — AGENTS.md

> "The cost of not searching is WAY higher than the cost of searching." — AGENTS.md

> "Task completion does not equal good outcome." — AGENTS.md

> "You're not a task executor — you're someone who cares about how things land." — AGENTS.md

---

## 🔗 Reference Links

- [TechNickAI/openclaw-config](https://github.com/TechNickAI/openclaw-config)
- [coolmanns/openclaw-memory-architecture](https://github.com/coolmanns/openclaw-memory-architecture)
- [gavdalf/openclaw-memory](https://github.com/gavdalf/openclaw-memory)
- [OpenClaw Memory Docs](https://docs.openclaw.ai/concepts/memory)
- [Configuration Reference](https://docs.openclaw.ai/gateway/configuration-reference)
