# Party Budget problem

## Problem description
https://docs.google.com/document/d/1mhKLc4LEIVvP0jUudIO2_WpOFF7knHA6Agmgbi6if3E/edit

- Set

    | Set               | Price | Main              | Side dish                | Drink     |
    | ----------------- | ----- | ----------------- | ------------------------ | --------- |
    | Beef hamburger    | 150   | Beef hamburger    | Fries                    | Coke      |
    | Pork hamburger    | 130   | Pork hamburger    | Popcorn chicken          | Sprite    |
    | Chicken hamburger | 140   | Chicken hamgurger | Smoothie                 | Black tea |
    | Fried Chicken     | 150   | Fried Chicken * 2 | Salad                    | Green tea |
    | Party             | 200   | Fried Chicken * 4 | Fires * 3 + Smoothie * 3 | Coke * 4  |

- Price
    - Main
        | Main              | Price |
        | ----------------- | ----- |
        | Beef hamburger    | 120   |
        | Pork hamburger    | 100   |
        | Chicken hamburger | 110   |
        | Fried Chicken     | 60    |
    - Side dish
        | Side dish       | Price |
        | --------------- | ----- |
        | Fries           | 55    |
        | Popcorn chicken | 60    |
        | Smoothie        | 45    |
        | Salad           | 50    |
    - Drink
        | Drink     | Price |
        | --------- | ----- |
        | Coke      | 30    |
        | Sprite    | 30    |
        | Black tea | 25    |
        | Green tea | 25    |

- Demand
  - 加總各個主餐、附餐、飲料的數量

## Mathemetical Model

- Set
  - $M$：主餐的集合
  - $N$：副餐的集合
  - $A$：飲料的集合
  - $B$：漢堡的集合
  - $S$：套餐的集合
  - $I$：參加派對人的集合
- Decision Variables
  - $x_m$：單點主餐 m 的數量, $\forall m \in M$
  - $y_n$：單點副餐 n 的數量, $\forall n \in N$
  - $z_a$：單點飲料 a 的數量, $\forall a \in A$
  - $\omega_s$：購買套餐 s 的數量, $\forall s \in S$
- Parameters
  - $p_{m}$：單點主餐 m 的價格, $\forall m \in M$
  - $p_{n}$：單點副餐 n 的價格, $\forall n \in N$
  - $p_{a}$：單點飲料 a 的價格, $\forall a \in A$
  - $p_{s}$：點套餐 s 的價格, $\forall s \in S$
  - $e_{M}$：最多可多買的主餐數量
  - $e_{N}$：最多可多買的副餐數量
  - $e_{A}$：最多可多點的飲料數量
  - $f^m_{s}$：套餐 s 包含主餐 m 的數量, $\forall m \in M, \forall s \in S$
  - $g^n_{s}$：套餐 s 包含副餐 n 的數量, $\forall n \in N, \forall s \in S$
  - $h^a_{s}$：套餐 s 包含飲料 a 的數量, $\forall a \in A, \forall s \in S$
  - $l^m_{i}$：人 i 需要主餐 m 的數量, $\forall m \in M, \forall i \in I$
  - $q^n_{i}$：人 i 需要副餐 m 的數量, $\forall n \in N, \forall i \in I$
  - $r^a_{i}$：人 i 需要飲料 a 的數量, $\forall a \in A, \forall i \in I$

- Cost

    $\displaystyle\sum_{\forall m \in M}p_{m}x_{m} + \displaystyle\sum_{\forall n \in N}p_{n}y_{n} + \displaystyle\sum_{\forall a \in A}p_{a}z_{a} + \displaystyle\sum_{\forall s \in S}p_{s}\omega_{s}$

- Demand

    - Main

        $\displaystyle\sum_{\forall i \in I}l^m_{i} + e_{M}\ge x_{m} + \displaystyle\sum_{\forall s \in S}f^m_{s}\omega_{s} \ge \displaystyle\sum_{\forall i \in I}l^m_{i}$, $\forall m \in M$
    
    - Side dish

        $\displaystyle \sum_{\forall i \in I}q^n_{i} + e_{N} \ge y_{n} + \displaystyle\sum_{\forall s \in S}g^n_{s}\omega_{s} \ge \displaystyle\sum_{\forall i \in I}q^n_{i}$, $\forall n \in N$

    - Drink

        $\displaystyle \sum_{\forall i \in I}r^a_{i} + e_{A} \ge z_{a} + \displaystyle\sum_{\forall s \in S}h^a_{s}\omega_{s} \ge \displaystyle\sum_{\forall i \in I}r^a_{i}$, $\forall a \in A$

- Objective function: Minimum Cost

    $\text{Minimize}$$\displaystyle\sum_{\forall m \in M}p_{m}x_{m} + \displaystyle\sum_{\forall n \in N}p_{n}y_{n} + \displaystyle\sum_{\forall a \in A}p_{a}z_{a} + \displaystyle\sum_{\forall s \in S}p_{s}\omega_{s}$

- Constraints

    $\displaystyle\sum_{\forall i \in I}l^m_{i} + e_{M}\ge x_{m} + \displaystyle\sum_{\forall s \in S}f^m_{s}\omega_{s} \ge \displaystyle\sum_{\forall i \in I}l^m_{i}$, $\forall m \in M$

    $\displaystyle \sum_{\forall i \in I}q^n_{i} + e_{N} \ge y_{n} + \displaystyle\sum_{\forall s \in S}g^n_{s}\omega_{s} \ge \displaystyle\sum_{\forall i \in I}q^n_{i}$, $\forall n \in N$

    $\displaystyle \sum_{\forall i \in I}r^a_{i} + e_{A} \ge z_{a} + \displaystyle\sum_{\forall s \in S}h^a_{s}\omega_{s} \ge \displaystyle\sum_{\forall i \in I}r^a_{i}$, $\forall a \in A$

    $0 \le x_{m}, x_{m} \in Integer, \forall m \in M$

    $0 \le y_{n}, y_{n} \in Integer, \forall n \in N$

    $0 \le z_{a}, z_{a} \in Integer, \forall a \in A$

    $0 \le \omega_{s}, \omega_{s} \in Integer, \forall s \in S$