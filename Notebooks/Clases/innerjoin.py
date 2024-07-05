import pandas as pd

# Supongamos que estos son tus DataFrames ya cargados:
# df_sales_order_header = pd.DataFrame(...) # Carga de [Sales].[SalesOrderHeader]
# df_sales_order_detail = pd.DataFrame(...) # Carga de [Sales].[SalesOrderDetail]
# df_product = pd.DataFrame(...) # Carga de [Production].[Product]
# df_customer = pd.DataFrame(...) # Carga de [Sales].[Customer]

# Realizar las uniones (joins) como en la consulta SQL

# 1. Unir df_sales_order_header con df_sales_order_detail
merged_df = pd.merge(df_sales_order_header, df_sales_order_detail, left_on='SalesOrderID', right_on='SalesOrderID')

# 2. Unir el resultado con df_product
merged_df = pd.merge(merged_df, df_product, left_on='ProductID', right_on='ProductID')

# 3. Unir el resultado con df_customer
merged_df = pd.merge(merged_df, df_customer, left_on='CustomerID', right_on='CustomerID')

# Seleccionar las columnas deseadas
result_df = merged_df[['AccountNumber', 'Comment', 'DueDate', 'CustomerID', 'PersonID', 'ProductID', 'Name']]

# Mostrar el DataFrame resultante
print(result_df)