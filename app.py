from flask import Flask, render_template, request, jsonify
#torch to manage the model imported from transformers
import torch 
#import pretrained gpt2models from transformer
import transformers
#create app
app = Flask(__name__)
#initialise gpt2 model and tokenizer
gpt_tokenizer = transformers.GPT2Tokenizer.from_pretrained('gpt2')
gpt_model = transformers.GPT2LMHeadModel.from_pretrained('gpt2')

#function to generate text based on the initial text
def gen_text(prompt_text, tokenizer=gpt_tokenizer, model=gpt_model, n_seqs=1, max_length=10000):
    #prompt_trext is encoded with tokenizer of gpt2 for better processing
    encoded_prompt = tokenizer.encode(prompt_text, add_special_tokens=False, return_tensors="pt")
    #outputsequences i.e the list of the number of sequences generated
    output_sequences = model.generate(input_ids=encoded_prompt, max_length=max_length+len(encoded_prompt), temperature=1.0, top_k=40, top_p=0.9, repetition_penalty=1.2, do_sample=True, num_return_sequences=n_seqs)
    if len(output_sequences.shape) > 2:
        output_sequences.squeeze_()
    generated_sequences = []
    for generated_sequences_idx, generated_sequence in enumerate(output_sequences):
        generated_sequence = generated_sequence.tolist()
        text = tokenizer.decode(generated_sequence)
        total_sequence = (prompt_text + text[len(tokenizer.decode(encoded_prompt[0],clean_up_tokenization_spaces=True, )): ])
        generated_sequences.append(total_sequence)
    #returning only first sequence as we need only one
    return generated_sequences[0]

#route for the page where we take input
@app.route('/', methods=["GET"])
def home():
    return render_template('home.html')

#route for recieve post request from the client
@app.route('/gen',methods=["POST"])
def gen():
    #text is recieved from the submitted form
    text=request.form["text"]
    #result is stored from the output of text generating function
    result = gen_text(text,max_length=(len(text)+10))
    #removing the unrequired string in the text
    result=result.replace('<|endoftext|>','')
    #returning the data in the form of json to fulfill the ajax request made
    return jsonify({'text' : result})


#running the app
if __name__ == "__main__":
    app.run(debug=True)
