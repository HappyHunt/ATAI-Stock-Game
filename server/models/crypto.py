from enum import Enum

class Timeframe(Enum):
    MIN1  =  "1"
    MIN5  =  "5"
    MIN15 =  "15"
    H1    =  "60"
    H2    =  "120"
    H4    =  "240"
    H8    =  "480"
    H12   =  "720"
    D1    =  "1440"
    W1    =  "10080"
