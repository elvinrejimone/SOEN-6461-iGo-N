import json

APP_CONFIG_FILE = "./configs/app_config.json"


class StateUtils:

    @staticmethod
    def get_app_state():
        with open(APP_CONFIG_FILE) as f:
            config = json.load(f)
        return config

    @staticmethod
    def set_state(state, value):
        # Load the config file
        with open(APP_CONFIG_FILE) as f:
            config = json.load(f)
        config[state] = value
        # Save the updated config file
        with open(APP_CONFIG_FILE, "w") as f:
            json.dump(config, f)

    @staticmethod
    def get_state(state):
        with open(APP_CONFIG_FILE) as f:
            config = json.load(f)
        return config[state]

    @staticmethod
    def reset_state():
        newConfig = {"machine-city": getPort(),"language": "", "current-page": "LAN_SEL", "current-ticket-ID": "", "current-ticket-Type": "","current-port": "None", "payment-type": "", "ticket-quantity": 0, "total-amount": 0, "machine-city": "Montreal"}
        # Save the New config file
        with open(APP_CONFIG_FILE, "w") as f:
            json.dump(newConfig, f)

    def getPort():
        with open("./configs/current_port.json") as f:
            config = json.load(f)
        return config["port"]
