import csv
import pandas as pd
import spacy
import ast

nlp = spacy.load("en_core_web_sm")

# with open("reddit_gentrification_unique.csv", "w") as f:
#     csv_writer = csv.writer(f)
#     csv_writer.writerow(["URL", "TITLE", "TEXT", "LEFT CONTEXT", "RIGHT CONTEXT", "CONTEXT"])

unique_df = pd.read_csv('reddit_gentrification_unique.csv')
all_df = pd.read_csv('reddit_gentrification_all.csv')

for index, row in all_df.iterrows():
    list_of_words = ast.literal_eval(row['RIGHT CONTEXT'])
    doc = nlp(' '.join(list_of_words))
    entity_present = False
    # for word in row['RIGHT CONTEXT']:
    for word in doc.ents:
        #print(word.text)
        if word.text in ' '.join(list_of_words):
            entity_present = True
    if entity_present:
        continue
    #add record to csv
    context = "gentrification of " + ' '.join(list_of_words)
    row = {'URL':row['URL'], 'TITLE':row['TITLE'], 'TEXT':row['TEXT'], 'LEFT CONTEXT':row['LEFT CONTEXT'], 
            'RIGHT CONTEXT':row['RIGHT CONTEXT'], 'CONTEXT':context}
    # row = [row['URL'], row['TITLE'], row['TEXT'], row['LEFT CONTEXT'], row['RIGHT CONTEXT'], context]
    print(row)
    unique_df = unique_df._append(row, ignore_index = True)

unique_df.to_csv('reddit_gentrification_unique.csv')