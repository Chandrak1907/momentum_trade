# Why this package?
	
	Purpose of this work is to identify high momentum stocks using daily adjusted close prices. This work is inspired by below:
	1. Stocks on the move by Andreas Clenow[https://www.followingthetrend.com/stocks-on-the-move/] 
	2. Algorithmic trading using Python [https://www.youtube.com/watch?v=xfzGZB4HhEE&t=5204s]

# what does this package do?
	
	For all tickers in US and Indian stock markets, 
	1. This package will fetch past 90 days of daily data. 
	2. Store the data in csv file in a local directory (stocks_history)
	3. Fits a linear regression model on log of adjusted closes(for US tickers) and log of close (for Indian tickers, I could not find adjusted close for Indian tickers)
	4. Generates Hurst Indicator, Moving Averages etc.
	5. Ranks stocks
	6. Saves results to google spreadsheet(Optional)
	Steps 1,2,3 and 4 are parallelized.

# How to use this package?
	
	1. Clone the repo - 'git clone https://github.com/Chandrak1907/momentum_trade.git'
	2. Create and activate a virtual environment for Python
	3. Install pip if not available
	4. $cd momentum_trade
	5. $pip install -e .
	6. $cd momentum_trade
	4. $python generate_slopes_360.py 


	
