---
title: "从LLM Safety到Alignment：一个大模型安全算法工程师的技术成长路线"
date: 2026-07-19T09:00:00+08:00
draft: false
description: "记录从LLM Safety工程实践走向大模型Alignment方向的学习路线，包括SFT、Preference Learning、DPO/RLHF、安全评测以及多模态安全探索。"
tags:
  - LLM Safety
  - Alignment
  - SFT
  - DPO
  - RLHF
  - VLM
hidden: true 
---

# 从LLM Safety到Alignment：一个大模型安全算法工程师的技术成长路线

## 1. 为什么写这篇文章

随着大语言模型（LLM）的快速发展，模型能力已经不再是唯一关注点。

如何让模型：

- 输出安全可靠的内容
- 理解人类偏好
- 避免产生有害行为
- 在复杂场景下保持稳定

成为大模型落地过程中越来越重要的问题。

LLM Safety和Alignment正是连接模型能力与实际应用的重要方向。

这篇文章用于记录自己从LLM Safety工程实践走向大模型Alignment方向的学习过程，也作为未来一年技术成长路线的规划。

---

# 2. 我的背景

目前主要经历：

- 硕士阶段：医学影像 + 文本的视觉语言模型（Vision-Language Model）研究
- 研究院阶段：人工智能相关算法工程实践
- 当前：大模型安全方向算法工程实践

目前主要涉及：

- 开源基座模型微调
- Safety数据构造
- 模型训练与评测
- 安全分类任务优化

未来希望进一步深入：

- LLM Alignment
- Preference Learning
- Reward Model
- DPO/RLHF
- Multimodal Safety

---

# 3. 当前能力与不足

## 已有积累

### 数据方向

- 安全数据构造
- 数据清洗
- 标签体系设计
- Bad Case分析


### 模型方向

- 开源大模型SFT
- 全参数微调
- 训练参数调优


### 评测方向

- 分类指标分析
- 准确率、召回率评估
- 误伤与漏放分析


---

## 下一阶段需要突破

目前距离完整的LLM Alignment流程还有一定距离：

需要进一步掌握：

- Preference Data Construction
- Reward Model
- DPO
- RLHF
- Safety Benchmark
- Jailbreak Defense
- Multimodal Safety


---

# 4. 技术成长路线

当前主要能力：

```
Safety Classifier
        |
        ↓
Safety SFT
        |
        ↓
Preference Data Construction
        |
        ↓
Reward Model / Preference Optimization
        |
        ↓
DPO / RLHF
        |
        ↓
Safety Evaluation
        |
        ↓
Multimodal Safety Alignment
```


目标：

从：

> LLM Safety SFT工程实践

成长为：

> LLM Safety Alignment算法工程师

---

# 5. 未来一年学习路线

# 阶段0：环境准备（第1周）

## 目标

建立完整的大模型训练实验环境。


## 必备工具

### 深度学习框架

- PyTorch
- CUDA
- NCCL


### HuggingFace生态

- Transformers
- Datasets
- Accelerate
- PEFT
- TRL


### 训练优化

- DeepSpeed
- FSDP


### 推理

- vLLM


---

## 实验模型

### 文本模型

推荐：

- Qwen2.5-1.5B
- Qwen2.5-3B
- Qwen2.5-7B


### 多模态模型

后续：

- Qwen2.5-VL
- LLaVA


---

# 阶段1：LLM基础与SFT强化（第1-2个月）

## 目标

从：

> 会使用SFT

提升到：

> 理解SFT机制，并能够优化训练流程。


---

# Transformer基础


## 必须掌握

理解：

```
Input

↓

Embedding

↓

Transformer Blocks

↓

LM Head

↓

Output
```


---

## Attention机制

掌握：

- Query
- Key
- Value
- Multi-head Attention
- Causal Mask


理解：

为什么Decoder-only架构适合生成任务。


---

## RoPE

理解：

- 旋转位置编码原理
- 长上下文扩展问题


---

## KV Cache

理解：

- 推理加速机制
- Decode阶段缓存原理


---

# SFT深入学习


## 数据层面

掌握：

- Instruction Tuning
- Chat Template
- Dataset Mixing
- Data Quality Control


安全场景：

```
General Data

+

Safety Data
```


理解数据比例对模型行为的影响。


---

## 训练层面

实验：

调整：

- Learning Rate
- Batch Size
- Epoch
- Max Sequence Length


观察：

- Loss变化
- Safety指标
- 通用能力变化


---

# 实践项目1：Safety SFT实验

目标：

基于：

- Qwen2.5-1.5B


完成：

```
Base Model

↓

Safety Dataset

↓

SFT

↓

Evaluation
```


输出：

- 数据构造说明
- 训练配置
- 指标变化
- Bad Case分析


---

# 阶段2：Preference Learning（第3-5个月）

## 目标

掌握：

