TODO: Reflect on what you learned this week and what is still unclear.
This week I began to analyse the information from my chosen dataset using Pandas.
Although it was difficult getting my head around Pandas at first, Ben's example layout made it easier to extract information bit by bit.
I learnt that some errors/typos in the original spreadsheet can affect how the data is interpreted through Pandas. This should be fixed in Pandas. For example, to ensure a column was all numerical and had no strings, it was necessary to replace all Nans with 0 using the DataFrame.ColumnName.fillna(0) method.
Eventually, I was able to create some graphs to show the frequency of deaths according to Event Category and Region.
