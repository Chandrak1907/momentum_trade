# Why this package?
	
	Purpose of this work is to identify high momentum stocks using daily adjusted close prices. This work is inspired by below:
	1. Stocks on the move by Andreas Clenow[https://www.followingthetrend.com/stocks-on-the-move/] 
	2. Algorithmic trading using Python [https://www.youtube.com/watch?v=xfzGZB4HhEE&t=5204s]

# what does this package do?
	
	For tickers in US and Indian stock markets, 
	1. This package will fetch past 90 days of daily data 
	2. Store the data in csv file in a local directory (stocks_history)
	3. Fits a linear regression model on log of adjusted closes(for US tickers) and log of close (for Indian tickers, I could not find adjusted close for Indian tickers)
	4. More details to write here

# How to use this package?
	
	1. To insall "pip install momentum_trade"
	2. For running the code
		1. Parameters in "portfolio_variables.py" need to be updated
		2. "from momentum_trade import generate_slopes_360"
		3. "generate_slopes_360.main()"
		2. If you want to save results in google spreadsheet, you need to save google spreadsheets API secret token in 'csvs_n_tokens' folder
		3. Otherwise, results for Indian stock market are saved as "NSE.csv" and for US market - "nasdaq.csv"
	
