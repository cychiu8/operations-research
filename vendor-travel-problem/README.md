# Vendor travel problem
## Problem description
https://docs.google.com/document/d/1mhKLc4LEIVvP0jUudIO2_WpOFF7knHA6Agmgbi6if3E/edit
- Revenue
  - $20 / 100m
- Tiredness
    | M   | kilometer     | tiredness for each 100 m | variable |
    | --- | ------------- | ------------------------ | -------- |
    | 0   | 0   km ~0.5km | 5                        |          |
    | 1   | 0.6 km ~ 1 km | 5                        |          |
    | 2   | 1.1 km ~ 2 km | 10                       |          |
    | 3   | 2.1 km ~ 3 km | 15                       |          |
    | 4   | 3.1 km ~ 4 km | 20                       |          |
- Extra Revenue
  > 第 500 公尺處的額外收入為 20，亦可多花 20 單位體力駐點叫賣，使額外收入**「提高到」**60。
  - 假設
    - 只要走到第 500 公尺處即有 $20
    - 若花 20 單位體力駐點叫賣，則會額外多 $40 ，提高到 $60
    - (不討論花 10 單位體力駐點叫賣可能額外多 $20 的情境，只有選擇花 20 體力叫賣，或是不花體力叫賣)

    | M   | position at Nth | bonus | extra effort | extra bonus |
    | --- | --------------- | ----- | ------------ | ----------- |
    | 0   | 0.5 km          | $20   | 20           | $40         |
    | 1   | 1   km          | $40   | 40           | $80         |
    | 2   | 2   km          | $60   | 100          | $240        |
    | 3   | 3   km          | $60   | 100          | $240        |
    | 4   | 4   km          | $60   | 120          | $300        |

## Mathemetical Model

### Abstract
> 先以一天為例，降低問題之維度

- Set
  - M 分段的集合
- Desicion Variables
  - $x$ : 攤販走的長度 (以 100 公尺為單位)
  - $y_{m}$：第 m 段的長度, $\forall m \in M$
  - $z_{m}$：人工變數，第 m 段是否全部走滿, $\forall m \in M$
  - $\omega_{m}$：於第 m 個點是否要停下來駐點叫賣, $\forall m \in M$
- Parameters
  - $c_m$：第 m 段，每 100 公尺所消耗的體力, $\forall m \in M$
  - $r$：每 100 公尺所取得的收入
  - $R$：須滿足之收入
  - $d_m$：第 m 段內，有多少 100 公尺, $\forall m \in M$
  - $b_m$：走完第 m 段，所得的額外收入, $\forall m \in M$
  - $t_m$：若於第 m 個點駐點叫賣，所需消耗的體力, $\forall m \in M$
  - $e_m$：若於第 m 個點駐點叫賣，所得的額外收入, $\forall m \in M$

- Revenue

    $r x$

- Tiredness Function

    $f(x)=\begin{cases}
c_0x &\text{, }0 \leq x \leq 10 \\
10c_0 + c_1(x-10) &\text{, }11 \leq x \leq 20 \\
10(c_0+c_1) + c_2(x-20) &\text{, }21 \leq x \leq 30 \\
10(c_0+c_1+c_2) + c_3(x-30) &\text{, }31 \leq x \leq 40 \\
\end{cases}$

- Extra revenue
  
    $\displaystyle\sum_{m \in M}b_mz_m$

- Revenue for extra effor

    $\displaystyle\sum_{m \in M}e_m\omega_m$

- Tiredness for extra effor

    $\displaystyle\sum_{m \in M}t_m\omega_m$

- Objective Function: Minimun tiredness
  
    $\text{Minimize}\displaystyle\sum_{m \in M} c_my_m + \displaystyle\sum_{m \in M}t_m\omega_m$

- Constraints
  - The lower bound of the revenue
  
    $rx+\displaystyle\sum_{m \in M}b_mz_m+\displaystyle\sum_{m \in M}e_m\omega_m \geq R$

  - Tiredeness function

    $\displaystyle\sum_{m \in M} y_m = x$

    $d_mz_m \leq y_m ,\forall m \in M$

    $y_m \leq Mz_{m-1},\forall m \in {1,...,|M|}$

    $z_m \geq z_{m+1},\forall m \in {0,...,|M|-1}$

  - relation between $z$ and $\omega$

    $z_m \geq \omega_m,\forall m \in M$

  - range of decision variables
  
    $0 \leq x \leq 40$

    $0 \leq y_m \leq 10 , \forall m \in M$

    $z_m \in {0,1}, \forall m \in M$

    $\omega_m \in {0,1}, \forall m \in M$

    


