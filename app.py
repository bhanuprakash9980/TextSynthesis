from flask import Flask, render_template, request
import torch
import transformers
app = Flask(__name__)
gpt_tokenizer = transformers.GPT2Tokenizer.from_pretrained('gpt2')
gpt_model = transformers.GPT2LMHeadModel.from_pretrained('gpt2')


def gen_text(prompt_text, tokenizer=gpt_tokenizer, model=gpt_model, n_seqs=1, max_length=1000):
    encoded_prompt = tokenizer.encode(prompt_text, add_special_tokens=False, return_tensors="pt")
    output_sequences = model.generate(input_ids=encoded_prompt, max_length=max_length+len(encoded_prompt), temperature=1.0, top_k=40, top_p=0.9, repetition_penalty=1.2, do_sample=True, num_return_sequences=n_seqs)
    if len(output_sequences.shape) > 2:
        output_sequences.squeeze_()
    generated_sequences = []
    for generated_sequences_idx, generated_sequence in enumerate(output_sequences):
        generated_sequence = generated_sequence.tolist()
        text = tokenizer.decode(generated_sequence)
        total_sequence = (prompt_text + text[len(tokenizer.decode(encoded_prompt[0],clean_up_tokenization_spaces=True, )): ])
        generated_sequences.append(total_sequence)
    return generated_sequences[0]


@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        result = gen_text(request.form["text"])
        text = result.rsplit(' ', 1)[0]
        return render_template('home.html', data=text)
    else:
        return render_template('home.html')


@app.route('/hello')
def hello():
    return "hello world"


if __name__ == "__main__":
    app.run(debug=True)