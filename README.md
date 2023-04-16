# tfidfcalculator

Calculate TF-IDF statistical measures of a word relevancies in text. 

**This was implemented purely as a learning experience.**

## Usage

Prepare your text file by manually splitting it into documents (chapters) using a dedicated separator line (e.g. ==============)


Instantiate cache repository, parser, data loader and calculator itself, feed file to loader:

```
file_path = "d:\\tf_df_test\\text_sample.txt"
dc = cache_repository()
dp = parser()
dp.config(document_separator = '==============')
ld = document_loader_service(dc, dp)
data = ld.load_file(file_path, False)

calc = tfidf_calculator(data)

tf = calc.build_tf_data(3)
df = calc.build_df_data(3)
tfidf = calc.build_tf_idf_data(tf, df,3)
```

