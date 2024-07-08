1.Старыгин Виталий

2.Тестовой задание Python: https://drive.google.com/file/d/1nTTSmdbbJPnTCC3_Pi0oeIc5oFXFW0K2/view

3.Проект содержит в себе три модели Shop, Street, City. 
 
	С помощью Django и Django Rest framework сделано взаимодействие с приложением GET и POST запросами для получения подробной информации, характерной для данных моделей. 
 
	Реализация GET и POST запросов сделана при помощи Django REST framework
 
	Дополнительно сделана реализация тех же запросов на Django(ответ после запросов выводитcя на html+css templates), методы и классы также находятся в citystreetshop/views.py) 
 
	Используется СУБД SQLite3 для работы с базой данных
 
	В приложении main расположен только код некоторых html templates + static.css, весь основной код расположен в приложении citystreetshop.


4. Зайти в терминал и прописать команды:
 
	   pip install django
	   
	   pip install djangorestframework
	   
	   pip install django-filter

5. /admin
   
	   логин: admin
	   
	   пароль: 1234

    
6. Зайти в терминал и прописать команды:

	    cd citysite
	
	    python manage.py migrate
	
	    python manage.py runserver
