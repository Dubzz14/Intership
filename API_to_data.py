import requests
import pandas as pd
from sqlalchemy import create_engine
import os

median = requests.get("https://dummyjson.com/products")

mode = median.json()

