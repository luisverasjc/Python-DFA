d = dict() # Global dict. Used to store DFA
    #{state: {input symbol: next state}}
def main():
    # ****this assumes good input**** #
    # Parse states
    s = input()
    s = s.split(" ")
    for i in range(len(s)):
        if s[i] != "states:":
            d[s[i]] = {}
    # Parse symbols
    # symbols = []
    s = input() #This bit of input seems unnecessary.
    #All relevant symbols appear in rules phase of input
    '''
    s = s.split(" ")
    for i in range(len(s)):
        if s[i] != "symbols:":
            symbols.append(s[i])
    '''
    # Parse rules
    s = input() # begin_rules
    while True:
        #rule dicts
        s = input()
        if s == "end_rules":
            break
        s = s.split(" ")
        state = s[0]
        next_state = s[2]
        symbol = s[4]
        d[state][symbol] = next_state
    # Get start state
    s = input()
    s = s.split(" ")
    for i in range(len(s)):
        if s[i] != "start:":
            start_state = s[i]
    # put final states in list
    final = []
    s = input()
    s = s.split(" ")
    for i in range(len(s)):
        if s[i] != "final:":
            final.append(s[i])
    while True:
        try:
            s = input()
        except EOFError:
            return
        end_state = traverse(s, start_state)
        if end_state in final:
            print("accepted")
        else:
            print("rejected")

#Takes in path string to be evaluated S and state state
#Returns state it ends on
def traverse(s, state):
    global d #Pulling in dict
    for i in s:
        try:
            state = d[state][i]
        except KeyError: #Not in dict
            return None
    return state


if __name__ == '__main__':
    main()
