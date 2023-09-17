# Medical English to Spanish Translation APP

+ **Model Name:** Med_English2Spanish **https://huggingface.co/ayoubkirouane/Med_English2Spanish**
+ **Model Type:** Transformer-based Neural Machine Translation (NMT) Model
+ **Task:** English to Spanish Medical Translation

## Description:
**Medical English to Spanish Translation APP** is a user-friendly web application built with **Streamlit** that harnesses the power of a fine-tuned Transformer-based neural machine translation model. Its primary purpose is to assist medical professionals, researchers, and students in translating medical documents and texts from English to Spanish quickly and accurately.

## About Dataset:
The dataset used in **Medical English to Spanish Translation APP** is a critical component in ensuring accurate and contextually relevant medical translations. It is a subset of the "WMT-16-PubMed" dataset, which has been meticulously curated and adapted for this specific machine translation task. The dataset was compiled by collecting data from various reputable sources on the internet, as well as integrating content from another medical dataset, resulting in a comprehensive and diverse collection of medical documents.

**https://huggingface.co/datasets/ayoubkirouane/med_en2es**

**https://huggingface.co/datasets/qanastek/WMT-16-PubMed**

### Dataset Statistics:
* **Source:** Adapted from the "WMT-16-PubMed" dataset and other reputable medical sources.
* **Total Examples:** 286,000
* **Content:** The dataset comprises a wide range of medical texts, including research papers, clinical notes, and medical literature, covering various subfields within the healthcare domain.
* **Data Cleaning:** The dataset underwent rigorous data cleaning and preprocessing, including the removal of personally identifiable information (PII) to ensure privacy and compliance with ethical standards.
.

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
![Screenshot at 2023-09-17 20-17-31](https://github.com/Kirouane-Ayoub/Med-English-2-Spanish-APP/assets/99510125/ecff076b-9e48-4aa9-a7e5-13fc3b9547ac)
