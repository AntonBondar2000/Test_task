# Описание API

Админимтрирование сайта производится ли с помощью админки django /admin, либо через API 
Посмотреть документация можно по урлу /docs

## Для пользователей

### Получение списка всех опросов
```
/api/general/surveys
```
### Получение списка опросов, которое не прошел пользователь
```
/api/general/remaining-surveys/?user_id=...
```
### Получение списка опросов, которое прошел пользователь
```
/api/general/completed-surveys/?user_id=...
```
### Получение пройденного опроса с ответами и вопросами
```
/api/general/completing-surveys/?user_id=...&survey_id=...
```
### Прохождение опроса (отправка результата)
```
/api/general/submit-surveys

Данные должны быть в формата:
{
    "user_id": int, 
    "survey_id": int, 
    "answer": [
        {
            "question_id": int,
            "text": str,
            "answer_choice": list
        },     
        {
            "question_id": int,
            "text": str, 
            "answer_choice": list
        }
    ]
}
```
## Для администраторов

### Изменение опросво 
```
/api/administration/surveys
/api/administration/surveys/{id}
```
### Изменение вопросов 
```
/api/administration/questions
/api/administration/questions/{id}
```
### Изменение ответов 
```
/api/administration/answers
/api/administration/answers/{id}
```
