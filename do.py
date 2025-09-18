import hashlib

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

# 示例
block_hash = "abc123def456"  # 假设某个区块哈希
stake_address = "stake1uxyz..."
draw_count = 1
external_factor = 25   # 美联储降息25基点
won, val = draw_result(block_hash, stake_address, draw_count, external_factor)

print(f"随机数={val}, 是否中奖={won}")
