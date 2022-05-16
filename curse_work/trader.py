from os import path
from random import uniform
from argparse import ArgumentParser

from utils.files import get_dict_from_json, update_json


class Trader:
    def __init__(self, config: str, system_status: str) -> None:
        self.config = config_path
        self.default_status = get_dict_from_json(config)
        self.system_status = system_status
        self.configurate_system_file()
        self.current_status = get_dict_from_json(system_status)
        self.current_rate = round(self.current_status['exchange_rate'], 2)
        self.current_balance_uah = round(self.current_status['balance_uah'], 2)
        self.current_balance_usd = round(self.current_status['balance_usd'], 2)
        self.current_delta = round(self.current_status['delta'], 2)

    def update_status(self) -> None:
        update_json(self.system_status, self.current_status)

    def configurate_system_file(self):
        if not path.exists(self.system_status):
            update_json(self.system_status, self.default_status)

    def get_current_rate(self) -> None:
        print(f"Current rate: {self.current_rate} UAH")

    def get_current_balance(self) -> None:
        print(f"Balance: \nUAH: {self.current_balance_uah} \nUSD: {self.current_balance_usd}")

    def buy(self, buy_usd: float) -> None:
        required_uah = round(buy_usd * self.current_rate, 2)
        if required_uah <= self.current_status['balance_uah']:
            self.current_status['balance_uah'] -= required_uah
            self.current_status['balance_usd'] += buy_usd
        else:
            print(f"UNAVAILABLE, REQUIRED BALANCE UAH {required_uah}, AVAILABLE {self.current_status['balance_uah']}")

    def sell(self, sell_usd: float) -> None:
        if sell_usd <= self.current_status['balance_usd']:
            self.current_status['balance_uah'] += round(sell_usd * self.current_rate, 2)
            self.current_status['balance_usd'] -= sell_usd
        else:
            print(f"UNAVAILABLE, REQUIRED BALANCE USD {sell_usd}, AVAILABLE {self.current_status['balance_usd']}")

    def buy_all(self) -> None:
        if self.current_balance_uah > 0:
            self.current_status['balance_uah'] -= self.current_balance_uah
            self.current_status['balance_usd'] += round(self.current_balance_uah / self.current_rate, 2)
        else:
            print(f"The UAH balance is empty")

    def sell_all(self) -> None:
        if self.current_balance_usd > 0:
            self.current_status['balance_uah'] += round(self.current_balance_usd * self.current_rate, 2)
            self.current_status['balance_usd'] -= self.current_balance_usd
        else:
            print(f"The USD balance is empty")

    def get_next_rate(self) -> None:
        random_delta_rate = round(uniform(-self.current_delta, self.current_delta), 2)
        self.current_status['exchange_rate'] = self.current_rate + random_delta_rate

    def restart(self) -> None:
        update_json(self.system_status, self.default_status)

    def make_operation(self, args_vars: dict) -> None:
        if args_vars['operation_type'] == 'RATE':
            self.get_current_rate()
        elif args_vars['operation_type'] == 'AVAILABLE':
            self.get_current_balance()
        elif args_vars['operation_type'] == 'BUY' and args_vars['amount'] != 'ALL':
            self.buy(float(args_vars['amount']))
            self.update_status()
        elif args_vars['operation_type'] == 'SELL' and args_vars['amount'] != 'ALL':
            self.sell(float(args_vars['amount']))
            self.update_status()
        elif args_vars['operation_type'] == 'BUY' and args_vars['amount'] == 'ALL':
            self.buy_all()
            self.update_status()
        elif args_vars['operation_type'] == 'SELL' and args_vars['amount'] == 'ALL':
            self.sell_all()
            self.update_status()
        elif args_vars['operation_type'] == 'NEXT':
            self.get_next_rate()
            self.update_status()
        elif args_vars['operation_type'] == 'RESTART':
            self.restart()
        else:
            print("Invalid argument")


args = ArgumentParser()
args.add_argument("operation_type", type=str)
args.add_argument("amount", nargs="?", default=0)
args = vars(args.parse_args())

config_path = path.join("config.json")
system_status_path = path.join("system_status.json")

trader = Trader(config_path, system_status_path)
trader.make_operation(args)
