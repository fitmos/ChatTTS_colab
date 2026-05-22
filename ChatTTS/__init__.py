import sys
try:
    import transformers.models.bert.tokenization_bert as tb
    sys.modules['transformers.models.bert.tokenization_bert_fast'] = tb
except ImportError:
    pass

from .core import Chat