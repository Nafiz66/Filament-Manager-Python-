from filament_manager import FilamentManager


def main():
    manager = FilamentManager()

    while True:
        print("\n=== Filament Manager ===")
        print("1. Filament hinzufügen")
        print("2. Filamente anzeigen")
        print("3. Filamentverbrauch eintragen")
        print("4. Kosten berechnen")
        print("5. Programm beenden")

        choice = input("Bitte wähle eine Option: ")

        if choice == "1":
            name = input("Name des Filaments: ").strip()
            material = input("Material (z. B. PLA, PETG, ABS): ").strip()

            try:
                weight = float(input("Restgewicht in Gramm: "))
                price_per_kg = float(input("Preis pro kg in Euro: "))
                manager.add_filament(name, material, weight, price_per_kg)
            except ValueError:
                print("Bitte gib bei Gewicht und Preis nur Zahlen ein.")

        elif choice == "2":
            manager.show_filaments()

        elif choice == "3":
            name = input("Name des Filaments: ").strip()

            try:
                amount = float(input("Verbrauch in Gramm: "))
                manager.use_filament(name, amount)
            except ValueError:
                print("Bitte gib für den Verbrauch nur Zahlen ein.")

        elif choice == "4":
            name = input("Name des Filaments: ").strip()

            try:
                amount = float(input("Menge in Gramm für die Kostenberechnung: "))
                manager.calculate_cost(name, amount)
            except ValueError:
                print("Bitte gib für die Menge nur Zahlen ein.")

        elif choice == "5":
            print("Programm wird beendet.")
            break

        else:
            print("Ungültige Auswahl. Bitte versuche es erneut.")


if __name__ == "__main__":
    main()