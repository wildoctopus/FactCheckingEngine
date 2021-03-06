# Fact Checker

Fact checker - A Fact Checking Engine (Universität Paderborn Semester Project)  based on Wikipedia corpus , developed using NLTK and Wikipedia packages.

## Team Name
SNLP

## Team Members:

| Name                  | Matriculation Number |
| --------------------- | -------------------- |
| Ashish Kumar Shukla   | 6844552              |
| Alok Kumar Pandey     | 6854287              |


### Prerequisites : 
* Python3
* Pip3 

## Setup Guide :
* Upgrade pip version with the current one. Execute below command - 
```
python3 -m pip install -U pip
```
* Run setup.py to Install project related packages like nltk, wikipedia and other mentioned in requirements.txt. 

```
python3 setup.py
```

## Corpus Creation and Validation

* Local Corpus Creation
    
    * Download the latest wikipedia dump. This is a bz2 archive, which contains a xml -file with the latest stand of the articles of wikipedia. https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2

    * A warning: the latest such English Wikipedia database dump file is ~14 GB in size, so downloading, storing, and processing said file is not exactly trivial.

    * install gensim python package. 
    
    * We wrote a simple python script create_corpus which uses gensim and the wikipedia dump file to create the corpus.

    * It might take several hours if you are trying to do it on cpu power.
    
    * Execute below command on terminal : 

    ```
    python3 create_corpus.py enwiki-latest-pages-articles.xml.bz2
    ```    
* Once the corpus is created we can validate the corpus with validate_corpus.py

    ```
    python3 validate_corpus.py
    ```
* If the wikipedia corpus is created locally we do the fact checking according to the local corpus otherwise Wikikipedia python package is used for fact checking.So in our project as processing of such a huge corpus consume more GPU and CPU power, we have used wikipedia package.

## Running the tests

* For train data
```
    pthon3 fact_checker.py train 
```
* For test data
```
    pthon3 fact_checker.py test  
``` 

## How it works : 

First we start with Tokenization , Given a character sequence and a defined document unit, tokenization is the task of chopping it up into pieces, called tokens , perhaps at the same time throwing away certain characters, such as punctuation.

Then we do POS Tagging , A Part-Of-Speech Tagger (POS Tagger)  reads text in some language and assigns parts of speech to each word (and other token), such as noun, verb, adjective, etc. 

After that we implement noun phrase chunking to identify named entities , also know as NER recognition. 
To efficiently identify NE we have wrote our own grammer - 
```
    grammar = r"""
    NBAR:
        # Nouns and Adjectives, terminated with Nouns
        {<NN.*>*<NN.*>}
    NP:
        {<NBAR>}
        # Above, connected with in/of/etc...
        {<NBAR><IN><NBAR>}
    """  
```

Once we have named entities values we search the Wikipedia using the NE values. We take the first value from NE which is the subject , search it in the Wikipedia. It gives us the page of the subject an once we get the page , we search for other entities in the page , if the search is successful , our fact is TRUE otherwise its false. 

Below are few examples of FN and TN, that are not part of Train or test Data -

    *False Positive Examples
        *Microsoft's appllication was Albuquerque, New Mexico.
        *Larry Page is Google’s CEO
        *Virat Kohli is Hockey player
        *Mukesh Ambani is son of Nita Ambani
        *Shah Rukh Khan was born in Pakistan
        
    *False Negative Examples
        *Bhagat Singh was a freedom Fighter
        *Sachin Tendulkar’s birth place is Mumbai India
        *Mahatma Gandhi’s death place is India
        *Narendra Modi was a TeaMaker
        *Rahul Gandhi is Cambridge graduate
     
