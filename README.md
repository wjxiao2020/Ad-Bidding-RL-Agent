# Ad Bidding Reinforcement Learning Agents

## Q-Learning Agent

## DQN Agent
<<<<<<< HEAD
To reproduce the result in the [report](report.pdf) (cumulative average win rate being over 50% at the end of training), please clone the repository and run the following command in the terminal under the DQN_Agent folder: 
=======

To reproduce the result in the report (cumulative average win rate over time being over 50%), please clone the repository and run the following command in the terminal under the DQN_Agent folder:
>>>>>>> upstream/main

`python MultiTaskAgent.py --num_episodes 10000`

### Specific Configuration Details:

Agent hyperparameters:

<<<<<<< HEAD
| Hyperparameter | Value |
| ----------- | ----------- |
| gamma | 0.75 |
| train_batch_size | 32 |
| replay_buffer_size | 50000 |
| min_replay_size | 1000 |
| reward_buffer_size | 10 |
| epsilon_start | 1.0 |
| epsilon_end | 0.01 |
| epsilon_decay_period | 20000 |
| weight_DQN_loss | 1.0 |
| weight_price_loss | 1.0 |
| target_update_frequency | 1000 |
| learning_rate | 0.0005 |
| initial_budget | 10000 |
| num_episodes | 10000 |

=======
| Hyperparameters         | Values |
| ----------------------- | ------ |
| gamma                   | 0.75   |
| train_batch_size        | 32     |
| replay_buffer_size      | 50000  |
| min_replay_size         | 1000   |
| reward_buffer_size      | 10     |
| epsilon_start           | 1.0    |
| epsilon_end             | 0.01   |
| epsilon_decay_period    | 20000  |
| weight_DQN_loss         | 1.0    |
| weight_price_loss       | 1.0    |
| target_update_frequency | 1000   |
| learning_rate           | 0.0005 |
| initial_budget          | 10000  |
| num_episodes            | 10000  |
>>>>>>> upstream/main

The training process took 3 hours to train on a cluster with the following settings:

<<<<<<< HEAD
| Setting | |
| ----------- | ----------- |
| GPU type | A100 | 
| GPU node count | 1 | 
| CPU count | 2 | 
| Memory | 16G | 
| python version | 3.8.8 | 
| anaconda version | 2021.11 | 
=======
| Hyperparameters  | Values  |
| ---------------- | ------- |
| GPU Type         | A100    |
| GPU node count   | 1       |
| CPU count        | 2       |
| Memory           | 16G     |
| python version   | 3.8.8   |
| anaconda version | 2021.11 |

## Q Learning Agent

To reproduce the result please use these hyperparameters and run the main.py file present in the QAgent directory associated with the q learning agent.

### Specific configuration details:

| Hyperparameters | Values                   |
| --------------- | ------------------------ |
| alpha           | 0.1                      |
| gamma           | 0.9                      |
| epsilon         | 1.0                      |
| epsilon_decay   | 0.999                    |
| actions         | [-6, -4, -2, 0, 2, 4, 6] |
| num_episodes    | 100000                   |
| initial_budget  | 10000                    |
>>>>>>> upstream/main
