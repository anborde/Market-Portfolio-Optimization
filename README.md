# Market-Portfolio-Optimization
The repository consists of the program which studies data of selected stocks of NIFTY for the period of 6 months and provides the optimized allocation of capital to the stocks.

**Note: The aim of the program is not to predict, but to understand stock data and carry out calculations depending on it. The program should not be tested on the grounds of future prediction but on the grounds of past interpretation.**

-- -
### Table of Content
1. optimize.py
  - The python code optimizes the allocation to the stock data provided
2. data/
  - This folder consists of the stock data over which the code runs

### Requirements
- Python 2.7.x
- Libraries: NumPy, SciPy, Matplotlib

### Usage
1. Run the optimize.py file to execute the program.
2. The code is written considering the stocks of INFY, LT, HDFCBANK and ICICIBANK which are listed on National Stock Exchange (NSE), India.
3. In order to suit the Indian stock data the parameter `dayfirst='True'` is used to instruct the `pd.read_csv()`at line 18 in `load_data()` function to read the date data in the dd/mm/yyyy format. If working on US data, do remove the parameter.
4. When the code is executed, it will ask for 2 inputs, namely Investment Capital and Savings Interest Rate.
5. Enter the inputs and the code will then optimize your capital over the stocks mentioned above.
6. The output will consist of the number of shares of each stock that should have been bought at the start date of the data under consideration to reap maximum benefits.
6. Furthermore, a graph showing the growth of your portfolio vs. that of the market index, NIFTY in this case is shown.
7. You can change the stocks and the market as per your requirement but do ensure you store the required stock data in the **data/** folder with the format of data file as *{Symbol}.csv* where Symbol is the stock Symbol. Also do change the part of the code at line 72 and 75 which deals with the date range of data and the stock symbols.

### License 
- Inclueded in the repo

### Acknowledgement
- Prof. Tucker Balch 
(Associate Chair for Graduate Studies, Interactive Computing
Professor, Interactive Computing
Professor, Electrical and Computer Engineering (adjunct)
Georgia Tech)
- Udacity
