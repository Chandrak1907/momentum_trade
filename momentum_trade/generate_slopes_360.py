import portfolio_variables 
import process_stocks_360_pool_volume
import logging
import datetime
from datetime import date
import os
import pickle
from pathlib import Path
import timeit
import pandas as pd
import nsepy

def main():
	start_time = timeit.default_timer()
	print(" generate slopes")
	prefix = datetime.datetime.now().strftime('%Y-%m-%d')
	os.makedirs("../logs/"+prefix,exist_ok=True)
	logging.basicConfig(filename='../logs/'+prefix+'/log_file.log',filemode='w',level=logging.INFO)
	sp500 = process_stocks_360_pool_volume.get_sp500_tickers()
	logging.info("processing sp500 tickers ... ")
	logging.info(" -- getting all nasdaq_symobols ... ")
	nasdaq_symbols = process_stocks_360_pool_volume.get_all_nasdaq_symbols()
	nyse = pd.read_csv("../csvs_n_tokens/nyse.csv",header=2)
	nyse_symbols = list(nyse.Symbol.values)
	nasdaq_sp500 = list(set(sp500+nasdaq_symbols+nyse_symbols))
	# nasdaq_sp500=['DQ','IBM']
	# sp500 = ['']
###############	#####################################US STOCKS ######################1
	process_stocks_360_pool_volume.get_results_data_frame(nasdaq_sp500,'nasdaq',sp500)
	print("Time for running this code .. ",timeit.default_timer() - start_time)
###############	############################################################1
	print("..Working on Indian stock market")
	nse = pd.read_csv("../csvs_n_tokens/ind_nifty100list.csv")
	nse100 = nse.Symbol.values
	nse_stocks = process_stocks_360_pool_volume.get_nse_list()
	results = process_stocks_360_pool_volume.get_results_data_frame(nse_stocks,"NSE",nse100)
	print("Time for running this code .. ",timeit.default_timer() - start_time)
###############	############################################################   2
if __name__=='__main__':
	main()