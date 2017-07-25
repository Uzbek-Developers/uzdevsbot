# uzdevsbot
Telegram bot for Uzbek Developers group

## Dependencies
1. Python 3
2. Postgresql 9.6

## How to install
```shell
$ virtualenv --python=python3 venv
$ source venv/bin/activate
(venv) $ pip install -r requirements.txt
```

## How to prepare database
```shell
$ psql < schema.sql
```

## How to run
There are 2 running modes already bundled.
1. `loop` mode (local or server) `python main.py loop`
2. `webhook` mode (server) `python main.py` (default)

## How to deploy
```shell
$ git push heroku master
```

## Contributors
Uzbek Developers group
