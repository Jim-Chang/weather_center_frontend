from abc import abstractmethod, ABC


class IChatbotApiConfigure(ABC):

    pass

class RealChatbotApiConfigure(IChatbotApiConfigure):

    pass

class FakeChatbotApiConfigure(IChatbotApiConfigure):

    def __init__(self):
        pass
