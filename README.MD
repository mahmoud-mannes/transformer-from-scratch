
🧠 GPT Transformer from Scratch

A complete GPT-style Transformer implementation built entirely from scratch in PyTorch, trained on a text dataset (an extract from ShakeSpeare's work) and capable of autoregressive text generation.

This project was built to deeply understand the internals of modern language models — from multi-head attention to positional encodings — without relying on any high-level Transformer APIs.


---

🚀 Overview

This notebook implements and trains a mini-GPT model from first principles.
It covers every major component in the GPT architecture, from tokenization and embedding to training and generation.


🔹 Key Features

Custom byte-level tokenizer

Positional embeddings and learned representations

Multi-head self-attention, feed-forward layers, and residual connections

Layer normalization and causal masking

Cosine learning rate decay with warmup

Autoregressive text generation using greedy decoding



---

🧩 Model Architecture

Component	Details

Embedding Dim:	384
Heads:	6
Layers (Blocks):	6
Feedforward Dim: 	768
Context Length:	128 tokens
Training Objective:	 Next-token prediction (causal LM)
Optimizer	: AdamW
Scheduler:	 Cosine decay + warmup



---

📊 Results

Metric 	Description

Dataset	: Tiny Shakespeare (or small custom text corpus)
Validation Loss 	Converged smoothly with stable gradients
Output Quality:	Generates coherent sequences with structure and learned token dependencies


Example output:

> "They’ll sit by the fire and presume to know who rises and who falls in the Capitol. They say there’s grain enough! I’d rather see the streets run red than bow to their gossip."

---

🧠 Motivation

This project was designed as a deep dive into the core mechanics of attention and transformer training dynamics.
Rather than using prebuilt frameworks like transformers, I wanted to rebuild the GPT training pipeline manually to fully grasp:

how data flows through the attention stack,

how layer normalization and residual connections stabilize training,

and how learning rate warmup and cosine decay affect convergence.


The goal was mastery through construction — not just replication.


---

🛠️ Implementation Details

Implemented entirely in PyTorch

Modular structure for easy experimentation

Supports flexible configuration for heads, layers, and embedding sizes


---

📈 Future Improvements

Add standalone generate.py for CLI inference

Add gradient flow and attention visualization

Experiment with dropout, rotary embeddings, and layer scaling

Evaluate on larger datasets or character-level corpora 


---

📚 References

Vaswani et al., Attention Is All You Need (2017)

Radford et al., Language Models are Unsupervised Multitask Learners (2019)

Brown et al., Language Models are Few-Shot Learners (2020)

Karpathy, Zero to Hero series



---

💬 Author

Mahmoud Mannes
Engineering Student — passionate about Deep Learning and Systems Design



✅ Note:
This project demonstrates a full working GPT training and generation pipeline from scratch — no prebuilt transformer code, no shortcuts, just pure understanding.