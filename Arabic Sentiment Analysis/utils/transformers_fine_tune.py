from transformers import AutoTokenizer
from datasets import Dataset
from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments
import pandas as pd

def transformes_model(model_name_):
    model_name = model_name_
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    return tokenizer, model

def generate_train_test_dataframe(X_train, X_test, y_train, y_test):
    train_df = pd.DataFrame({'Review': X_train, 'Sentiment': y_train})
    test_df = pd.DataFrame({'Review': X_test, 'Sentiment': y_test})

    train_dataset = Dataset.from_pandas(train_df)
    test_dataset = Dataset.from_pandas(test_df)

    return train_dataset, test_dataset



def prepare_data_for_transformers(train_dataset, test_dataset, tokenizer):

    def tokenize_function(examples):
        return tokenizer(
            examples["Review"],                  
            padding="max_length",                
            truncation=True,                      
            max_length=128,                       
            return_tensors="pt"                   
        )
    
    train_data = train_dataset.map(tokenize_function, batched=True)
    test_data = test_dataset.map(tokenize_function, batched=True)


    train_data = train_data.remove_columns(["Review"])
    test_data = test_data.remove_columns(["Review"])

    train_data = train_data.map(lambda examples: {'label': int(examples['Sentiment'])})
    test_data = test_data.map(lambda examples: {'label': int(examples['Sentiment'])})

    train_data.set_format("torch", columns=["input_ids", "attention_mask", "label"])
    test_data.set_format("torch", columns=["input_ids", "attention_mask", "label"])

    return train_data, test_data

def train_arguments(epochs):
    training_args = TrainingArguments(
        output_dir="./results",
        evaluation_strategy="epoch",                
        save_strategy="epoch",                     
        learning_rate=2e-5,                         
        per_device_train_batch_size=8,              
        per_device_eval_batch_size=8,
        num_train_epochs=epochs,                        
        weight_decay=0.01,                         
        save_total_limit=1,                         
        load_best_model_at_end=True)
    return training_args

def training(model, training_args, train_dataset, test_dataset):
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=test_dataset)
    
    return trainer.train()

def save_model_tokenizer(model, tokenizer):
    return model.save_pretrained('./fine_tuned_arabic_bert'), tokenizer.save_pretrained('./fine_tuned_arabic_bert')