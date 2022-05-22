# MiniMax Tic-Tac-Toe
Don't use neural nets when you don't have to

## MiniMax Algorith

![]("./pics/minimax_tictactoe.jpg")


In pseudocode (depth limited):

```
function  minimax(node, depth, maximizingPlayer) is
    if depth = 0 or node is a terminal node then
        return the heuristic value of node
    if maximizingPlayer then
        value := −∞
        for each child of node do
            value := max(value, minimax(child, depth − 1, FALSE))
        return value
    else (* minimizing player *)
        value := +∞
        for each child of node do
            value := min(value, minimax(child, depth − 1, TRUE))
        return value
```

## Use
```
python3 play_game.py
```
or
```
./play_game.py
```
