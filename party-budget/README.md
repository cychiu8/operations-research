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

    | item       | total needs |
    | ---------- | ----------- |
    | Main       | 8           |
    | Hamburgers | 6           |
    | Side dish  | 13          |
    | Drink      | 6           |
## Mathemetical Model

- Set
  - $M$：主餐的集合
  - $N$：副餐的集合
  - $A$：飲料的集合
  - $B$：漢堡的集合
  - $S$：套餐的集合
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
  - $t_{M}$：主餐所需總數量
  - $t_{B}$：漢堡所需總數量
  - $t_{N}$：附餐所需總數量
  - $t_{A}$：飲料所需總數量
  - $e_{M}$：最多可多買的主餐數量
  - $e_{N}$：最多可多買的副餐數量
  - $e_{A}$：最多可多點的飲料數量
  - $f^m_{s}$：套餐 s 包含主餐 m 的數量, $\forall m \in M, \forall s \in S$
  - $g^n_{s}$：套餐 s 包含副餐 n 的數量, $\forall n \in N, \forall s \in S$
  - $h^a_{s}$：套餐 s 包含飲料 a 的數量, $\forall a \in A, \forall s \in S$
  - $l^m$：需要主餐 m 的數量, $\forall m \in M \setminus \{甲,戊,庚\}$
  - $q^n$：需要副餐 n 的數量, $\forall n \in N \setminus \{辛\}$
  - $r^a$：需要飲料 a 的數量, $\forall a \in A$


- Cost

    $\displaystyle\sum_{\forall m \in M}p_{m}x_{m} + \displaystyle\sum_{\forall n \in N}p_{n}y_{n} + \displaystyle\sum_{\forall a \in A}p_{a}z_{a} + \displaystyle\sum_{\forall s \in S}p_{s}\omega_{s}$

- Demand

    - Main

        $\displaystyle\sum_{\forall i \in I}l^m_{i} + e_{M}\ge x_{m} + \displaystyle\sum_{\forall s \in S}f^m_{s}\omega_{s} \ge l^m$, $\forall m \in M$
    
    - Side dish

        $\displaystyle \sum_{\forall i \in I}q^n_{i} + e_{N} \ge y_{n} + \displaystyle\sum_{\forall s \in S}g^n_{s}\omega_{s} \ge q^n$, $\forall n \in N$

    - Drink

        $\displaystyle \sum_{\forall i \in I}r^a_{i} + e_{A} \ge z_{a} + \displaystyle\sum_{\forall s \in S}h^a_{s}\omega_{s} \ge r^a$, $\forall a \in A$

- Objective function: Minimum Cost

    $\text{Minimize}$$\displaystyle\sum_{\forall m \in M}p_{m}x_{m} + \displaystyle\sum_{\forall n \in N}p_{n}y_{n} + \displaystyle\sum_{\forall a \in A}p_{a}z_{a} + \displaystyle\sum_{\forall s \in S}p_{s}\omega_{s}$

- Constraints

    - number of main dish for each kind

        $x_{m} + \displaystyle\sum_{\forall s \in S}f^m_{s}\omega_{s} \ge l^m$, $\forall m \in M$

    - number of side dish for each kind

        $y_{n} + \displaystyle\sum_{\forall s \in S}g^n_{s}\omega_{s} \ge q^n$, $\forall n \in N$

    - number of drink for each kind

        $z_{a} + \displaystyle\sum_{\forall s \in S}h^a_{s}\omega_{s} \ge r^a$, $\forall a \in A$

    - number of main dish for all

        $t_{M} + e_{M} \ge \displaystyle \sum_{\forall m \in M}x_{m} + \displaystyle\sum_{\forall m \in M}\displaystyle\sum_{\forall s \in S}f^m_{s}\omega_{s} \ge t_{M}$

    - number of hamburger

        $\displaystyle\sum_{\forall m \in B}x_{m} + \displaystyle\sum_{\forall m \in B}\displaystyle\sum_{\forall s \in S}f^m_{s}\omega_{s} \ge t_{B}$

    - number of Side dish for all


        $t_{N} + e_{N} \ge \displaystyle\sum_{\forall n \in N}y_{n} + \displaystyle\sum_{\forall n \in N}\displaystyle\sum_{\forall s \in S}g^n_{s}\omega_s \ge t_{N}$

    - number of drink for all


        $t_A + e_{A} \ge \displaystyle\sum_{\forall a \in A}z_{a} + \displaystyle\sum_{\forall a \in A}\displaystyle\sum_{\forall s \in S}h^a_{s}\omega_{s}\ge t_{A}$

    - range of decision variables

        $0 \le x_{m}, x_{m} \in Integer, \forall m \in M$

        $0 \le y_{n}, y_{n} \in Integer, \forall n \in N$

        $0 \le z_{a}, z_{a} \in Integer, \forall a \in A$

        $0 \le \omega_{s}, \omega_{s} \in Integer, \forall s \in S$


## Solution

### solved by or-tool
- Objective function - total cost = 905
- Decision Variables
  - $x_m$：單點主餐 m 的數量, $\forall m \in M$
    | Item              | order numbers |
    | ----------------- | ------------- |
    | Beef hamburger    | 0             |
    | Pork hamburger    | 0             |
    | Chicken hamburger | 0             |
    | Fried Chicken     | 0             |
  - $y_n$：單點副餐 n 的數量, $\forall n \in N$
    | Item            | order numbers |
    | --------------- | ------------- |
    | Fries           | 1             |
    | Popcorn chicken | 0             |
    | Smoothie        | 0             |
    | Salad           | 2             |
  - $z_a$：單點飲料 a 的數量, $\forall a \in A$
    | Item      | order numbers |
    | --------- | ------------- |
    | Coke      | 0             |
    | Sprite    | 0             |
    | Black tea | 0             |
    | Green tea | 0             |
  - $\omega_s$：購買套餐 s 的數量, $\forall s \in S$
    | Item              | order numbers |
    | ----------------- | ------------- |
    | Beef hamburger    | 1             |
    | Pork hamburger    | 2             |
    | Chicken hamburger | 1             |
    | Fried Chicken     | 0             |
    | Party             | 1             |