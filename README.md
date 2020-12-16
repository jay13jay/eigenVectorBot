# Eigen Vector Stock Portfolio Bot
A portfolio bot based on EigenVectors to create a weighted non-market correlative stock portfolio


# Source Links

This bot is based largely on this post, with a number of usability modifications planned:

[EigenVesting by Scott Rome ](https://srome.github.io/Eigenvesting-I-Linear-Algebra-Can-Help-You-Choose-Your-Stock-Portfolio)



# Usage
1) clone the repo
```bash
git clone git@github.com:jay13jay/eigenVectorBot.git
cd eigenVectorBot
```

2) Create and activate virtual environment (optional)
```bash
virtualenv -p $(which python3) ~/eigenVectorBot_env
source ~/eigenVectorBot_env/bin/activate
```

3) Install dependencies
```bash
pip install -r requirements.txt
```

4) Configure Tickers
    - Open data/config.ini
    - Using the format provided, enter in whatever tickers you wish to use

5) Run the program
    - Run from the main project folder
    ```python
    python eigenBot/main.py
    ```
    - NOTE: to run from eigenBot folder, simply change the loadConfig method (line 18 on eigenBot/main.py)
    ```bash
    Change This:
        config.read('data/config.ini')j
    To This:
        config.read('../data/config.ini')
