string = 'geeks'
def test(string):
    string = 'geeksforgeeks'
    print('inside function:', string)

    test(id(string))
    print('outside function:', string)