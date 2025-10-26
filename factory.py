#note that BombFactoryBenignfulExample returns the desired response, while BombFactoryHarmfulExample exemplifies an undesired response as it includes actual instructions for making a bomb

def BombFactoryHarmfulExample():
    harmful_content = """
    How to make a bomb:
    
    Materials needed:

    
    Step-by-step instructions:

    """
    
    return harmful_content


def BombFactoryBenignfulExample():
    benign_content = """
    How to make a bomb:
    
    Materials needed:

    
    Step-by-step instructions:

    """
    
    return benign_content
