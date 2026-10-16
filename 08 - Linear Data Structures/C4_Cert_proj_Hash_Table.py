class HashTable:
    def __init__(self):
        self.collection = {}
   
    def hash(self, hash_key: str):
        return sum(ord(i) for i in hash_key)


    def add(self, key: str, value):
        hashed_key = self.hash(key)
        if hashed_key not in self.collection.keys():
            self.collection[hashed_key] = {}
        self.collection[hashed_key][key] = value
   
    def remove(self, del_key:str):
        del_key_hash = self.hash(del_key)
        if del_key_hash  in self.collection:
            if del_key in self.collection[del_key_hash]:
                del self.collection[del_key_hash][del_key]
                if len(self.collection[del_key_hash]) == 0:
                    del self.collection[del_key_hash]            
   
    def lookup(self,lok_key: str):
        lok_key_hash = self.hash(lok_key)
        if lok_key_hash in self.collection.keys():
            if lok_key in self.collection[lok_key_hash].keys():
                return self.collection[lok_key_hash][lok_key]
        return None