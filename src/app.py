from todo import ToDo

app = ToDo()

def main():
    while True:
        print("\n=== Todo App ===")
        print("1. Lägg till en ny uppgift")
        print("2. Lista alla uppgifter")
        print("3. Märk uppgift som klar")
        print("4. Ta bort en uppgift")
        print("5. Avsluta")
        
        ch = input("Välj ett alternativ (1-5): ")
        
        if ch == "5":
            print("Avslutar programmet...")
            break
        
        match ch:
            case "1":
                title = input("Ange uppgiftens titel: ")
                print("1. Låg",
                      "2. Medium",
                      "3. Hög")
                priority_in = input("Ange prioritet för uppgiften : ")
                priority = {"1": "Låg", 
                            "2": "Medium", 
                            "3": "Hög"}.get(priority_in, "Medium")
                
                app.add_task(title,priority)
                
            case "2":
                list_tasks()
            
            case "3":
                mark_complete()
                
def list_tasks():
    tasks = app.list_tasks()
    print(tasks)
    for task in tasks:
        status = "✓" if task[3] else " "
        print(f"- [{status}] ID: {task[0]} - {task[1]}")
        
def mark_complete():
    task_id = input('Ange ID för uppgiften som ska markeras som klar: ')
    app.mark_complete(task_id)
    print(f"Uppgift med ID {task_id} markerad som klar.")
            
            
if __name__ == "__main__":
    main()
