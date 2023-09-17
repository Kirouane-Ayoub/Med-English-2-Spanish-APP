# Medical English to Spanish Translation APP

+ **Model Name:** Med_English2Spanish
+ **Model Type:** Transformer-based Neural Machine Translation (NMT) Model
+ **Task:** English to Spanish Medical Translation

## Description:
**Medical English to Spanish Translation APP** is a user-friendly web application built with **Streamlit** that harnesses the power of a fine-tuned Transformer-based neural machine translation model. Its primary purpose is to assist medical professionals, researchers, and students in translating medical documents and texts from English to Spanish quickly and accurately.

## Ethical Considerations
**Med_English2Spanish**  is intended for medical professionals and researchers. Care has been taken to minimize biases in translations and ensure privacy by stripping PII during preprocessing. However, users are encouraged to review translations for accuracy in sensitive medical contexts.

+ **Bias and Fairness:** We have attempted to reduce bias, but users should be aware of potential translation biases.
+ **Privacy:** PII has been removed, but users should handle sensitive data with caution.
+ **Transparency:** The model's decisions are not explicitly explainable but can be understood through inspection of the input and output.

## Intended Use
**Med_English2Spanish** is designed for medical professionals, researchers, and students. It can be used for tasks like translating medical documents, research papers, and clinical notes from English to Spanish.
* **Target Audience:** Medical professionals, researchers, and students.
* **Use Cases:** Medical document translation, research paper translation, clinical note translation.

## Limitations
* **Data Limitations**: Performance may vary for extremely rare medical terms or languages other than English and Spanish.
* **Generalization**: The model may struggle with highly specialized subfields of medicine.
* **Domain-Specific Challenges**: Slang and colloquialisms may not be accurately translated.

## Usage 
```
pip -q install -r requirements.txt
streamlit run app.py

```
