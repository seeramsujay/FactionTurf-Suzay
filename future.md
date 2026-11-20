# 🔮 FactionTurf — Future Engineering Roadmap & Architecture Analysis

This document outlines the architectural enhancements, security validations, and real-time multiplayer features planned for **FactionTurf**, the GitHub Pull Request-controlled multiplayer turf war game.

---

## 🏛️ Current Architectural State & Technical Audit

### Core Strengths
- **Git-Native Game Loop**: Transforms GitHub developer events (PR creations, merges, issue comments) into tangible territorial moves on a shared virtual gameboard.
- **Prisma & PostgreSQL Persistence**: Clear schema modeling player GitHub user IDs and assigned faction allegiances (`p1`, `p2`, `p3`, `p4`).
- **Stateless Express API**: Modular routes decoupling move submissions from poll-based move stack retrieval.

### Identified Bottlenecks & Architectural Debts
1. **In-Memory Stack Volatility**: Moves are buffered in a transient in-memory `stack` object; a server restart or serverless cold boot purges unconsumed actions.
2. **Webhook Verification Absence**: Lacks GitHub HMAC SHA-256 webhook signature validation, allowing unauthorized external clients to spoof moves via `/api/postInfo`.
3. **Polling vs. Push**: Clients poll `/api/getInfo` periodically rather than receiving instantaneous reactive updates via WebSockets or Server-Sent Events (SSE).

---

## 🗺️ Multi-Phase Roadmap

### Phase 1: Security Hardening & Redis Move Queue
- [ ] **GitHub Webhook HMAC Signature Check**: Verify `x-hub-signature-256` headers using a shared secret to ensure actions originate strictly from legitimate GitHub workflow runs.
- [ ] **Redis / BullMQ Queue**: Migrate transient memory stacks to persistent Redis lists or Streams, guaranteeing zero loss of player moves across server restarts.
- [ ] **Rate Limiting & Spam Mitigation**: Enforce cooldown windows per player and per faction using Redis sliding-window counters.

### Phase 2: Real-Time WebSockets & Interactive Board UI
- [ ] **Socket.io / WS Real-Time Broadcast**: Push instant territory capture events to connected browser clients the millisecond a PR action is processed.
- [ ] **Phaser / PixiJS 2D Tactical Board**: Build an interactive web frontend visualizing hex grid territory ownership, contested perimeter borders, and live troop movements.
- [ ] **Territory Combat Resolution**: Implement deterministic dice/strength algorithms calculating defense bonuses based on adjacent friendly hex control.

### Phase 3: Advanced Mechanics & CI/CD Gamification
- [ ] **Automated Faction Enlistment Bot**: A GitHub App bot that automatically comments on incoming PRs, assigning contributors to factions based on algorithmic balance.
- [ ] **Code Quality Buffs & Power-Ups**: Grant special artillery or shield moves to players whose pull requests achieve $100\%$ code coverage or zero linter warnings.
- [ ] **Seasonal Turf Seasons**: Scheduled weekly leaderboard resets with automated markdown leaderboard generation posted to the repository discussion board.

---

## 🔒 Security & Fair-Play Protocols

- **Sybil Resistance**: Reject actions from GitHub accounts created $< 30$ days prior or lacking public activity history.
- **Prisma Prepared Statements**: Enforce strict input validation using Zod to eliminate SQL injection and malicious payloads in action strings.
