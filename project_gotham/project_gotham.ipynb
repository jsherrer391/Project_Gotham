{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "612bbf4c-b64d-4125-9895-fc09ef687175",
   "metadata": {},
   "outputs": [],
   "source": [
    "#!pip install alpaca_trade_api"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "7ba008c1-0e19-4018-a6d2-f9e6e54dd11e",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import the required libraries and dependencies\n",
    "import os\n",
    "import requests\n",
    "import pandas as pd\n",
    "from dotenv import load_dotenv\n",
    "import alpaca_trade_api as tradeapi\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "95088165-ec85-4b18-a2dd-17eb67d6b6f0",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Load .env environment varaables\n",
    "load_dotenv()\n",
    "\n",
    "# Set Alpaca API key and secret\n",
    "alpaca_api_key = os.getenv(\"API_KEY\")\n",
    "#alpaca_secret_key = os.getenv(5YiQuK9E8xlvJA18PlKX9u8MIC4Bdf2YOype1Uzn)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2f8ec7a6-4714-4545-b6ed-d496b2ff4867",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create the Alpaca API object\n",
    "alpaca = tradeapi.REST(\n",
    "    alpaca_api_key,\n",
    "    alpaca_secret_key,\n",
    "    api_version=\"v2\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "36ed7031-8e94-408e-a23f-bca131a19065",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'PKPMWB2FBTP5LMG8X8E0'"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "today_date = str(datetime.datetime.now()).split()[0]\n",
    "one_year_ago = str(datetime.datetime.now() - datetime.timedelta(days=1*365)).split()[0]\n",
    "today_date, one_year_ago"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7aeaf408-036b-4b82-ba23-a5d3fd6e8216",
   "metadata": {},
   "outputs": [],
   "source": [
    "# set teh tickers\n",
    "ticker = [\"GME\", \"AMZN\"]\n",
    "\n",
    "# SET TIMEFRAME TO \"1D\"\n",
    "timeframe = \"1D\"\n",
    "\n",
    "#set start and end datetimes of 1 Year, between now and 365 days ago\n",
    "start_date = pd.Timestamp(one_year_ago, tz=\"America/New_York\").isoformat()\n",
    "end_date = pd.Timestamp(today_date, tz=\"America/New_York\").isoformat()\n",
    "\n",
    "# get 1 year's worth of histroical data for \n",
    "df_ticker = alpaca.get_barest(\n",
    "    ticker,\n",
    "    timeframe\n",
    "    start=start_date,\n",
    "    end=end_date\n",
    ").df\n",
    "\n",
    "#display sample data\n",
    "df_ticker.head(10)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "45439f92-51a0-48f0-be2c-c01a0a7a114b",
   "metadata": {},
   "outputs": [],
   "source": [
    "#create and empty dataframe for closing prices\n",
    "df_closing_prices = pd.DataFrame()\n",
    "\n",
    "#Fetch the closing prices of \n",
    "df_closing_prices[] = df_ticker[][close]\n",
    "df_closing_prices[] = df_ticker[][close]\n",
    "\n",
    "#drop the time componet of the date\n",
    "df_closing_prices.index = df_closing_prices.index.date\n",
    "\n",
    "#compute daily returns\n",
    "df_daily_returns = df_closing_prices.pct_change().dropna()\n",
    "\n",
    "#display smale data\n",
    "df_daily returns.head(10)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7e1d08c4-5ab8-4c8d-9164-e1df2380c159",
   "metadata": {},
   "outputs": [],
   "source": [
    "# generate descriptive statistics\n",
    "df_daily_returns.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f545e74e-dc6c-45e2-a36d-60102f6f289d",
   "metadata": {},
   "outputs": [],
   "source": [
    "# visualize distribution of  percent change in closing prices using a historgram plot\n",
    "df_daily_returns[].plot.hist()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:dev2]",
   "language": "python",
   "name": "conda-env-dev2-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
