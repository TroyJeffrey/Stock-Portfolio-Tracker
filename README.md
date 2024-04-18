# Stock Portfolio Management System

## Project Description:

The Stock Portfolio Management System is a command-line platform designed to help users efficiently track their stock portfolio and report profits. This system offers two accounting methods, LIFO (Last In, First Out) and FIFO (First In, First Out), allowing users to choose the method that best suits their investment strategy.

## Key Features:

Method Selection: Users are prompted to select their preferred accounting method, either LIFO or FIFO, upon launching the program.
Stock Transactions:
Buy Stocks (Long): Users can add stocks to their portfolio by specifying the company name, quantity of shares, and market price per share. The system calculates the total value of the purchased stocks and updates the portfolio accordingly.
Sell Stocks (Short): Users can sell stocks from their portfolio by specifying the company name and the quantity of shares they wish to sell. The system validates the availability of stocks for sale and calculates the total sale value. If the user sells more stocks than available, the system automatically adjusts the remaining stocks and updates the portfolio.
Portfolio Management:
View Current Portfolio: Users can view the list of companies in which they currently hold shares along with the total number of shares in their portfolio.
View Profit/Loss: Users can check the realized profit or loss from their stock transactions, providing valuable insights into their investment performance.
Implementation Details:

The system utilizes two data structures, Stack and Queue, to implement the LIFO and FIFO accounting methods, respectively.
User inputs are collected through the command-line interface, allowing for interactive usage.
Error handling is implemented to ensure data integrity and prevent invalid transactions, such as selling more stocks than available.
Realized profit or loss is calculated based on the difference between the total value of stocks bought and the total value of stocks sold.

## Usage Instructions:

Run the program and select the desired accounting method (LIFO or FIFO).
Follow the prompts to perform stock transactions, including buying and selling stocks.
View the current portfolio to monitor the stocks held and their quantities.
Check the realized profit or loss to evaluate the investment performance.vv
