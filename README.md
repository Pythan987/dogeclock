# DOGE Clock Bot

A Twitter bot that posts regular updates about the Department of Government Efficiency (DOGE) savings from the US Debt Clock website.

## Free Hosting Options

### 1. GitHub Actions (Recommended)

1. Fork this repository
2. Go to Settings → Secrets and variables → Actions
3. Add the following repository secrets:
   - `TWITTER_API_KEY`
   - `TWITTER_API_SECRET`
   - `TWITTER_ACCESS_TOKEN`
   - `TWITTER_ACCESS_TOKEN_SECRET`
4. The bot will run on the schedule defined in `.github/workflows/run_bot.yml`
5. You can also manually trigger the workflow from the Actions tab

**Note:** GitHub Actions has a limit of 2,000 minutes per month for free accounts, which is enough for this bot.

### 2. Railway.app

Railway offers 500 hours/month of free runtime:

1. Sign up on [Railway.app](https://railway.app/)
2. Connect your GitHub repository
3. Create a new project from GitHub repo
4. Add environment variables for Twitter API credentials
5. Deploy with the command: `python dogeclock.py`

### 3. Render.com

Render offers 750 hours/month on their free tier:

1. Sign up on [Render.com](https://render.com/)
2. Create a new Web Service
3. Connect your GitHub repository
4. Set the build command: `pip install -r requirements.txt`
5. Set the start command: `python dogeclock.py`
6. Add environment variables for Twitter API credentials

### 4. PythonAnywhere

For PythonAnywhere's free tier:

1. Sign up on [PythonAnywhere](https://www.pythonanywhere.com/)
2. Upload your code
3. Set up a scheduled task to run every hour
4. Configure environment variables

## Security Note

⚠️ Never commit your API keys directly in the code. Always use environment variables or secrets.

## Requirements

- Python 3.6+
- Packages listed in requirements.txt 