class IntelTools:
    @staticmethod
    def encrypt_message(msg: str):
        return msg[::-1]

    @staticmethod
    def log_transmission(agent_name: str, message: str):
        return agent_name, "sent encrypted message:", message



print(IntelTools.encrypt_message("meir"))
print(IntelTools.log_transmission("meir",IntelTools.encrypt_message("meir")))