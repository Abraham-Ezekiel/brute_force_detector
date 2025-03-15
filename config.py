# Configuration file

LOG_FILE = "/var/log/auth.log"  # SSH authentication log file (Linux)
FAILED_LOGIN_REGEX = r"Failed password for .* from (\d+\.\d+\.\d+\.\d+) port"
ATTACK_THRESHOLD = 5  # Number of failed attempts before blocking

# Telegram API for Notifications
TELEGRAM_BOT_TOKEN = "your_bot_token"
CHAT_ID = "your_chat_id"
