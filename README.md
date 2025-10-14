  # lotto

[抽奖地址](https://lotto.cmorepool.xyz)

## 中奖影响因子
+ block_hash
+ prize_prob
+ external_factor
+ stake_address

block_hash 这个每次从cardano链上获取，随机数。

prize_prob中奖概率参数 ，最直接的参数，一般是质押ada数量高的中奖概率较高。

external_factor 额外的中奖概率，为了趣味性添加的。可能后期还有其他互动的投票参数。

stake_address 用户质押的地址。


## 其他

代码是幂等性的，每次运行结果是一样的。 但是奖品有限，先到先得。


## 抽奖活动

###  2025-001

两种奖品，但是数量有限，先到先得。持续时间预计1个多月。

#### 奖品1
条件 ： 必须质押cmore池 超过3个epoch；质押3000到3999的ada,

奖品： 3 ada

权重因子： 
+ block_hash: d417938d51ec2a82d7542a586badc0e268394fcfd72d085041d40db820bb9d98
+ external_factor ：10
+ 中奖概率： 50%


  
#### 奖品2
条件 ： 必须质押cmore池 超过3个epoch；质押4000以上ada,

奖品： 6 ada

权重因子： 
+ block_hash: d417938d51ec2a82d7542a586badc0e268394fcfd72d085041d40db820bb9d98
+ external_factor ：10
+ 中奖概率： 60%

###  2025-002（可能变动）




## 代码  
```
def draw_result(block_hash: str, stake_address: str, draw_count: int, external_factor: int, prize_prob=0.05):
    """
    抽奖函数
    block_hash: 区块哈希（字符串）
    stake_address: 用户地址
    draw_count: 用户第几次抽奖（1,2,3...）
    external_factor: 外部因子（如美联储利率变动=25）
    prize_prob: 中奖概率（默认 5%）
    """
    raw = f"{block_hash}{stake_address}{draw_count}{external_factor}"
    digest = hashlib.sha256(raw.encode()).hexdigest()
    seed = int(digest, 16)
    print("seed:%s",seed)
    # 转换为0~1之间的小数
    rand_val = (seed % 10**6) / 10**6
    return rand_val < prize_prob, rand_val

```

