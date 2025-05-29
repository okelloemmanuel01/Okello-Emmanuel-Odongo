import pandas as pd
import numpy as np
from datetime import datetime

def clean_sales_data(df):
    """Specialized cleaning function for Sales data"""
    cleaned_df = df.copy()
    
    # 1. Handle missing values
    if 'amount' in cleaned_df.columns:
        cleaned_df['amount'] = cleaned_df['amount'].fillna(cleaned_df['amount'].median())
    
    if 'product_id' in cleaned_df.columns:
        cleaned_df['product_id'] = cleaned_df['product_id'].fillna('Unknown').astype('string')
    
    # 2. Standardize date formats
    date_cols = [col for col in cleaned_df.columns if 'date' in col.lower()]
    for col in date_cols:
        cleaned_df[col] = pd.to_datetime(cleaned_df[col], errors='coerce', format='mixed')
        cleaned_df[col] = cleaned_df[col].fillna(pd.to_datetime('today'))
    
    # 3. Remove duplicate transactions
    cleaned_df = cleaned_df.drop_duplicates()
    
    # 4. Fix wrong data
    if 'amount' in cleaned_df.columns:
        cleaned_df['amount'] = cleaned_df['amount'].abs()
        cleaned_df['amount'] = pd.to_numeric(cleaned_df['amount'], errors='coerce').fillna(0)
    
    if 'quantity' in cleaned_df.columns:
        cleaned_df['quantity'] = cleaned_df['quantity'].apply(lambda x: int(abs(x)) if pd.notnull(x) else 1)
        cleaned_df['quantity'] = cleaned_df['quantity'].astype('int64')
    
    # 5. Remove unnecessary columns
    cols_to_drop = ['temp', 'notes', 'unused_column', 'legacy_id']
    cleaned_df = cleaned_df.drop(columns=[col for col in cols_to_drop if col in cleaned_df.columns])
    
    return cleaned_df

def clean_mine_data(df):
    """Specialized cleaning function for Mine data"""
    cleaned_df = df.copy()
    
    # 1. Handle missing values
    num_cols = cleaned_df.select_dtypes(include=[np.number]).columns
    for col in num_cols:
        cleaned_df[col] = cleaned_df[col].fillna(cleaned_df[col].median())
    
    cat_cols = cleaned_df.select_dtypes(include=['object']).columns
    for col in cat_cols:
        cleaned_df[col] = cleaned_df[col].fillna('Unknown').astype('string')
    
    # 2. Standardize date/time formats
    if 'extraction_date' in cleaned_df.columns:
        cleaned_df['extraction_date'] = pd.to_datetime(cleaned_df['extraction_date'], errors='coerce', format='mixed')
        cleaned_df['extraction_date'] = cleaned_df['extraction_date'].fillna(pd.to_datetime('today'))
    
    # 3. Remove duplicate records
    cleaned_df = cleaned_df.drop_duplicates()
    
    # 4. Fix wrong data
    if 'grade' in cleaned_df.columns:
        cleaned_df['grade'] = cleaned_df['grade'].clip(0, 100)
        cleaned_df['grade'] = pd.to_numeric(cleaned_df['grade'], errors='coerce').fillna(0)
    
    if 'tonnage' in cleaned_df.columns:
        cleaned_df['tonnage'] = cleaned_df['tonnage'].apply(lambda x: x if x > 0 else np.nan)
        cleaned_df['tonnage'] = cleaned_df['tonnage'].fillna(cleaned_df['tonnage'].median())
        cleaned_df['tonnage'] = cleaned_df['tonnage'].astype('int64')
    
    # 5. Remove unnecessary columns
    cols_to_drop = ['old_reference', 'comments', 'deprecated_id']
    cleaned_df = cleaned_df.drop(columns=[col for col in cols_to_drop if col in cleaned_df.columns])
    
    return cleaned_df

def main():
    try:
        # Load datasets
        sales_df = pd.read_csv('Sales.csv')
        mine_df = pd.read_csv('Mine.csv')
        
        print("Original Data Overview:")
        print("Sales data shape:", sales_df.shape)
        print("Mine data shape:", mine_df.shape)
        
        # Clean datasets
        cleaned_sales = clean_sales_data(sales_df)
        cleaned_mine = clean_mine_data(mine_df)
        
        # Verification
        print("\nMissing Values After Cleaning:")
        print("Sales missing values:", cleaned_sales.isna().sum().sum())
        print("Mine missing values:", cleaned_mine.isna().sum().sum())
        
        # Save cleaned data with explicit handling of null representations
        cleaned_sales.to_csv(
            'Cleaned_Sales.csv',
            index=False,
            na_rep='NA',
            float_format='%.2f',
            date_format='%Y-%m-%d'
        )
        
        cleaned_mine.to_csv(
            'Cleaned_Mine.csv',
            index=False,
            na_rep='NA',
            float_format='%.2f',
            date_format='%Y-%m-%d'
        )
        
        print("\nData cleaning completed successfully!")
        print("\nCleaned Data Samples:")
        
        print("\nSales Data (first 3 rows):")
        print(cleaned_sales.head(3).to_string())
        
        print("\nMine Data (first 3 rows):")
        print(cleaned_mine.head(3).to_string())
        
        print("\nOutput files created:")
        print("- Cleaned_Sales.csv")
        print("- Cleaned_Mine.csv")
        
    except FileNotFoundError as e:
        print(f"\nError: {str(e)} - Please ensure both Sales.csv and Mine.csv are in the current directory")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {str(e)}")
        print("Please check your input files and try again.")

if __name__ == "__main__":
    main()