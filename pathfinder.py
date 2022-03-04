import os
import re 

class searchFiles:
    
    
    def __init__(self, path, key):
        self.parent_path = path
        self.keyword = b'(?i)' + str(key).encode()
        
        
    def __get_all_paths(self):
        """Function to get all the paths in the parent folder"""    
        try:
            lst = [x[0] for x in os.walk(self.parent_path)]
            return lst
        except Exception as e:
            err = "Could not search because: " + str(e)
            print(err)
            
    
    def __get_files(self, folder_path):
        """Get paths along with all the filenames"""
        try:
            lst = [f for f in os.listdir(folder_path) if os.path.isfile(folder_path + '/' + f)]
            if len(lst) == 0:
                return None 
            else:
                final_lst = [folder_path + "/" + l for l in lst]
                return final_lst 
        except Exception as e:
            err = "Could not search because: " + str(e)
            print(err)
            
            
    
    def __check_keyword(self, path):
        "Function to check if the keyword exists in the file"
        with open(path, 'rb') as myFile:
            for num,line in enumerate(myFile):
                if re.search(self.keyword, line):
                    found = """String was found in file {} at line {}
                    """.format(path, num)
                    print(found)
                    self.count = 1
                    break
                    
    
    def process_paths(self):
        """Main function to search files in the paths"""
        all_paths = self.__get_all_paths()
        
        for ap in all_paths:
            all_files = self.__get_files(ap)
            if all_files != None:
                for f in all_files: self.__check_keyword(f)
        
        if self.count != 1:
            print("No file match for the keyword")


if __name__  == '__main__':
    sf = searchFiles("/Users/onkar/Projects/", 'test')
    sf.process_paths()
