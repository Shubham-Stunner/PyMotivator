from apscheduler.schedulers.background import BackgroundScheduler
from Motivator import send_whatsapp_text,client,quotes
import time

scheduler = BackgroundScheduler(timezone= "Asia/Kolkata")
scheduler.start()

job = scheduler.add_job(send_whatsapp_text,'cron',[client,quotes],hour="09",minute="07")
print(job)

while True:
    time.sleep(1)