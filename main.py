"""
Start in REPL and interact with manager with command examples below

Spawn a single instance or multiple with threading:
manager.spawn_instance()
manager.spawn_instances(5)

Delete a single instance or all with threading:
manager.delete_latest()
manager.delete_all_instances()
"""

from spawner import BrowserManager

target_url = "https://www.twitch.tv/username"
SPAWNER_THREAD_COUNT = 3
CLOSER_THREAD_COUNT = 10

manager = BrowserManager(target_url, SPAWNER_THREAD_COUNT, CLOSER_THREAD_COUNT)

print("Available proxies", len(manager.proxies.proxy_list))
print("Available window locations", len(manager.screen.spawn_locations))