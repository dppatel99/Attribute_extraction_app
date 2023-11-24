import os
import pandas as pd
import evadb

def main():
    os.environ['OPENAI_API_KEY'] = 'sk-xxxxxxxxxxxxxxxxxx'
    # first convert config_ethos.json using config_converter using config_converter.py
    cursor = evadb.connect().cursor()
    print("Connected to EvaDB")
    
    create_function_query = f"""CREATE FUNCTION IF NOT EXISTS AutoLabel
            IMPL  'autolabel.py';
            """
    cursor.query("DROP FUNCTION IF EXISTS AutoLabel;").execute()
    cursor.query(create_function_query).execute()
    print("Created Function")

    create_table_query = f"""
    CREATE TABLE IF NOT EXISTS YTCOMMENTS(
    id TEXT(10),
    text TEXT(300),
    violence TEXT(15),
    directed_vs_generalized TEXT(15),
    gender TEXT(10)
    );
    """

    load_data_query = f""" LOAD CSV 'test.csv' INTO YTCOMMENTS;"""

    cursor.query(create_table_query).execute()
    cursor.query(load_data_query).execute()

    query= f""" SELECT AutoLabel("run", id, text, violence, directed_vs_generalized, gender) FROM YTCOMMENTS;"""
    result = cursor.query(query).execute()

    df = pd.read_csv("labeled_data.csv")

    # Compare 'violence' columns and compute accuracy
    total_rows = len(df)
    correct_predictions = (df.iloc[:,2] == df.iloc[:,5]).sum()
    vio_accuracy = correct_predictions / total_rows
    dir_accuracy = (df.iloc[:,3] == df.iloc[:,6]).sum() / total_rows
    gender_accuracy = (df.iloc[:,4] == df.iloc[:,7]).sum() / total_rows

    # Display the accuracy
    print(f"Total Accuracy for violence: {vio_accuracy * 100:.2f}%")
    print(f"Total Accuracy for directed_vs_generalized: {dir_accuracy * 100:.2f}%")
    print(f"Total Accuracy for gender: {gender_accuracy * 100:.2f}%")


if __name__ == "__main__":
    main()