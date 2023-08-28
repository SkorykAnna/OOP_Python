import re
import pandas as pd

class Corpus:
    def __init__(self, texts):
        self.texts = texts
        
    def concorde(self, expression, context_size):
        results = []
        pattern = r'(.{0,%d}%s.{0,%d})' % (context_size, expression, context_size)
        
        for text in self.texts:
            matches = re.findall(pattern, text)
            for match in matches:
                left_context = match[:context_size]
                right_context = match[-context_size:]
                results.append((left_context, expression, right_context))
        
        df = pd.DataFrame(results, columns=['Left Context', 'Match', 'Right Context'])
        return df