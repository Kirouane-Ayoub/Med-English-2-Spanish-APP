from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("ayoubkirouane/Med_English2Spanish")
model = AutoModelForSeq2SeqLM.from_pretrained("ayoubkirouane/Med_English2Spanish")

def run(src_text , model=model) : 
  translated = model.generate(**tokenizer([src_text], return_tensors="pt", padding=True))
  return [tokenizer.decode(t, skip_special_tokens=True) for t in translated][0]