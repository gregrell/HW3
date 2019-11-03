from rouge_score import rouge_scorer
import pyrouge

scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
scores = scorer.score('The quick brown fox jumps over the lazy dog. He is a bad dog. fuck that dog.',
                      'The quick brown dog jumps on the log.')

print(scores)