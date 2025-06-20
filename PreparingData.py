# importing polars to read csv and edit it
import polars as pl
import pandas as pd
import csv



csv.field_size_limit(100000000)
dt_1000 = pd.read_csv("email_spam.csv")
dt_20 = pd.read_csv("Enron.csv")
dt_30 = pd.read_csv("enron_spam_data.csv")
dt_90 = pd.read_csv("spam.csv",encoding="latin-1")
dt_110 = pd.read_csv("spam_ham_dataset.csv")
# read the spam emails csvs
dt0 = pd.read_csv("CEAS_08.csv",engine="python",on_bad_lines="skip")
dt_40 = pd.read_csv("Ling.csv",engine="python",on_bad_lines="skip")
dt_50 = pd.read_csv("Nazario.csv",engine="python",on_bad_lines="skip")
dt_60 = pd.read_csv("Nazario_5.csv",engine="python",on_bad_lines="skip")
dt_70 = pd.read_csv("Nigerian_5.csv",engine="python",on_bad_lines="skip")
dt_80 = pd.read_csv("Nigerian_Fraud.csv",engine="python",on_bad_lines="skip")
dt_100 = pd.read_csv("SpamAssasin.csv",engine="python",on_bad_lines="skip")
dt_120 = pd.read_csv("TREC_05.csv",engine="python",on_bad_lines="skip")
dt_130 = pd.read_csv("TREC_06.csv",engine="python",on_bad_lines="skip")
dt_140 = pd.read_csv("TREC_07.csv",engine="python",on_bad_lines="skip")

dt = dt0
dt_1 = dt_1000
dt_2 = dt_20
dt_3 = dt_30        
dt_4 = dt_40
dt_5 = dt_50
dt_6 = dt_60
dt_7 = dt_70
dt_8 = dt_80
dt_9 = dt_90
dt_10 = dt_100
dt_11 = dt_110
dt_12 = dt_120
dt_13 = dt_130
dt_14 = dt_140


#find the label features to add them to new one big dataset

try:    
    print(dt["label"])
    print("1 done......")
    for i in range(len(dt_1["type"])):
        if dt_1["type"][i] == "spam":
            dt_1.loc[i, "type"] = 1
        else:
            dt_1.loc[i, "type"] = 0
    print(dt_1["type"])
    print("2 done......")
    print(dt_2["label"])
    print("3 done......")
    # Convert 'spam' to 1 and 'ham' to 0 in the 'Spam/Ham' column of dt_3
    for i in range(len(dt_3["Spam/Ham"])):
        if dt_3["Spam/Ham"][i] == "spam":
            dt_3.loc[i, "Spam/Ham"] = 1
        else:
            dt_3.loc[i, "Spam/Ham"] = 0
    print(dt_3["Spam/Ham"])
    print("4 done......-------------------------------------------")
    print(dt_4["label"])
    print("5 done......--------------------------------------------")
    print(dt_5["label"]) 
    print("6 done......------------------------------------------")       
    print(dt_6["label"])
    print("7 done......------------------------------------------")
    print(dt_7["label"])
    print("8 done......------------------------------------------")
    print(dt_8["label"])
    print("9 done......------------------------------------------")
    # Convert 'spam' to 1 and 'ham' to 0 in the 'v1' column of dt_9
    for i in range(len(dt_9["v1"])):
        if dt_9["v1"][i] == "spam":
            dt_9.loc[i, "v1"] = 1
        else:
            dt_9.loc[i, "v1"] = 0
    print(dt_9["v1"])
    print("10 done......-------------------------------------------")
    print(dt_10["label"])
    print("11 done......-------------------------------------------")
    # Convert 'spam' to 1 and 'ham' to 0 in the 'label' column of dt_11
    for i in range(len(dt_11["label"])):
        if dt_11["label"][i] == "spam":
            dt_11.loc[i, "label"] = 1
        else:
            dt_11.loc[i, "label"] = 0
    print(dt_11["label"])
    print("12 done......-------------------------------------------")
    print(dt_12["label"])
    print("13 done......-------------------------------------------")
    print(dt_13["label"])
    print("14 done......--------------------------------------------")
    print(dt_14["label"])
    print("15 done......-------------------------------------------")
except KeyError:
    print("One of the datasets does not have a 'label' column. Please check the dataset structure.")

# now finding all the body features from 

try:    
    print(dt["body"])
    print("1 done......")
    print(dt_1["text"])
    print("2 done......")
    print(dt_2["body"])
    print("3 done......")
    print(dt_3["Message"])
    print("4 done......-------------------------------------------")
    print(dt_4["body"])
    print("5 done......--------------------------------------------")
    print(dt_5["body"]) 
    print("6 done......------------------------------------------")       
    print(dt_6["body"])
    print("7 done......------------------------------------------")
    print(dt_7["body"])
    print("8 done......------------------------------------------")
    print(dt_8["body"])
    print("9 done......------------------------------------------")
    print(dt_9["v2"])
    print("10 done......-------------------------------------------")
    print(dt_10["body"])
    print("11 done......-------------------------------------------")
    print(dt_11["text"])
    print("12 done......-------------------------------------------")
    print(dt_12["body"])
    print("13 done......-------------------------------------------")
    print(dt_13["body"])
    print("14 done......--------------------------------------------")
    print(dt_14["body"])
    print("15 done......-------------------------------------------")
except KeyError:
    print("One of the datasets does not have a 'body' column. Please check the dataset structure.")

dt_15 = pd.read_csv("spam_or_not_spam.csv")


final_dt = pd.DataFrame(
    {
        "body":pd.concat([
            dt["body"],
            dt_1["text"],
            dt_2["body"],
            dt_3["Message"],
            dt_4["body"],
            dt_5["body"],
            dt_6["body"],
            dt_7["body"],
            dt_8["body"],
            dt_9["v2"],
            dt_10["body"],
            dt_11["text"],
            dt_12["body"],
            dt_13["body"],
            dt_14["body"],
            dt_15["email"].fillna(' ')
        ],ignore_index=True),
        "label":pd.concat([
            dt["label"],
            dt_1["type"],
            dt_2["label"],
            dt_3["Spam/Ham"],
            dt_4["label"],
            dt_5["label"],
            dt_6["label"],
            dt_7["label"],
            dt_8["label"],
            dt_9["v1"],
            dt_10["label"],
            dt_11["label"],
            dt_12["label"],
            dt_13["label"],
            dt_14["label"],
            dt_15["label"],

        ],ignore_index=True),
    }
)

final_dt.to_csv("email_spam_detection.csv")

df_1 = pd.read_csv("email_spam_detection.csv")
df = df_1
print(df[0:20])

df["label"] = df["label"].fillna(0).astype(int)
df.to_csv("email_spam_detection_final.csv")