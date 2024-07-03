def preprocess_dataframe(df):
    # Rename columns
    def standardize_col(col):
        return col.lower().replace(" ", "_")

    
    # Map gender values
  
    def map_gender(df, column_name='gender'):
 
        gender_mapping = {
        'F': 'F',
        'Femal': 'F',
        'female': 'F',
        'M': 'M',
        'Male': 'M'
    }
    
    df[column_name] = df[column_name].replace(gender_mapping)
    return df
  
    
    # Standardize state values
    def map_states(df, column_name='state'):
 
     state_mapping = {
        "AZ": "Arizona",
        "CA": "California",
        "WA": "Washington",
        "Cali": "California",
        "OR": "Oregon"
    }
    df['state'] = df['state'].replace(state_mapping)
    return df
    
    

    def map_education(df, column_name='education'):
 
        education_mapping = {
        'Bachelors': 'Bachelor',
        # Add more mappings as needed
    }
    
    df[column_name] = df[column_name].replace(education_mapping)
    return df
    

    def clean_customer_lifetime_value(df, column_name='customer_lifetime_value'):
    # Convert to string
        df[column_name] = df[column_name].astype(str)
    # Remove the '%' character
        df[column_name] = df[column_name].str.replace('%', '')
    # Convert the values to float
        df[column_name] = df[column_name].astype(float)
    return df


    def map_vehicles(df, column_name='vehicle_class'):
   
        car_mapping = {
        'Luxury Car': 'Luxury',
        'Sports Car': 'Luxury',
        'Luxury SUV': 'Luxury',
    }

    df['vehicle_class'] = df['vehicle_class'].replace(car_mapping)
    return df


    def open_complaints_format(df, column_name='open_complaints'):
   
        df['number_of_open_complaints'].unique()
        df["number_of_open_complaints"] = df["number_of_open_complaints"].str.split('/').str[1]
        df['number_of_open_complaints'] = pd.to_numeric(df['number_of_open_complaints'], errors='coerce')
        df['number_of_open_complaints'].unique()
    return df

    def nul_value_drop(df):
        df = df.drop_duplicates()
        df['gender'] = df['gender'].fillna('Unknown')
        df.gender.unique()
        customer_mean = df.customer_lifetime_value.mean()
        df['customer_lifetime_value'] = df['customer_lifetime_value'].fillna(customer_mean)
        return df
    
    return df

    # Apply all the functions above
   