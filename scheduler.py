from apscheduler.schedulers.asyncio import AsyncIOScheduler
from db import get_all_users
from riot_api import get_match_data

def schedule_weekly_summary(bot):
    scheduler = AsyncIOScheduler()
    scheduler.add_job(lambda: send_summaries(bot), "interval", weeks=1)
    scheduler.start()

async def send_summaries(bot):
    for user in get_all_users():
        if user["notify"] == "weekly":
            channel = await bot.fetch_user(user["discord_id"])
            data = get_match_data(user["puuid"])
            await channel.send(f"Your weekly summary: Map: {data['map']}, K/D: {data['kdr']}")