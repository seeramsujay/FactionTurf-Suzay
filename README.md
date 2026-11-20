<div align="center">

<img src="assets/logo.svg" alt="FactionTurf Logo" width="220" />

# FactionTurf

### *GitHub Pull Request-Controlled Multiplayer Turf War & Territory Conquest Game*

[![Node.js](https://img.shields.io/badge/Runtime-Node.js%20%7C%20TypeScript-339933?style=for-the-badge&logo=node.js&logoColor=white)](package.json)
[![Express API](https://img.shields.io/badge/Backend-Express%20v5-000000?style=for-the-badge&logo=express&logoColor=white)](src/index.ts)
[![Prisma ORM](https://img.shields.io/badge/ORM-Prisma%20%7C%20PostgreSQL-2D3748?style=for-the-badge&logo=prisma&logoColor=white)](prisma/schema.prisma)
[![License: ISC](https://img.shields.io/badge/License-ISC-blue.svg?style=for-the-badge)](package.json)
[![Engineering Roadmap](https://img.shields.io/badge/Engineering-Future%20Roadmap-8A2BE2?style=for-the-badge)](future.md)

<p align="center">
  <b>Turn GitHub Pull Requests, code reviews, and developer workflows into strategic territory conquests across four competing factions.</b>
</p>

---

</div>

## 🎮 How FactionTurf Works

**FactionTurf** bridges GitHub collaborative development and competitive gaming. Developers join one of four rival factions (`p1`: Crimson Legion, `p2`: Azure Syndicate, `p3`: Emerald Vanguard, `p4`: Amber Order). Whenever a pull request or code action is executed, a GitHub Actions workflow dispatches move commands to the FactionTurf server, advancing territorial boundaries in real time.

```mermaid
flowchart LR
    A["Developer Submits PR / Review"] -->|GitHub Action Trigger| B["GitHub Actions Workflow"]
    B -->|POST /api/postInfo\n{username, action}| C["FactionTurf Express API"]
    C -->|Lookup Faction| D[("PostgreSQL\n(Prisma ORM)")]
    C -->|Push Move| E["Faction Move Stack (p1..p4)"]
    E -->|GET /api/getInfo| F["Interactive Turf Gameboard\n(Phaser / Canvas Client)"]
```

---

## ⚡ API Specification

*   `POST /api/postInfo`: Submits an action event on behalf of a GitHub username. Resolves faction membership and queues action into the active game loop.
*   `GET /api/getInfo`: Atomically retrieves and flushes the current turn stack across all 4 factions for gameboard rendering.
*   `GET /api/getMPRs`: Inspects pending moves across faction queues for telemetry and debugging.

---

## 🚀 Local Development Setup

### 1. Install Dependencies
```bash
npm install
```

### 2. Configure Environment & Database
Create a `.env` file containing your PostgreSQL database connection string:
```bash
DATABASE_URL="postgresql://user:password@localhost:5432/factionturf?schema=public"
```

### 3. Generate Prisma Client & Run Migrations
```bash
npx prisma generate
npx prisma db push
```

### 4. Start Development Server
```bash
npm run dev
# Server listening on http://localhost:3001
```

---

## 🔮 Engineering Roadmap

For GitHub Webhook HMAC verification, Redis persistent queues, and real-time WebSockets streaming, explore the [Future Roadmap](future.md).

---

## 📄 License

Distributed under the **ISC License**. See `package.json` for details.
