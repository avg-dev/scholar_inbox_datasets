import pandas as pd

def load_dataset(filename):
    # load any of our datasets from a csv file using pandas
    assert filename in ["rated_papers.csv", "implicit_interactions.csv", "abstract_sentences.csv"], 'Options for filenames are: "rated_papers.csv" or "implicit_interactions.csv" or "abstract_sentences.csv"'
 
    return pd.read_csv('data/' + filename)


if __name__ == '__main__':
    print(load_dataset("rated_papers.csv").head())
    print(load_dataset("implicit_interactions.csv").head())
    print(load_dataset("abstract_sentences.csv").head())

    print(load_dataset("rated_papers.csv").shape)
    print(load_dataset("implicit_interactions.csv").shape)
    print(load_dataset("abstract_sentences.csv").shape)