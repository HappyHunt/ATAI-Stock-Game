class Collector:
    '''
        General collector class
    '''

    # Constuctor
    def __init__(self, name: str, timeframe: str) -> None:
        self.name = name
        self.timeframe = timeframe
    
    # Destructor
    def __del__(self) -> None:
        pass

    '''
        TODO: Develop generic collector methods to gather
                info about specified cryptocurrency
    '''
    
    
    '''
    # Example method:
    def get_current_course(self) -> float:
        # Request to certain URL
        pass
        
        # Get specified data from url data
        data = 0.0

        # Return data
        return data
    '''




