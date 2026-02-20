import random
from mcp.server.fastmcp import FastMCP

#create fastmcp server instance
mcp =FastMCP(name="Demo-Remote-Server")

@mcp.tool()
def roll_dice(n_dice:int=1)->list[int]:
    """
    Roll n_dice 6sided dice and return the results
    """
    return [random.randint(1,6) for _ in range(n_dice)]

@mcp.tool()
def add_numbers(a:float,b:float)->float:
    """add two numbers"""
    return a+b

if __name__ == "__main__":

    # mcp.run(transport="streamable-http")
    mcp.run()