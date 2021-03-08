import os, re
from wit import Wit
from pathlib import Path
import datetime as dt
from dotenv import load_dotenv
import emoji

load_dotenv()   
WIT_ACCESS_TOKEN = os.getenv("WIT_ACCESS_TOKEN")

class WitAnalysis: 

    def __init__(self):
        self.client = Wit(WIT_ACCESS_TOKEN)
    
    def extract_sentiments(self, title):
        has_emoji = bool(emoji.get_emoji_regexp().search(title))
        if has_emoji:
            return None
        resp = self.client.message(title)
        return resp

    def extract_intents(self, sentiment):
        if not sentiment:
            return None
        if len(sentiment['intents']) == 0:
            return ''
        return sentiment['intents'][0]['name']
    
    def extract_intents_confidence(self, sentiment):
        if not sentiment:
            return None
        if len(sentiment['intents']) == 0:
            return ''
        return sentiment['intents'][0]['confidence']
    
    def extract_traits(self, sentiment):
        if not sentiment:
            return None
        if len(sentiment['traits']) == 0:
            return ''
        return sentiment['traits']['wit$sentiment'][0]['value']

    def extract_traits_confidence(self, sentiment):
        if not sentiment:
            return None
        if len(sentiment['traits']) == 0:
            return ''
        return sentiment['traits']['wit$sentiment'][0]['confidence']

    def get_sentiments(self, master, top_tickers):
        tickers_sentiments = []
        for ticker in top_tickers:
            sentiment_df = master.loc[master['extracted'] == {ticker}]
            sentiment_df['sentiments'] = sentiment_df['title'].apply(self.extract_sentiments)
            sentiment_df['intents'] = sentiment_df['sentiments'].apply(self.extract_intents)
            sentiment_df['intents_confidence'] = sentiment_df['sentiments'].apply(self.extract_intents_confidence)
            sentiment_df['traits'] = sentiment_df['sentiments'].apply(self.extract_traits)
            sentiment_df['traits_confidence'] = sentiment_df['sentiments'].apply(self.extract_traits_confidence)
            tickers_sentiments.append((sentiment_df, ticker))

        for sentiment, ticker in tickers_sentiments:
            data_directory = Path('./data/sentiments')
            data_directory.mkdir(parents=True, exist_ok=True)
            output_path = data_directory / f'{dt.date.today()}_{ticker}_sentiment_df.csv'
            sentiment.to_csv(output_path, index=False)

        return tickers_sentiments
        