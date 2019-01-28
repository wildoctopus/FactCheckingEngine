# Fact Checker

Fact checker based on Wikipedia corpus , done using NLTK and Wikipedia packages

## Team Name
SNLP

## Team Members:

| Name                  | Matriculation Number |
| --------------------- | -------------------- |
| Ashish Kumar Shukla   | 6844552              |
| Alok Pandey           | 6854287              |


### Prerequisites : 

* Python3
* Pip3 
* NLTK
* Wikipedia 


## Setup Guide :

* If the wikipedia corpus is created locally we do the fact checking according to the local corpus otherwise Wikikipedia python package is used for fact checking.

* Local Corpus Creation
    * Download the latest wikipedia dump. This is a bz2 archive, which contains a xml -file with the latest stand of the articles of wikipedia. https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2

    * A warning: the latest such English Wikipedia database dump file is ~14 GB in size, so downloading, storing, and processing said file is not exactly trivial.

    * install gensim python package. 
    
    * We wrote a simple python script create_corpus which uses gensim and the wikipedia dump file to create the corpus.

    * It might take several hours if you are trying to do it on cpu power.
    
    * example : 

    ```
    python3 create_corpus.py enwiki-latest-pages-articles.xml.bz2 wiki_en.txt
    ```
* We created our own grammar which helps us to extract name and entity from the sentence and then we seach in wikipedia with the help of name and entity.    


## Running the tests

* for train data
```
    pthon3 fact_checker.py train 
```
* for test data
```
    pthon3 fact_checker.py test  
``` 

## How it works : 