- Reward Model
- Preference Optimization
- DPO
- RLHF


---

# RLHF流程

理解：

```
Base Model

↓

SFT Model

↓

Reward Model

↓

PPO

↓

Aligned Model
```


---

## 核心概念

掌握：

- Preference Data
- Reward Function
- Reward Hacking
- KL Constraint


---

# 必读论文

## InstructGPT

重点：

- SFT
- Reward Model
- PPO


---

## Constitutional AI

重点：

- AI Feedback
- Safety Alignment


---

# DPO


## 数据格式

```json
{
  "prompt": "...",
  "chosen": "...",
  "rejected": "..."
}
```


核心思想：

提高：

```
chosen probability
```

降低：

```
rejected probability
```


---

# 实践项目2：Safety DPO实验


流程：

```
Qwen2.5

↓

Safety SFT

↓

Preference Dataset

↓

DPO

↓

Evaluation
```


指标：

- Harmful Response Rate
- Refusal Rate
- Over-refusal
- Helpfulness


---

# 阶段3：LLM Safety专项（第6-8个月）


## 目标

从：

安全分类任务

扩展到：

完整LLM Safety体系。


---

# Safety Taxonomy


掌握：

风险分类：

```
Violence

Sexual

Fraud

Cyber Attack

Self Harm

Hate Speech
```


理解：

- 标签设计
- 标注规范
- 边界Case


---

# Jailbreak


学习：

- Prompt Injection
- Jailbreak Prompt
- Adversarial Suffix
- Role Play Attack


---

# 推荐论文

- Universal Jailbreak
- AutoDAN


---

# Safety Benchmark


熟悉：

- AdvBench
- HarmBench
- SafetyBench
- TruthfulQA


---

# 实践项目3：Safety Evaluation Framework


实现：

输入：

```
Harmful Prompts Dataset
```


输出：

```
Attack Success Rate

Refusal Rate

False Refusal

Category Breakdown
```


---

# 阶段4：多模态Safety（第9-10个月）


## 目标

结合已有VLM研究背景，探索多模态大模型安全。


---

# VLM基础

掌握：

- CLIP
- BLIP-2
- LLaVA
- Qwen-VL


---

# 多模态Safety问题


## Image Jailbreak

图片诱导模型产生危险行为。


---

## OCR Attack

图片中的隐藏文本攻击。


---

## Vision Hallucination

视觉理解错误导致风险输出。


---

## Medical VLM Safety

结合医疗场景：

- 医疗幻觉
- 错误诊断
- 安全拒答


---

# 实践项目4：Vision Language Model Safety Alignment


流程：

```
Qwen2.5-VL

↓

图文Safety Dataset

↓

SFT

↓

DPO

↓

Benchmark
```


---

# 阶段5：求职准备（第11-12个月）


## 简历定位


避免：

```
内容安全分类算法
```


升级为：

```
LLM Safety Alignment Algorithm Engineer
```


---

# 项目描述模板


> 基于开源大语言模型开展Safety Alignment研究，通过安全指令微调、Preference Data构造、DPO优化以及自动化Safety Benchmark评测，提升模型安全性和泛化能力。


---

# 面试准备


## LLM基础

掌握：

- Transformer
- Attention
- RoPE
- KV Cache
- Scaling Law


---

## 微调

掌握：

- Full Fine-tuning
- LoRA
- SFT
- DPO


---

## 分布式训练

掌握：

- DeepSpeed
- ZeRO
- FSDP


---

## Safety

掌握：

- Jailbreak
- Reward Hacking
- Over-refusal
- Safety Evaluation


---

# 6. 每周学习安排


## 工作日

每天1小时：

| 时间 | 内容 |
| --- | --- |
|20分钟|论文阅读|
|20分钟|代码实践|
|20分钟|总结笔记|


---

## 周末

6-8小时：

重点：

- 跑实验
- 调参数
- 写技术总结


---

# 7. 学习优先级


## S级（必须）

★★★★★

- SFT
- DPO
- Reward Model
- Safety Evaluation


---

## A级

★★★★

- RLHF
- Jailbreak
- DeepSpeed


---

## B级

★★★

- VLM Safety


---

## C级

★★

- 预训练细节


---

# 8. 实践记录

后续持续更新：

- 实验结果
- 论文阅读笔记
- 项目总结
- 技术踩坑记录


---

# 总结

LLM Safety并不是简单的分类任务，而是连接模型能力和实际应用的重要环节。

未来一年，希望从当前的大模型安全工程实践出发，进一步深入Preference Learning、DPO以及多模态安全方向，建立完整的大模型安全对齐能力。

目标：

> 成为具备VLM研究背景、LLM Safety工程经验，并掌握SFT/DPO/RLHF与安全评测闭环的大模型算法工程师。

方向：

- LLM Safety Engineer
- Alignment Engineer
- Reward Model Engineer
- Multimodal Safety Engineer