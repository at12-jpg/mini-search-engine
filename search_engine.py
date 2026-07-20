
import os



def search(query):
    search_words = query.lower().split()
  
    results = []
  
    documents = os.listdir("documents")
  
    for file in documents:
       
        filepath = os.path.join("documents", file)

    
        with open(filepath, "r") as current_file:
          
            content = current_file.read()

  
        matching_lines = []

       
        lines = content.split("\n")

   
        for line in lines:
      
            if any(word in line.lower() for word in search_words):
                matching_lines.append(line)

      
        if matching_lines:

           
            result = {

          
                "filename": os.path.basename(file),

               
                "matches": len(matching_lines),

                
                "lines": matching_lines
            }

           
            results.append(result)
            results.sort(key=lambda result: result["matches"], reverse=True)
    return results
def get_all_words():
    words = set()

    documents = os.listdir("documents")
    
    for file in documents:

        filepath = os.path.join("documents", file)

        with open(filepath, "r") as current_file:
            content = current_file.read().lower()


        for word in content.split():
            word = word.strip(".,!?;:()[]{}\"'")
            words.add(word)

    return sorted(words)
