from speedtest import SpeedTest
from twitter import Twitter


speedtest = SpeedTest()
speed = speedtest.get_internet_speed()

twitter_bot = Twitter()
twitter_bot.post_a_message(f"My speed: Download {speed[0]} Mbps and Upload {speed[1]} Mbps")

