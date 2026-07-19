---
title: "大模型的注意力机制"
date: 2026-07-19T17:31:14+0800
draft: false
description: ""
tags: ["大模型", "注意力机制", "self-attention", "cross-attention"]
---

大模型的发展与 Attention 机制息息相关，从一开始为了解决长序列依赖的问题，到如今追求推理效率，其进化路线可以概括为：从“能看多长”到“看多快”，再到“看多准”。

既然提到了注意力机制，那不得不从 RNN（循环神经网络，Recurrent Neural Network）说起，RNN 采用门控单元和顺序结构处理一个个的 token。如图，需要输出 Out3，则模型需要等到 Out1 和 Out2 都生成以后，才会生成 Out3。这会导致两个问题：

1. 由于门控单元的设计，信息在传送的距离中容易出现信息丢失的情况，也就是很难“看见”远距离的信息。
2. 由于 RNN 是顺序执行，随着句子序列的增长，模型的计算时间也随之增长，模型的并行计算能力差。

为了解决上面的问题，既能不损失信息地看到其他 token，另一方面又能提高模型的并行运算能力，2017 年《Attention Is All You Need》提出了 Self-Attention（自注意力）。

## 注意力机制

![Self-Attention](./lulu.PNG)

上面这张图，大部分人一眼都会看到其中的噜噜，而不会聚焦于旁边的爆米花和手中的薯片，这就是注意力机制在发挥作用。

换句话说，注意力机制能让你关注到更加重要的、主体的部分。同样地，神经网络通过注意力机制能更好地关注到输入信息中重要的部分。所以注意力机制的目的就是让神经网络关注到需要关注的部分。

在公式：

$$ {Attention}(Q, K, V) = {Softmax}\left(\frac{Q K^T}{\sqrt{d\_k}}\right) V
$$

我们的目的就是关注到 $V$ 中更值得关注的部分。

那如何知道哪一部分更值得关注呢？

我们先从激活函数 $ {Softmax}(\mathbf{z})\_i = \frac{\exp(z\_i)}{\sum\_{j=1}^{K} \exp(z\_j)}$说起。从公式可以看出来，$z\_i$ 越大，则 $\operatorname{Softmax}(z\_i)$ 也越大（越接近 1），值越大越表示值得我们（神经网络）关注。问题就进一步转换为 $\frac{Q K^T}{\sqrt{d\_k}}$ 的大值（由于 $\operatorname{Softmax}$ 不是 Hardmax（只保留最大值），而是软分配（Soft Allocation）。它保留所有位置的概率，只是让大的更大、小的更小）。由于 $d\_k$ 是固定值维度，所以就是要在 $Q$ 和 $K$ 的运算中找到大值。根据文章《Attention is all you need》中的设计，$Q$ 是查询 Query，$K$ 是数据（信息）的索引 Key，通过 $Q K^T$ 计算其点积以衡量在特征空间的相似性（匹配度），相似性越大则注意力值越大，也就是更值得关注。

那现在问题又出现了，$Q$、$K$、$V$ 怎么得到的呢？

$$
Q = W\_q X, \quad K = W\_k X, \quad V = W\_v X
$$

从公式可以看出来，$Q$、$K$、$V$ 都是通过 $X$（输入张量）进行矩阵运算得到的。也就是说，一次矩阵运算，我们能得到所有 token 对应的 $Q$、$K$、$V$，大大缩短了计算时间。

总结一下：

1. 输入：整个输入序列（例如一句话的所有词向量）可以被一次性构造成一个矩阵 $X$。
2. 计算 QKV：通过一次矩阵乘法，我们就能同时得到所有 token 对应的 $Q$、$K$、$V$ 矩阵。
3. 计算注意力：$Q^T K$ 这一步会计算出序列中每一个 token 与所有其他 token 的相似度分数。这个计算过程是矩阵计算、高度并行的。

那么注意力机制如何解决上面两个问题的呢？

1. 在生成任何一个位置的输出时，Attention 不再依赖于一个被压缩过的、可能已经失真的历史信息。相反，它会直接计算原始输入序列中的所有信息（即与所有的 $V$ 向量进行计算），解决了 RNN 信息丢失的问题。
2. 由于计算 QKV 和 Attention 值都是矩阵运算，高度并行，解决了 RNN 顺序执行的问题。

<br />

## Self-Attention

那什么是自注意力机制？“自”又是什么意思？

很简单，自就是自己的意思，也就是 $QKV$的出身都是一样的，都是一个输入 $X$。

也就是上面提到的 $Q = W\_qX$， $K = W\_kX$， $V = W\_vX$。

![self-attention](./self-attention.PNG)
上面图的意思就是：
对于每个token，先产生三个向量 $Q、K、V$
- Q（查询需求）的作用是用来查询其余的向量和我有多少关系。
- K（信息标签）的作用是索引标签或特征标识，不是主动去检索，而是等待被Q匹配。Q和K的点积运算，本质上就是看“查询意图”和“索引标签”是否吻合。
- V（信息本体）的作用是回答，是根据输入信息又凝练了一层的信息Value，是实际承载的语义信息。
举个例子：
Q：找关于“水豚噜噜”的资料。
K：图书馆里上万本书的索引卡片，上面写在“哺乳动物”、“水豚”等信息。
根据Q和K的的信息信息比对，找到匹配度最高的书
V：书里的内容
```PYTHON
import torch
import torch.nn as nn
import math

class Attention(nn.Module):
    def __init__(self, d_model, d_k, d_v):
        super(Attention, self).__init__()
        # 定义线性变换层，将输入映射到 Q, K, V 空间
        self.w_q = nn.Linear(d_model, d_k)
        self.w_k = nn.Linear(d_model, d_k)
        self.w_v = nn.Linear(d_model, d_v)
        self.softmax = nn.Softmax(dim=-1) # 在最后一个维度进行归一化

    def forward(self, x):
        # 1. 线性投影：生成 Query, Key, Value
        q = self.w_q(x)
        k = self.w_k(x)
        v = self.w_v(x)
        
        # 2. 计算注意力分数 (Q * K^T)
        # transpose(-2, -1) 用于转置 K 的最后两个维度，以进行矩阵乘法
        scores = torch.matmul(q, k.transpose(-2, -1))
        
        # 3. 缩放：除以 sqrt(d_k)
        # 这一步至关重要，防止点积结果过大导致 Softmax 进入梯度极小的区域
        d_k = k.size(-1)
        scaled_scores = scores / math.sqrt(d_k)
        
        # 4. 归一化：Softmax 得到注意力权重
        attention_weights = self.softmax(scaled_scores)
        
        # 5. 加权求和：权重 * V
        attention_output = torch.matmul(attention_weights, v)
        
        return attention_output
```
从代码可以看到，查询（Q）、键（K）和值（V）这三个向量，都是由同一个输入 X 通过不同的线性变换得到的。这意味着模型是在分析输入序列内部各个元素之间的关系，比如一个句子中词与词的关联，所以是“自己关注自己”。