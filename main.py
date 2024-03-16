
from gramformer import Gramformer
import torch
from fastapi import FastAPI


def set_seed(seed):
  torch.manual_seed(seed)
  if torch.cuda.is_available():
    torch.cuda.manual_seed_all(seed)

set_seed(1212)


gf = Gramformer(models = 1, use_gpu=False) # 1=corrector, 2=detector
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/correct-sentence")
def correctSentence(q: str = None):
   corrected_sentences = gf.correct(q, max_candidates=1)
   return list(corrected_sentences)[0]