# Advanced Phishing Email Detection

A machine learning pipeline for classifying emails into **Ham (legitimate)**, **Spam (unwanted bulk)**, or **Phishing (malicious/fraudulent)** using two models: Naive Bayes + TF-IDF and RoBERTa with engineered phishing features.

## Overview

This project combines **7 public datasets** (~560K emails) to train robust 3-class classifiers. The pipeline extracts custom phishing-specific features (urgency patterns, brand impersonation, credential requests, typosquatting, suspicious URLs, etc.) and evaluates both traditional and deep learning approaches.

## Dataset Sources

| Source | Rows | Labels |
|--------|------|--------|
| Existing (spam_Emails_data) | 193,852 | Ham, Spam |
| Enron Spam | 31,716 | Ham, Spam |
| SpamAssassin | 6,046 | Ham, Spam |
| Phishing Liu | 18,650 | Ham, Phishing |
| Phishing 7DS | 162,413 | Ham, Spam |
| Phishing v2.0 | 120,000 | Ham, Spam, Phishing |
| Phishing Rabin | 26,946 | Ham, Phishing |
| **Total** | **559,623** | **3 classes** |

**Final label distribution:** Ham: 240,418 | Spam: 191,897 | Phishing: 127,308

## Models

### 1. Naive Bayes + TF-IDF

- **Text features:** TF-IDF vectors (unigrams + bigrams)
- **Engineered features:** 16 phishing-specific metrics (text length, URL count, brand mentions, urgency/threat scores, typosquatting, etc.)
- **Class weighting** to handle imbalance

### 2. RoBERTa with Phishing Features

- **Base model:** `roberta-base` fine-tuned on 100K sampled emails
- **Custom architecture:** Concatenates RoBERTa's CLS token embedding with 16 engineered phishing features before final classification
- **Training:** 2 epochs, batch size 8, learning rate 2e-5

## Results

| Metric | Naive Bayes | RoBERTa |
|--------|-------------|---------|
| **Accuracy** | 97.00% | 97.48% |
| **Precision** | 97.01% | 97.50% |
| **Recall** | 97.00% | 97.48% |
| **F1-Score** | 96.99% | 97.48% |

### Per-Class Performance (Naive Bayes)

| Class | Precision | Recall | F1-Score |
|-------|-----------|--------|----------|
| Ham | 0.98 | 0.99 | 0.99 |
| Spam | 0.95 | 0.96 | 0.96 |
| Phishing | 0.98 | 0.94 | 0.96 |

### Per-Class Performance (RoBERTa)

| Class | Precision | Recall | F1-Score |
|-------|-----------|--------|----------|
| Ham | 0.99 | 0.99 | 0.99 |
| Spam | 0.95 | 0.97 | 0.96 |
| Phishing | 0.99 | 0.95 | 0.97 |

## Project Structure

```
Email_detection/
├── Dataset/
│   ├── Email-spam-phishing-Detection.ipynb   # Main notebook
│   ├── combined_phishing.csv                 # Combined dataset (generated)
│   └── *.csv                                 # Raw data sources
├── naive_bayes_3class_model.pkl              # Saved NB model
├── tfidf_vectorizer_3class.pkl               # Saved TF-IDF vectorizer
├── feature_scaler_3class.pkl                 # Saved feature scaler
├── roberta_phishing_final/                   # Saved RoBERTa model
├── phishing_detection_results.json           # Evaluation results
├── model_comparison.json                     # Model comparison summary
└── README.md
```

## Features Extracted

16 engineered phishing features per email:
- Text length, word count, average word length, capital ratio
- URL count, exclamation/question/dollar counts
- Presence of "free" or urgency keywords
- Brand name mentions (PayPal, Amazon, Netflix, etc.)
- Urgency score, threat score, credential request score
- Typosquatting detection, suspicious URL patterns

## Requirements

- Python 3.12+
- PyTorch, Transformers, Datasets (HuggingFace)
- scikit-learn, pandas, numpy, matplotlib, seaborn
- CUDA-capable GPU recommended for RoBERTa training

## Usage

1. Place raw CSV datasets in the `Dataset/` directory
2. Run the notebook end-to-end
3. Saved models and results will be written to the root directory
