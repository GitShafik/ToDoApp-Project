from todo import ToDo

app = ToDo()
app.add_task("Test")

def main():
    while True:
        print("\n=== Todo App ===")
        print("1. Lägg till en ny uppgift")
        print("2. Lista alla uppgifter")
        print("5. Avsluta")
        
        ch = input("Välj ett alternativ (1-5): ")
        
        if ch == "5":
            print("Avslutar programmet...")
            break
        
        if ch == "1":
            title = input("Ange uppgiftens titel: ")
            app.add_task(title)
            
if __name__ == "__main__":
    main()
