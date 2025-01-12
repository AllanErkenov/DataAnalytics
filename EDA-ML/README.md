# Анализ данных сайта e-commerce

[Ссылка на тетрадь](https://github.com/AllanErkenov/DataAnalytics/blob/main/EDA-ML/Project%201.ipynb)

**Цель исследования**

Получить полезные данные из csv фаила и попытаться построить относительно точную модель машинного обучения. 

**Задачи исследования**

- Подготовить данные и провести исследовательский анализ
- Обучение трех моделей машинного обучения и последующий выбор более точной из них

**Использованные библиотеки**
- pandas
- sklearn
- joblib
- matplotlib

**Результат исследования**

- Проведен обзор данных, переименованы колонки, удалены дубликаты, изменен формат данных;
- Обнаружена страна, покупатель, время и товар более всего продававшийся;
- Проведено обучение трех моделей машинного обучени - Линейная регрессия, случайный лес и градиентный спуск:
  - Для этого категориальные данные были переведены в числовые с помощью Frequency Encoding;
  - Эмпирическим путем в союзе с исследований показателей этих моделей была выделена модель случайного леса как самая эффективная.