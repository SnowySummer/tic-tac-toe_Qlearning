# Tic-tac-toe through Q-learning

## Tic-tac-toe

The famous game which is almost never played by people who can think for at least 5 seconds because it usually ends up in a draw. Each player takes turn placing their symbol in a 3x3 grid, the first person to get 3 in a row wins!

The goal for the A.I. is to avoid losing and at least draw, since if played perfectly, both player can achieve a draw. If the A.I. can win, this is a well-appreciated bonus.

## Q-learning

The basis of learning is this: the A.I. will play against itself by playing random moves. Each end of game, he will update his method of choosing the best action to take. By the end of the training, he should be able to find the optimal choice.

For choosing the best action, there will be a table where we associate the state of the board and the possible action with a score. This score is called a Q value. A better Q value means that the board is more favorable. We update our Q value with the following equation:
> $Q[state][action] = (1 - \alpha) * Q[state][action] + \alpha(reward + \gamma * max_{a} Q[nextstate][a])$

## Results


This is not a great idea, not necesarilly because the Q-learning algorithm is bad, but it doesn't try to solve the same problem.

When we update our Q value, we look at the next state in order to see which is the best next action. However, let's suppose that we can choose an action that lets our opponent win in 2 turns if he plays correctly. This is a bad choice as we shouldn't let our opponent win. But, by playing this action, if he doesn't play correctly, we have the possibility to win. Us having the possibility to win means that there is a positive Q value, and so the choice that we first assumed was bad seems like a good choice.

The Q-learning algorithm isn't all bad since if given the possibility to win, he will win, and if he can avoid a loss, he will block the opponents move. But for such problems, it is best to use an algorithm such as min-max which takes into consideration the fact that our opponent plays optimally.


