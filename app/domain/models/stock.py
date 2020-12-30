class Stock:

    def __init__(
        self,
        name: str,
        bid: float,         # bid
        pre_close: float,   # regularMarketPreviousClose
        day_high: float,    # regularMarketDayHigh
        day_low: float,     # regularMarketDayLow
        year_high: float,   # fiftyTwoWeekHigh
        year_low: float,    # fiftyTwoWeekLow
    ):
        self.name = name
        self.bid = bid
        self.pre_close = pre_close
        self.day_high = day_high
        self.day_low = day_low
        self.year_high = year_high
        self.year_low = year_low

    def __eq__(self, other):
        return self.name == other.name and \
            self.bid == other.bid and \
            self.pre_close == other.pre_close and \
            self.day_high == other.day_high and \
            self.day_low == other.day_low and \
            self.year_high == other.year_high and \
            self.year_low == other.year_low
            
    def format_to_message(self) -> str:
        '''
        0050.TW
        => 漲 +10
        目前：120.1
        作收：110.1
        最高：121.1
        最低：115.1
        52周最高：121.1
        52周最低：67.1
        '''
        diff = self.bid - self.pre_close
        if diff > -1:
            diff_str = '漲 +{:.2f}'.format(diff)
        else:
            diff_str = '跌 {:.2f}'.format(diff)

        return '{name}\n=> {diff}\n目前：{bid}\n作收：{pre_close}\n最高：{day_high}\n最低：{day_low}\n52周最高：{year_high}\n52周最低：{year_low}'.format(
            name=self.name,
            diff=diff_str,
            bid=self.bid,
            pre_close=self.pre_close,
            day_high=self.day_high,
            day_low=self.day_low,
            year_high=self.year_high,
            year_low=self.year_low
        )