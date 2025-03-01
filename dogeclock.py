import tweepy
import schedule
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Twitter API v2 credentials
TWITTER_API_KEY = "3aH6BB8OxLciXHQ6dXc4YdY1k"
TWITTER_API_SECRET = "mNCmLexpJdcGDpHTT1WsdQhbwxYB9UfABRgUH0u6Px5ksxg7cV"
TWITTER_ACCESS_TOKEN = "1888613261718990848-fWykgH5THYlrd1owZyZFW02D5lp2tN"
TWITTER_ACCESS_TOKEN_SECRET = "kz2UGW8orN8iZmq647npFTlHIlk7wuf915qZh6wTTq94i"

# Global tweet counter
tweet_count = 0

def setup_twitter_v2():
    client = tweepy.Client(
        consumer_key=TWITTER_API_KEY,
        consumer_secret=TWITTER_API_SECRET,
        access_token=TWITTER_ACCESS_TOKEN,
        access_token_secret=TWITTER_ACCESS_TOKEN_SECRET
    )
    return client

def get_doge_savings():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    
    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        driver.get("https://www.usdebtclock.org/")
        time.sleep(15)
        
        script = """
            const layer = document.getElementById('layer185');
            if (layer) {
                const span = layer.querySelector('span');
                return span ? [span.textContent] : [];
            }
            return [];
        """
        
        savings_data = driver.execute_script(script)
        print("Raw data found:", savings_data)
        
        if savings_data:
            return savings_data
            
        raise Exception("D.O.G.E CLOCK data not found")
        
    finally:
        driver.quit()

def format_tweet(savings_data):
    return (f"💰 D.O.G.E Clock Update 🕒\n"
            f"Department of Government Efficiency\n"
            f"Total Potential Savings: {savings_data[0]}\n"
            f"#DOGE #Government #USDebt #ForThePeople #GovEfficiency")

def post_update_v2():
    global tweet_count
    max_retries = 3
    retry_count = 0
    
    while retry_count < max_retries:
        try:
            if tweet_count >= 500:
                print("Monthly tweet limit reached. Stopping script.")
                return
            
            print(f"Starting update process... (Attempt {retry_count + 1}/{max_retries})")
            twitter_client = setup_twitter_v2()
            print("Twitter API setup complete")
            
            print("Getting DOGE savings data...")
            savings_data = get_doge_savings()
            print(f"Retrieved savings data: {savings_data}")
            
            if savings_data and savings_data[0]:
                tweet_text = format_tweet(savings_data)
                print(f"Formatted tweet: {tweet_text}")
                response = twitter_client.create_tweet(text=tweet_text)
                print(f"Successfully tweeted: {tweet_text}")
                print(f"Tweet ID: {response.data['id']}")
                tweet_count += 1
                print(f"Total tweets this month: {tweet_count}")
                break
            
            retry_count += 1
            if retry_count < max_retries:
                print(f"Retrying in 60 seconds...")
                time.sleep(60)
                
        except Exception as e:
            print(f"Detailed error information:")
            print(f"Error type: {type(e).__name__}")
            print(f"Error message: {str(e)}")
            retry_count += 1
            if retry_count < max_retries:
                print(f"Retrying in 60 seconds...")
                time.sleep(60)

def main():
    # Schedule the tweet every 1.5 hours (90 minutes)
    schedule.every(90).minutes.do(post_update_v2)
    
    # Run the first tweet immediately
    post_update_v2()
    
    # Keep the script running
    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    main()