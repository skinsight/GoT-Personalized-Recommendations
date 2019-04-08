def get_complimentary_gifts(df, df2):
    # Convert the columns: Existing product and New Product into a dictionary of this type: {'Dragon Fire Foundation': 'Stormborn Setting Powder SPF 50', ...}
    dict_existing_new = dict(zip(df2.Existing_Product, df2.New_Product))
    
    #Get most purchased product YTD for each customer and then print using .format() to inform fulfillment team
    clients = df.columns[1:]
    for client in clients:
        item_bght_most_freq = df[client].value_counts().index.tolist()[0]
        # Get the new product that is most similar to the most frequently-purchased product
        new_prod_market = dict_existing_new[item_bght_most_freq]
        print("Send {} a complimentary {} based on previous loyalty to {}".format(client, new_prod_market, item_bght_most_freq))

        
