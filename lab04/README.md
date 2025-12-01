# Лабораторная работа 4: Алгоритмы сортировки

## Описание проекта
Исследование и реализация алгоритмов сортировки: пузырьком, выбором, вставками, слиянием, быстрой. Сравнительный анализ временной сложности и производительности.

## Цели работы
- Реализовать 5 алгоритмов сортировки
- Провести теоретический анализ сложности
- Экспериментально сравнить время выполнения
- Исследовать влияние начальной упорядоченности данных

## Структура проекта
```
lab-04-Сортировка/
├── src/
│   ├── sorts.py              # Реализация алгоритмов сортировки
│   ├── generate_data.py      # Генерация тестовых данных
│   ├── performance_test.py   # Тестирование производительности
│   └── plot_results.py       # Визуализация результатов
├── docs/
│   └── results/              # Графики и таблицы
├── README.md
├── ОТЧЕТ.md
└── requirements.txt
```

## Установка и запуск
```bash
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate     # Windows
pip install -r requirements.txt

python src/generate_data.py
python src/performance_test.py
python src/plot_results.py
```

## Требования
- Python 3.8+
- matplotlib
- numpy