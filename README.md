# Scholar Inbox Datasets
As part of our submission to the ACL Systems Demo Track, we provide the following datasets:

## Recommendations
### Explicit user ratings
`rated_papers.csv`  
We publish explicit user ratings, as submitted via the thumbs up/ down buttons on papers displayed on scholar-inbox.com.  
$N=774k$
| arxiv_id | user_id | rating | time |
|---|---|---|---|

### Implicit user interactions
`implicit_interactions.csv`  
This is a dataset containing the user-paper interactions that were not explicit up/down ratings.
Such interactions include reading a paper, or clicking on any of the paper buttons to collect, share, etc.  
$N=556k$

| arxiv_id | user_id | time |
|---|---|---|


## Abstract highlighting 
`abstract_sentences.csv`  
Scholar Inbox's sentence highlighting feature was built using user-collected sentence classification data.   
We used this data to train out abstract sentence highlighting model.   
This dataset contains 2538 samples and four sentence labels: problem, task, idea, result


| arxiv_id | abstract | start_idx | end_idx | label |
|---|---|---|---|---|