### Original Problem

> 增加天數的維度
- Assumption
  - 一天：假設為攤販從家裡出發回到家裡為一天，因此假設有 7 天 (出發 7 次)
- Set
  - M 分段的集合
  - D 天數的集合
- Desicion Variables
  - $x_i$ : 第 i 天攤販走的長度 (以 100 公尺為單位), $\forall i \in D$
  - $y_{mi}$：第 i 天第 m 段的長度, $\forall m \in M$, $\forall i \in D$
  - $z_{mi}$：人工變數，第 i 天第 m 段是否全部走滿, $\forall m \in M$, $\forall i \in D$
  - $\omega_{mi}$：第 i 天於第 m 個點是否要停下來駐點叫賣, $\forall m \in M$, $\forall i \in D$
- Parameters
  - $c_m$：第 m 段，每 100 公尺所消耗的體力, $\forall m \in M$
  - $r$：每 100 公尺所取得的收入
  - $R$：須滿足之收入
  - $d_m$：第 m 段內，有多少 100 公尺, $\forall m \in M$
  - $b_m$：走完第 m 段，所得的額外收入, $\forall m \in M$
  - $t_m$：若於第 m 個點駐點叫賣，所需消耗的體力, $\forall m \in M$
  - $e_m$：若於第 m 個點駐點叫賣，所得的額外收入, $\forall m \in M$

- Objective Function: Minimun tiredness
  
    $\text{Minimize}\displaystyle\sum_{i \in D}\displaystyle\sum_{m \in M} c_my_{mi} + \displaystyle\sum_{i \in D}\displaystyle\sum_{m \in M}t_m\omega_{mi}$

- Constraints
  - The lower bound of the revenue
  
    $r\displaystyle\sum_{i \in D}x_i+\displaystyle\sum_{i \in D}\displaystyle\sum_{m \in M}b_mz_{mi}+\displaystyle\sum_{i \in D}\displaystyle\sum_{m \in M}e_m\omega_{mi} \geq R$

  - Tiredeness function

    $\displaystyle\sum_{m \in M} y_{mi} = x_i$, $\forall i \in D$

    $d_mz_{mi} \leq y_{mi} ,\forall m \in M$, $\forall i \in D$

    $y_{mi} \leq Mz_{(m-1)i},\forall m \in {1,...,|M|}$, $\forall i \in D$

    $z_{mi} \geq z_{(m+1)i},\forall m \in {0,...,|M|-1}$, $\forall i \in D$

  - relation between $z$ and $\omega$

    $z_{mi} \geq \omega_{mi},\forall m \in M$, $\forall i \in D$

  - range of decision variables
  
    $0 \leq x_i \leq \displaystyle\sum_{m \in M}d_m$, $\forall i \in D$

    $0 \leq y_{mi} \leq d_m , \forall m \in M$, $\forall i \in D$

    $z_{mi} \in {0,1}, \forall m \in M$, $\forall i \in D$

    $\omega_{m} \in {0,1}, \forall m \in M$, $\forall i \in D$

## Solution

### solved by or-tool
- Objective function - the tiredness: 4140 unit
- Decision Variables for business
  - $x_i$ : 第 i 天攤販走的長度

    |           | D1  | D2  | D3  | D4  | D5  | D6  | D7  |
    | --------- | --- | --- | --- | --- | --- | --- | --- |
    | kilometer | 3   | 3   | 3.1 | 3   | 3   | 4   | 3   |

  - $\omega_{mi}$：第 i 天於第 m 個點是否要停下來駐點叫賣

    |        | D1  | D2  | D3  | D4  | D5  | D6  | D7  |
    | ------ | --- | --- | --- | --- | --- | --- | --- |
    | 0.5 km | 1   | 1   | 1   | 1   | 1   | 1   | 1   |
    | 1 km   | 0   | 1   | 1   | 1   | 1   | 0   | 0   |
    | 2 km   | 1   | 1   | 1   | 1   | 1   | 1   | 1   |
    | 3 km   | 1   | 1   | 1   | 1   | 1   | 1   | 1   |
    | 4 km   | 0   | 0   | 0   | 0   | 0   | 1   | 0   |
