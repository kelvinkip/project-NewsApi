from distutils.command.config import config
import os

class Config:
    
    NEWS_API_BASE_URL ='https://newsapi.org/v2/sources?apiKey={}'
    NEWS_ARTICLES_BASE_URL = 'https://newsapi.org/v2/top-headlines?language=en&apiKey={}'
    NEWS_API_KEY =  '4e76f508ebd04889982e995a6f20f93c'

    
    
    
class ProdConfig(Config):
        pass
    
class DevConfig(Config):
        DEBUG = True
        
config_options = {      #config_options ia a dictionary to help us make choices
    'development':DevConfig,
    'production':ProdConfig   
}
