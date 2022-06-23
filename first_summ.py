from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer

#load tokenizer

#load model

class SummaryText:
#accept input


#token number representation of text, word after word


#>>tokens
    def __init__(self, data):
        self.summary = data

        
        
    def Tokenizer(self):
        tokenizer = AutoTokenizer.from_pretrained("google/pegasus-xsum")
        tokens = tokenizer(self.summary, truncation=True, padding="longest", return_tensors="pt")
        return tokens

#perform summarization
    def get_summary(self):
        tokenizer = AutoTokenizer.from_pretrained("google/pegasus-xsum")
        model = AutoModelForSeq2SeqLM.from_pretrained("google/pegasus-xsum")
        summary=model.generate(**summary)
        final_summary=tokenizer.decode(summary[0])
    #Decode token number summary
        tokenizer.decode(summary[0])
        return final_summary
#return summary tokens as output
#>>summary[0]


text="""Python is an interpreted high-level general-purpose programming language. Its design philosophy emphasizes code readability with its use of significant indentation. Its language constructs as well as its object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.[30]

Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly, procedural), object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library.[31]

Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.[32] Python 2.0 was released in 2000 and introduced new features, such as list comprehensions and a garbage collection system using reference counting. Python 3.0 was released in 2008 and was a major revision of the language that is not completely backward-compatible. Python 2 was discontinued with version 2.7.18 in 2020.[33]

Python consistently ranks as one of the most popular programming languages.[34][35][36][37]  

"""