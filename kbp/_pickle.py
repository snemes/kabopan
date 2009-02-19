import sys, os.path, pickle
def getfilename():
    return os.path.splitext(os.path.split(sys.argv[0])[1])[0]

def get_variables(filename, variables):
    filename += ".pik"
    try:
        with open(filename, "rb") as f:
            pi = pickle.load(f)
            #rebuilding the dictionary checks the actual existence of all variables
            return dict([variable, pi[variable]] for variable in variables)
    except:
        return None

def save_variables(filename, variables):
    filename += ".pik"
    try:
        with open(filename, "wb") as f:
            pickle.dump(variables, f)
    except:
        return None
