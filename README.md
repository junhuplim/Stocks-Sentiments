# Reddit Stocks Sentiments
Scrapes data from Reddit from selected subreddits and filters the top 30 penny stocks based on number of mentions. I then use Wit.AI to analyse the basic sentiments of the top 3 stocks to allow better understanding of the scrapped data.

These data are then displayed on a simple React website. 

--- 
## Backend
### Reddit API
* Retrieve your Reddit API [here](https://www.reddit.com/prefs/apps)
* From above link, create an app at the bottom of the page
* Go to `/backend` directory 
* Create a `praw.ini` file with:
```python
[RedditSecrets]
client_id=<14 CHARACTER PERSONAL USE SCRIPT>
client_secret=<27 CHARACTER SECRET>
user_agent=<YOUR APP NAME>
```
### To start backend
* Create new conda env `conda create --n reddit_sentiments`
* Activate newly created env with `conda activate reddit_sentiments` 
* Go to backend directory with `cd backend`
* Install required modules using `pip install -r requriements.txt`
* Run `python server.py`
* You will be able to see your csv files results in `backend/data` directory

### Wit.AI API
* Go to Wit.AI and create an App 
* After you create your App in Wit.AI, get your `WIT_ACCESS_TOKEN` from Settings (Server Access Token)
* You can simply initialise your Wit App and interact with it by:
 ```python
client = Wit(WIT_ACCESS_TOKEN)
resp = client.message('hello')
```
* Follow this [Wit.AI Quick Start Docs](https://wit.ai/docs/quickstart) to train your Wit.AI app
--- 
Things to note: 
* Always keep your API secrets (both Reddit and Wit.AI) secret
* How accurate/useful the sentiments analysis for the scrapped Reddit data depends on what how train your Wit.AI 
* You can always change the subreddits scrapped in `backend/config/config.ini`. 
* If you decide to target stocks other than penny stocks, remember to change the tickers in `backend/config/tickers.json` as well. 
--- 
## Frontend 
A simple react frontend that displays the csv results scrapped by backend, and the sentiments analysed by Wit.AI

### To start frontend
* You should have your server running in a terminal following the previous steps on starting the backend
* Using a seperate terminal: 
 ```javascript
cd frontend
npm install
npm start
```
--- 

### Ticker Symbol API - EOD Historical Data
Included for potential future use is a csv file that contains all the listed ticker symbols for stocks, ETFs, and mutual funds (~50,000 tickers). This was retrieved from https://eodhistoricaldata.com/. You can register for a free api key and get up to 20 api calls every 24 hours.

To retrieve a csv of all USA ticker symbols, use the following:

https://eodhistoricaldata.com/api/exchange-symbol-list/US?api_token={YOUR_API_KEY}

--- 
## Contribution 
I would love to see more work done on this, I think this could be something very useful at some point. All contributions are welcome. Go ahead and open a PR.