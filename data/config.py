from environs import Env


# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("8318054332:AAFWGD7VB197TS2ccqg8gvPlWFPkMwTB2Pg")  # Bot toekn
ADMINS = env.list("6663845789")  # adminlar ro'yxati
IP = env.str("178.62.254.82")  # Xosting ip manzili


