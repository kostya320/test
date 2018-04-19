---------------------------------------------------------------------------------------------------
3 правила совместной разработки
1. Писать понятные коммиты:
    а) что сделал
    б) с каким файлом
    в) на английском
Fix margin in login.html
Add register-form to landing.html
2. Одна ветка - одна задача
3. Не молчать и как можно быстрее уведомлять об изменениях
---------------------------------------------------------------------------------------------------

Комманды для работы с GitLab

git config --global user.name "kostya320"
git config --global user.email "taskin1999ab@gmail.com"

git clone https://gitlab.com/kostya320/my-project.git   	//скопировать на комп репозиторий
cd my-project
git pull origin "название ветки"  	//"стянуть" изменения с определенной ветки

git add .  	//Или название файла вместо точки
git commit -m "здесь писать комментарий"
git push -u origin master  	//выгрузить на ветку master

git branch "Название новой ветки"
git checkout "Название ветки на которую нужно перейти"

https://www.youtube.com/watch?v=BbFmd5NxO7M
