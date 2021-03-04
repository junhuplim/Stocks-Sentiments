import os, re
from wit import Wit
from pathlib import Path
import datetime as dt
from dotenv import load_dotenv

load_dotenv()   
WIT_ACCESS_TOKEN = os.getenv("WIT_ACCESS_TOKEN")

class WitAnalysis: 

    def __init__(self):
        self.client = Wit(WIT_ACCESS_TOKEN)
    
    def deEmojify(self, text):
        regrex_pattern = re.compile(pattern = "["
            u"\U0001F600-\U0001F64F"  # emoticons
            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
            u"\U0001F680-\U0001F6FF"  # transport & map symbols
            u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                            "]+", flags = re.UNICODE)
        return regrex_pattern.sub(r'',text)
        
    def extract_sentiments(self, title):
        resp = self.client.message(self.deEmojify(title))
        return resp

    def extract_intents(self, sentiment):
        return sentiment['intents']
    
    def extract_traits(self, sentiment):
        if len(sentiment['traits']) == 0:
            return ''
        return sentiment['traits']['wit$sentiment'][0]['value']

    def get_sentiments(self, master, top_tickers):
        tickers_sentiments = []
        for ticker in top_tickers:
            sentiment_df = master.loc[master['extracted'] == {ticker}]
            sentiment_df['sentiments'] = sentiment_df['title'].apply(self.extract_sentiments)
            sentiment_df['intents'] = sentiment_df['sentiments'].apply(self.extract_intents)
            sentiment_df['traits'] = sentiment_df['sentiments'].apply(self.extract_traits)
            tickers_sentiments.append((sentiment_df, ticker))

        for sentiment, ticker in tickers_sentiments:
            data_directory = Path('./data/sentiments')
            data_directory.mkdir(parents=True, exist_ok=True)
            output_path = data_directory / f'{dt.date.today()}_{ticker}_sentiment_df.csv'
            sentiment.to_csv(output_path, index=False)

        return tickers_sentiments
        