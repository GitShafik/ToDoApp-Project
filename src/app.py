from todo import ToDo

app = ToDo()
app.add_task("Test")
app.mark_task_as_done("Test1")
app.list_tasks("Test2")

def main():
    while True:
        print("\n=== Todo App ===")
        print("1. Lägg till en ny uppgift")
        print("2. Lista alla uppgifter")
        print("4. Märk uppgift som klar")
        print("5. Avsluta")
        
        ch = input("Välj ett alternativ (1-5): ")
        
        if ch == "5":
            print("Avslutar programmet...")
            break
        
        if ch == "1":
            title = input("Ange uppgiftens titel: ")
            app.add_task(title)
            
        if ch == "2":
            title = input(" lista alla uppgifter: ")
            app.list_tasks(title)
            print("Uppgifter listade.")
        
        if ch == "3":
            pass
        
        if ch == "4":
            title = input("Märkera uppgift som klar: ")
            app.mark_task_as_done(title)
            
            
if __name__ == "__main__":
    main()
