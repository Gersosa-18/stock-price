import warnings
import yfinance as yf
import pandas as pd

# Función para obtener el precio de una acción
def get_stock_price(symbol):
    stock = yf.Ticker(symbol)
    data = stock.history(period='1d')  # Obtener los datos del último día
    close_price = data['Close'].iloc[-1]  # Obtener el precio de cierre
    return close_price

# Función principal del programa
def main():
    symbols = ['AMZN', 'TSLA']

    while True:
        print("\nOpciones:")
        print("1. Ver precios actuales de las acciones seguidas")
        print("2. Agregar una nueva acción")
        print("3. Eliminar una acción")
        print("4. Salir")

        choice = input("Seleccione una opción: ")

        if choice == '1':
            print("\nPrecios actuales de las acciones:")
            for symbol in symbols:
                try:
                    close_price = get_stock_price(symbol)
                    print(f"{symbol}: {close_price:.2f}")
                except Exception as e:
                    print(f"Error al obtener el precio de {symbol}: {e}")

        elif choice == '2':
            new_symbol = input("Ingrese el símbolo de la nueva acción: ").upper()
            if new_symbol not in symbols:
                symbols.append(new_symbol)
                print(f"Acción {new_symbol} agregada.")
            else:
                print(f"La acción {new_symbol} ya está en la lista.")

        elif choice == '3':
            del_symbol = input("Ingrese el símbolo de la acción a eliminar: ").upper()
            if del_symbol in symbols:
                symbols.remove(del_symbol)
                print(f"Acción {del_symbol} eliminada.")
            else:
                print(f"La acción {del_symbol} no está en la lista.")

        elif choice == '4':
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    # Ignorar advertencias específicas de pandas yfinance
    warnings.simplefilter(action='ignore', category=FutureWarning)
    warnings.simplefilter(action='ignore', category=UserWarning)
    main()
