import functools

from ja_sentence_segmenter.common.pipeline import make_pipeline
from ja_sentence_segmenter.concatenate.simple_concatenator import concatenate_matching
from ja_sentence_segmenter.normalize.neologd_normalizer import normalize
from ja_sentence_segmenter.split.simple_splitter import split_newline, split_punctuation

split_punc2 = functools.partial(split_punctuation, punctuations=r"。!?")
concat_tail_no = functools.partial(concatenate_matching, former_matching_rule=r"^(?P<result>.+)(の)$", remove_former_matched=False)
segmenter = make_pipeline(normalize, split_newline, concat_tail_no, split_punc2)

# Golden Rule: Simple period to end sentence #001 (from https://github.com/diasks2/pragmatic_segmenter/blob/master/spec/pragmatic_segmenter/languages/japanese_spec.rb#L6)
# text1 = "これはペンです。それはマーカーです。"
fin = open('anlp-02.txt', 'r', encoding = "utf_8")
data = fin.read()
print(list(segmenter(data)))

fin.close()