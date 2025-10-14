  # lotto

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

