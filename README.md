# tfidfcalculator

Calculate TF-IDF statistical measures of a word relevancies in text. 


**This was implemented purely as a learning experience.**


## Description:

TF stands for 'Term Frequency' - represents the frequency of the word in each document. The number of times the word appears in the document divided by total amount of words in the document.

DF stands for 'Document Frequency' - the proportion of documents that contain certain word. The amount documents containing certain word divided by the total amount of documents.

IDF stands for "Inverse Document Frequency" and essentially 1/DF.

TF-IDF stands for "Term Frequency-Inverse Document Frequency" - evaluates relevancy of a word to a document in a collection of documents.
TF-IDF = TF * log(IDF)



    
## Usage

Prepare your text file by manually splitting it into documents (chapters) using a dedicated separator line (e.g. ==============) Text may contain special characters:

![sample_text](https://user-images.githubusercontent.com/130370305/232334432-c52442fc-577f-49a5-89fe-649bcd767e4b.png)

Instantiate cache repository, parser, data loader and calculator itself, feed file to loader:


```
file_path = "d:\\tf_df_test\\text_sample.txt"
dc = cache_repository()
dp = parser()
dp.config(document_separator = '==============')
ld = document_loader_service(dc, dp)
data = ld.load_file(file_path, False)

calc = tfidf_calculator(data)

tfidf = calc.build_tf_idf_data(None,None)
tf = calc.tf_data
df = calc.df_data

flatten_tfidf = calc.flatten_data([], top_w = 10)
pd_tfidf_data = pd.DataFrame(data = flatten_tfidf, columns=['id', 'title', 'word', 'tfidf'])
```


Example of a heatmap for top ten words for each chapter of 'Alice in Wonderland':


![sample_heatmap](https://user-images.githubusercontent.com/130370305/232334804-1914fac5-86db-4c29-a6c5-3781a983301d.png)



