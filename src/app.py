from todo import ToDo
from colorama import Fore, Style, init
init(autoreset=True)

app = ToDo()

def main():
    while True:
        
        print(f" {Style.BRIGHT}{Fore.MAGENTA} \n Väkommen till \n=== Todo App ===")
        print()
        print(f"1. {Style.BRIGHT}{Fore.LIGHTCYAN_EX} 📝 Lägg till en ny uppgift")
        print(f"2. {Style.BRIGHT}{Fore.LIGHTCYAN_EX} 📋 Lista alla uppgifter")
        print(f"3. {Style.BRIGHT}{Fore.LIGHTCYAN_EX} ☑️  Markera uppgift som klar")
        print(f"4. {Style.BRIGHT}{Fore.LIGHTYELLOW_EX} 🅧  Ta bort uppgift")
        print(f"5. {Style.BRIGHT}{Fore.LIGHTRED_EX} 🔚  Avsluta")
        print()
        ch = input("Välj ett alternativ (1-5): ")
        print()
        
        if ch == "5":
            print("Avslutar programmet...")
            break
        
        match ch:
            case "1":
                title = input(f"{Style.BRIGHT}Ange uppgiftens titel: ")
                print(f"\n{Style.BRIGHT}{Fore.LIGHTCYAN_EX}Välj prioritet för uppgiften: {Style.RESET_ALL} \n\n"
                      "Tryck 1: för Låg\n"
                      "Tryck 2: för Medium\n"
                      "Tryck 3: för Hög")
                print()   
                priority_in = input("Ange ditt Val : ")
                print()
                priority = {"1": "Låg" ,"2": "Medium", "3": "Hög"}.get(priority_in, "Medium")
                
                app.add_task(title,priority)
                print(f" {Fore.LIGHTGREEN_EX}☑️  Uppgift '{title}' med prioditet '{priority}' är sparad")
                print()
                print(f"\n{Style.BRIGHT}{Fore.LIGHTCYAN_EX}Vill du lägga till fler uppgifter?{Style.RESET_ALL} \n\n" 
                        "Skriv Ja: för att lägga till uppgifter,\n"
                        "Skriv Pm: för påminelse,\n"
                        "Skriv End: för att Avsluta programmet.")
                
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
