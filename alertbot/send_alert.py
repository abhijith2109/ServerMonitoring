import time

import requests
from telegram import Bot
import json
import asyncio

with open("../config.json") as config_file:
    config = json.load(config_file)


telegram_token = config["telegram_token"]
chat_id = config["telegram_chat_id"]

cpu_limit  = config["cpu_limit"]
memory_limit = config["memory_limit"]
storage_limit = config["storage_limit"]

server_ips = config["server_ips"]

async def monitor_server_specs():

    while True:
        for server_ip in server_ips:
            server_specs = get_server_specs(server_ip)
            server_name = server_specs['server_name']
            cpu_percent = server_specs['cpu_usage']
            memory_percent = server_specs['memory_usage']
            storage_percent = server_specs['storage_usage']

            if cpu_percent > cpu_limit:
                message = f"{server_name} CPU usage is high: {cpu_percent}%"
                await send_telegram_notification(message)

            if memory_percent > memory_limit:
                message = f"{server_name} Memory usage is high: {memory_percent}%"
                await send_telegram_notification(message)

            if storage_percent > storage_limit:
                message = f"{server_name} Storage usage is high: {storage_percent}%"
                await send_telegram_notification(message)
            time.sleep(60)

def get_server_specs(server_ip):
    url = f'http://{server_ip}:5000/'
    response = requests.get(url)
    server_specs = response.json()
    return server_specs

async def send_telegram_notification(message):
    bot = Bot(token=telegram_token)
    await bot.send_message(chat_id=chat_id, text=message)

if __name__ == '__main__':

    loop = asyncio.get_event_loop()
    loop.run_until_complete(monitor_server_specs())




