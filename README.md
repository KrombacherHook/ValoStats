# 🎯 ValStats – A Discord Bot for Valorant Player Statistics

**ValStats** is a lightweight Discord bot built in Python that integrates with the official Riot Games API (Valorant) to provide players with personalized performance tracking, match summaries, and automated updates via Discord.  
Perfect for small communities, scrim groups, or casual players who want to track their progress over time.

---

## ✅ Features

- 🔐 Riot Sign-On (OAuth2) integration *(coming soon)*
- 👤 Per-user tracking of match data via Riot API
- 🧠 Commands to register, manage, and view stats
- 📬 Automated notifications (after each match or weekly)
- 🕓 Scheduler for weekly reports (via APScheduler)
- 💾 Local user database using JSON (easy and portable)
- 📡 Integration with Discord webhooks or DMs

---

## 📦 Project Structure

```
valstats-bot/
├── bot.py              # Main Discord bot logic and commands
├── riot_api.py         # Riot API access (currently mocked)
├── db.py               # Local JSON database for user tracking
├── scheduler.py        # Weekly task scheduler (APScheduler)
├── requirements.txt    # Python package dependencies
```

---

## 🚀 Getting Started

### 1. Clone the Project

```bash
git clone https://github.com/yourusername/valstats-bot.git
cd valstats-bot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure the Bot

In `bot.py`, replace this line:

```python
bot.run("YOUR_DISCORD_BOT_TOKEN")
```

with your actual **Discord bot token**.

---

## 🧪 Example Commands

Once your bot is running:

| Command                  | Description                                |
|--------------------------|--------------------------------------------|
| `!register`              | Starts the registration (OAuth) process    |
| `!notify every_match`    | Enables live match notifications           |
| `!notify weekly`         | Enables weekly performance summary         |
| `!stats`                 | Shows your most recent match performance   |

---

## 🔗 Riot API (Production-Ready Plan)

You'll need to register your product at [https://developer.riotgames.com/](https://developer.riotgames.com/) and:

- Apply for a **Production API Key**
- Implement Riot Sign-On (OAuth2) for account linking
- Use `puuid` to fetch:
  - Match history (`/matchlists/by-puuid/{puuid}`)
  - Match details
  - Competitive ranks

Authentication will be handled via a web server (Flask or FastAPI).

---

## 🔧 Scheduler

A background task checks all registered users weekly and sends them a summary of their most recent performance stats.

You can extend this with:
- Team stats
- Leaderboards
- Personalized tips

---

## 📬 Webhook Integration

Webhook or DM notifications can be customized. For example:

```python
📊 New Match Finished!
🗺 Map: Haven
⚔️ K/D: 1.45
🏆 Result: Victory
```

---

## 📄 License

This bot is open source under the **MIT License**. It is intended for private use in small communities.

---

## 💡 Roadmap

- [ ] Full Riot OAuth2 integration
- [ ] Match summaries from real data
- [ ] GUI dashboard for players
- [ ] Leaderboard support
- [ ] Agent-based performance trends

---

## 🙌 Contributions

Pull requests, ideas and feedback are always welcome.  
This project is aimed at anyone who wants to improve their Valorant game through easy tracking inside Discord.

---

Made with ❤️ for the Valorant community.

For Riot: 4af2652a-0780-455d-b92b-a9e2de639c48
