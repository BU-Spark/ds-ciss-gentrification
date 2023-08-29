import spacy
from spacy import displacy
from spacy import tokenizer

nlp = spacy.load("en_core_web_sm")

text ="The World Health Organization (WHO)[1] is a specialized agency of the United Nations responsible for international public health.[2] The WHO Constitution states its main objective as 'the attainment by all peoples of the highest possible level of health'.[3] Headquartered in Geneva, Switzerland, it has six regional offices and 150 field offices worldwide. The WHO was established on 7 April 1948.[4][5] The first meeting of the World Health Assembly (WHA), the agency's governing body, took place on 24 July of that year. The WHO incorporated the assets, personnel, and duties of the League of Nations' Health Organization and the Office International d'Hygiène Publique, including the International Classification of Diseases (ICD).[6] Its work began in earnest in 1951 after a significant infusion of financial and technical resources.[7]"

doc = nlp(text)
#doc2 = nlp(text2)
# sentences = list(doc.sents)
# print(sentences)
# print entities
for word in doc.ents:
    print(word.text)
ents = [(e.text, e.start_char, e.end_char, e.label_) for e in doc.ents]
print(ents)