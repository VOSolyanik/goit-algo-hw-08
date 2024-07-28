import heapq

def min_cables_connection_cost(cables):
    # Перетворити список кабелів на мін-купу
    heapq.heapify(cables)
    
    total_cost = 0
    
    # Поки в купі більше одного кабеля
    while len(cables) > 1:
        # Взяти два найкоротші кабелі
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        
        # Об'єднуємо
        combined = first + second
        
        # Збільшуємо витрати на об'єднання
        total_cost += combined
        
        # Додаємо новий об'єднаний кабель назад до купи
        heapq.heappush(cables, combined)
    
    return total_cost

def main() -> None:
    cables = [4, 3, 2, 6, 10]
    
    cost = min_cables_connection_cost(cables)
    
    print("Мінімальні витрати на об'єднання кабелів:", cost)
    
if __name__ == "__main__":
    main()