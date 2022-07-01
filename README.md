# Tic-Tac-Toe through Q-learning

This is not a great idea, not necesarilly because the Q-learning algorithm is bad, but it doesn't try to solve the same problem.

The Q learning algorithm is an algorithm in which an agent takes a decision based on a score found during training. This score depends on the state of the problem and the available decision. By trying out different scenarios, we end up with a table full of scores to determine which is the optimal solution

First of all, the Q learning equation :
> $Q[state][action] = (1 - \alpha) * Q[state][action] + \alpha(reward + \gamma * max_{a} Q[next_{}state][a])$

This is the driving force of the Q-learning algorithm. It basically says that if we made a good decision, we give it a reward, and if it didn't, we punish him. Also, we update our scores according to the best next state, and therein lies our problem. The best next state in not necessarily the one in which we find ourselves.

Let's suppose that we can choose an action that lets our opponent win in 2 turns if he plays correctly. This is a bad choice as we shouldn't let our opponent win. But, by playing this action, if he doesn't play correctly, we have the possibility to win. Us having the possibility to win means that there is a positive Q value, and so the choice that we first assumed was bad seems like a good choice.

For this reason, it is best to use an algorithm such as min-max which takes into consideration the fact that our opponent plays optimally.

The Q-learning algorithm isn't as bad as it seems since if given the possibility to win, he will win, and if he can avoid a loss, he will block the opponents move.
