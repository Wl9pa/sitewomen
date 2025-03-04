# 👜 Каталог Женщин
Веб-сайт для создания и управления каталогом профилей женщин с использованием Django framework.

---

## ✨ Функциональность
- 📝 Создание и редактирование профилей
- 🌐 Публикация статей
- 🔐 Аутентификация через GitHub
- 👨‍💻 Административная панель
- 📖 Фильтрация результатов
- 👩‍💼 Регистрация и аутентификация пользователей

---

## 📸 Скриншоты
### Главная страница
![Главная страница]![image](https://github.com/user-attachments/assets/f28e15ec-dc89-455e-86eb-dea8f140a7ed)

### Страница профиля/статьи
![Страница профиля]![image](https://github.com/user-attachments/assets/c0da0786-6c81-4cc9-955b-517354c5a1c0)

### Форма создания поста
![Создание поста]![image](https://github.com/user-attachments/assets/b2b12426-e930-4382-b967-cdec0e061c52)

### Форма обратной связи
![Обратная связь]![image](https://github.com/user-attachments/assets/107a84e3-23e4-4e63-91fe-c1876dc5865f)

### Профиль пользователя
![Профиль пользователя]![image](https://github.com/user-attachments/assets/58bcfc24-4478-4fe1-8bce-ae8254913261)

### Панель администратора
![Панель администратора]![image](https://github.com/user-attachments/assets/1641f47f-62ee-40ac-8c03-25507eaa880e)

![image](https://github.com/user-attachments/assets/ac9ff049-d5ba-4617-81e4-40b81f5e6f8f)


## 🚀 Установка

1. Клонировать репозиторий:
```bash
# Клонирование репозитория
git clone https://github.com/Wl9pa/sitewomen.git
cd sitewomen
```

2. Установить зависимости:
```bash
# Создание виртуального окружения
python -m venv venv
# Активация виртуального окружения
# Для Windows
venv\Scripts\activate
# Для Linux/MacOS
source venv/bin/activate
```

3. Создание .env из .env.example

4. Настройка БД:
```bash
python manage.py migrate
python manage.py createsuperuser
```

5. Запустить сервер:
```bash
python manage.py runserver
```
