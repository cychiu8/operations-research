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
  - $J$