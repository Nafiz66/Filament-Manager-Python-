import json
import os


class FilamentManager:
    def __init__(self, filename="filaments.json"):
        self.filename = filename
        self.filaments = self.load_filaments()

    def load_filaments(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r", encoding="utf-8") as file:
                    return json.load(file)
            except (json.JSONDecodeError, FileNotFoundError):
                return []
        return []

    def save_filaments(self):
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(self.filaments, file, indent=4, ensure_ascii=False)

    def add_filament(self, name, material, weight, price_per_kg):
        filament = {
            "name": name,
            "material": material,
            "weight": weight,
            "price_per_kg": price_per_kg
        }
        self.filaments.append(filament)
        self.save_filaments()
        print("Filament wurde erfolgreich hinzugefügt und gespeichert.")

    def show_filaments(self):
        if not self.filaments:
            print("Keine Filamente vorhanden.")
            return

        print("\n--- Vorhandene Filamente ---")
        for index, filament in enumerate(self.filaments, start=1):
            print(
                f"{index}. Name: {filament['name']} | "
                f"Material: {filament['material']} | "
                f"Restmenge: {filament['weight']} g | "
                f"Preis pro kg: {filament['price_per_kg']:.2f} €"
            )

    def use_filament(self, name, amount):
        for filament in self.filaments:
            if filament["name"].lower() == name.lower():
                if amount <= 0:
                    print("Der Verbrauch muss größer als 0 sein.")
                    return

                if filament["weight"] >= amount:
                    filament["weight"] -= amount
                    self.save_filaments()
                    print(
                        f"{amount} g wurden von '{filament['name']}' abgezogen. "
                        f"Neue Restmenge: {filament['weight']} g"
                    )
                else:
                    print("Nicht genug Filament vorhanden.")
                return

        print("Filament nicht gefunden.")

    def calculate_cost(self, name, amount):
        for filament in self.filaments:
            if filament["name"].lower() == name.lower():
                if amount <= 0:
                    print("Die Menge muss größer als 0 sein.")
                    return

                cost = (amount / 1000) * filament["price_per_kg"]
                print(
                    f"Die Kosten für {amount} g von '{filament['name']}' "
                    f"betragen {cost:.2f} €"
                )
                return

        print("Filament nicht gefunden.")