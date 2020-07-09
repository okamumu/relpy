import relpy.bdd as bdd

class Env:
    def __init__(self, env = {}):
        self.env = env
        self.cache = {}
        self.bdd = bdd.BDD()
    
    def clear_cache(self):
        self.cache = {}
    
    def __getitem__(self, key):
        return self.env[key]

    def __setitem__(self, key, value):
        self.clear_cache()
        self.env[key] = value
    
    def __delitem__(self, key):
        del self.env[key]
    
    def __repr__(self):
        return str(self.env)
    
    def __str__(self):
        return str(self.env)
    
    def __iter__(self):
        return self.env.iteritems()
    
    def __len__(self):
        return len(self.env)
